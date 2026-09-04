# Author: Samson Samuel Ikhayere
# Date: August 2026

import pandas as pd
import numpy as np

np.random.seed(7)
n = 40

demographics = pd.DataFrame({
    "PatientID": [f"PT{i:03d}" for i in range(1, n+1)],
    "Age":       np.random.randint(18, 80, n),
    "Sex":       np.random.choice(["M", "F"], n),
    "Ward":      np.random.choice(["ICU", "General", "Paediatric", "Maternity"], n)
})

lab_results = pd.DataFrame({
    "PatientID":  [f"PT{i:03d}" for i in range(1, n+1)],
    "WBC":        np.random.uniform(4.0, 15.0, n),     # White blood cells
    "Haemoglobin":np.random.uniform(8.0, 17.0, n),
    "CRP":        np.random.uniform(0.1, 120.0, n),    # C-Reactive Protein
    "Diagnosis":  np.random.choice(["Sepsis","Malaria","Pneumonia","Typhoid"], n)
})

# Introduce missing values deliberately
lab_results.loc[np.random.choice(n, 5, replace=False), "WBC"] = np.nan
lab_results.loc[np.random.choice(n, 4, replace=False), "CRP"] = np.nan

microbiology = pd.DataFrame({
    "PatientID":  [f"PT{i:03d}" for i in range(1, 26)],   # only 25 patients
    "Organism":   np.random.choice(["E. coli","S. aureus","K. pneumoniae","No growth"], 25),
    "Antibiotic": np.random.choice(["Ceftriaxone","Ciprofloxacin","Vancomycin"], 25),
    "Sensitivity":np.random.choice(["Sensitive","Resistant","Intermediate"], 25)
})


#Merge all three DataFrames into one master DataFrame — keep all 40 patients
master_df = demographics.merge (lab_results, on= 'PatientID', how = 'left').merge(microbiology, on = 'PatientID', how = 'left')
#print (master_df)
#Report how many patients have missing lab values and handle them appropriately — justify your choice of method
missing_values = master_df.isnull().sum()

master_df = master_df.fillna({
    'WBC'         :  master_df['WBC'].median(),
    'CRP'         :  master_df ['CRP'].median(),
    'Organism'    :  'Unknown',
    'Antibiotic'  :  'Unknown',
    'Sensitivity' :  'Unknown'
})

#Add a column "Infection_severity" based on CRP: <10 = "Low", 10–50 = "Moderate", >50 = "High"
conditions = [
    master_df ['CRP'] < 10,
    (master_df ['CRP'] >= 10)  & (master_df ['CRP'] <= 50),
    master_df ['CRP'] > 50
]
choices = ['Low', 'Moderate', 'High']

master_df["Infection_severity"] = np.select(conditions, choices, default= 'unknown')

#Add a column "Anaemia" — True if Haemoglobin < 12 for F, < 13 for M
male_anaemia = (master_df['Sex'] == 'M') & (master_df['Haemoglobin'] < 13)
female_anaemia = (master_df['Sex'] == 'F') & (master_df['Haemoglobin'] < 12)

master_df["Anaemia"] = male_anaemia | female_anaemia

#Summarise: mean WBC and CRP per Diagnosis
WBC_CRP_mean = master_df.groupby('Diagnosis').agg({
    'WBC': ['mean'],
    'CRP': ['mean']
})
#Find which Ward has the highest proportion of Resistant organisms
ward_rest = master_df.groupby('Ward')['Sensitivity'].apply(lambda s: (s == 'Resistant').mean()).idxmax()

#Identify patients in ICU with High infection severity
ICU_high_mask = (master_df['Ward']== 'ICU') & (master_df["Infection_severity"]== "High")
ICU_high = master_df [ICU_high_mask]

#Save the master DataFrame to master_patient_data.csv
master_df.to_csv('master_patient_data.csv', index= False)
#Print a clean summary report

print("="*60)
print (f"\n                     SUMMARY REPORT                     ")
print("="*60)
print ("The three DataFrames merged as master_df")
print (master_df)

print ('Columns with the number of missing values')
print(missing_values)


#print (list(master_df.columns))

print(WBC_CRP_mean)

print (f'\n --- Ward with the highest proportion of Resistant organisms: {ward_rest}')

print ("\n ---patients in ICU with High infection severity---")
print (ICU_high)

print("\n master DataFrame successfully saved as master_patient_data.csv")
print("="*60)


print("\n" + "=" *60)
print(
    "Numeric lab parameters (WBC, CRP) were imputed using median values to prevent skewness from extreme infection levels."
)
print(
    "Missing microbiology fields (for un-sampled patients PT026-PT040) were labeled as 'Unknown' to retain cohort integrity."
)
print("="*60)
