import streamlit as st
import pandas as pd
from nutrition import calculate_bmi, bmi_category, calculate_bmr, calculate_tdee, calorie_guidance
from food_data import load_foods, nutrition_for_food
from meal_planner import generate_meal_plan
from ai_agent import ask_ai

st.set_page_config(page_title="NutriAI | Nutrition Assistant", page_icon="🥗", layout="wide")

st.title("🥗 NutriAI — AI Nutrition Assistant")
st.caption("A learning/demo project for nutrition education. Estimates are not medical advice.")

foods = load_foods()

with st.sidebar:
    st.header("Your profile")
    age = st.number_input("Age (years)", min_value=18, max_value=100, value=25)
    sex = st.selectbox("Sex used for calorie equation", ["Female", "Male"])
    height = st.number_input("Height (cm)", min_value=100.0, max_value=230.0, value=160.0, step=1.0)
    weight = st.number_input("Weight (kg)", min_value=25.0, max_value=250.0, value=60.0, step=0.5)
    activity = st.selectbox("Activity level", ["Sedentary", "Lightly active", "Moderately active", "Very active", "Extra active"])
    goal = st.selectbox("Goal", ["Maintain weight", "Weight loss", "Weight gain"])
    preference = st.selectbox("Food preference", ["Vegetarian", "Non-vegetarian", "Vegan"])
    allergies = st.text_input("Allergies / foods to avoid (optional)")

bmi = calculate_bmi(weight, height)
bmr = calculate_bmr(age, weight, height, sex)
tdee = calculate_tdee(bmr, activity)
guidance = calorie_guidance(tdee, goal)

tab1, tab2, tab3, tab4 = st.tabs(["📊 Dashboard", "🍽️ Meal planner", "🥑 Food tracker", "💬 AI nutrition chat"])

with tab1:
    st.subheader("Your estimated nutrition overview")
    c1, c2, c3 = st.columns(3)
    c1.metric("BMI", f"{bmi:.1f}", bmi_category(bmi))
    c2.metric("BMR", f"{bmr:,.0f} kcal/day")
    c3.metric("Estimated maintenance calories", f"{tdee:,.0f} kcal/day")
    st.info(guidance)
    st.markdown("""
    **What these numbers mean**
    - **BMI** is a screening measure based on height and weight; it does not measure body composition.
    - **BMR** estimates energy used at rest.
    - **TDEE** estimates daily energy use after activity is considered.
    """)
    st.warning("Calorie estimates are approximate. Do not use this demo to manage pregnancy, eating disorders, chronic illness, or medical diets. Consult a registered dietitian or clinician for individual medical advice.")

with tab2:
    st.subheader("Meal ideas")
    st.write("These are example meal ideas, not a prescribed diet. Adjust portions and ingredients to your needs.")
    if st.button("Generate meal ideas", type="primary"):
        plan = generate_meal_plan(preference, goal, allergies)
        for meal, idea in plan.items():
            st.markdown(f"**{meal}:** {idea}")
    else:
        st.caption("Choose your profile in the sidebar, then select Generate meal ideas.")

with tab3:
    st.subheader("Daily food tracker")
    if "food_log" not in st.session_state:
        st.session_state.food_log = []

    food_names = foods["food"].tolist()
    selected_food = st.selectbox("Food", food_names)
    grams = st.number_input("Amount (grams)", min_value=1, max_value=2000, value=100, step=10)
    if st.button("Add food to today's log"):
        item = nutrition_for_food(selected_food, grams, foods)
        st.session_state.food_log.append(item)
        st.success(f"Added {grams} g of {selected_food}.")

    if st.session_state.food_log:
        log_df = pd.DataFrame(st.session_state.food_log)
        st.dataframe(log_df, use_container_width=True, hide_index=True)
        totals = log_df[["calories_kcal", "protein_g", "carbs_g", "fat_g"]].sum()
        a, b, c, d = st.columns(4)
        a.metric("Calories", f"{totals['calories_kcal']:.0f} kcal")
        b.metric("Protein", f"{totals['protein_g']:.1f} g")
        c.metric("Carbs", f"{totals['carbs_g']:.1f} g")
        d.metric("Fat", f"{totals['fat_g']:.1f} g")
        csv = log_df.to_csv(index=False).encode("utf-8")
        st.download_button("Download food log (CSV)", csv, "nutrition_food_log.csv", "text/csv")
        if st.button("Clear today's food log"):
            st.session_state.food_log = []
            st.rerun()
    else:
        st.caption("No foods logged yet. Add a food above to see estimated nutrient totals.")
    st.caption("Food values are illustrative averages per 100 g and vary by brand, recipe, and preparation.")

with tab4:
    st.subheader("Ask the nutrition assistant")
    st.write("Ask general questions about balanced meals, food groups, or nutrition basics.")
    question = st.text_area("Your question", placeholder="Example: What are vegetarian sources of protein?")
    if st.button("Send question", type="primary"):
        if not question.strip():
            st.warning("Please enter a question.")
        else:
            with st.spinner("Preparing an answer..."):
                answer = ask_ai(
                    question=question,
                    age=age,
                    weight=weight,
                    height=height,
                    goal=goal,
                    preference=preference,
                    allergies=allergies,
                )
            st.markdown(answer)

st.divider()
st.caption("NutriAI demo • Built with Python and Streamlit • Not a substitute for professional healthcare.")
