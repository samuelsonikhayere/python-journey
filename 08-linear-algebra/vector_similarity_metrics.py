# Author: Samson Samuel Ikhayere
# Date: August 2026

import numpy as np

# Data
patient_A = np.array([4.2, 1.8, 3.5, 6.1, 2.3, 0.9, 5.4, 3.1])
patient_B = np.array([1.1, 4.3, 2.8, 1.5, 7.2, 3.6, 1.2, 4.8])
gene_names = ["BRCA1", "TP53", "EGFR", "MYC", "ALK", "KRAS", "PTEN", "CDH1"]

# 1. Dot product
dot_product = np.dot(patient_A, patient_B)
print(f"1. Dot Product: {dot_product:.3f}")

# 2. Euclidean distance
euclidean_dist = np.linalg.norm(patient_A - patient_B)
print(f"2. Euclidean Distance: {euclidean_dist:.3f}")

# 3. Cosine similarity (FIXED: parentheses!)
cos_sim = np.dot(patient_A, patient_B) / (np.linalg.norm(patient_A) * np.linalg.norm(patient_B))
print(f"3. Cosine Similarity: {cos_sim:.3f}")

# 4. Normalize vectors
A_unit = patient_A / np.linalg.norm(patient_A)
B_unit = patient_B / np.linalg.norm(patient_B)
print(f"4. Magnitude of normalized A: {np.linalg.norm(A_unit):.3f}")
print(f"   Magnitude of normalized B: {np.linalg.norm(B_unit):.3f}")

# 5. Interpretation
print(f"\n5. Interpretation:")
print(f"   Cosine similarity = {cos_sim:.3f}")
print(f"   Angle = {np.arccos(cos_sim) * 180 / np.pi:.1f}°")
print(f"   Patients are moderately similar in expression profiles")
