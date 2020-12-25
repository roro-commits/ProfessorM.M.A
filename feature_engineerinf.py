import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import model_selection
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder as encoder
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report, confusion_matrix


# df = pd.read_csv ('pokemon_data.csv', delimiter =',')
# print(df[['Name','Type 1','HP','Attack','Legendary']])
#lopplp

UFC_data = pd.read_csv('/home/rotimi/Documents/FYP/UFC_data.csv')
UFC_data['Stance'] = encoder().fit_transform(UFC_data['Stance'])
UFC_data['Stance.1'] = encoder().fit_transform(UFC_data['Stance'])
UFC_data = UFC_data.drop(['Unnamed: 0'], axis=1)
UFC_data = UFC_data.drop(['Name'], axis=1)
UFC_data = UFC_data.drop(['Name.1'], axis=1)
UFC_data = UFC_data.drop(['AvgTime2Win.1'], axis=1)
UFC_data = UFC_data.drop(['AvgTime2Win'], axis=1)
cols_to_norm = ['Height', 'Stance', 'Weight', 'Reach', 'DOB', 'SLpm', 'SAcc',
                'SApm', 'StrDef', 'TDAvg', 'TDAcc', 'TDDef', 'SubAvg',
                'Height.1', 'Stance.1', 'Weight.1', 'Reach.1', 'DOB.1',
                'SLpm.1', 'SApm.1', 'StrDef.1', 'TDAvg.1', 'TDAcc.1',
                'TDDef.1', 'SubAvg.1']

UFC_data[cols_to_norm] = UFC_data[cols_to_norm].apply(lambda x: (x - x.min()) / (x.max() - x.min()))

x_data = UFC_data.drop('Win', axis=1)
labels = UFC_data['Win']

X_train, X_test, y_train, y_test = train_test_split(x_data, labels, test_size=0.33, random_state=596)

rfc =  RandomForestRegressor(n_estimators=20, random_state=0)
rfc.fit(X_train,y_train)

# predictions
test_one = ""

print(y_test)
print(y_test)

# print(X_test)

rfc_cv_score = cross_val_score(rfc, X_test, y_test, cv=10, scoring="roc_auc")
# # y_1 =confusion_matrix(y_test, rfc_predict)
# # print(y_1,'\n')
# # print("=== Classification Report ===")
# # print(classification_report(y_test, rfc_predict))
# # print('\n')
print("=== All AUC Scores ===")
print(rfc_cv_score)
print('\n')
print("=== Mean AUC Score ===")
print("Mean AUC Score - Random Forest: ", rfc_cv_score.mean())


score = []


for i in range(0,3176):
    test_two = x_data.iloc[i]
    test_res = labels.iloc[i]
    scop = np.asarray(test_two).reshape(1,-1)
    rfc_predict = rfc.predict(scop)

    if (rfc_predict >= 0.5):
        rfc_predict = 1
    
    elif (rfc_predict < 0.5):
        rfc_predict = 0

    if( rfc_predict == test_res):
        score.append(rfc_predict)



    # print("res",rfc_predict)
    # print("label",test_res)


print(len(labels))
#print(score)
print(len(score))
print("score",(len(score)/len(labels) * (100)))

def_two = np.asarray(x_data.iloc[1]).reshape(1,-1)
rfc_predict = rfc.predict(def_two)
print(rfc_predict)