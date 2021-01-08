import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, RepeatedStratifiedKFold
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder as encoder, MinMaxScaler
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import pickle as DataStore

# from sklearn.metrics import confusion_matrix

UFC_data = pd.read_csv('clean_dataset.csv')
UFC_data['STANCE'].value_counts().plot(kind='bar', color = 'green')
plt.show()

#Removing outlier Stance
print("@serious test",UFC_data[UFC_data['STANCE']=='Open Stance'].index.values)
print("@serious test",UFC_data[UFC_data['STANCE']=='Sideways'].index.values)
UFC_data.drop(UFC_data.index[[5372,5832,5838,5853,4112,4496, 4590, 4709, 4773, 4877 ,4908, 5367, 5706 ,5904]])




UFC_data['STANCE'] = encoder().fit_transform(UFC_data['STANCE'])
UFC_data['STANCE1'] = encoder().fit_transform(UFC_data['STANCE1'])
# UFC_data = UFC_data.drop(['Unnamed: 0'], axis=1)
UFC_data = UFC_data.drop(['NAME'], axis=1)
UFC_data = UFC_data.drop(['NAME1'], axis=1)
# UFC_data = UFC_data.drop(['AvgTime2Win.1'], axis=1)
# UFC_data = UFC_data.drop(['AvgTime2Win'], axis=1)
UFC_data = UFC_data.dropna()

cols_to_norm = ['HEIGHT', 'STANCE', 'WEIGHT', 'REACH', 'DOB', 'SLpM', 'StrAcc',
                'SApM', 'StrDef', 'TDAvg', 'TDAcc', 'TDDef', 'SubAvg',
                'HEIGHT1', 'STANCE1', 'WEIGHT1', 'REACH1', 'DOB1',
                'SLpM1', 'StrAcc1', 'SApM1', 'StrDef1', 'TDAvg1', 'TDAcc1',
                'TDDef1', 'SubAvg1']



UFC_data['STANCE'].value_counts().plot(kind='bar' ,color ="red")
plt.show()
scaler = MinMaxScaler()
# df= scaler.fit_transform(df)
UFC_data[cols_to_norm] = scaler.fit_transform(UFC_data[cols_to_norm])
# UFC_data[cols_to_norm] = UFC_data[cols_to_norm].apply(lambda x: (x - x.min()) / (x.max() - x.min()))

x_data = UFC_data.drop('WIN', axis=1)
labels = UFC_data['WIN']

X_train, X_test, y_train, y_test = train_test_split(x_data, labels, test_size=0.33, random_state=200)

rfc = RandomForestRegressor(n_estimators=20, random_state=0)
rfc.fit(X_train, y_train)


# predictions
prediction = rfc.predict(X_test)


rfc_cv_score = cross_val_score(rfc, X_test, y_test, cv=7, scoring="roc_auc")
print("=== All AUC Scores ===")
print(rfc_cv_score)
print('\n')
print("=== Mean AUC Score ===")
print("Mean AUC Score - Random Forest: ", rfc_cv_score.mean())

cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
print('Accuracy: %.3f (%.3f)', accuracy_score(y_test, prediction.round()))

conf_mat = confusion_matrix(y_test, prediction.round())
print("=== Confusion Matrix ===")
print(conf_mat)
sns.heatmap(conf_mat,  annot=True)
plt.show()
# score = []
#
# for i in range(0, 4000):
#     test_two = x_data.iloc[i]
#     test_res = labels.iloc[i]
#     scop = np.asarray(test_two).reshape(1, -1)
#     rfc_predict = rfc.predict(scop)
#
#     if rfc_predict >= 0.5:
#         rfc_predict = 1
#
#     elif rfc_predict < 0.5:
#         rfc_predict = 0
#
#     if rfc_predict == test_res:
#         score.append(rfc_predict)
#
#     # print("res",rfc_predict)
#     # print("label",test_res)
#
# print(len(labels))
# # print(score)
# print(len(score))
# print("score", (len(score) / len(labels) * 100))

# predicting a single value

def_two = np.asarray(x_data.iloc[1]).reshape(1, -1)
# print("def2", def_two)
rfc_predict = rfc.predict(def_two)
print(rfc_predict, labels.iloc[1])

DataStore.dump(rfc, open('model.pkl', 'wb'))

# x_data.iloc[1].to_json('test.json')
# x_data.iloc[1:20].to_csv('test.csv')
