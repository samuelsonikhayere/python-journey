# Author: Samson Samuel Ikhayere
# Date: August 2026

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set style
plt.style.use('seaborn-v0_8-darkgrid')

# ============================================================================
# 1. GENERATE DATA
# ============================================================================

np.random.seed(42)
gene_data = np.random.randn(200, 6)    # 200 cells, 6 genes
gene_data[:100, :3] += 2               # Introduce structure in first 100 cells

print("Data shape:", gene_data.shape)
print("First 5 rows:\n", gene_data[:5, :])

# ============================================================================
# 2. COMPUTE COVARIANCE MATRIX
# ============================================================================

cov_matrix = np.cov(gene_data, rowvar=False)
print("\nCovariance Matrix (6x6):\n", cov_matrix)

# ============================================================================
# 3. COMPUTE EIGENVALUES AND EIGENVECTORS
# ============================================================================

eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
print("\nEigenvalues (pre-sort):", eigenvalues)

# ============================================================================
# 4. SORT BY EIGENVALUE (DESCENDING)
# ============================================================================

sort_idx = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[sort_idx]
eigenvectors = eigenvectors[:, sort_idx]

print("\nEigenvalues (post-sort):", eigenvalues)
print("\nEigenvectors (post-sort):\n", eigenvectors)

# ============================================================================
# 5. CALCULATE VARIANCE EXPLAINED
# ============================================================================

explained_variance = eigenvalues / eigenvalues.sum()
cumulative_variance = np.cumsum(explained_variance)

print("\nVariance Explained:")
for i, (ev, cv) in enumerate(zip(explained_variance, cumulative_variance), 1):
    print(f"PC{i}: {ev:.2%} (Cumulative: {cv:.2%})")

# ============================================================================
# 6. SCREE PLOT
# ============================================================================

fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle('Principal Component Analysis', fontsize=16, fontweight='bold')

# Scree plot (individual variance)
axes[0].bar(range(1, len(explained_variance)+1), explained_variance, 
            color='steelblue', alpha=0.7)
axes[0].set_xlabel('Principal Component')
axes[0].set_ylabel('Variance Explained')
axes[0].set_title('Scree Plot', fontweight='bold')
axes[0].set_xticks(range(1, len(explained_variance)+1))
axes[0].grid(True, alpha=0.3)

# Cumulative variance
axes[1].plot(range(1, len(cumulative_variance)+1), cumulative_variance, 
             'ro-', linewidth=2, markersize=8)
axes[1].axhline(y=0.95, color='red', linestyle='--', alpha=0.7, 
                label='95% threshold')
axes[1].axhline(y=0.90, color='orange', linestyle='--', alpha=0.7,
                label='90% threshold')
axes[1].set_xlabel('Number of Components')
axes[1].set_ylabel('Cumulative Variance Explained')
axes[1].set_title('Cumulative Variance', fontweight='bold')
axes[1].set_xticks(range(1, len(cumulative_variance)+1))
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# ============================================================================
# 7. PROJECT DATA ONTO TOP 2 COMPONENTS
# ============================================================================

# Project data
projected_data = gene_data @ eigenvectors[:, :2]

print("\nProjected data shape:", projected_data.shape)
print("First 5 projected points:\n", projected_data[:5, :])

# ============================================================================
# 8. VISUALIZE PCA PROJECTION
# ============================================================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('PCA Projection of Gene Expression Data', fontsize=16, fontweight='bold')

# Panel 1: Color by group (first 100 vs last 100)
ax1.scatter(projected_data[:100, 0], projected_data[:100, 1], 
           c='blue', label='First 100 cells', alpha=0.7, s=50)
ax1.scatter(projected_data[100:, 0], projected_data[100:, 1], 
           c='red', label='Last 100 cells', alpha=0.7, s=50)
ax1.set_xlabel('PC1', fontsize=12)
ax1.set_ylabel('PC2', fontsize=12)
ax1.set_title('Color by Group', fontweight='bold')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Panel 2: Color by gene expression (e.g., gene 0)
scatter = ax2.scatter(projected_data[:, 0], projected_data[:, 1], 
                     c=gene_data[:, 0], cmap='coolwarm', 
                     alpha=0.7, s=50)
ax2.set_xlabel('PC1', fontsize=12)
ax2.set_ylabel('PC2', fontsize=12)
ax2.set_title('Color by Gene 0 Expression', fontweight='bold')
ax2.grid(True, alpha=0.3)
cbar = plt.colorbar(scatter, ax=ax2)
cbar.set_label('Gene 0 Expression', fontsize=11)

plt.tight_layout()
plt.show()

# ============================================================================
# 9. INTERPRETATION
# ============================================================================

print("\n" + "="*70)
print("INTERPRETATION")
print("="*70)

print("\n1. SCREE PLOT:")
print("   - The first PC explains {:.1%} of variance".format(explained_variance[0]))
print("   - The first 2 PCs explain {:.1%} of variance".format(cumulative_variance[1]))
print("   - The first 3 PCs explain {:.1%} of variance".format(cumulative_variance[2]))

print("\n2. PCA PROJECTION:")
print("   - First 100 cells (blue) cluster separately from last 100 (red)")
print("   - This separation is captured by PC1 (x-axis)")
print("   - This confirms the artificial structure we introduced!")
print("   - PC1 likely represents the +2 difference in first 3 genes")

print("\n3. COMPONENT INTERPRETATION:")
print("   - PC1 separates groups: Positive vs Negative cells")
print("   - PC2 captures variation within groups")
print("   - Higher PCs likely represent noise")

print("\n" + "="*70)
