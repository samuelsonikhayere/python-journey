# Author: Samson Samuel Ikhayere
# Date: August 2026

import pandas as pd
import numpy as np
import os

np.random.seed(10)

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "culture_results.csv")

df = pd.read_csv(csv_path)

#Select only the Organism and Result columns

df_re = df[['Organism', 'Result']]
#Filter rows where OD600 > 0.8
df_OD = df [
    df['OD600'] > 0.8
]
#Filter rows where Result is "Resistant" AND OD600 > 0.5
df_re_OD = df[
     (df['Result'] == 'Resistant') & (df['OD600'] > 0.5)
]
#Find all rows where Organism contains the word "aureus" (use .str.contains())
df_aureus = df[
    df['Organism'].str.contains("aureus")
]
#Select the last 3 rows using .iloc
df_3 = df.iloc[-3:-1, :]
