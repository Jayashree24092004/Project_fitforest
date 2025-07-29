
import pandas as pd
import time
import matplotlib.pyplot as plt

# Load data
user_df = pd.read_csv('user_input.csv')
meals_df = pd.read_csv('meals.csv')
workouts_df = pd.read_csv('workouts.csv')

# Rule-based plan mapping
def get_plan_id(goal):
    if goal == 'lose weight':
        return 0
    elif goal == 'gain muscle':
        return 1
    else:
        return 2

# Simulate for each user
tree_count = 0
for idx, row in user_df.iterrows():
    plan_id = get_plan_id(row['Goal'])

    meal = meals_df.loc[meals_df['PlanID'] == plan_id, 'Meal'].values[0]
    workout = workouts_df.loc[workouts_df['PlanID'] == plan_id, 'Workout'].values[0]

    print(f"\nUser {row['UserID']} - Goal: {row['Goal']}")
    print(f"Suggested Meal: {meal}")
    print(f"Suggested Workout: {workout}")
    print("Starting workout timer...")

    duration = int(row['Time'])
    for i in range(3, 0, -1):  # Shortened countdown for demo
        print(f"Workout ends in {i} seconds...", end='\r')
        time.sleep(1)

    print("Workout completed! 🌱 One tree planted!")
    tree_count += 1

# Visualize progress
plt.figure(figsize=(6, 4))
plt.bar(['Trees Grown'], [tree_count], color='green')
plt.title('Virtual Forest Growth')
plt.ylabel('Number of Trees')
plt.ylim(0, max(5, tree_count + 1))
plt.savefig('tree_progress.png')
plt.show()
