import pandas as pd
import matplotlib.pyplot as mpl

df = pd.read_csv('/home/rotimi/Documents/FYP/ProfessorM.M.A/clean.csv')
df.series(['WEIGHT']).str.replace([' lbs.'], value='', inplace=True)
# df['StrAcc'].replace(['%'],  value = '', inplace = True)
# a = df.head()
# print(a.iloc[0]