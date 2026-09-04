# Author: Samson Samuel Ikhayere
# Date: August 2026

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================================================
# 1. DATA DEFINITION
# ============================================================================

isolates = {
    "EC1": [0.82, 0.15, 1.20, 0.45],
    "EC2": [0.79, 0.18, 1.15, 0.42],
    "SA1": [0.31, 0.85, 0.45, 1.20],
    "SA2": [0.28, 0.91, 0.40, 1.25],
    "KP1": [0.55, 0.50, 0.80, 0.75],
    "KP2": [0.58, 0.48, 0.82, 0.71],
}

# Convert to numpy array for easier computation
isolate_names = list(isolates.keys())
isolate_matrix = np.array([isolates[name] for name in isolate_names])

print("="*70)
print("BACTERIAL ISOLATE DATA")
print("="*70)
print(f"Number of isolates: {len(isolate_names)}")
print(f"Number of features: {isolate_matrix.shape[1]}")
print("\nFeature matrix:")
print(pd.DataFrame(isolate_matrix, 
                   index=isolate_names,
                   columns=['Feature1', 'Feature2', 'Feature3', 'Feature4']))
print("="*70)

keys = list(isolates.keys())
n = len(keys)

# Initialize a 6x6 matrix of zeros
matrix = np.zeros((n, n))

# Calculate pairwise distance between every pair
for i in range(n):
    for j in range(n):
        vec_i = np.array(isolates[keys[i]])
        vec_j = np.array(isolates[keys[j]])
        # Euclidean distance formula using NumPy
        matrix[i, j] = np.sqrt(np.sum((vec_i - vec_j) ** 2))

# Convert to a labeled Pandas DataFrame
dist_df = pd.DataFrame(matrix, index=keys, columns=keys)

plt.figure(figsize=(7, 6))
# 'annot=True' prints numerical values inside each cell
# 'cmap="Blues_r"' or 'viridis_r' uses darker colors for SMALLER distances
sns.heatmap(dist_df, annot=True, fmt=".3f", cmap="YlGnBu_r")

plt.title("Euclidean Distance Matrix of Bacterial Isolates", fontweight="bold")
plt.tight_layout()
plt.show()
