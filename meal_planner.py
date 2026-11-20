def generate_meal_plan(preference: str, goal: str, allergies: str = "") -> dict:
    if preference == "Vegan":
        meals = {
            "Breakfast": "Vegetable oats or idli with sambar (check ingredients)",
            "Lunch": "Rice or millet with dal, vegetables, and tofu",
            "Snack": "Seasonal fruit with roasted chana",
            "Dinner": "Chapati with chickpea curry and vegetables",
        }
    elif preference == "Vegetarian":
        meals = {
            "Breakfast": "Idli with sambar and a serving of fruit",
            "Lunch": "Rice or millet with dal, vegetables, and curd",
            "Snack": "Seasonal fruit with nuts or roasted chana",
            "Dinner": "Chapati with paneer/tofu curry and vegetables",
        }
    else:
        meals = {
            "Breakfast": "Idli with sambar and boiled egg",
            "Lunch": "Rice with chicken or fish, vegetables, and curd",
            "Snack": "Seasonal fruit with nuts",
            "Dinner": "Chapati with egg/chicken curry and vegetables",
        }

    if goal == "Weight loss":
        note = "Use satisfying portions, include vegetables and protein, and limit sugary drinks; avoid skipping meals."
    elif goal == "Weight gain":
        note = "Consider adding nourishing snacks and energy-dense foods such as nuts, seeds, dairy or suitable alternatives."
    else:
        note = "Aim for variety, regular meals, adequate hydration, and portions that suit your hunger and activity."

    avoid = allergies.strip()
    if avoid:
        note += f" Important: review every ingredient and label to avoid your stated restriction(s): {avoid}."
    meals["General note"] = note
    return meals
