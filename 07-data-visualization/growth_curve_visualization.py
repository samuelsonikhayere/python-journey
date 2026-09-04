# Author: Samson Samuel Ikhayere
# Date: August 2026

import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches

od_data = np.array([
    [0.05,0.08,0.15,0.31,0.58,0.89,1.12,1.31,1.40,1.44,1.45,1.44,1.43],
    [0.05,0.06,0.09,0.14,0.24,0.45,0.78,1.05,1.28,1.38,1.42,1.41,1.40],
    [0.05,0.12,0.28,0.61,0.98,1.18,1.30,1.36,1.39,1.40,1.40,1.39,1.38],
])
timepoints = np.arange(0, 26, 2)
strains    = ["Strain A", "Strain B", "Strain C"]


# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# Plot each strain with different marker and color
markers = ['o', 's', '^']
colors = ["#0b5c96", "#f17304", "#05a705"]

fig, ax = plt.subplots(figsize=(11, 8))

for i, strain in enumerate(strains):
    ax.plot(timepoints, od_data[i], 
            marker=markers[i],
            markersize=5,
            linestyle='-', 
            linewidth=2,
            color=colors[i], 
            label=strain,
            alpha=0.8)

# Horizontal dashed line at OD = 1.0
ax.axhline(y=1.0, color = 'red', linestyle = '--', linewidth = 2)

# Shaded regions
ax.axvspan (0,4, alpha = 0.12, color = 'grey')
ax.axvspan (0,16, alpha = 0.12, color = 'blue')
ax.axvspan (16,24, alpha = 0.12, color = 'green')

#Title and Labels
ax.set_title("Growth Curve Visualisation", fontweight='bold', fontsize = 14)
ax.set_xlabel("Time (Hours)", fontweight='bold', fontsize = 12)
ax.set_ylabel("Optical Density (OD600)", fontweight='bold', fontsize = 12)

# Axis limits
ax.set_xlim(0, 26)
ax.set_ylim(0, 2)

# Legend
ax.legend(strains, fontsize=11, loc="upper left")

plt.tight_layout()
plt.show()

#Save high-res PNG before showing
plt.savefig("growth_curves.png", dpi=300, bbox_inches="tight")
