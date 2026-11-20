# NutriAI — AI Nutrition Assistant

A beginner-friendly Python + Streamlit project for nutrition education.

## Features
- Adult BMI estimate and category
- BMR and TDEE estimates
- General calorie guidance by goal
- Vegetarian, vegan, and non-vegetarian meal ideas
- Food tracker with estimated calories, protein, carbohydrates, and fat
- Optional AI chatbot using the OpenAI Responses API
- Download daily food log as CSV

## Requirements
- Python 3.10 or newer
- Internet access for optional AI chat
- An OpenAI API key for AI-powered responses (the rest of the app works without it)

## Setup

### Windows
```powershell
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

### macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Open the local URL shown in the terminal (usually http://localhost:8501).

## Enable the AI chatbot

PowerShell (current terminal only):
```powershell
$env:OPENAI_API_KEY="your-api-key"
$env:OPENAI_MODEL="gpt-4.1-mini"
streamlit run app.py
```

macOS / Linux:
```bash
export OPENAI_API_KEY="your-api-key"
export OPENAI_MODEL="gpt-4.1-mini"
streamlit run app.py
```

Never commit API keys to GitHub. For deployment, configure secrets/environment variables in your hosting provider.

## Project structure
```text
AI_Nutrition_Agent/
├── app.py
├── nutrition.py
├── food_data.py
├── meal_planner.py
├── ai_agent.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
└── data/
    └── foods.csv
```

## Notes and limitations
- This is an educational prototype, not a medical device or a replacement for a registered dietitian.
- BMI is a screening measure and does not diagnose health status.
- BMR/TDEE and calorie guidance are rough estimates. The BMR equation uses a binary sex coefficient and may not represent every individual.
- Food database values are approximate examples per 100 g. Real values vary by ingredients, brand, and preparation.
- The tracker stores entries only in the current Streamlit session; it does not use a persistent database.
- The meal planner creates general meal ideas, not medically tailored diets. Always verify ingredients for allergies and dietary restrictions.
