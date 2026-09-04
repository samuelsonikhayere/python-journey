# Author: Samson Samuel Ikhayere
# Date: August 2026

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Data
X = np.array([
    [25, 8.2, 12.1, 45.0],
    [67, 14.1, 9.8, 98.0],
    [34, 6.5, 13.4, 22.0],
    [45, 11.2, 10.5, 76.0],
    [58, 9.8, 11.8, 55.0],
], dtype=float)

y = np.array([45.0, 98.0, 22.0, 76.0, 55.0])

# 1. X.T @ X
XT_X = X.T @ X
print(f"X.T @ X shape: {XT_X.shape}\n")

# 2. Add bias and solve
X_design = np.column_stack([np.ones(len(X)), X])
weights = np.linalg.inv(X_design.T @ X_design) @ X_design.T @ y

print(f"Weights: {weights}\n")

# 3. Predictions and residuals
y_pred = X_design @ weights
residuals = y - y_pred

print(f"Predictions: {y_pred}")
print(f"Residuals: {residuals}\n")

# 4. R²
y_mean = np.mean(y)
SS_tot = np.sum((y - y_mean) ** 2)
SS_res = np.sum((y - y_pred) ** 2)
R_squared = 1 - SS_res / SS_tot

print(f"R² = {R_squared:.4f}")
