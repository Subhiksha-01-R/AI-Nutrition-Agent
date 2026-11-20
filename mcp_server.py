
import pandas as pd
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("AI Nutrition Server")


@mcp.tool()
def calculate_bmi(weight: float, height: float) -> dict:
    """Calculate BMI using weight in kg and height in cm."""

    height_m = height / 100
    bmi = weight / (height_m ** 2)

    return {"bmi": round(bmi, 2)}


@mcp.tool()
def lookup_food(food_name: str, grams: float = 100) -> dict:
    """Look up food nutrition from foods.csv."""

    df = pd.read_csv("data/foods.csv")

    food = df[
        df["food"].str.contains(
            food_name, case=False, na=False, regex=False
        )
    ]

    if food.empty:
        return {"error": "Food not found"}

    item = food.iloc[0]

    return {
        "food": item["food"],
        "quantity_grams": grams,
        "calories": round(float(item["calories_kcal"]) * grams / 100, 2),
        "protein": round(float(item["protein_g"]) * grams / 100, 2),
        "carbs": round(float(item["carbs_g"]) * grams / 100, 2),
        "fat": round(float(item["fat_g"]) * grams / 100, 2)
    }


@mcp.tool()
def suggest_meals(preference: str) -> dict:
    """Suggest meals based on food preference."""

    meals = {
        "vegetarian": ["Idli", "Vegetable rice", "Chapati"],
        "non-vegetarian": ["Egg rice", "Chicken rice", "Fish curry"],
        "vegan": ["Vegetable salad", "Fruit bowl", "Dal rice"]
    }

    return {
        "preference": preference,
        "meals": meals.get(
            preference.lower(),
            ["Preference not found"]
        )
    }


if __name__ == "__main__":
    mcp.run()
