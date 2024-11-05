# predict_early_pregnancy.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

# Step 1: Load the data
data = pd.read_csv('early_pregnancy_data.csv')  # Update with your CSV file path

# Step 2: Explore the data
print(data.head())
print(data.describe())
print(data.info())

# Step 3: Data Preprocessing
# Handle missing values
data.fillna(method='ffill', inplace=True)

# Example: Encoding categorical variables (customize as needed)
data = pd.get_dummies(data, columns=['education_level'])  # Change 'education_level' to your column name

# Normalize numerical values (if needed)
scaler = StandardScaler()
data[['age']] = scaler.fit_transform(data[['age']])  # Normalize 'age' column

# Step 4: Feature Selection
features = data[['age', 'previous_pregnancies']]  # Adjust features as needed
target = data['early_pregnancy']  # Adjust target column name

# Step 5: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Step 6: Choose a Predictive Model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Step 7: Model Evaluation
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print(f'Mean Squared Error: {mse}')
print(f'R² Score: {r2}')

# Step 8: Future Predictions
# Example future data (adjust as needed)
future_data = pd.DataFrame({
    'age': [16, 18],  # Example ages
    'previous_pregnancies': [0, 1]  # Example previous pregnancies
})
# Normalize future data (if you normalized the training data)
future_data[['age']] = scaler.transform(future_data[['age']])  # Normalize 'age' column

# Make predictions
future_predictions = model.predict(future_data)
print(f'Predicted early pregnancies: {future_predictions}')
