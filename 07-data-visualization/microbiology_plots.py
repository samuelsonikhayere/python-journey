# Author: Samson Samuel Ikhayere
# Date: August 2026

import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("coolwarm")

fig, axes = plt.subplots(1, 2, figsize=(11, 8))

#Load culture_results.csv:
df = pd.read_csv("C:\\Users\\USER\\Documents\\Data Analysis\\Python\\py4e\\Day06\\culture_results.csv")

# A grouped bar chart showing count of Sensitive/Resistant/Intermediate results per Organism
sns.barplot(data=df,
            x='Organism',
            hue = 'Result',
            palette = 'Set2',
            ax=axes[0])

axes[0].set_title('Bar chart of Result per Organism', fontweight='bold', fontsize = 15)
axes[0].set_xlabel('Result (Sensitive/Resistant/Intermediate)', fontsize = 13)
axes[0].set_ylabel('Organism', fontsize = 13)
axes[0].tick_params(axis='x', rotation=45)
axes[0].legend(title='Result', fontsize=10)

sns.violinplot(data=df, 
               x= 'Organism',
               y='OD600',
               palette='Set2',
               ax=axes[1])

axes[1].set_title('OD600 distribution per Organism', fontweight='bold', fontsize = 15)
axes[1].set_xlabel('Organism', fontsize = 13)
axes[1].set_ylabel('Optical Density (OD600)', fontsize = 13)
axes[0].tick_params(axis='x', rotation=45)


plt.savefig('microbiology_plots.png', dpi=300, bbox_inches="tight")

plt.tight_layout()
plt.show()
