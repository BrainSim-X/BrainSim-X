import numpy as np
import matplotlib.pyplot as plt
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C

# Generate sample data
X = np.array([[1], [2], [3], [4], [5]])
y = np.sin(X).ravel()  # Sine function values

# Kernel definition
kernel = C(1.0, (1e-3, 1e3)) * RBF(1, (1e-2, 1e2))
gp = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=10)

# Fitting Gaussian Process model
gp.fit(X, y)

# Making predictions
X_pred = np.linspace(1, 5, 100).reshape(-1, 1)
y_pred, sigma = gp.predict(X_pred, return_std=True)

# Visualization of results
plt.figure(figsize=(10, 6))
plt.plot(X, y, 'or', label='Observed Data')
plt.plot(X_pred, y_pred, 'b-', label='Prediction')
plt.fill_between(X_pred.ravel(), y_pred - 1.96 * sigma, y_pred + 1.96 * sigma, alpha=0.2, color='lightblue')
plt.title("Gaussian Process Regression & Confidence Intervals")
plt.xlabel('Input Feature')
plt.ylabel('Signal Value')
plt.legend()
plt.show()
