
import pandas as pd

df = pd.read_csv('..\..\data\processed\\resultat.csv')

print(df.isnull().sum())

# Pandas conditonal access