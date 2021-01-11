import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import model_selection
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder as encoder
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report, confusion_matrix



UFC_data = pd.read_csv('scrapy /clean_dataset.csv')
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

UFC_data[cols_to_norm] = UFC_data[cols_to_norm].apply(lambda x: (x - x.min()) / (x.max() - x.min()))

x_data = UFC_data.drop('WIN', axis=1)
labels = UFC_data['WIN']

X_train, X_test, y_train, y_test = train_test_split(x_data, labels, test_size=0.33, random_state=200)

rfc = RandomForestClassifier(n_estimators=20, random_state=0)
rfc.fit(X_train, y_train)

# predictions
test_one = ""

print(y_test)
print(y_test)

# print(X_test)

rfc_cv_score = cross_val_score(rfc, X_test, y_test, cv=7, scoring="roc_auc")
# y_1 =confusion_matrix(y_test, rfc_predict)
# print(y_1,'\n')
# print("=== Classification Report ===")
# print(classification_report(y_test, rfc_predict))
# print('\n')
print("=== All AUC Scores ===")
print(rfc_cv_score)
print('\n')
print("=== Mean AUC Score ===")
print("Mean AUC Score - Random Forest: ", rfc_cv_score.mean())

score = []

for i in range(0, 4000):
    test_two = x_data.iloc[i]
    test_res = labels.iloc[i]
    scop = np.asarray(test_two).reshape(1, -1)
    rfc_predict = rfc.predict(scop)

    if rfc_predict >= 0.5:
        rfc_predict = 1

    elif rfc_predict < 0.5:
        rfc_predict = 0

    if rfc_predict == test_res:
        score.append(rfc_predict)

    # print("res",rfc_predict)
    # print("label",test_res)

print(len(labels))
# print(score)
print(len(score))
print("score", (len(score) / len(labels) * (100)))

def_two = np.asarray(x_data.iloc[1]).reshape(1, -1)
rfc_predict = rfc.predict(def_two)
print(rfc_predict,labels.iloc[1])
