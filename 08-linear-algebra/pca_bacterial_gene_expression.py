# Author: Samson Samuel Ikhayere
# Date: August 2026

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.spatial.distance import euclidean

# Set style for publication-quality plots
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# ============================================================================
# 1. GENERATE DATA
# ============================================================================

np.random.seed(2026)

species = ["E_coli", "S_aureus", "K_pneumoniae"]
genes = ["virA", "virB", "toxC", "resD", "mobE", "capF", "invG", "secH"]

# Expression matrix: 30 isolates per species, 8 genes
E_coli = np.random.normal(loc=[3, 3, 2, 1, 4, 2, 3, 2], scale=0.5, size=(30, 8))
S_aureus = np.random.normal(loc=[1, 2, 4, 3, 2, 4, 1, 3], scale=0.5, size=(30, 8))
K_pneumo = np.random.normal(loc=[2, 1, 3, 4, 1, 3, 4, 2], scale=0.5, size=(30, 8))

# Combine into single matrix (90 isolates, 8 genes)
X = np.vstack([E_coli, S_aureus, K_pneumo])
labels = np.array([0]*30 + [1]*30 + [2]*30)  # 0=E_coli, 1=S_aureus, 2=K_pneumo

print("="*70)
print("GENE EXPRESSION DATA OVERVIEW")
print("="*70)
print(f"Data shape: {X.shape} (90 isolates × 8 genes)")
print(f"Species labels: {np.unique(labels)} (0=E_coli, 1=S_aureus, 2=K_pneumo)")
print(f"Genes: {genes}")
print("="*70)

# ============================================================================
# 2. COMPUTE MEAN EXPRESSION PROFILE PER SPECIES
# ============================================================================

mean_profiles = np.array([
    E_coli.mean(axis=0),
    S_aureus.mean(axis=0),
    K_pneumo.mean(axis=0)
])

print("\nMEAN EXPRESSION PROFILES (Shape: 3 species × 8 genes):")
mean_df = pd.DataFrame(mean_profiles, 
                       index=species, 
                       columns=genes)
print(mean_df.round(3))

# ============================================================================
# 3. PAIRWISE EUCLIDEAN DISTANCE BETWEEN SPECIES MEAN PROFILES
# ============================================================================

print("\n" + "="*70)
print("PAIRWISE DISTANCES BETWEEN SPECIES")
print("="*70)

distances = {}
for i, species1 in enumerate(species):
    for j, species2 in enumerate(species):
        if i < j:  # Only upper triangle
            dist = euclidean(mean_profiles[i], mean_profiles[j])
            distances[f"{species1} ↔ {species2}"] = dist

for pair, dist in distances.items():
    print(f"{pair}: {dist:.4f}")

# Find closest pair
closest_pair = min(distances, key=distances.get)
closest_dist = distances[closest_pair]
print(f"\nMost similar species: {closest_pair} (distance = {closest_dist:.4f})")

# Find most distant pair
furthest_pair = max(distances, key=distances.get)
furthest_dist = distances[furthest_pair]
print(f"Most different species: {furthest_pair} (distance = {furthest_dist:.4f})")

# ============================================================================
# 4. STANDARDISE X COLUMN-WISE (Z-SCORE)
# ============================================================================

# Z-score: (x - mean) / standard deviation
X_mean = X.mean(axis=0)
X_std = X.std(axis=0)
X_standardized = (X - X_mean) / X_std

print("\n" + "="*70)
print("STANDARDIZATION")
print("="*70)
print("Original data mean:", X.mean(axis=0).round(3))
print("Original data std:", X.std(axis=0).round(3))
print("\nAfter standardization:")
print("Mean:", X_standardized.mean(axis=0).round(10))  # Should be ~0
print("Std:", X_standardized.std(axis=0).round(10))    # Should be ~1

# ============================================================================
# 5. COMPUTE COVARIANCE MATRIX
# ============================================================================

# Covariance matrix (8x8)
cov_matrix = np.cov(X_standardized.T)
print("\nCOVARIANCE MATRIX (8x8):")
print(pd.DataFrame(cov_matrix, index=genes, columns=genes).round(3))

# ============================================================================
# 6. PERFORM EIGENDECOMPOSITION - SORT BY VARIANCE EXPLAINED
# ============================================================================

# Eigendecomposition
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

# Sort descending
idx = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[idx]
eigenvectors = eigenvectors[:, idx]

# Variance explained
explained_variance = eigenvalues / eigenvalues.sum()
cumulative_variance = np.cumsum(explained_variance)

print("\n" + "="*70)
print("PRINCIPAL COMPONENT ANALYSIS")
print("="*70)
print("Eigenvalues:", eigenvalues.round(4))
print("Explained variance:", explained_variance.round(4))
print("Cumulative variance:", cumulative_variance.round(4))

print(f"\nTop 2 PCs explain {cumulative_variance[1]:.1%} of variance")
print(f"Top 3 PCs explain {cumulative_variance[2]:.1%} of variance")

# ============================================================================
# 7. PROJECT ALL 90 ISOLATES ONTO TOP 2 PRINCIPAL COMPONENTS
# ============================================================================

# Select top 2 eigenvectors
top_2_eigenvectors = eigenvectors[:, :2]

# Project data (90 isolates × 2 components)
X_pca = X_standardized @ top_2_eigenvectors

print("\n" + "="*70)
print("PCA PROJECTION")
print("="*70)
print(f"Projected data shape: {X_pca.shape} (90 isolates × 2 PCs)")
print("First 5 isolates (PC1, PC2):")
print(X_pca[:5].round(4))

# ============================================================================
# 8. PLOT PCA SCATTER COLOURED BY SPECIES
# ============================================================================

# Create figure with multiple panels
fig, axes = plt.subplots(2, 3, figsize=(18, 12))
fig.suptitle('Bacterial Gene Expression Analysis', fontsize=18, fontweight='bold', y=0.98)

# Panel 1: PCA Scatter Plot
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
species_names = ['E. coli', 'S. aureus', 'K. pneumoniae']

for i, label in enumerate(np.unique(labels)):
    mask = labels == i
    axes[0, 0].scatter(X_pca[mask, 0], X_pca[mask, 1], 
                       c=colors[i], label=species_names[i], 
                       alpha=0.7, s=80, edgecolors='white', linewidth=0.5)

# Plot species means in PCA space
for i in range(3):
    mean_pca = X_pca[labels == i].mean(axis=0)
    axes[0, 0].scatter(mean_pca[0], mean_pca[1], 
                       c=colors[i], marker='*', s=300, 
                       edgecolors='black', linewidth=1,
                       label=f'{species_names[i]} mean')

axes[0, 0].set_xlabel(f'PC1 ({explained_variance[0]*100:.1f}% variance)', fontsize=12)
axes[0, 0].set_ylabel(f'PC2 ({explained_variance[1]*100:.1f}% variance)', fontsize=12)
axes[0, 0].set_title('PCA Projection of Bacterial Isolates', fontweight='bold', fontsize=13)
axes[0, 0].legend(loc='best', fontsize=10)
axes[0, 0].grid(True, alpha=0.3)

# Panel 2: Scree Plot
axes[0, 1].bar(range(1, len(explained_variance)+1), explained_variance, 
               color='steelblue', alpha=0.7, label='Individual')
axes[0, 1].plot(range(1, len(cumulative_variance)+1), cumulative_variance, 
                'ro-', linewidth=2, markersize=8, label='Cumulative')
axes[0, 1].axhline(y=0.95, color='red', linestyle='--', alpha=0.5, label='95% threshold')
axes[0, 1].set_xlabel('Principal Component', fontsize=12)
axes[0, 1].set_ylabel('Variance Explained', fontsize=12)
axes[0, 1].set_title('Scree Plot', fontweight='bold', fontsize=13)
axes[0, 1].set_xticks(range(1, len(explained_variance)+1))
axes[0, 1].legend()
axes[0, 1].grid(True, alpha=0.3)

# Panel 3: Loading Plot (Gene Contributions)
loadings = top_2_eigenvectors
for i, gene in enumerate(genes):
    axes[0, 2].arrow(0, 0, loadings[i, 0], loadings[i, 1], 
                     head_width=0.05, head_length=0.05, 
                     fc='red', ec='red', alpha=0.7)
    axes[0, 2].text(loadings[i, 0]*1.1, loadings[i, 1]*1.1, 
                    gene, fontsize=9)

# Add circle to show unit contribution
circle = plt.Circle((0, 0), 1, fill=False, linestyle='--', alpha=0.3)
axes[0, 2].add_artist(circle)
axes[0, 2].set_xlabel('PC1 Loading', fontsize=12)
axes[0, 2].set_ylabel('PC2 Loading', fontsize=12)
axes[0, 2].set_title('Gene Loadings on PC1 and PC2', fontweight='bold', fontsize=13)
axes[0, 2].axhline(y=0, color='black', linestyle='-', alpha=0.2)
axes[0, 2].axvline(x=0, color='black', linestyle='-', alpha=0.2)
axes[0, 2].grid(True, alpha=0.3)
axes[0, 2].set_aspect('equal')

# ============================================================================
# 9. HEATMAP OF MEAN EXPRESSION PER SPECIES VS GENE
# ============================================================================

# Panel 4: Heatmap of mean expression
sns.heatmap(mean_df, 
            annot=True, 
            fmt='.2f',
            cmap='RdYlBu_r',
            cbar_kws={'label': 'Mean Expression (log2)'},
            linewidths=0.5,
            ax=axes[1, 0])
axes[1, 0].set_title('Mean Expression Profile by Species', fontweight='bold', fontsize=13)
axes[1, 0].set_xlabel('Genes', fontsize=12)
axes[1, 0].set_ylabel('Species', fontsize=12)

# Panel 5: Gene expression comparison (bar plot of means)
x = np.arange(len(genes))
width = 0.25

for i, sp in enumerate(species):
    axes[1, 1].bar(x + i*width, mean_profiles[i], width, 
                   label=species_names[i], color=colors[i], alpha=0.7)

axes[1, 1].set_xlabel('Genes', fontsize=12)
axes[1, 1].set_ylabel('Mean Expression (log2)', fontsize=12)
axes[1, 1].set_title('Gene Expression Comparison Across Species', fontweight='bold', fontsize=13)
axes[1, 1].set_xticks(x + width)
axes[1, 1].set_xticklabels(genes, rotation=45)
axes[1, 1].legend()
axes[1, 1].grid(True, alpha=0.3, axis='y')

# ============================================================================
# 10. FIND TOP 2 GENES THAT VARY MOST BETWEEN SPECIES
# ============================================================================

# Calculate between-species variance for each gene
# Between-species variance = variance of species means
between_species_variance = mean_profiles.var(axis=0)

# Get top 2 genes
top_2_indices = np.argsort(between_species_variance)[::-1][:2]
top_2_genes = [genes[i] for i in top_2_indices]
top_2_variances = between_species_variance[top_2_indices]

# Panel 6: Top 2 genes visualization
for idx, (gene_idx, gene_name) in enumerate(zip(top_2_indices, top_2_genes)):
    # Boxplot of gene expression by species
    data_to_plot = []
    for i in range(3):
        if i == 0:
            data = E_coli[:, gene_idx]
        elif i == 1:
            data = S_aureus[:, gene_idx]
        else:
            data = K_pneumo[:, gene_idx]
        data_to_plot.append(data)
    
    bp = axes[1, 2].boxplot(data_to_plot, 
                           positions=[idx*3 + i for i in range(3)],
                           widths=0.6,
                           patch_artist=True,
                           boxprops=dict(facecolor='lightblue', alpha=0.7),
                           medianprops=dict(color='red', linewidth=2))

# Add species labels
axes[1, 2].set_xlabel('Species', fontsize=12)
axes[1, 2].set_ylabel('Expression (log2)', fontsize=12)
axes[1, 2].set_title(f'Top Variable Genes: {top_2_genes[0]} & {top_2_genes[1]}', 
                     fontweight='bold', fontsize=13)
axes[1, 2].set_xticks([1, 4, 7])
axes[1, 2].set_xticklabels(['E. coli', 'S. aureus', 'K. pneumoniae'])
axes[1, 2].grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('gene_expression_analysis.png', dpi=300, bbox_inches='tight')
print("\n✅ Figure saved as 'gene_expression_analysis.png'")
plt.show()

# ============================================================================
# 11. PRINT TOP 2 GENES
# ============================================================================

print("\n" + "="*70)
print("TOP 2 GENES THAT VARY MOST BETWEEN SPECIES")
print("="*70)

for i, (gene, variance) in enumerate(zip(top_2_genes, top_2_variances), 1):
    print(f"{i}. {gene}: between-species variance = {variance:.4f}")
    
    # Show species means for this gene
    means = [mean_profiles[0, top_2_indices[i-1]], 
             mean_profiles[1, top_2_indices[i-1]], 
             mean_profiles[2, top_2_indices[i-1]]]
    print(f"   E. coli: {means[0]:.3f}, S. aureus: {means[1]:.3f}, K. pneumoniae: {means[2]:.3f}")

# ============================================================================
# 12. INTERPRETATION
# ============================================================================

print("\n" + "="*70)
print("INTERPRETATION")
print("="*70)

print("""
KEY FINDINGS:
─────────────

1. Species Separation in PCA:
   • The three species form distinct clusters in PC space
   • PC1 explains the majority of variance, separating species
   • This confirms species-specific expression patterns

2. Most Similar Species:
   • {closest_pair} have the most similar expression profiles
   • Distance = {closest_dist:.4f}

3. Most Different Species:
   • {furthest_pair} have the most different expression profiles
   • Distance = {furthest_dist:.4f}

4. Key Discriminatory Genes:
   • {top_2_genes[0]} shows the greatest between-species variation
   • {top_2_genes[1]} shows the second greatest between-species variation
   • These genes are likely important for species-specific pathogenesis

5. Biological Interpretation:
   • E. coli: High expression of virA, virB (virulence factors)
   • S. aureus: High expression of toxC (toxin), capF (capsule)
   • K. pneumoniae: High expression of resD (resistance), invG (invasion)

6. Clinical Relevance:
   • These expression patterns may explain different disease presentations
   • Can be used for species identification in clinical samples
   • Potential therapeutic targets for each species
""".format(closest_pair=closest_pair, closest_dist=closest_dist,
           furthest_pair=furthest_pair, furthest_dist=furthest_dist,
           top_2_genes=top_2_genes))
