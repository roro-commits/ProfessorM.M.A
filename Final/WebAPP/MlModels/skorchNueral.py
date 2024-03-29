import pandas as pd
import numpy as np
import pickle

import matplotlib.pyplot as plt
from sklearn_evaluation import plot
from sklearn_evaluation.plot import grid_search
import skorch
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split, RepeatedStratifiedKFold, cross_val_score
from sklearn.preprocessing import LabelEncoder as encoder, MinMaxScaler
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
from sklearn.model_selection import GridSearchCV

from skorch.callbacks import EpochScoring

from skorch import NeuralNetClassifier
from skorch import NeuralNetBinaryClassifier

# UFC_data = pd.read_csv('/root/PycharmProjects/pythonProject1/clean_dataset.csv')
UFC_data = pd.read_csv('./clean_dataset.csv')
# UFC_data['STANCE'].value_counts().plot(kind='bar', color='green')
# plt.show()

# Removing outlier Stance
print("@Removing outlier stance", UFC_data[UFC_data['STANCE'] == 'Open Stance'].index.values)
print("@Removing outlier stance", UFC_data[UFC_data['STANCE'] == 'Sideways'].index.values)
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

# UFC_data['STANCE'].value_counts().plot(kind='bar', color="red")
# plt.show()
scaler = MinMaxScaler()
# df= scaler.fit_transform(df)
UFC_data[cols_to_norm] = scaler.fit_transform(UFC_data[cols_to_norm])
# UFC_data[cols_to_norm] = UFC_data[cols_to_norm].apply(lambda x: (x - x.min()) / (x.max() - x.min()))

x_data = UFC_data.drop('WIN', axis=1)
labels = UFC_data['WIN']

print("testingType", type(x_data))


# x_torch = torch.tensor(x_data.values).float()
# y_torch = torch.tensor(labels.values)
#
# print(len(x_torch[0]))
# print(y_torch[-1])
# print(x_torch[-1])


class Net(nn.Module):

    def __init__(self,
                 layer_one_units=17,
                 layer_two_units=17,
                 layer_three_units=17,
                 layer_four_units=17,
                 general_layer_node=17):
        super(Net, self).__init__()
        self.layer_one_units = layer_one_units
        self.layer_two_units = layer_two_units
        self.layer_three_units = layer_three_units
        self.layer_four_units = layer_four_units
        self.general_layer_node = general_layer_node

        self.input_layer = nn.Linear(26, layer_one_units)
        self.hidden_layer1 = nn.Linear(layer_one_units, layer_two_units)
        self.hidden_layer2 = nn.Linear(layer_two_units, layer_three_units)
        self.hidden_layer3 = nn.Linear(general_layer_node, general_layer_node)
        self.hidden_layer4 = nn.Linear(general_layer_node, general_layer_node)
        self.hidden_layer5 = nn.Linear(general_layer_node, general_layer_node)
        self.hidden_layer6 = nn.Linear(general_layer_node, general_layer_node)
        self.hidden_layer7 = nn.Linear(general_layer_node, general_layer_node)
        self.hidden_layer8 = nn.Linear(general_layer_node, general_layer_node)
        self.output_layer = nn.Linear(general_layer_node, 1)

    def forward(self, x):
        x = F.relu(self.input_layer(x))
        x = F.relu(self.hidden_layer1(x))
        x = F.relu(self.hidden_layer2(x))
        x = F.relu(self.hidden_layer3(x))
        x = F.relu(self.hidden_layer4(x))
        x = F.relu(self.hidden_layer5(x))
        x = F.relu(self.hidden_layer6(x))
        x = F.relu(self.hidden_layer7(x))
        x = F.relu(self.hidden_layer8(x))
        x = torch.sigmoid(self.output_layer(x))
        return x

    def get_num_correct(self, preds, labels):
        return preds.round().squeeze().eq(labels).numpy().sum()


X_train, X_test, y_train, y_test = train_test_split(x_data, labels, test_size=0.33, random_state=200)

# converting th data type to float for the nueral network
X_train = X_train.astype(np.float32)
X_test = X_test.astype(np.float32)
y_train = y_train.astype(np.float32)
y_test = y_test.astype(np.float32)

print("X_train", y_train)

# auc = EpochScoring(scoring='roc_auc', lower_is_better=False)

# skorch.make_binary_classifier(squeeze_output=True)

net = NeuralNetBinaryClassifier(
    Net,
    max_epochs=120,
    lr=0.001,
    criterion=nn.BCEWithLogitsLoss,
    # criterion = torch.nn.BCELoss,
    optimizer=optim.AdamW,
)

net.fit(X_train.values, y_train.values)

# y_proba = net.predict_proba(X_test[:20].values)
Accuracy = net.score(X_test.values, y_test.values)
y_probas = net.predict_proba(X_test.values)
print("Accuracy",Accuracy)

# cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
# print('Accuracy: %.3f (%.3f)', accuracy_score(y_test, y_probas.round()))

file_name = './Skorchmymodel.pkl'
net.save_params(f_params=file_name)

plt.show()

# #  #Grid Searching Parameter
params = {
    # 'modules':[Net],
    'lr': [0.001, 0.01, 0.05, 0.1],
    'max_epochs': [100, 200, 250, 500],
    'optimizer': [optim.Adam, optim.ASGD, optim.Adagrad, optim.Adadelta, optim.AdamW]
}

gs = GridSearchCV(net, params, refit=False, cv=3, scoring='accuracy', verbose=2)

# trains each parameter
# gs = gs.fit(X_train.values, y_train.values)

# #prints best score of the search
# print(gs.best_score_, gs.best_params_)

# #gettign all the possible parameneters
# print(net.get_params().keys())

# grid_search(gs.cv_results_, change='max_epochs')
plot.grid_search(gs.cv_results_, change='max_epochs', kind='bar')

plt.show()
