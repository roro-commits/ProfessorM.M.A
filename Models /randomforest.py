import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, RepeatedStratifiedKFold, GridSearchCV, RandomizedSearchCV
# import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder as encoder, MinMaxScaler
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import pickle as DataStore

# from sklearn.metrics import confusion_matrix

UFC_data = pd.read_csv('/home/roroblacc/Desktop/test/ProfessorM.M.A/WebAPP/clean_dataset.csv')
UFC_data['STANCE'].value_counts().plot(kind='bar', color='green')
plt.show()

# Removing outlier Stance , obselete stance from early mma days such as open stance & side way stance
print("@serious test", UFC_data[UFC_data['STANCE'] == 'Open Stance'].index.values)
print("@serious test", UFC_data[UFC_data['STANCE'] == 'Sideways'].index.values)
UFC_data.drop(UFC_data.index[[5372, 5832, 5838, 5853, 4112, 4496, 4590, 4709, 4773, 4877, 4908, 5367, 5706, 5904]])

# Drop datapoint with missing value at this point & transform Stance categorical data to numerical value  while dropping name axis to prepare dat for prediction
UFC_data = UFC_data.dropna()
UFC_data['STANCE'] = encoder().fit_transform(UFC_data['STANCE'])
UFC_data['STANCE1'] = encoder().fit_transform(UFC_data['STANCE1'])
# UFC_data = UFC_data.drop(['Unnamed: 0'], axis=1)
UFC_data = UFC_data.drop(['NAME'], axis=1)
UFC_data = UFC_data.drop(['NAME1'], axis=1)
# UFC_data = UFC_data.drop(['AvgTime2Win.1'], axis=1)
# UFC_data = UFC_data.drop(['AvgTime2Win'], axis=1)

cols_to_norm = ['HEIGHT', 'STANCE', 'WEIGHT', 'REACH', 'DOB', 'SLpM', 'StrAcc',
                'SApM', 'StrDef', 'TDAvg', 'TDAcc', 'TDDef', 'SubAvg',
                'HEIGHT1', 'STANCE1', 'WEIGHT1', 'REACH1', 'DOB1',
                'SLpM1', 'StrAcc1', 'SApM1', 'StrDef1', 'TDAvg1', 'TDAcc1',
                'TDDef1', 'SubAvg1']

UFC_data['STANCE'].value_counts().plot(kind='bar', color="red")
plt.show()

# Converts the data between 0-1 to make it easier for the model to predict also better accuracy
scaler = MinMaxScaler()
# df= scaler.fit_transform(df)
UFC_data[cols_to_norm] = scaler.fit_transform(UFC_data[cols_to_norm])
# UFC_data[cols_to_norm] = UFC_data[cols_to_norm].apply(lambda x: (x - x.min()) / (x.max() - x.min()))

x_data = UFC_data.drop('WIN', axis=1)
labels = UFC_data['WIN']

X_train, X_test, y_train, y_test = train_test_split(x_data, labels, test_size=0.33, random_state=200)

rfc = RandomForestClassifier(n_estimators=100, random_state=0, max_depth=20, min_samples_split=20, max_features=5,
                             n_jobs=-1)
rfc_model = RandomForestClassifier()
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
# sns.heatmap(conf_mat,  annot=True)
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
rfc_predict = rfc.predict_proba(def_two)
print("pridicting single data", rfc_predict, labels.iloc[1])

DataStore.dump(rfc, open('RandModel.pkl', 'wb'))

# x_data.iloc[1].to_json('test.json')
# x_data.iloc[1:20].to_csv('test.csv')


# # Grid Search Parameters
grid_search_params = {
    'n_estimators': [20, 30, 40, 50, 60, 100, 200, 300, 400],
    'max_depth': [10, 20, 40, 50, 60, 100],
    'min_samples_split': [20, 25, 30, 40, 45, 50, 60, 100],
    'max_features': [5, 10, 12, 13, 15, 18],
}
#
# grid = GridSearchCV(estimator= rfc_model, param_grid=grid_search_params, scoring='roc_auc',
#                     cv=4, verbose=0, n_jobs=-1)
#
# grid.fit(X_test, y_test)
# print("GridSearchCV")
# print("Best parameters found: ", grid.best_params_)
# print("Lowest RMSE found: ", np.sqrt(np.abs(grid.best_score_)))


# search = RandomizedSearchCV(rfc_model, param_distributions=grid_search_params, random_state=42, n_iter=200, cv=3,
#                             verbose=1, n_jobs=-1, return_train_score=True)
# search.fit(X_test, y_test)
#
# print("Random SearchCV")
# print("Best parameters found: ", search.best_params_)
# print("Lowest RMSE found: ", np.sqrt(np.abs(search.best_score_)))
