def calculate_bmi(weight_kg: float, height_cm: float) -> float:
    if weight_kg <= 0 or height_cm <= 0:
        raise ValueError("Weight and height must be greater than zero.")
    height_m = height_cm / 100
    return weight_kg / (height_m ** 2)


def bmi_category(bmi: float) -> str:
    # General adult BMI screening categories; not intended for children or pregnancy.
    if bmi < 18.5:
        return "Below the usual adult reference range"
    if bmi < 25:
        return "Usual adult reference range"
    if bmi < 30:
        return "Above the usual adult reference range"
    return "Higher adult BMI range"


def calculate_bmr(age: int, weight_kg: float, height_cm: float, sex: str) -> float:
    """Mifflin-St Jeor estimate. The equation uses a binary sex coefficient."""
    base = 10 * weight_kg + 6.25 * height_cm - 5 * age
    if sex == "Male":
        return base + 5
    return base - 161


def calculate_tdee(bmr: float, activity: str) -> float:
    factors = {
        "Sedentary": 1.2,
        "Lightly active": 1.375,
        "Moderately active": 1.55,
        "Very active": 1.725,
        "Extra active": 1.9,
    }
    return bmr * factors[activity]


def calorie_guidance(tdee: float, goal: str) -> str:
    if goal == "Weight loss":
        estimate = max(0, tdee - 300)
        return (
            f"Your estimated maintenance energy is about {tdee:,.0f} kcal/day. "
            f"A modest illustrative planning estimate would be around {estimate:,.0f} kcal/day, "
            "but this is not a prescription. Avoid restrictive diets and seek professional guidance."
        )
    if goal == "Weight gain":
        estimate = tdee + 300
        return (
            f"Your estimated maintenance energy is about {tdee:,.0f} kcal/day. "
            f"An illustrative gradual-gain planning estimate would be around {estimate:,.0f} kcal/day. "
            "Individual needs vary; a dietitian can help set a suitable target."
        )
    return f"Your estimated maintenance energy is about {tdee:,.0f} kcal/day. This is an estimate, not an exact target."
