import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from multiprocessing import Process

df = pd.read_csv('clean_dataset.csv')

# df['HEIGHT'].fillna(value = df['HEIGHT'].mean())
# df['REACH'].fillna(value = str(df['REACH'].mean()))
df['REACH'] = df['REACH'].replace('nan', np.nan).fillna(df['REACH'].median())
df['HEIGHT'] = df['HEIGHT'].replace('nan', np.nan).fillna(df['HEIGHT'].median())
df['REACH1'] = df['REACH1'].replace('nan', np.nan).fillna(df['REACH1'].median())
df['HEIGHT1'] = df['HEIGHT1'].replace('nan', np.nan).fillna(df['HEIGHT1'].median())
df = df.replace(0, np.nan).dropna(thresh=22)
df = df.replace(np.nan, 0)
df['STANCE'] = df['STANCE'].replace(0, np.nan)  # .fillna('Open Stance')
df['STANCE1'] = df['STANCE1'].replace(0, np.nan)  # .fillna('Open Stance')
# df['STANCE'].fillna(df['STANCE'].mode(), inplace=True)
df['STANCE'].fillna(df['STANCE'].value_counts().index[0], inplace=True)
df['STANCE1'].fillna(df['STANCE1'].value_counts().index[0], inplace=True)
df['DOB'] = df['DOB'].replace(0, np.nan).fillna(df['DOB'].median())
df['DOB1'] = df['DOB1'].replace(0, np.nan).fillna(df['DOB1'].median())


df.to_csv('UfcFight_Dataset.csv', index=False)

# y = df.drop(['Name', 'STANCE','Name1', 'STANCE1'], axis=1)

# sns.displot(y['REACH'])
# sns.displot(y['HEIGHT'])
# sns.displot(y['Str. Acc..'])
# sns.displot(y['SApM'], bins=20)
# sns.displot(y['SLpM'], bins=20)
# sns.pairplot(y)
#
# plt.show()

# col_mask=df.isnull().any(axis=0)
# row_mask=df.isnull().any(axis=1)
#
# df.loc[row_mask,col_mask]
