from flask import Flask, request, jsonify, render_template
import numpy as np
import pickle
import joblib
import pandas as pd
from flask_cors import CORS, cross_origin
import torch.nn as nn
import torch.optim as optim
from sklearn.preprocessing import LabelEncoder as encoder, MinMaxScaler
from skorch import NeuralNetBinaryClassifier
import subprocess
import sys
# from NueralNetwork_M import Net
from skorchNueral import Net as SkorchNet
#import xgboost


application = Flask(__name__, static_folder='./ReactWebApp/WebApp/professorMMA/build', static_url_path='/')
app = application
CORS(app, support_credentials=True)



# Loading random Forest Model

model = pickle.load(open('savedModel/RandModel.pkl', 'rb'))

# # Loading the Xgb Boost Model
xgbModel = joblib.load(open("savedModel/joblibXGBboostModel.dat", "rb"))

# Loading the Skorch Model

# SkorchModel = pickle.load(open('savedModel/Skorchmymodel.pkl', 'rb'))

SkorchModel = NeuralNetBinaryClassifier(
    SkorchNet,
    max_epochs=120,
    lr=0.001,
    criterion=nn.BCEWithLogitsLoss,
    optimizer=optim.AdamW,
).initialize()


SkorchModel.load_params('Skorchmymodel.pkl')


@app.route('/', methods=['GET', 'POST'])
def home():
    print("ccheking2", flush=True)
    return app.send_static_file('index.html')


# catching React Router urls 
@app.errorhandler(404)   
def not_found(e):   
  return app.send_static_file('index.html')


@app.route("/fighterDataset2.json", methods=["GET"])
@cross_origin(supports_credentials=True)
def get_example():
    """GET in server"""
    response = jsonify(message="Simple server is running")

    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route('/api/react_api', methods=['POST'])
@cross_origin(supports_credentials=True)
def react_api():
    global randomForestFavWins, randomForestUnderDogWins

    if request.method == 'POST':
        if request.data:
            data = request.data.decode('UTF-8')
            # print(request.data)
            # print(len(request.data))
            print("data", data)

            # after receiving data
            print("receiving data", flush=True)
            data = data.replace("[", "")  # dataset = [x for x in data] stored in a list
            data = data.replace("]", "")
            dataset = lambda x: list(x.split(","))
            dataset = dataset(data)
            # dataset = access_token

            print("Datasets", dataset, flush=True)
            print("Datasets 2", dataset[0], flush=True)
            print("Datasets 3", dataset[1], flush=True)
            print("Datasets 4", dataset[2], flush=True)

            # idex not to conver = 0,4,14,18
            # Convert for adding to data frame  # convert to float excluding name stance on both side to be removed or with one hot encoder
            for x in range(0, len(dataset)):
                if (x == 0) or (x == 4) or (x == 14) or (x == 18):
                    pass
                else:
                    dataset[x] = float(dataset[x])
                    print(dataset[x])

            # apppend one for extra column for dataframe to be dropped later
            dataset.append(1)
            print("Datasets check", dataset, flush=True)
            print("Datasets check for float ", type(dataset[1]), flush=True)

            UFC_data = pd.read_csv('clean_dataset.csv')
            UFC_data = UFC_data.dropna()
            length_dataframe = len(UFC_data)
            UFC_data.loc[length_dataframe] = dataset
            print(UFC_data.iloc[-1])
            UFC_data['STANCE'] = encoder().fit_transform(UFC_data['STANCE'])
            UFC_data['STANCE1'] = encoder().fit_transform(UFC_data['STANCE1'])
            # UFC_data = UFC_data.drop(['Unnamed: 0'], axis=1)
            UFC_data = UFC_data.drop(['NAME'], axis=1)
            UFC_data = UFC_data.drop(['NAME1'], axis=1)
            UFC_data = UFC_data.drop('WIN', axis=1)

            cols_to_norm = ['HEIGHT', 'STANCE', 'WEIGHT', 'REACH', 'DOB', 'SLpM', 'StrAcc',
                            'SApM', 'StrDef', 'TDAvg', 'TDAcc', 'TDDef', 'SubAvg',
                            'HEIGHT1', 'STANCE1', 'WEIGHT1', 'REACH1', 'DOB1',
                            'SLpM1', 'StrAcc1', 'SApM1', 'StrDef1', 'TDAvg1', 'TDAcc1',
                            'TDDef1', 'SubAvg1']

            UFC_data['STANCE'].value_counts().plot(kind='bar', color="red")
            scaler = MinMaxScaler()
            UFC_data[cols_to_norm] = scaler.fit_transform(UFC_data[cols_to_norm])

            #################### Prediction Data #################
            print("Prediction  Data raw ")
            print(UFC_data.iloc[-1])
            print(len(UFC_data.iloc[-1]))

            toPredict = np.asarray(UFC_data.iloc[-1]).reshape(1, -1)
            print("Data to predict before reverse")
            print(toPredict)
            print("length")
            print(len(toPredict[0]))
            # data is cut  for the purpose of making underDog the favourite
            toPredictReverseOne = UFC_data.iloc[-1][0:13]
            toPredictReverseTwo = UFC_data.iloc[-1][13:]
            topredictTwo = []
            ######## reversing  the Data for Fav and underdog ########
            [topredictTwo.append(x) for x in toPredictReverseTwo]
            [topredictTwo.append(x) for x in toPredictReverseOne]
            topredictTwo = np.asarray(topredictTwo).reshape(1, -1)
            # topredictTwo = np.asarray(topredictTwo)
            print("Reversing Data for under Dog  ")
            print(topredictTwo)
            print("xpected 26 ", len(topredictTwo[0]))

            ### Skorch Model Prediction
            skorch_data = toPredict.astype(np.float32)
            skorch_dataTwo = topredictTwo.astype(np.float32)

            skorchPrediction = SkorchModel.predict_proba(skorch_data)
            skorchPredictionTwo = SkorchModel.predict_proba(skorch_dataTwo)
            print("Skorch Prediction", skorchPrediction)
            print("Skorch Prediction Two", skorchPredictionTwo)

            # XGB Prediction
            xgbPredictionTwo = xgbModel.predict_proba(topredictTwo)
            xgbPrediction = xgbModel.predict_proba(toPredict)
            print("XGB Boost prediction", xgbPrediction, flush=True)
            print("XGB Boost prediction Two", xgbPredictionTwo, flush=True)


            ## Random \Forest prediction
            prediction = model.predict_proba(toPredict)
            outputRandForest = prediction
            predictionTwo = model.predict_proba(topredictTwo)
            outputRandForestTwo = predictionTwo
            # print(prediction[0].round(), flush=True)
            # outputRandForest = (prediction[0] * 100)
            print("Random Forest Prediction ", outputRandForest, flush=True)
            print("Random Forest Prediction ", outputRandForestTwo, flush=True)

            ######### Predictions #########
            # random forest win and loss ratio
            randomForestFavLose = outputRandForest[0][0]
            randomForestFavWins = outputRandForest[0][1]
            randomForestUnderDogLose = outputRandForestTwo[0][0]
            randomForestUnderDogWins = outputRandForestTwo[0][1]

            # xvg boost prediction
            xgbFavLose = xgbPrediction[0][0]
            xgbFavWins = xgbPrediction[0][1]
            xgbUnderDogLose = xgbPredictionTwo[0][0]
            xgbUnderDogWins = xgbPredictionTwo[0][1]
      
            # Skorch Prediction  # just getting the win percentage .. loss can be calculated
            skorchPredfavLose = skorchPrediction[0][0]
            skorchPredFavWins = skorchPrediction[0][1]
            skorchPredUndLose = skorchPredictionTwo[0][0]
            skorchPredUndWins = skorchPredictionTwo[0][1]
            ####### Voting System #############
            favouriteWins = (randomForestFavWins + xgbFavWins + skorchPredFavWins) / 3
            underDog = (randomForestUnderDogWins + xgbUnderDogWins + skorchPredUndWins) / 3
            favloss = (randomForestFavLose + xgbFavLose + skorchPredfavLose) / 3
            undLoss = (randomForestUnderDogLose + xgbUnderDogLose + skorchPredUndLose) / 3
            fav_Score = 0
            und_score = 0

            # Random Forest Vote  for Favourite
            if randomForestFavWins > randomForestUnderDogWins:
                fav_Score += 1

            elif randomForestUnderDogWins > randomForestFavWins:
                und_score += 1
            else:
                fav_Score += 0.5
                und_score += 0.5
            # Xgb Vote
            if xgbFavWins > xgbUnderDogWins:
                fav_Score += 1
            elif xgbUnderDogWins > xgbFavWins:
                und_score += 1
            else:
                fav_Score += 0.5
                und_score += 0.5
            # Skorch Vote
            if skorchPredFavWins > skorchPredUndWins:
                fav_Score += 1
            elif skorchPredUndWins > skorchPredFavWins:
                und_score += 1
            else:
                fav_Score += 0.5
                und_score += 0.5

            # Random Forest Vote  for UnderDogs

            if fav_Score > und_score:
                print("fav", favouriteWins)
                print(underDog)
                fav = format(round(favouriteWins * 100))
                und = format(100 - round(favouriteWins * 100))
                return ({'UNDERDOG': und,
                         'FAVOURITE': fav,
                         })
            elif und_score > fav_Score:
                print("under", underDog)
                print(favouriteWins)
                und = format(round(underDog * 100))
                fav = format(100 - round(underDog * 100))
                return ({'UNDERDOG': und,
                         'FAVOURITE': fav,
                         })

            else:
                return ({'UNDERDOG': 'Draw',
                         'FAVOURITE': 'Draw',
                         })

        else:
            print("Did not get dataset", flush=True)

            # outputRandForest = (round(1000, 2) * 100 / 1)
            #
            # print(outputRandForest, flush=True)
            request.headers.add("Access-Control-Allow-Origin", "*")

        return render_template('index.html')


if __name__ == "__main__":
	    application.run(debug=True)
    #app.run(host='0.0.0.0', port=8000)
