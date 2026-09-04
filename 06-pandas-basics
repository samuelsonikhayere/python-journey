# Author: Samson Samuel Ikhayere
# Date: August 2026

import pandas as pd
import numpy as np
import os

np.random.seed(10)

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "culture_results.csv")

df = pd.read_csv(csv_path)

#df = pd.read_csv('culture_results.csv')
#Shape, dtypes, and info

print(df.shape)
print (df.dtypes)
print (df.info())

#First 5 rows and last 3 rows
print (df.head())
print (df.tail())

#Statistical summary of numeric columns
print (df.describe())

#Count of missing values per column
print (df.isnull().sum())

#Number of unique organisms
print (df['Organism'].nunique())
