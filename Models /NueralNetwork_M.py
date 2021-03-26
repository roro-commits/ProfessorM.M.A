import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder as encoder, MinMaxScaler
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset

UFC_data = pd.read_csv('clean_dataset.csv')
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

print("testingType", type(x_data))


# x_torch = torch.tensor(x_data.values).float()
# y_torch = torch.tensor(labels.values)
#
# print(len(x_torch[0]))
# print(y_torch[-1])
# print(x_torch[-1])


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()

        self.fc1 = nn.Linear(26, 700)  # 26*1
        self.fc2 = nn.Linear(700, 500)
        self.fc3 = nn.Linear(500, 200)
        self.fc4 = nn.Linear(200, 60)
        self.fc5 = nn.Linear(60, 1)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = F.relu(self.fc4(x))
        x = F.softmax(self.fc5(x))
        return x

    def get_num_correct(self, preds, labels):
        return preds.round().squeeze().eq(labels).numpy().sum()


X_train, X_test, y_train, y_test = train_test_split(x_data, labels, test_size=0.33, random_state=200)

X_train = torch.tensor(X_train.values).float()
X_test = torch.tensor(X_test.values).float()
y_train = torch.tensor(y_train.values).float()
y_test = torch.tensor(y_test.values).float()

train_data = []
test_data = []

for i in range(len(X_train)):
    train_data.append([X_train[i], y_train[i]])

for i in range(len(X_test)):
    test_data.append(([X_test[i], y_test[i]]))

# print(train_data)
train_loader = DataLoader(train_data, batch_size=100, shuffle=False)
test_loader = DataLoader(test_data, batch_size=100, shuffle=False)

i1, l1 = next(iter(train_loader))
print(l1[-1])

# training_dataset = Dataset(X_train,y_train)

# train_loader = DataLoader(training_dataset, batch_size=100)
#
net = Net()
# test = net(i1[98])

# criterion = nn.MSELoss()
# criterion = nn.CrossEntropyLoss()
criterion = nn.BCEWithLogitsLoss()
# criterion = nn.BCELoss()
# loss = criterion(test, l1[98])
# print("original", l1[98], i1[98])
# print("test", test)
# print("loss", loss)

optimizer = optim.Adam(net.parameters(), lr=0.001)

EPOCHS = 100

for epoch in range(EPOCHS):
    totalLoss = 0
    totalCorrect = 0
    for data in train_loader:
        X, y = data
        # y = y.numpy()
        # y = y.reshape(100,1)
        # y = torch.LongTensor(y)
        net.zero_grad()
        output = net(X)
        # print(y)
        # print("training output", output[99], "test",y)
        # print("training output", type(output), type(y))
        # y = y.size([100,1])
        # y = y.view(100,1)

        # for i in range(len(output)):
        # loss = F.mse_loss(output, y)
        # loss = criterion
        # print(type(loss))
        # criterion = nn.BCEWithLogitsLoss()
        loss = criterion(output.squeeze(), y)  # loss functions output - y (target)
        print("loosss", loss)
        loss = loss.type(torch.FloatTensor)
        loss.backward()  # back propagation
        optimizer.step()  # adjust weights

        totalLoss += loss.item()
        # print("output",output)
        totalCorrect += net.get_num_correct(output, y)
        print("Total right for training", totalCorrect)
    # print(loss)

    PATH = "savedModel/p_Nueralnet.pth"
    # saving the model
    torch.save(net,PATH)
    # torch.save(net.state_dict(),PATH)



correct = 0
total = 0

# ## for testing not gradiant decent needed
with torch.no_grad():
    for data in test_data:
        X, y = data
        output = net(X)
        # # print(X)
        # # output = float(round(output.numpy()[0]))
        # y = y.numpy()
        # # print("y",net(X[0:11]))
        # # print("y2",net(X[11:22]))
        # print("result",output, y)
        print(output, output.round().squeeze(), y)

        for i in range(len(output)):
            total += 1
            # print(total)
            correct += net.get_num_correct(output.squeeze(), y)
            # print("Total right for testing", totalCorrect / totalLoss)

print("Accuracy:", correct, "/", total, (correct / total) * 100 / 1)

