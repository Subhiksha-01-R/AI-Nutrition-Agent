import os


def ask_ai(question: str, age: int, weight: float, height: float,
           goal: str, preference: str, allergies: str = "") -> str:
    """Optional OpenAI-powered chat. Without a key, return a useful local fallback."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return (
            "The AI connection is not configured yet. Set OPENAI_API_KEY in your environment "
            "to enable AI answers.\n\n"
            "**General guidance:** Build meals around vegetables or fruit, a protein source, "
            "whole grains or other starchy foods, and healthy fats. Nutrition needs vary by person. "
            "For medical conditions, allergies, pregnancy, or therapeutic diets, ask a qualified "
            "health professional."
        )

    try:
        from openai import OpenAI
        client = OpenAI(api_key=api_key)
        model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
        response = client.responses.create(
            model=model,
            instructions=(
                "You are a cautious nutrition education assistant. Give general, evidence-informed "
                "nutrition information in plain language. Do not diagnose, prescribe treatment, "
                "recommend supplements or extreme diets, or claim certainty about calorie needs. "
                "If the user mentions a medical condition, pregnancy, eating disorder, or serious "
                "symptoms, recommend a qualified clinician or registered dietitian."
            ),
            input=(
                f"Profile: age {age}; weight {weight} kg; height {height} cm; "
                f"goal {goal}; preference {preference}; foods/allergies to avoid: {allergies or 'not provided'}.\n"
                f"Question: {question}"
            ),
        )
        return response.output_text
    except Exception as exc:
        return (
            "I couldn't connect to the AI service. Check your API key, internet connection, "
            f"and account access. Technical detail: {exc}"
        )
