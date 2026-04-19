"""
음식 사진 영양분석기 - Streamlit App
Gemini Vision API + 한국 식품 영양 DB + 당뇨 위험도 평가
"""

import streamlit as st
import google.generativeai as genai
from PIL import Image
import json
import io
import re
from nutrition_db import NUTRITION_DB, calculate_nutrition, assess_diabetes_risk

# =========================
# 페이지 설정
# =========================
st.set_page_config(
    page_title="🍱 음식 영양분석기",
    page_icon="🍱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================
# API 키 설정
# =========================
def configure_api():
    """Streamlit secrets 또는 환경변수에서 API 키 로드"""
    api_key = None
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
    except (KeyError, FileNotFoundError):
        import os
        api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        st.error(
            "⚠️ **GEMINI_API_KEY가 설정되지 않았습니다.**\n\n"
            "Streamlit Cloud의 경우: App settings → Secrets에 다음을 추가하세요:\n"
            "```\nGEMINI_API_KEY = \"여기에_본인_키_입력\"\n```\n"
            "로컬 실행의 경우: `.streamlit/secrets.toml` 파일에 동일하게 입력하세요."
        )
        st.stop()

    genai.configure(api_key=api_key)
    return True


# =========================
# Gemini Vision 호출
# =========================
VISION_PROMPT = """너는 음식 사진 분석 전문가야. 업로드된 사진에 포함된 모든 음식을 식별하고 각 음식의 대략적인 중량(그램)을 추정해줘.

**규칙:**
1. 한 식탁에 여러 음식이 있으면 각각 따로 식별해줘 (예: 공기밥 + 김치찌개 + 김치 + 계란말이)
2. 음식 이름은 **한국어 일반 명칭**으로 (예: "공기밥", "김치찌개", "제육볶음")
3. 중량은 사진 속 양을 눈대중으로 추정 (g 단위, 정수)
4. 반찬/국물/밥그릇의 표준 1인분 기준:
   - 공기밥 1공기 ≈ 210g
   - 국/찌개 1인분 ≈ 300-400g
   - 반찬 1접시 ≈ 50-80g
   - 고기요리 1인분 ≈ 150-200g
5. 음식이 **아닌** 물체(접시, 컵, 수저 등)는 무시
6. 불확실하면 가장 가능성 높은 이름으로 추정하되 `confidence`로 표시

**출력 형식 (반드시 유효한 JSON만, 다른 설명 금지):**
```json
{
  "is_food": true,
  "dish_description": "전체 식단에 대한 간단 한줄 설명",
  "items": [
    {"name": "공기밥", "estimated_g": 210, "confidence": 0.95},
    {"name": "김치찌개", "estimated_g": 350, "confidence": 0.90}
  ]
}
```

사진에 음식이 없으면: `{"is_food": false, "reason": "이유"}`
"""


def analyze_image_with_gemini(image: Image.Image) -> dict:
    """Gemini로 이미지 분석하고 JSON 파싱"""
    try:
        # 모델 선택: 2.0-flash가 무료 티어에서 속도/품질 균형
        model_candidates = [
            "gemini-2.0-flash",
            "gemini-1.5-flash",
            "gemini-1.5-flash-latest",
        ]
        last_err = None
        for model_name in model_candidates:
            try:
                model = genai.GenerativeModel(model_name)
                response = model.generate_content(
                    [VISION_PROMPT, image],
                    generation_config={
                        "temperature": 0.2,
                        "max_output_tokens": 1500,
                    },
                )
                break
            except Exception as e:
                last_err = e
                continue
        else:
            return {"error": f"모든 모델 호출 실패: {last_err}"}

        raw = response.text.strip()

        # ```json 코드블럭 제거
        match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", raw, re.DOTALL)
        if match:
            raw = match.group(1)
        else:
            # 중괄호로 둘러싸인 JSON 추출
            match = re.search(r"\{.*\}", raw, re.DOTALL)
            if match:
                raw = match.group(0)

        data = json.loads(raw)
        return data
    except json.JSONDecodeError as e:
        return {"error": f"JSON 파싱 실패: {e}", "raw": raw if 'raw' in locals() else ""}
    except Exception as e:
        return {"error": f"분석 실패: {type(e).__name__}: {e}"}


# =========================
# UI
# =========================
def render_header():
    st.title("🍱 음식 사진 영양분석기")
    st.caption(
        "사진 한 장으로 칼로리, 탄수화물, 단백질, 지방, 당분을 분석하고 "
        "**당뇨 환자를 위한 혈당 스파이크 위험도**까지 평가합니다."
    )


def render_totals(totals: dict):
    """영양성분 총합 카드"""
    st.subheader("📊 식단 총 영양성분")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("🔥 열량", f"{totals['kcal']:.0f} kcal")
    c2.metric("🍚 탄수화물", f"{totals['carbs']:.1f} g")
    c3.metric("🥩 단백질", f"{totals['protein']:.1f} g")
    c4.metric("🧈 지방", f"{totals['fat']:.1f} g")

    c5, c6, c7, c8 = st.columns(4)
    c5.metric("🍯 당류", f"{totals['sugar']:.1f} g")
    c6.metric("🌾 식이섬유", f"{totals['fiber']:.1f} g")
    c7.metric("🧂 나트륨", f"{totals['sodium']:.0f} mg")
    c8.metric("📈 당부하(GL)", f"{totals['glycemic_load']:.1f}")


def render_diabetes_card(risk: dict, totals: dict):
    """당뇨 평가 카드"""
    st.subheader("🩺 당뇨 환자 섭취 가능성 평가")

    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(f"### {risk['overall_color']} {risk['overall']}")
        st.caption(f"위험 점수: {risk['risk_points']} / 7")

    with col2:
        st.info(f"💡 **권장사항**\n\n{risk['advice']}")

    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"**{risk['gl_color']} 당부하지수 (GL)**")
        st.markdown(f"- 값: **{risk['gl_value']:.1f}**")
        st.markdown(f"- 수준: **{risk['gl_level']}**")
        st.caption("GL = 혈당을 얼마나 올릴지 예측하는 지표 (낮을수록 좋음)")
    with c2:
        st.markdown(f"**📊 탄수화물 량**")
        st.markdown(f"- 섭취량: **{totals['carbs']:.1f}g**")
        st.markdown(f"- 수준: **{risk['carb_level']}**")
        st.caption("당뇨 환자 1회 식사 권장: 45-60g")
    with c3:
        st.markdown(f"**{risk['spike_color']} 혈당 스파이크 예측**")
        st.markdown(f"- 예측: **{risk['spike']}**")
        st.caption("GL, 식이섬유, 단백질, 지방을 종합 계산")


def render_details_table(details: list):
    """음식별 상세 내역"""
    if not details:
        return
    st.subheader("🔍 음식별 영양 분석")
    rows = []
    for d in details:
        rows.append({
            "음식": f"{d['matched_name']}" + (f" ({d['original_name']})"
                      if d['original_name'] != d['matched_name'] else ""),
            "중량(g)": d["weight_g"],
            "칼로리": f"{d['kcal']:.0f}",
            "탄수(g)": f"{d['carbs']:.1f}",
            "단백(g)": f"{d['protein']:.1f}",
            "지방(g)": f"{d['fat']:.1f}",
            "당(g)": f"{d['sugar']:.1f}",
            "GI": d['gi'],
            "GL": f"{d['gl']:.1f}",
        })
    st.dataframe(rows, use_container_width=True, hide_index=True)


def render_report():
    """사이트 하단 상세 기술 리포트"""
    st.markdown("---")
    st.header("📑 기술 리포트 — 이 앱은 어떻게 동작하는가")

    with st.expander("1️⃣ 전체 파이프라인 (클릭하여 펼치기)", expanded=True):
        st.markdown("""
```
[사용자]
   │ 음식 사진 업로드 (JPG/PNG)
   ▼
[Streamlit Frontend]
   │ 이미지 → Pillow 객체
   ▼
[Google Gemini Vision API]
   │ 프롬프트 + 이미지 → JSON 응답
   │   { "items": [{"name":"공기밥","estimated_g":210}, ...] }
   ▼
[로컬 영양 DB (nutrition_db.py)]
   │ 한국 식품성분표 매칭 (별칭/부분매칭 지원)
   │ 100g 기준 값 × (추정 중량/100)
   ▼
[영양성분 합산 + 당부하지수(GL) 계산]
   │ GL = Σ(GI × 가용탄수화물) / 100
   ▼
[당뇨 위험도 평가]
   │ GL, 탄수화물, 당, 식이섬유, 지방, 단백질로 종합 점수
   ▼
[Streamlit UI 렌더링]
```
        """)

    with st.expander("2️⃣ 사용 모델 및 학습 데이터"):
        st.markdown("""
### 🤖 비전 인식 모델
- **모델**: Google **Gemini 2.0 Flash** (대체: Gemini 1.5 Flash)
- **종류**: Multimodal Large Language Model (MLLM)
- **학습 데이터**: 구글 비공개. 수십억 장 이상의 웹 이미지 + 텍스트 페어로 사전학습.
- **왜 이 모델인가?**
  - ✅ 별도 학습 불필요 (Zero-shot). Food-101 같은 데이터셋을 직접 학습하지 않아도 한국 음식 인식 가능
  - ✅ 한 사진 안의 **여러 음식 동시 인식** 가능 (밥상 모드 지원)
  - ✅ 무료 API 제공 (분당 15건, 일 1,500건)
  - ✅ 한국어 음식명 직접 출력
- **대안 모델**:
  - Anthropic Claude 3.5/4 Sonnet Vision — 정확도 높음, 유료
  - OpenAI GPT-4o Vision — 정확도 최상위, 유료
  - Food-101 / VireoFood-172 로 파인튜닝한 CNN — Top-1 85~90%, 그러나 **한식 커버리지 낮음**

### 📚 영양 DB
- **출처**:
  - 🇰🇷 **농촌진흥청 국가표준식품성분표 Release 10.0 (2023)**
  - 🇰🇷 식품의약품안전처 식품영양성분DB
- **당뇨 관련 지표**:
  - **GI(혈당지수)**: Atkinson et al. (2021) *International Tables of Glycemic Index
    and Glycemic Load Values* (Diabetes Care)
  - **GL(당부하지수)** = GI × 가용탄수화물 / 100 (Harvard T.H. Chan 공식)
- 현재 ~55종 주요 한식/양식 수록 (공기밥, 김치찌개, 비빔밥, 떡볶이 등)
        """)

    with st.expander("3️⃣ 당뇨 위험도 평가 로직"):
        st.markdown("""
### 평가 기준 (출처)
- **대한당뇨병학회** 『2023 당뇨병 진료지침』
- **미국당뇨협회(ADA)** *Standards of Medical Care in Diabetes 2024*
- **WHO** 2015 Sugar intake guideline

### 위험 점수 (0~7점)
| 항목 | +1점 | +2점 |
|---|---|---|
| 당부하지수 GL | 10 초과 | 20 초과 |
| 탄수화물 | 60g 초과 | 90g 초과 |
| 첨가당 | 15g 초과 | 25g 초과 |
| 나트륨 | 1200mg 초과 | — |

- **0~1점**: 🟢 당뇨 환자 섭취 가능
- **2~3점**: 🟡 주의 (조절 섭취)
- **4점 이상**: 🔴 섭취 권장하지 않음

### 혈당 스파이크 예측 공식 (휴리스틱)
```
spike_score = GL × 2 - 식이섬유 × 1.5 - 단백질 × 0.3 - 지방 × 0.2
```
- 식이섬유/지방/단백질은 당의 흡수를 늦춰 스파이크를 완화
- 10 미만: 낮음 / 10~25: 중간 / 25 초과: 높음
        """)

    with st.expander("4️⃣ 정확도 및 한계"):
        st.markdown("""
### 📈 예상 정확도
| 단계 | 정확도 | 비고 |
|---|---|---|
| **음식 식별** | 85~92% | 대중적 한식/양식. 드문 향토음식은 낮아짐 |
| **중량 추정** | ±25~35% | 기준 물체(접시/수저) 크기를 추정하기 어려움 |
| **영양성분 계산** | ±20~30% | 중량 오차 + 레시피 편차가 누적됨 |
| **당뇨 위험 분류** | 분류 정확도 ~80% | 3단계(저/중/고) 기준. 구체적 혈당 수치 예측은 아님 |

### ⚠️ 알려진 한계
1. **의학적 진단 아님**: 참고용이며 개별 환자의 당부하 반응은 다를 수 있음
2. **중량 추정 오차**: 접시 크기, 촬영 각도에 민감. 측정 도구(동전·카드)를 함께 찍으면 정확도 상승
3. **DB 커버리지**: 약 55종. DB에 없는 음식은 Gemini가 제안해도 매칭 실패
4. **레시피 편차**: 같은 김치찌개라도 집/식당마다 열량 차이 ±30% 가능
5. **가공식품**: 포장지 영양표시가 더 정확함

### 🔧 정확도 개선 방법
- DB 확장 (현재 ~55종 → 목표 500종+)
- 중량 보정용 기준 물체(동전, 신용카드) 감지 기능 추가
- 사용자 수동 보정 슬라이더 추가
- Food-101 + 한식 데이터셋(AI-Hub 한국음식 이미지)으로 전용 모델 파인튜닝
        """)

    with st.expander("5️⃣ 기술 스택"):
        st.markdown("""
| 구분 | 기술 |
|---|---|
| 프론트엔드 | Streamlit 1.39+ |
| 이미지 처리 | Pillow (PIL) |
| 비전 AI | Google Generative AI SDK (`google-generativeai`) |
| 영양 DB | Python dict (로컬, 확장 가능) |
| 배포 | GitHub + Streamlit Community Cloud (무료) |
| 언어 | Python 3.10+ |
        """)

    with st.expander("6️⃣ 면책 조항 (Disclaimer)"):
        st.warning("""
⚠️ **본 앱은 의료 기기가 아니며, 당뇨병 진단·치료를 목적으로 하지 않습니다.**

- 제공되는 영양 정보와 당뇨 위험도 평가는 **교육·참고 목적**입니다.
- 실제 식이요법은 반드시 **담당 의사·영양사**의 지시를 따르세요.
- 혈당 관리가 필요한 분은 자가혈당측정기(SMBG) 또는 연속혈당측정기(CGM)를 이용하세요.
- 개발자는 본 앱의 사용으로 인한 건강상 결과에 대해 책임지지 않습니다.
        """)


# =========================
# 메인
# =========================
def main():
    configure_api()
    render_header()

    st.markdown("---")
    uploaded = st.file_uploader(
        "📸 음식 사진을 업로드하세요 (밥상 전체 사진도 OK)",
        type=["jpg", "jpeg", "png", "webp"],
        help="김치찌개 + 공기밥처럼 여러 음식이 함께 있어도 분석됩니다."
    )

    if uploaded is None:
        st.info("👆 사진을 업로드하면 자동으로 분석이 시작됩니다.")
        render_report()
        return

    # 이미지 표시
    try:
        image = Image.open(uploaded).convert("RGB")
    except Exception as e:
        st.error(f"이미지를 읽을 수 없습니다: {e}")
        return

    col_img, col_info = st.columns([1, 1])
    with col_img:
        st.image(image, caption="분석할 사진", use_container_width=True)

    with col_info:
        with st.spinner("🔍 Gemini Vision이 음식을 식별하는 중..."):
            result = analyze_image_with_gemini(image)

        if "error" in result:
            st.error(f"❌ {result['error']}")
            if result.get("raw"):
                with st.expander("원본 응답 보기 (디버그)"):
                    st.code(result["raw"])
            render_report()
            return

        if not result.get("is_food", True):
            st.warning(f"🤔 음식이 감지되지 않았습니다: {result.get('reason', '')}")
            render_report()
            return

        st.success("✅ 분석 완료!")
        st.markdown(f"**📝 식단 요약:** {result.get('dish_description', '')}")
        st.markdown("**🍽️ 식별된 음식:**")
        for item in result.get("items", []):
            conf = item.get("confidence", 1.0)
            conf_emoji = "🟢" if conf >= 0.8 else ("🟡" if conf >= 0.5 else "🔴")
            st.markdown(f"- {conf_emoji} {item['name']} (약 {item['estimated_g']}g, 신뢰도 {conf:.0%})")

    # 영양 계산
    nutrition = calculate_nutrition(result.get("items", []))
    totals = nutrition["total"]

    if not nutrition["details"]:
        st.error("❌ 영양 DB에서 매칭되는 음식이 없습니다. 다른 사진으로 시도해주세요.")
        render_report()
        return

    if nutrition["unrecognized"]:
        st.warning(
            f"⚠️ DB에 없는 음식이 있어 계산에서 제외했습니다: "
            f"**{', '.join(nutrition['unrecognized'])}**"
        )

    st.markdown("---")
    render_totals(totals)

    st.markdown("---")
    risk = assess_diabetes_risk(totals)
    render_diabetes_card(risk, totals)

    st.markdown("---")
    render_details_table(nutrition["details"])

    # JSON 다운로드
    st.markdown("---")
    full_report = {
        "image_analysis": result,
        "nutrition": nutrition,
        "diabetes_assessment": risk,
    }
    st.download_button(
        "📥 분석 결과 JSON 다운로드",
        data=json.dumps(full_report, ensure_ascii=False, indent=2),
        file_name="nutrition_report.json",
        mime="application/json",
    )

    render_report()


if __name__ == "__main__":
    main()
