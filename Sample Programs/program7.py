import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load Dataset
df = pd.read_csv("housedata.csv")

# Features and Target
X = df[["Square_Feet"]]
y = df["Price_Lakhs"]

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict Price
predicted_price = model.predict([[1500]])

print("Predicted House Price:", round(predicted_price[0], 2), "Lakhs")