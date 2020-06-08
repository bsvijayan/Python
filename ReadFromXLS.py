%matplotlib notebook
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
print ('Matplotlib version: ', mpl.__version__)

df=pd.read_excel(r'C:\Users\Public\samp.xlsx',usecols='A:B')
print(df.loc[df['Duration'] >=1000])
print(df_new)
df_new.plot()f