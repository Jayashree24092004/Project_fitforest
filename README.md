 FitForest AI – ML Integrated Fitness App

FitForest AI is a machine learning-powered fitness assistant that recommends personalized meal plans and workout routines based on user input.
For every completed workout, you plant a virtual tree  in your forest — helping you visualize your progress in a fun and eco-friendly way.


---

 Features

🔹 Personalized Recommendations – Meals & workouts based on age, gender, and fitness goal

🔹 ML Integration – Decision Tree classifier trained on user profile dataset

🔹 Interactive Workout Timer – Counts down workout duration entered by user

🔹 Gamification – Each workout = one virtual tree planted 

🔹 Progress Visualization – Graph shows your growing forest over time
 
 Installation

1. Clone this repository
git clone https://github.com/your-username/FitForest-AI.git
cd FitForest-AI

2. Install dependencies
pip install -r requirements.txt

3. Ensure data files are available
Place user_profiles.csv, meals.csv, and workouts.csv in the data/ folder.

Usage
Train the Model
python src/train_model.py
This will create model.pkl and encoders.pkl in the models/ directory.
Run the App
In Google Colab or locally:
python src/app.py

📊 Example Output

User Input:

Age: 25  
Gender: Male  
Goal: gain muscle  
Workout Time: 20 minutes

AI Recommendation:
Meal: High-protein chicken bowl 
Workout: Push-ups & Dumbbell Routine  
Duration: 20 minutes

Virtual Forest Progress:

Each completed workout adds one tree  to your forest.
<img width="697" height="639" alt="image" src="https://github.com/user-attachments/assets/79a66532-c9e8-43b8-9601-5cddc826e962" />





