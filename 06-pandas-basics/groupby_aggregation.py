# Author: Samson Samuel Ikhayere
# Date: August 2026

import pandas as pd
import numpy as np
import os

np.random.seed(10)

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "culture_results.csv")

df = pd.read_csv(csv_path)

#Calculate mean and max OD600 per organism


Org_stat = df.groupby('Organism').agg({
    'OD600':['mean', 'max']
})
#Count how many samples per Result category
result_count = df.groupby('Result').size()

#Find the organism with the highest average OD600
Org_grouped = df.groupby('Organism')
highest_mean_OD_Org = Org_grouped['OD600'].mean().idxmax()

#Group by both Organism and Result and count occurrences
multi_group = df.groupby(['Organism', 'Result']).size()
