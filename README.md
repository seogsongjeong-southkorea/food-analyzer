# 🍱 음식 사진 영양분석기

> 음식 사진 한 장 → 칼로리·영양성분·당뇨 위험도까지 자동 분석하는 Streamlit 앱

---

## 📸 주요 기능
- 🔍 **다중 음식 인식** — 김치찌개 + 공기밥 + 반찬이 한 사진에 있어도 각각 분석
- 📊 **7가지 영양성분** — 칼로리, 탄수화물, 단백질, 지방, 당류, 식이섬유, 나트륨
- 🩺 **당뇨 위험도 평가** — 당부하지수(GL) 기반 3단계 위험 분류 + 혈당 스파이크 예측
- 🇰🇷 **한식 특화 DB** — 농촌진흥청 국가표준식품성분표 기반

---

## 🍼 신생아 배포 가이드 (Step-by-Step)

> **아무것도 몰라도 괜찮아요. 아래를 순서대로 따라하면 됩니다. 예상 소요시간: 20~30분.**

### 📋 준비물 체크리스트
- [ ] 이메일 계정 (Gmail 추천)
- [ ] 인터넷 연결된 PC/노트북
- [ ] 웹브라우저 (Chrome 권장)

**설치할 프로그램은 없습니다.** (전부 웹에서 합니다)

---

### 🪜 STEP 1. Google Gemini API 키 발급받기 (무료)

**왜 필요한가?** 이 앱이 사진을 분석하려면 구글의 AI가 필요합니다. 키는 "이 AI를 쓸 수 있는 비밀번호"라고 생각하면 됩니다.

1. 웹브라우저에서 **https://aistudio.google.com/apikey** 접속
2. 구글 계정으로 로그인 (Gmail 계정 사용)
3. 화면 중앙의 파란색 **"Create API key"** 버튼 클릭
4. "Create API key in new project" 선택
5. 생성된 긴 문자열 (예: `AIzaSyA...xxx`)을 **복사**해서 메모장에 임시 저장
   - ⚠️ **이 키를 절대 남에게 보여주거나 GitHub에 올리지 마세요.**
6. ✅ **완료 기준**: 메모장에 `AIzaSy`로 시작하는 40글자 내외의 문자열이 저장됨

> 💰 **비용**: 완전 무료입니다. 분당 15건, 하루 1,500건까지 공짜. 개인 사용으론 평생 무료.

---

### 🪜 STEP 2. GitHub 계정 만들고 저장소 만들기

**왜 필요한가?** 코드를 온라인에 보관하고 Streamlit에 배포하려면 GitHub가 필요합니다.

#### 2-1. GitHub 가입
1. **https://github.com/signup** 접속
2. 이메일 → 비밀번호 → 사용자명 입력 (사용자명은 앞으로 계속 쓰이니 신중하게!)
3. 인증 퍼즐 → 확인 코드 이메일 입력
4. 무료 플랜 선택하고 가입 완료

#### 2-2. 새 저장소(Repository) 만들기
1. 로그인 후 화면 우측 상단의 **"+" 아이콘** 클릭 → **"New repository"** 선택
2. 다음과 같이 입력:
   - **Repository name**: `food-analyzer` (원하는 이름 OK)
   - **Description**: `음식 사진 영양분석기` (선택)
   - **Public** 선택 ✅ (무료 배포하려면 Public이어야 함)
   - **Add a README file**: 체크 ❌ (우리가 따로 만들 거라서 체크하지 마세요)
   - 나머지는 기본값
3. 초록색 **"Create repository"** 버튼 클릭
4. ✅ **완료 기준**: `https://github.com/본인아이디/food-analyzer` 주소의 빈 저장소 생성됨

---

### 🪜 STEP 3. 프로젝트 파일 업로드

**원본 파일들을 이 저장소에 올려야 합니다.** 두 가지 방법이 있는데 **방법 A (웹 업로드)** 가 제일 쉽습니다.

#### 📁 올려야 할 파일 목록
```
food-analyzer/
├── app.py                  ← 메인 앱 코드
├── nutrition_db.py         ← 음식 영양 DB
├── requirements.txt        ← 필요한 파이썬 패키지 목록
├── .gitignore              ← GitHub에 올리지 말아야 할 파일 목록
├── README.md               ← 이 문서
└── .streamlit/
    ├── config.toml         ← Streamlit 테마 설정
    └── secrets.toml.example ← API 키 템플릿 (실제 키 아님)
```

#### 방법 A. 웹 브라우저로 업로드 (추천, 가장 쉬움)

1. 방금 만든 저장소 페이지에서 **"uploading an existing file"** 파란 링크 클릭
   - 또는 **"Add file" → "Upload files"** 버튼 클릭
2. 내 컴퓨터에서 파일들을 **드래그 & 드롭**으로 끌어다 놓기
   - `.streamlit` 폴더도 통째로 끌어놓으면 됩니다
3. 아래 **"Commit changes"** 녹색 버튼 클릭
4. ✅ **완료 기준**: 저장소에 `app.py` 등 모든 파일이 보임

> ⚠️ **주의**: `.streamlit/secrets.toml` 파일은 절대 올리지 마세요! (API 키가 노출됨)
> `.streamlit/secrets.toml.example`만 올립니다.

---

### 🪜 STEP 4. Streamlit Community Cloud에 배포하기

**드디어 실제 웹사이트로 만드는 단계입니다!**

1. **https://share.streamlit.io** 접속
2. **"Continue with GitHub"** 클릭 → 방금 만든 GitHub 계정으로 로그인
3. GitHub이 "Streamlit에게 권한을 주겠냐"고 물으면 **"Authorize Streamlit"** 클릭
4. 대시보드에서 **"Create app"** 또는 **"New app"** 버튼 클릭
5. 다음과 같이 설정:
   - **Repository**: `본인아이디/food-analyzer` 선택
   - **Branch**: `main`
   - **Main file path**: `app.py`
   - **App URL (선택)**: 원하는 주소 설정 (예: `my-food-analyzer`)
6. **"Advanced settings..."** 클릭 → **"Secrets"** 항목에 아래 내용 붙여넣기:
   ```
   GEMINI_API_KEY = "STEP1에서_복사한_키_그대로_붙여넣기"
   ```
   예시:
   ```
   GEMINI_API_KEY = "AIzaSyAbc123xyz...여러분의실제키..."
   ```
   - ⚠️ 큰따옴표(`"`) 반드시 포함!
7. **"Deploy!"** 버튼 클릭
8. 2~5분 기다리면 배포 완료
9. ✅ **완료 기준**: `https://어쩌고.streamlit.app` 주소로 앱 접속 → 사진 업로드 → 영양분석 결과가 나오면 성공!

---

### 🎉 완료! 

이제 전 세계 누구나 `https://여러분앱.streamlit.app` 주소로 여러분이 만든 음식 영양분석기를 쓸 수 있습니다.

---

## 🔧 로컬 컴퓨터에서 먼저 테스트 해보고 싶다면

**배포 전에 내 PC에서 돌려보고 싶을 때만 읽으세요. 배포만 할 거면 건너뛰어도 OK.**

### 필요한 것
- Python 3.10 이상 설치 (https://www.python.org/downloads/)

### 실행 순서
```bash
# 1. 프로젝트 폴더로 이동
cd food-analyzer

# 2. 필요한 패키지 설치
pip install -r requirements.txt

# 3. secrets 파일 생성
# .streamlit/secrets.toml.example을 복사해서 .streamlit/secrets.toml로 이름 변경
# 그 파일 안의 "여기에_본인_키_입력" 부분에 실제 API 키 붙여넣기

# 4. 실행
streamlit run app.py
```

브라우저가 자동으로 열리고 `http://localhost:8501`에서 앱이 실행됩니다.

---

## 🐛 자주 발생하는 문제 & 해결법

| 증상 | 원인 | 해결 방법 |
|---|---|---|
| `GEMINI_API_KEY가 설정되지 않았습니다` 에러 | Streamlit Cloud Secrets 누락 | **App settings → Secrets**에 `GEMINI_API_KEY = "키"` 입력 후 앱 재시작 |
| `JSON 파싱 실패` | Gemini 응답 형식 변동 | 다른 사진으로 재시도. 반복되면 이슈 등록 |
| `모든 모델 호출 실패` | API 쿼터 초과 또는 지역 제한 | 24시간 후 재시도 / VPN 없이 접속 |
| 음식이 엉뚱하게 인식됨 | 사진 각도/조명 | 음식이 정면으로 보이는 밝은 사진으로 재촬영 |
| 중량 추정이 너무 차이남 | 크기 기준 부재 | 동전이나 신용카드를 음식 옆에 함께 촬영 (향후 개선 예정) |
| `DB에서 매칭되는 음식이 없음` | 희귀 음식 | `nutrition_db.py`에 직접 추가하고 push |

---

## 📂 파일별 역할 설명

```
├── app.py                  # Streamlit UI + Gemini API 호출
├── nutrition_db.py         # 음식 영양 DB + 계산 함수 + 당뇨 평가 함수
├── requirements.txt        # 필요 패키지: streamlit, google-generativeai, Pillow
├── .gitignore              # secrets.toml 등 민감 파일 차단
└── .streamlit/
    ├── config.toml         # 앱 테마
    └── secrets.toml        # (로컬용) API 키 저장소 — GitHub 업로드 금지
```

---

## 🧠 기술 스택 요약
- **Frontend**: Streamlit 1.39+
- **Vision AI**: Google Gemini 2.0 Flash (MLLM, zero-shot 식품 인식)
- **영양 DB**: 농촌진흥청 국가표준식품성분표 Release 10.0 (2023)
- **당뇨 지표**: Atkinson et al. (2021) International GI/GL Tables
- **Deploy**: Streamlit Community Cloud (무료)
- **Language**: Python 3.10+

> 📝 앱 하단의 **"기술 리포트"** 섹션에 모델 선택 이유, 정확도, 한계점이 상세히 나와있습니다.

---

## ⚠️ 면책 조항
본 앱은 **의료 기기가 아니며**, 당뇨병 진단·치료를 목적으로 하지 않습니다. 제공되는 영양 정보와 당뇨 위험도 평가는 **교육·참고 목적**이며, 실제 식이요법은 반드시 담당 의사·영양사의 지시를 따르세요.

---

## 📧 개선 제안
- DB 확장, 정확도 개선, UI 개선 등 PR 환영합니다
- 이슈: GitHub Issues 탭에 남겨주세요
