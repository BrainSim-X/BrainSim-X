import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Simulated years since diagnosis and cognitive scores
years = np.arange(0, 10, 1)
cognitive_scores = 30 - years * (np.random.normal(3, 0.5, len(years))) + np.random.normal(0, 1, len(years))

# Create DataFrame for simplicity
data = np.array(list(zip(years, cognitive_scores)))

# Regression modeling
X = data[:, 0].reshape(-1, 1)  # Use years as features
y = data[:, 1]  # Cognitive scores as targets
model = LinearRegression()
model.fit(X, y)

# Predictions
predicted_scores = model.predict(X)

# Plotting the results
plt.figure(figsize=(8, 5))
plt.scatter(X, y, color='orange', label='Observed Data')
plt.plot(X, predicted_scores, color='red', linewidth=2, label='Regression Line')
plt.title("Model of Alzheimer's Disease Progression")
plt.xlabel('Years Since Diagnosis')
plt.ylabel('Cognitive Score')
plt.legend()
plt.show()
