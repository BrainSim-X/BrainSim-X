Lesson 7: Advanced Regression Techniques 

7.1 Gaussian Processes for Neuroimaging Predictions 

Understanding Gaussian Processes (GPs): Gaussian Processes are a non-parametric, Bayesian 
approach to regression that provides not only predictions but also measures of uncertainty for 
those predictions. 

Key Features: 

 Distribution Over Functions: Instead of providing a single prediction, GPs define a 
distribution of possible functions that fit the data, giving credibility to uncertainty 
assessments. 

 Kernel Function: GPs utilize kernel functions to encode assumptions about the 
function's smoothness and other properties, essential for determining covariance 
structure. 

Mathematical Foundation: For any finite collection of points X = [x₁, x₂, ..., xₙ], the prior 
distribution of the function values f(X) can be characterized as: 

f(X) ~ 𝒩(μ, K(X, X)) 

Where: 

 K(X, X) is the covariance matrix defined by a chosen kernel and μ is the mean function. 

7.2 Time-Series Modeling for Neural Activity 

Utilizing Time-Series Data: Neuroimaging often involves time-series data, such as fMRI or 
EEG recordings. Analyzing these data types with techniques suited to temporal processes is 
crucial. 

Temporal Models: 

 Autoregressive Integrated Moving Average (ARIMA): A widely applied time-series 
method for forecasting that can include seasonal components. 
 State Space Models: Offers flexibility for modeling complex dynamics that evolve over 
time. 

Challenge in Neural Activity Data: The temporal interdependencies, variability, and noise in 
the signals pose challenges that require robust statistical approaches. 
7.3 Hands-on Implementation: Apply Gaussian Processes 

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
plt.fill_between(X_pred.ravel(), y_pred - 1.96 * sigma, y_pred + 1.96 * 
sigma,  
alpha=0.2, color='lightblue') 
plt.title("Gaussian Process Regression & Confidence Intervals") 
plt.xlabel('Input Feature') 
plt.ylabel('Signal Value') 
plt.legend() 
plt.show() 

Explanation: This example utilizes Gaussian Processes for predicting a sine wave, allowing 
students to visualize how uncertainty is quantified alongside predictions, an invaluable skill in 
neuroimaging analysis. 
