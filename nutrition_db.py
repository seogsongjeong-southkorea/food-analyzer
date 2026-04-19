"""
한국 음식 영양성분 DB (100g 기준)
출처: 농촌진흥청 국가표준식품성분표 Release 10.0 (2023) 및 식품의약품안전처 데이터
GI(혈당지수) 출처: Atkinson et al. (2021) International tables of glycemic index and glycemic load values

모든 값은 100g당 수치. portion_g는 통상적인 1인분 중량.
GI는 포도당=100 기준.
"""

NUTRITION_DB = {
    # ===== 밥류 =====
    "공기밥": {
        "aliases": ["흰쌀밥", "쌀밥", "밥", "백미밥"],
        "kcal": 143, "carbs": 31.7, "protein": 2.6, "fat": 0.2,
        "sugar": 0.1, "fiber": 0.5, "sodium": 2, "gi": 73,
        "portion_g": 210, "category": "주식"
    },
    "현미밥": {
        "aliases": ["잡곡밥", "현미"],
        "kcal": 136, "carbs": 29.0, "protein": 3.2, "fat": 1.0,
        "sugar": 0.3, "fiber": 1.8, "sodium": 3, "gi": 55,
        "portion_g": 210, "category": "주식"
    },
    "비빔밥": {
        "aliases": ["돌솥비빔밥"],
        "kcal": 119, "carbs": 18.0, "protein": 4.5, "fat": 3.2,
        "sugar": 1.5, "fiber": 2.0, "sodium": 380, "gi": 68,
        "portion_g": 500, "category": "주식"
    },
    "김밥": {
        "aliases": ["김초밥"],
        "kcal": 143, "carbs": 26.0, "protein": 4.2, "fat": 2.5,
        "sugar": 1.8, "fiber": 1.2, "sodium": 480, "gi": 75,
        "portion_g": 230, "category": "주식"
    },
    "김치볶음밥": {
        "aliases": [],
        "kcal": 158, "carbs": 25.0, "protein": 4.0, "fat": 4.8,
        "sugar": 2.0, "fiber": 1.5, "sodium": 620, "gi": 73,
        "portion_g": 350, "category": "주식"
    },
    "오므라이스": {
        "aliases": [],
        "kcal": 152, "carbs": 22.0, "protein": 5.5, "fat": 5.0,
        "sugar": 3.5, "fiber": 0.8, "sodium": 540, "gi": 72,
        "portion_g": 400, "category": "주식"
    },
    "카레라이스": {
        "aliases": ["카레"],
        "kcal": 128, "carbs": 20.0, "protein": 3.8, "fat": 3.5,
        "sugar": 3.0, "fiber": 1.5, "sodium": 480, "gi": 70,
        "portion_g": 400, "category": "주식"
    },

    # ===== 면류 =====
    "라면": {
        "aliases": ["신라면", "진라면", "컵라면"],
        "kcal": 128, "carbs": 18.0, "protein": 3.5, "fat": 5.0,
        "sugar": 1.5, "fiber": 1.0, "sodium": 780, "gi": 73,
        "portion_g": 500, "category": "면류"
    },
    "짜장면": {
        "aliases": [],
        "kcal": 155, "carbs": 22.0, "protein": 5.5, "fat": 5.0,
        "sugar": 4.5, "fiber": 1.2, "sodium": 520, "gi": 68,
        "portion_g": 650, "category": "면류"
    },
    "짬뽕": {
        "aliases": [],
        "kcal": 120, "carbs": 15.0, "protein": 6.0, "fat": 4.0,
        "sugar": 2.0, "fiber": 1.5, "sodium": 820, "gi": 62,
        "portion_g": 700, "category": "면류"
    },
    "냉면": {
        "aliases": ["물냉면", "비빔냉면"],
        "kcal": 115, "carbs": 23.0, "protein": 4.0, "fat": 0.8,
        "sugar": 3.0, "fiber": 0.8, "sodium": 420, "gi": 45,
        "portion_g": 600, "category": "면류"
    },
    "우동": {
        "aliases": [],
        "kcal": 95, "carbs": 18.0, "protein": 3.5, "fat": 0.5,
        "sugar": 0.8, "fiber": 0.7, "sodium": 380, "gi": 62,
        "portion_g": 550, "category": "면류"
    },
    "칼국수": {
        "aliases": [],
        "kcal": 110, "carbs": 20.0, "protein": 4.5, "fat": 1.2,
        "sugar": 1.0, "fiber": 0.9, "sodium": 520, "gi": 60,
        "portion_g": 600, "category": "면류"
    },
    "파스타": {
        "aliases": ["스파게티", "크림파스타", "토마토파스타"],
        "kcal": 165, "carbs": 24.0, "protein": 5.8, "fat": 5.5,
        "sugar": 2.5, "fiber": 1.8, "sodium": 420, "gi": 55,
        "portion_g": 350, "category": "면류"
    },
    "잡채": {
        "aliases": [],
        "kcal": 165, "carbs": 25.0, "protein": 3.5, "fat": 6.0,
        "sugar": 4.5, "fiber": 1.5, "sodium": 420, "gi": 65,
        "portion_g": 200, "category": "반찬"
    },

    # ===== 국/찌개 =====
    "김치찌개": {
        "aliases": [],
        "kcal": 68, "carbs": 4.5, "protein": 5.5, "fat": 3.2,
        "sugar": 1.8, "fiber": 1.2, "sodium": 620, "gi": 35,
        "portion_g": 400, "category": "국/찌개"
    },
    "된장찌개": {
        "aliases": [],
        "kcal": 52, "carbs": 4.0, "protein": 4.5, "fat": 2.0,
        "sugar": 1.2, "fiber": 1.5, "sodium": 680, "gi": 32,
        "portion_g": 400, "category": "국/찌개"
    },
    "순두부찌개": {
        "aliases": [],
        "kcal": 58, "carbs": 3.5, "protein": 5.0, "fat": 3.0,
        "sugar": 1.0, "fiber": 1.0, "sodium": 640, "gi": 30,
        "portion_g": 450, "category": "국/찌개"
    },
    "부대찌개": {
        "aliases": [],
        "kcal": 98, "carbs": 6.5, "protein": 7.0, "fat": 5.5,
        "sugar": 2.0, "fiber": 1.0, "sodium": 820, "gi": 45,
        "portion_g": 500, "category": "국/찌개"
    },
    "미역국": {
        "aliases": [],
        "kcal": 28, "carbs": 2.0, "protein": 2.5, "fat": 1.0,
        "sugar": 0.5, "fiber": 0.8, "sodium": 320, "gi": 25,
        "portion_g": 350, "category": "국/찌개"
    },
    "된장국": {
        "aliases": ["시래기국"],
        "kcal": 32, "carbs": 2.5, "protein": 2.8, "fat": 1.2,
        "sugar": 0.8, "fiber": 1.0, "sodium": 520, "gi": 28,
        "portion_g": 300, "category": "국/찌개"
    },
    "삼계탕": {
        "aliases": [],
        "kcal": 118, "carbs": 5.5, "protein": 12.0, "fat": 5.5,
        "sugar": 0.5, "fiber": 0.3, "sodium": 380, "gi": 40,
        "portion_g": 700, "category": "국/찌개"
    },
    "설렁탕": {
        "aliases": ["곰탕", "갈비탕"],
        "kcal": 82, "carbs": 2.5, "protein": 9.5, "fat": 4.0,
        "sugar": 0.3, "fiber": 0.2, "sodium": 420, "gi": 30,
        "portion_g": 600, "category": "국/찌개"
    },
    "육개장": {
        "aliases": [],
        "kcal": 78, "carbs": 4.0, "protein": 7.5, "fat": 3.5,
        "sugar": 1.0, "fiber": 1.2, "sodium": 680, "gi": 35,
        "portion_g": 500, "category": "국/찌개"
    },

    # ===== 육류 요리 =====
    "불고기": {
        "aliases": [],
        "kcal": 175, "carbs": 6.0, "protein": 18.0, "fat": 8.5,
        "sugar": 4.5, "fiber": 0.8, "sodium": 480, "gi": 45,
        "portion_g": 200, "category": "육류"
    },
    "제육볶음": {
        "aliases": ["돼지불고기"],
        "kcal": 195, "carbs": 7.0, "protein": 15.0, "fat": 12.0,
        "sugar": 5.0, "fiber": 1.0, "sodium": 580, "gi": 48,
        "portion_g": 200, "category": "육류"
    },
    "삼겹살": {
        "aliases": ["구운삼겹살"],
        "kcal": 331, "carbs": 0.5, "protein": 17.0, "fat": 28.0,
        "sugar": 0, "fiber": 0, "sodium": 60, "gi": 0,
        "portion_g": 200, "category": "육류"
    },
    "갈비": {
        "aliases": ["소갈비", "LA갈비"],
        "kcal": 245, "carbs": 4.5, "protein": 18.0, "fat": 17.0,
        "sugar": 3.5, "fiber": 0.3, "sodium": 420, "gi": 40,
        "portion_g": 200, "category": "육류"
    },
    "치킨": {
        "aliases": ["후라이드치킨", "양념치킨", "프라이드"],
        "kcal": 245, "carbs": 12.0, "protein": 18.0, "fat": 14.0,
        "sugar": 4.5, "fiber": 0.5, "sodium": 520, "gi": 55,
        "portion_g": 250, "category": "육류"
    },
    "돈까스": {
        "aliases": ["돈가스"],
        "kcal": 255, "carbs": 18.0, "protein": 14.0, "fat": 14.0,
        "sugar": 2.0, "fiber": 0.8, "sodium": 480, "gi": 65,
        "portion_g": 250, "category": "육류"
    },
    "찜닭": {
        "aliases": ["안동찜닭"],
        "kcal": 142, "carbs": 9.0, "protein": 13.0, "fat": 5.5,
        "sugar": 4.5, "fiber": 1.2, "sodium": 620, "gi": 55,
        "portion_g": 350, "category": "육류"
    },
    "족발": {
        "aliases": [],
        "kcal": 224, "carbs": 0.5, "protein": 22.0, "fat": 15.0,
        "sugar": 0.3, "fiber": 0, "sodium": 380, "gi": 0,
        "portion_g": 200, "category": "육류"
    },
    "보쌈": {
        "aliases": [],
        "kcal": 185, "carbs": 1.0, "protein": 20.0, "fat": 11.0,
        "sugar": 0.5, "fiber": 0.2, "sodium": 320, "gi": 0,
        "portion_g": 200, "category": "육류"
    },

    # ===== 생선/해산물 =====
    "생선구이": {
        "aliases": ["고등어구이", "삼치구이", "갈치구이", "연어구이"],
        "kcal": 180, "carbs": 0, "protein": 22.0, "fat": 10.0,
        "sugar": 0, "fiber": 0, "sodium": 220, "gi": 0,
        "portion_g": 150, "category": "생선"
    },
    "회": {
        "aliases": ["생선회", "광어회", "연어회"],
        "kcal": 110, "carbs": 0, "protein": 22.0, "fat": 2.5,
        "sugar": 0, "fiber": 0, "sodium": 80, "gi": 0,
        "portion_g": 200, "category": "생선"
    },
    "초밥": {
        "aliases": ["스시"],
        "kcal": 155, "carbs": 28.0, "protein": 6.0, "fat": 1.5,
        "sugar": 3.5, "fiber": 0.5, "sodium": 380, "gi": 75,
        "portion_g": 250, "category": "주식"
    },

    # ===== 분식/간식 =====
    "떡볶이": {
        "aliases": [],
        "kcal": 165, "carbs": 32.0, "protein": 2.5, "fat": 2.5,
        "sugar": 6.5, "fiber": 1.0, "sodium": 580, "gi": 80,
        "portion_g": 300, "category": "분식"
    },
    "순대": {
        "aliases": [],
        "kcal": 180, "carbs": 22.0, "protein": 6.0, "fat": 7.0,
        "sugar": 0.5, "fiber": 1.5, "sodium": 420, "gi": 55,
        "portion_g": 150, "category": "분식"
    },
    "만두": {
        "aliases": ["군만두", "찐만두", "물만두"],
        "kcal": 210, "carbs": 22.0, "protein": 7.5, "fat": 10.0,
        "sugar": 1.5, "fiber": 1.2, "sodium": 480, "gi": 60,
        "portion_g": 180, "category": "분식"
    },
    "김치전": {
        "aliases": ["부침개", "파전", "전"],
        "kcal": 185, "carbs": 20.0, "protein": 4.5, "fat": 9.5,
        "sugar": 1.5, "fiber": 1.0, "sodium": 420, "gi": 65,
        "portion_g": 200, "category": "분식"
    },
    "피자": {
        "aliases": [],
        "kcal": 266, "carbs": 33.0, "protein": 11.0, "fat": 10.0,
        "sugar": 3.5, "fiber": 2.0, "sodium": 580, "gi": 60,
        "portion_g": 200, "category": "양식"
    },
    "햄버거": {
        "aliases": ["버거"],
        "kcal": 254, "carbs": 28.0, "protein": 12.0, "fat": 11.0,
        "sugar": 5.0, "fiber": 1.5, "sodium": 520, "gi": 66,
        "portion_g": 220, "category": "양식"
    },
    "샌드위치": {
        "aliases": [],
        "kcal": 230, "carbs": 26.0, "protein": 9.0, "fat": 10.0,
        "sugar": 3.5, "fiber": 2.0, "sodium": 480, "gi": 55,
        "portion_g": 180, "category": "양식"
    },

    # ===== 반찬/밑반찬 =====
    "김치": {
        "aliases": ["배추김치", "포기김치"],
        "kcal": 18, "carbs": 2.5, "protein": 1.5, "fat": 0.3,
        "sugar": 1.5, "fiber": 2.0, "sodium": 620, "gi": 15,
        "portion_g": 50, "category": "반찬"
    },
    "깍두기": {
        "aliases": ["무김치"],
        "kcal": 22, "carbs": 3.5, "protein": 1.0, "fat": 0.2,
        "sugar": 2.0, "fiber": 1.5, "sodium": 580, "gi": 20,
        "portion_g": 50, "category": "반찬"
    },
    "계란후라이": {
        "aliases": ["계란프라이", "달걀프라이"],
        "kcal": 196, "carbs": 0.8, "protein": 13.0, "fat": 15.0,
        "sugar": 0.5, "fiber": 0, "sodium": 180, "gi": 0,
        "portion_g": 55, "category": "반찬"
    },
    "계란말이": {
        "aliases": ["계란롤"],
        "kcal": 156, "carbs": 2.0, "protein": 11.5, "fat": 11.0,
        "sugar": 1.2, "fiber": 0.2, "sodium": 240, "gi": 10,
        "portion_g": 120, "category": "반찬"
    },
    "콩나물무침": {
        "aliases": ["콩나물"],
        "kcal": 32, "carbs": 3.5, "protein": 3.5, "fat": 1.0,
        "sugar": 0.8, "fiber": 2.0, "sodium": 180, "gi": 15,
        "portion_g": 60, "category": "반찬"
    },
    "시금치무침": {
        "aliases": ["시금치나물"],
        "kcal": 38, "carbs": 3.0, "protein": 3.2, "fat": 1.8,
        "sugar": 0.5, "fiber": 2.5, "sodium": 220, "gi": 15,
        "portion_g": 60, "category": "반찬"
    },
    "멸치볶음": {
        "aliases": [],
        "kcal": 205, "carbs": 12.0, "protein": 22.0, "fat": 7.5,
        "sugar": 6.5, "fiber": 0.5, "sodium": 680, "gi": 35,
        "portion_g": 30, "category": "반찬"
    },
    "두부조림": {
        "aliases": ["두부"],
        "kcal": 95, "carbs": 3.5, "protein": 8.5, "fat": 5.5,
        "sugar": 1.5, "fiber": 0.5, "sodium": 380, "gi": 20,
        "portion_g": 100, "category": "반찬"
    },

    # ===== 샐러드/과일/야채 =====
    "샐러드": {
        "aliases": ["그린샐러드", "야채샐러드"],
        "kcal": 25, "carbs": 4.0, "protein": 1.5, "fat": 0.3,
        "sugar": 2.0, "fiber": 2.0, "sodium": 20, "gi": 15,
        "portion_g": 150, "category": "샐러드"
    },
    "닭가슴살샐러드": {
        "aliases": [],
        "kcal": 95, "carbs": 5.0, "protein": 15.0, "fat": 2.0,
        "sugar": 2.5, "fiber": 1.8, "sodium": 180, "gi": 20,
        "portion_g": 250, "category": "샐러드"
    },
    "과일": {
        "aliases": ["사과", "배", "바나나"],
        "kcal": 52, "carbs": 14.0, "protein": 0.3, "fat": 0.2,
        "sugar": 10.0, "fiber": 2.5, "sodium": 1, "gi": 38,
        "portion_g": 150, "category": "과일"
    },

    # ===== 음료/디저트 =====
    "아이스크림": {
        "aliases": [],
        "kcal": 207, "carbs": 24.0, "protein": 3.5, "fat": 11.0,
        "sugar": 21.0, "fiber": 0.5, "sodium": 80, "gi": 62,
        "portion_g": 100, "category": "디저트"
    },
    "케이크": {
        "aliases": ["조각케이크"],
        "kcal": 340, "carbs": 45.0, "protein": 4.5, "fat": 16.0,
        "sugar": 32.0, "fiber": 0.8, "sodium": 220, "gi": 70,
        "portion_g": 100, "category": "디저트"
    },
    "떡": {
        "aliases": ["가래떡", "인절미", "시루떡"],
        "kcal": 230, "carbs": 50.0, "protein": 4.5, "fat": 0.5,
        "sugar": 8.0, "fiber": 0.8, "sodium": 120, "gi": 85,
        "portion_g": 100, "category": "디저트"
    },
}


def search_food(name: str):
    """음식 이름으로 DB 검색 (별칭 포함)"""
    name = name.strip()
    # 정확 매칭
    if name in NUTRITION_DB:
        return name, NUTRITION_DB[name]
    # 별칭 매칭
    for key, data in NUTRITION_DB.items():
        if name in data.get("aliases", []):
            return key, data
    # 부분 매칭
    for key, data in NUTRITION_DB.items():
        if name in key or key in name:
            return key, data
        for alias in data.get("aliases", []):
            if name in alias or alias in name:
                return key, data
    return None, None


def calculate_nutrition(food_items: list) -> dict:
    """
    food_items: [{"name": "공기밥", "estimated_g": 210}, ...]
    합산된 영양성분 딕셔너리 반환
    """
    total = {
        "kcal": 0, "carbs": 0, "protein": 0, "fat": 0,
        "sugar": 0, "fiber": 0, "sodium": 0,
        "glycemic_load": 0,  # 당부하지수
    }
    details = []
    unrecognized = []

    for item in food_items:
        name = item.get("name", "")
        weight = float(item.get("estimated_g", 0))
        if weight <= 0:
            continue

        matched_name, data = search_food(name)
        if not data:
            unrecognized.append(name)
            continue

        factor = weight / 100.0
        item_nutrition = {
            "original_name": name,
            "matched_name": matched_name,
            "weight_g": weight,
            "kcal": round(data["kcal"] * factor, 1),
            "carbs": round(data["carbs"] * factor, 1),
            "protein": round(data["protein"] * factor, 1),
            "fat": round(data["fat"] * factor, 1),
            "sugar": round(data["sugar"] * factor, 1),
            "fiber": round(data["fiber"] * factor, 1),
            "sodium": round(data["sodium"] * factor, 1),
            "gi": data["gi"],
            "category": data.get("category", "기타"),
        }
        # 당부하지수 GL = (GI × 가용탄수화물) / 100
        available_carb = max(item_nutrition["carbs"] - item_nutrition["fiber"], 0)
        item_nutrition["gl"] = round(data["gi"] * available_carb / 100, 1)

        details.append(item_nutrition)

        total["kcal"] += item_nutrition["kcal"]
        total["carbs"] += item_nutrition["carbs"]
        total["protein"] += item_nutrition["protein"]
        total["fat"] += item_nutrition["fat"]
        total["sugar"] += item_nutrition["sugar"]
        total["fiber"] += item_nutrition["fiber"]
        total["sodium"] += item_nutrition["sodium"]
        total["glycemic_load"] += item_nutrition["gl"]

    total = {k: round(v, 1) for k, v in total.items()}
    return {"total": total, "details": details, "unrecognized": unrecognized}


def assess_diabetes_risk(total: dict) -> dict:
    """
    당뇨 환자 관점에서 식단 위험도 평가
    기준 (미국당뇨협회 ADA 및 대한당뇨병학회 가이드라인 참고):
      - 당부하지수 GL: <10 저, 10-20 중, >20 고
      - 1회 식사 탄수화물 권장: 45-60g (당뇨 환자)
      - 단순당(설탕 등): <25g/일 권장
      - 나트륨: 1회 식사 < 600mg 권장
    """
    gl = total["glycemic_load"]
    carbs = total["carbs"]
    sugar = total["sugar"]
    sodium = total["sodium"]
    fiber = total["fiber"]

    # GL 평가
    if gl < 10:
        gl_level = "낮음"
        gl_color = "🟢"
    elif gl <= 20:
        gl_level = "중간"
        gl_color = "🟡"
    else:
        gl_level = "높음"
        gl_color = "🔴"

    # 탄수화물 평가 (당뇨 환자 기준 1회 식사 45-60g)
    if carbs <= 60:
        carb_level = "적정"
    elif carbs <= 90:
        carb_level = "다소 많음"
    else:
        carb_level = "과다"

    # 혈당 스파이크 예측
    # GI 가중평균 + 식이섬유/지방/단백질 보정
    spike_score = gl * 2 - fiber * 1.5 - total["protein"] * 0.3 - total["fat"] * 0.2
    if spike_score < 10:
        spike = "낮음 (급격한 혈당 상승 가능성 적음)"
        spike_color = "🟢"
    elif spike_score < 25:
        spike = "중간 (식후 1-2시간 혈당 주의)"
        spike_color = "🟡"
    else:
        spike = "높음 (큰 혈당 스파이크 예상)"
        spike_color = "🔴"

    # 종합 판정
    risk_points = 0
    if gl > 20: risk_points += 2
    elif gl > 10: risk_points += 1
    if carbs > 90: risk_points += 2
    elif carbs > 60: risk_points += 1
    if sugar > 25: risk_points += 2
    elif sugar > 15: risk_points += 1
    if sodium > 1200: risk_points += 1

    if risk_points <= 1:
        overall = "당뇨 환자도 섭취 가능"
        overall_color = "🟢"
        advice = "균형잡힌 식사입니다. 천천히 꼭꼭 씹어드시고, 식사 후 가벼운 산책을 권장합니다."
    elif risk_points <= 3:
        overall = "주의 필요 (조절하여 섭취)"
        overall_color = "🟡"
        advice = "탄수화물이 다소 많습니다. 밥의 양을 줄이거나, 채소/단백질 반찬을 먼저 드시면 혈당 상승이 완만해집니다."
    else:
        overall = "당뇨 환자 섭취 권장하지 않음"
        overall_color = "🔴"
        advice = "혈당 스파이크 위험이 높습니다. 탄수화물/당분을 절반 이하로 줄이거나 다른 메뉴를 고려하세요. 꼭 드셔야 한다면 식사 전 채소 섭취, 식후 30분 운동을 권장합니다."

    return {
        "overall": overall,
        "overall_color": overall_color,
        "advice": advice,
        "gl_level": gl_level,
        "gl_color": gl_color,
        "gl_value": gl,
        "carb_level": carb_level,
        "spike": spike,
        "spike_color": spike_color,
        "spike_score": round(max(spike_score, 0), 1),
        "risk_points": risk_points,
    }
