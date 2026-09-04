# Author: Samson Samuel Ikhayere
# Date: August 2026

import pandas as pd
import numpy as np
import os

np.random.seed(10)

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "culture_results.csv")

df = pd.read_csv(csv_path)

data = {
    'Antibiotic' : ['Ciprofloxacin', 'Tobramycin', 'Meropenem', 'Ampicillin'],
    "Class": ["Penicillin", "Fluoroquinolone", "Aminoglycoside", "Glycopeptide"],
    "Mechanism": ["Cell wall synthesis inhibitor", "DNA gyrase inhibitor", "Protein synthesis inhibitor", "Cell wall synthesis inhibitor"]
}

antibiotic_info = pd.DataFrame(data)

merge_df = df.merge(antibiotic_info, on = 'Antibiotic', how = 'left')

print (merge_df.head())
