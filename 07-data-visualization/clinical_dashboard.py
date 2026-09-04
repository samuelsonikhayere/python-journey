# Author: Samson Samuel Ikhayere
# Date: August 2026

import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("coolwarm")

#Load Data
df = pd.read_csv('C:\\Users\\USER\\Documents\\Data Analysis\\Python\\master_patient_data.csv')

fig, axes = plt.subplots(3, 2, figsize=(15, 5))

#Panel A — Histogram of patient ages with KDE
sns.histplot(data=df, x='Age', kde=True, color= 'steelblue', ax=axes[0,0])
axes[0,0].set_title("Histogram of patient ages with KDE", fontweight='bold', fontsize = 14)

#Panel B — Box plot of CRP by Diagnosis
sns.boxplot(x="Diagnosis", y="CRP", data=df, palette="Set2", ax=axes[0,1])
axes[0,1].set_title("Box plot of CRP by Diagnosis")

#Panel C — Count plot of Infection Severity
sns.countplot(x="Infection_severity", data=df, palette="Set3", ax=axes[1,0])
axes[1,0].set_title("Count plot of Infection Severity")

#Panel D — Scatter plot of WBC vs CRP coloured by Diagnosis
sns.scatterplot(x="WBC", y="CRP", data=df, hue="Diagnosis", s = 100, ax=axes[1,1])
axes[1,1].set_title("Scatter plot of WBC vs CRP coloured by Diagnosis")

#Panel E — Bar plot of mean Haemoglobin by Ward and Sex
sns.barplot(x= "Ward", y="Haemoglobin", data=df, palette="Set1", hue="Sex", ax=axes[2,0])
axes[2,0].set_title("Bar plot of mean Haemoglobin by Ward and Sex")
axes[2,0].legend(title="Sex", fontsize=11, loc="upper right")

#Panel F — Pie chart of Ward distribution
ward_counts = df['Ward'].value_counts()
colors2 = sns.color_palette("Set2", len(ward_counts))

wedges, texts, autotexts = axes[2,1].pie(
    ward_counts.values,
    labels=ward_counts.index,
    autopct='%1.1f%%',
    colors=colors2,
    startangle=90,
    textprops={'fontsize': 11}
)
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
axes[2,1].set_title('Ward', fontweight='bold', fontsize=14)

plt.tight_layout()
plt.show()

#Save high-res PNG before showing
#plt.savefig("clinical_dashboard.png", dpi=300, bbox_inches="tight")
