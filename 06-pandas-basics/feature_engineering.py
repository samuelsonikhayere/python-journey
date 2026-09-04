# Author: Samson Samuel Ikhayere
# Date: August 2026

import pandas as pd
import numpy as np
import os

np.random.seed(10)
 
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "culture_results.csv")

df = pd.read_csv(csv_path)

#Add a column "OD_Class" using your classify_od logic from Concept 5
def classify_od(od):
    if od < 0.3:
        return "Low"
    elif od < 1.0:
        return "Medium"
    else:
        return "High"

df["OD_class"] = df["OD600"].apply(classify_od)

#Add a column "Growth_flag" that is "High growth" if OD600 > 1.0, otherwise "Normal"
df ["Growth_flag"] = np.where (df["OD600"] > 1.0, "High growth", "Normal")

#Add a column "Organism_short" containing only the first word of the organism name (e.g. "Pseudomonas" from "Pseudomonas aeruginosa")
df["Organism_short"] = df['Organism'].str.split().str[0]

#Convert the Result column to uppercase
df['Result'] = df['Result'].str.upper()
