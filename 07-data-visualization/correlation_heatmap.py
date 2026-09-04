# Author: Samson Samuel Ikhayere
# Date: August 2026

import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("coolwarm")

#Load Data
df = pd.read_csv('C:\\Users\\USER\\Documents\\Data Analysis\\Python\\master_patient_data.csv')

corr_matrx = df[['Age', 'WBC', 'CRP', 'Haemoglobin']].corr()

#fig, axes = plt.subplot(figsize=(11,8))

sns.heatmap(data=corr_matrx,
            cmap='coolwarm',
            vmax = 1,
            vmin = -1,
            fmt = '.2f',
            annot = True,
            linewidths = 2.0,
            square = True)

plt.title ('Correlation Between Age and Selected Clinical Biomarkers')
plt.tight_layout()
plt.show()

plt.savefig('correlation_heatmap.png', dpi=300, bbox_inches="tight")
