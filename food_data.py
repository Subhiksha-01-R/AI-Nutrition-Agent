from pathlib import Path
import pandas as pd

DATA_FILE = Path(__file__).parent / "data" / "foods.csv"


def load_foods() -> pd.DataFrame:
    return pd.read_csv(DATA_FILE)


def nutrition_for_food(food: str, grams: int, foods: pd.DataFrame) -> dict:
    row = foods.loc[foods["food"] == food]
    if row.empty:
        raise ValueError("Food not found in the food database.")
    r = row.iloc[0]
    scale = grams / 100
    return {
        "food": food,
        "amount_g": grams,
        "calories_kcal": round(float(r["calories_kcal"]) * scale, 1),
        "protein_g": round(float(r["protein_g"]) * scale, 1),
        "carbs_g": round(float(r["carbs_g"]) * scale, 1),
        "fat_g": round(float(r["fat_g"]) * scale, 1),
    }
