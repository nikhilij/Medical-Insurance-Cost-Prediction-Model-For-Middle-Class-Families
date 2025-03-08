import pandas as pd
import numpy as np
from faker import Faker

# Initialize Faker for realistic names and locations
fake = Faker()

# Define sample size
num_samples = 5000

# Generate dummy data
data = {
    "id": np.arange(1, num_samples + 1),
    "age": np.random.randint(18, 80, num_samples),
    "gender": np.random.choice(["Male", "Female"], num_samples),
    "region": np.random.choice(["North", "South", "East", "West"], num_samples),
    "bmi": np.round(np.random.uniform(15, 40, num_samples), 1),
    "smoker": np.random.choice(["Yes", "No"], num_samples, p=[0.2, 0.8]),
    "alcohol_consumption": np.random.choice(["Rarely", "Occasionally", "Frequently"], num_samples),
    "exercise_frequency": np.random.choice(["None", "Low", "Moderate", "High"], num_samples),
    "diet_type": np.random.choice(["Vegetarian", "Non-Vegetarian", "Vegan"], num_samples),
    "stress_level": np.random.choice(["Low", "Medium", "High"], num_samples),
    "medical_history_score": np.round(np.random.uniform(0, 1, num_samples), 2),
    "has_diabetes": np.random.choice(["Yes", "No"], num_samples, p=[0.15, 0.85]),
    "has_hypertension": np.random.choice(["Yes", "No"], num_samples, p=[0.2, 0.8]),
    "has_heart_disease": np.random.choice(["Yes", "No"], num_samples, p=[0.1, 0.9]),
    "has_cancer_history": np.random.choice(["Yes", "No"], num_samples, p=[0.05, 0.95]),
    "annual_income": np.random.randint(200000, 2000000, num_samples),
    "employment_type": np.random.choice(["Salaried", "Self-Employed", "Retired"], num_samples),
    "credit_score": np.random.randint(300, 900, num_samples),
    "savings_amount": np.random.randint(50000, 2000000, num_samples),
    "num_dependents": np.random.randint(0, 6, num_samples),
    "previous_insurance_claims": np.random.randint(0, 10, num_samples),
    "policy_type": np.random.choice(["Basic", "Comprehensive", "Premium"], num_samples),
    "policy_renewal_status": np.random.choice(["Yes", "No"], num_samples),
    "hospital_visits_per_year": np.random.randint(0, 10, num_samples),
    "annual_medical_expenses": np.random.randint(5000, 500000, num_samples),
    "medication_costs_per_year": np.random.randint(1000, 200000, num_samples)
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Calculate insurance cost based on risk factors
df["insurance_cost"] = (
    (df["age"] * 100) +
    (df["bmi"] * 500) +
    (df["smoker"].map({"Yes": 10000, "No": 0})) +
    (df["medical_history_score"] * 20000) +
    (df["num_dependents"] * 2000) +
    (df["has_diabetes"].map({"Yes": 5000, "No": 0})) +
    (df["has_hypertension"].map({"Yes": 3000, "No": 0})) +
    (df["has_heart_disease"].map({"Yes": 7000, "No": 0})) +
    (df["has_cancer_history"].map({"Yes": 15000, "No": 0})) +
    (df["hospital_visits_per_year"] * 2000) +
    (df["annual_medical_expenses"] * 0.1) -
    (df["annual_income"] * 0.002)
).astype(int)

# Save the dataset to CSV
df.to_csv("medical_insurance_dummy_data.csv", index=False)

# Display first few rows
print(df.head())
