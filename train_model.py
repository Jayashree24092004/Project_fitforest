import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import pickle

# ✅ Corrected paths to data folder
df = pd.read_csv("data/user_input.csv")
workout_df = pd.read_csv("data/workouts.csv")
meal_df = pd.read_csv("data/meals.csv")
training_df = pd.read_csv("data/training_data.csv")


# Encode categorical features
le_goal = LabelEncoder()
le_food = LabelEncoder()
le_equip = LabelEncoder()

df['Goal'] = le_goal.fit_transform(df['Goal'])
df['Food Type'] = le_food.fit_transform(df['Food Type'])
df['Equipment'] = le_equip.fit_transform(df['Equipment'])

# For simplicity, create mock PlanID (labels) based on index
df['PlanID'] = df.index % len(workout_df)

# Features and labels
X = df[['Goal', 'Food Type', 'Equipment', 'Time']]
y = df['PlanID']

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save model
with open("ml_model/model.pkl", "wb") as f:
    pickle.dump({
        "model": model,
        "goal_enc": le_goal,
        "food_enc": le_food,
        "equip_enc": le_equip
    }, f)

print("✅ Model trained and saved to ml_model/model.pkl")
