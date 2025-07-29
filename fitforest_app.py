import streamlit as st
import pandas as pd
import time

# Load data
meals_df = pd.read_csv("meals_data.csv")
workouts_df = pd.read_csv("workouts_data.csv")
profiles_file = "user_profiles.csv"

# Load or initialize user profiles
try:
    profiles_df = pd.read_csv(profiles_file)
except FileNotFoundError:
    profiles_df = pd.DataFrame(columns=["username", "goal", "food", "equipment", "time", "trees_planted"])

# --- App UI ---

st.title("🌱 FitForest – AI-Powered Fitness + Tree Planting App")

username = st.text_input("Enter your name")

if username:
    # Load existing or new user profile
    if username in profiles_df["username"].values:
        user_data = profiles_df[profiles_df["username"] == username].iloc[0]
        goal = user_data["goal"]
        food_type = user_data["food"]
        equipment = user_data["equipment"]
        time_available = int(user_data["time"])
        trees_planted = int(user_data["trees_planted"])
        st.success(f"Welcome back, {username}! 🌿")
    else:
        st.info("New user! Please answer a few questions to get started.")
        goal = st.selectbox("What is your fitness goal?", ["Lose weight", "Gain muscle", "Stay fit"])
        food_type = st.selectbox("What food do you usually eat?", ["Hostel food", "Local ingredients"])
        equipment = st.selectbox("Do you have any workout equipment?", ["None", "Basic (e.g., mat, dumbbell)"])
        time_available = st.slider("How much time can you exercise daily (in minutes)?", 5, 60, 15)
        trees_planted = 0

        # Save new user
        new_profile = pd.DataFrame([{
            "username": username,
            "goal": goal,
            "food": food_type,
            "equipment": equipment,
            "time": time_available,
            "trees_planted": trees_planted
        }])
        profiles_df = pd.concat([profiles_df, new_profile], ignore_index=True)
        profiles_df.to_csv(profiles_file, index=False)
        st.success("Profile created! 🎉")

    # --- Meal Suggestions ---
    st.header("🍽️ Today's Meal Plan")
    suggested_meals = meals_df[
        (meals_df["goal"] == goal) & 
        (meals_df["food_type"] == food_type)
    ]
    for idx, row in suggested_meals.iterrows():
        st.write(f"✅ {row['meal']}")

    # --- Workout Suggestions ---
    st.header("🏋️ Workout Plan")
    suggested_workouts = workouts_df[
        (workouts_df["goal"] == goal) &
        (workouts_df["equipment"] == equipment)
    ]
    st.write(f"Here’s a {time_available}-minute workout plan:")

    for idx, row in suggested_workouts.iterrows():
        st.write(f"🔥 {row['workout']} – {row['duration']} minutes")

    # --- Workout Timer ---
    st.header("⏱️ Start Workout")

    if st.button(f"Start {time_available}-Minute Workout Timer"):
        st.write(f"🏃 Workout started for {time_available} minutes... Timer running ⏳")

        workout_placeholder = st.empty()

        for minute in range(time_available, 0, -1):
            workout_placeholder.write(f"⏱️ {minute} minute(s) left...")
            time.sleep(60)

        st.success("✅ Workout complete! You planted a tree! 🌳")
        trees_planted += 1

        # Update user profile
        profiles_df.loc[profiles_df["username"] == username, "trees_planted"] = trees_planted
        profiles_df.to_csv(profiles_file, index=False)

    # --- Show Progress ---
    st.header("🌳 Your FitForest Progress")
    st.metric(label="Trees Planted", value=trees_planted)
