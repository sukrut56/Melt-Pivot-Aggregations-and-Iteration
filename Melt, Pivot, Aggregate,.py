import pandas as pd 
import numpy as np 

diabetes_df = pd.read_csv("C:/Kaggle Data/melt/diabetic_data.csv")	#importing the data using pandas 
print(diabetes_df.columns)

melt = pd.melt(diabetes_df, id_vars=['race'], value_vars=['diabetesMed'], var_name = 'Med') #melting the race and diabetesMed column to get better understanding about how they are related  
print(melt)

pivot = diabetes_df.pivot(index= 'encounter_id', columns='diabetesMed', values='num_medications') #using pivot to understand patient encounter_id and if they have diabetesMed and how much num of medication are taken
print(pivot)

aggregation = diabetes_df.agg({'num_lab_procedures' : ['max', 'mean', 'min', 'std'], 'time_in_hospital': ['max','mean', 'min', 'std']}) #using aggregation to understand how many lab_procedures are carried out in given time while patient is in hospital
print(aggregation)

#Iteration
for index, row in diabetes_df.iterrows(): #using iterrow to go through the indexes and rows of certain column in the database
	print(row['age'])

groupby = diabetes_df.groupby(diabetes_df['race']).apply(lambda x: pd.Series({'diabetesMed': len(x['diabetesMed'])})).reset_index()	#using groupby to get the total number of races and how diabetesMed changes based on it. 
print(groupby)