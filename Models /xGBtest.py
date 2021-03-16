import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder as encoder, MinMaxScaler
from xgboost import plot_tree
from sklearn.metrics import balanced_accuracy_score, roc_auc_score, make_scorer
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix
from sklearn.metrics import plot_confusion_matrix

UFC_data = pd.read_csv('../WebAPP/clean_dataset.csv')
UFC_data['STANCE'].value_counts().plot(kind='bar', color='green')
# plt.show()

# Removing outlier Stance
print("@serious test", UFC_data[UFC_data['STANCE'] == 'Open Stance'].index.values)
print("@serious test", UFC_data[UFC_data['STANCE'] == 'Sideways'].index.values)
UFC_data.drop(UFC_data.index[[5372, 5832, 5838, 5853, 4112, 4496, 4590, 4709, 4773, 4877, 4908, 5367, 5706, 5904]])

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
scaler = MinMaxScaler()
# df= scaler.fit_transform(df)
UFC_data[cols_to_norm] = scaler.fit_transform(UFC_data[cols_to_norm])
# UFC_data[cols_to_norm] = UFC_data[cols_to_norm].apply(lambda x: (x - x.min()) / (x.max() - x.min()))

x_data = UFC_data.drop('WIN', axis=1)
labels = UFC_data['WIN']

X_train, X_test, y_train, y_test = train_test_split(x_data, labels, test_size=0.50, random_state=200)

model = xgb.XGBClassifier(objective="binary:logistic",
                          learning_rate=0.1,
                          missing=None,
                          gamma=0.25,
                          max_depth=5,
                          reg_alpha=10,
                          seed=42,
                          n_estimators=100,
                          scale_pos_weight=3,
                          subsample=0.8,
                          colsample_bytree=0.3,
                          )
model.fit(X_train, y_train, verbose=True, early_stopping_rounds=10, eval_metric='aucpr', eval_set=[(X_test, y_test)])

plot_confusion_matrix(model, X_test, y_test, values_format='d', display_labels=["Loose", "Win"])


plt.figure(figsize=(12,12))
plot_tree(model)
plt.savefig('tree_high_dpi', dpi=300)
plt.show()

def_two = np.asarray(x_data.iloc[9].values).reshape(1, -1)
single  = model.predict_proba(def_two)

# print("data 2",x_data)

# single_no = model.predict(def_two)

print("prediciting single data",single)
print("predicting none")


# # Grid Search Parameters
# grid_search_params = {
#     'colsample_bytree': [0.3, 0.7],
#     'learning_rate': [0.01, 0.1, 0.2, 0.5],
#     'n_estimators': [100],
#     'subsample': [0.2, 0.5, 0.8],
#     'max_depth': [2, 3, 5]
# }
#
# grid = GridSearchCV(estimator= model, param_grid=grid_search_params, scoring='roc_auc',
#                     cv=4, verbose=0)
#
# grid.fit(X_test, y_test)
# print("GridSearchCV")
# print("Best parameters found: ", grid.best_params_)
# print("Lowest RMSE found: ", np.sqrt(np.abs(grid.best_score_)))
