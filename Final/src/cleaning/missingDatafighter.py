import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
from multiprocessing import Process

df = pd.read_csv('fighter_clean_Dataset.csv')


# df['HEIGHT'].fillna(value = df['HEIGHT'].mean())
# df['REACH'].fillna(value = str(df['REACH'].mean()))
df['REACH'] = df['REACH'].replace('nan',np.nan).fillna(df['REACH'].median())
df['HEIGHT'] = df['HEIGHT'].replace('nan',np.nan).fillna(df['HEIGHT'].median())
df = df.replace(0,np.nan).dropna(thresh=11)
df = df.replace(np.nan,0)
df['STANCE'] = df['STANCE'].replace(0,np.nan) #.fillna('Open Stance')
# df['STANCE'].fillna(df['STANCE'].mode(), inplace=True)
df['STANCE'].fillna(df['STANCE'].value_counts().index[0], inplace=True)
df['DOB'] = df['DOB'].replace(0,np.nan).fillna(df['DOB'].median())

df = df.dropna()

#late change in naming convention
csv_rows = ['NAME', 'HEIGHT', 'WEIGHT', 'REACH', 'STANCE', 'DOB', 'SLpM', 'StrAcc', 'SApM', 'StrDef', 'TDAvg',
            'TDAcc', 'TDDef', 'SubAvg']

df.columns = csv_rows



df.to_csv('fighter_Dataset.csv', index=False)
df.to_json('fighterDataset2.json',orient='index')

# y = df.drop(['Name','STANCE'], axis =1 )
#
#
# sns.displot(y['REACH'])
# sns.displot(y['HEIGHT'])
# sns.displot(y['Str. Acc..'])
# sns.displot(y['SApM'] ,bins = 20)
# sns.displot(y['SLpM'] ,bins = 20)
# sns.pairplot(y)
#
#


plt.show()
print(df.head(100))

