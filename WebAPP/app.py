import numpy as np
import torch
from flask import Flask, request, jsonify, render_template
import pickle
import joblib
import pandas as pd
from flask_cors import CORS, cross_origin
from sklearn.preprocessing import LabelEncoder as encoder, MinMaxScaler
from NueralNetwork_M import Net
import xgboost

app = Flask(__name__)
CORS(app, support_credentials=True)
model = pickle.load(open('savedModel/RandModel.pkl', 'rb'))

PATH = "savedModel/p_Nueralnet.pth"
# model_pyt = Net()
# model_pyt.load_state_dict(torch.load(PATH))
# model_pyt.eval()

##### entire model
# model_pyt = torch.load(PATH)
# model_pyt.eval()

model_pyt = Net()
model_pyt.load_state_dict(torch.load(PATH))
model_pyt.eval()

# # Loading the Xgb Boost Model
# xgbModel = pickle.load(open("savedModel/XGBboostModel.dat", "rb"))
xgbModel = joblib.load(open("savedModel/joblibXGBboostModel.dat", "rb"))


# xgbModel = xgboost.Booster({'n_thread':4})
# xgbModel.load_model("savedModel/XGBboost.model")

def getPrediction(tensor):
    input_x = torch.tensor(tensor)
    input_x = input_x.type(torch.FloatTensor)
    output = model_pyt.forward(input_x)
    return output


# class ufc(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     pass
#
# class Form(FlaskForm):
#     name = SelectField('NAME', choices=[])
#


@app.route('/', methods=['GET', 'POST'])
def home():
    print("ccheking2", flush=True)
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    '''
    Renders result in HTML
    '''
    global randomForestWinFav, randomForestWinTwoUnd
    if request.method == 'POST':
        print("test1", flush=True)

        if 'form' in request.form:

            # after receiving data
            print("receiving data", flush=True)
            data = request.form['form']
            # dataset = [x for x in data] stored in a list
            dataset = lambda x: list(x.split(","))
            dataset = dataset(data)
            print("Datasets", dataset, flush=True)
            print("Datasets 2", dataset[0], flush=True)

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

            # df = pd.DataFrame(dataset)
            # # df.replace(stance)
            # df.replace(regex=['Orthodox'], value=1, inplace=True)
            # df.replace(regex=['Southpaw'], value=3, inplace=True)
            # df.replace(regex=['Switch'], value=4, inplace=True)
            # df.replace(regex=['Open Stance'], value=1, inplace=True)
            # df.replace(regex=['Sideways'], value=1, inplace=True)
            # print("Datasets", df, flush=True)
            # print(df, flush=True)
            # final_features = df[0:].values.tolist()
            # result = np.array(final_features)
            # result = result.T
            # print("result", result.T, flush=True)
            # result = result.astype(float)
            # result = result[0]
            # print('final feature *** ', result, flush=True)

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
            print("system check")
            print(toPredict)
            print("length")
            print(len(toPredict[0]))
            toPredictReverseOne = UFC_data.iloc[-1][0:13]
            toPredictReverseTwo = UFC_data.iloc[-1][13:]
            topredictTwo = []
            ######## revresing the Data for Fav and underdog ########
            [topredictTwo.append(x) for x in toPredictReverseTwo]
            [topredictTwo.append(x) for x in toPredictReverseOne]
            topredictTwo = np.asarray(topredictTwo).reshape(1, -1)
            # topredictTwo = np.asarray(topredictTwo)
            print("Testing ")
            print(topredictTwo)

            # print("to predict 2", toPredictTwo, flush=True)
            # print("Prediction  Data Processed ", flush=True)
            # print("testing!!!!!!!!!!!!",toPredictReverseOne)
            # print("testing!!!!!!!!!!!!",toPredictReverseTwo)

            # Pytorch Probabilities
            pyt = getPrediction(toPredict)
            pytTwo = getPrediction(topredictTwo)
            print("!!!!!!!!!!!pytorch", pyt.round(), flush=True)

            # XGB Prediction
            xgbPredictionTwo = xgbModel.predict_proba(topredictTwo)
            xgbPrediction = xgbModel.predict_proba(toPredict)
            print("XGB Boost prediction", xgbPrediction, flush=True)
            print("XGB Boost prediction Two", xgbPredictionTwo, flush=True)

            # # result = result.apply(lambda x: (x - x.min()) / (x.max() - x.min()))
            # print("Datasets2", df, flush=True)
            # # final_features = np.hstack(df)
            # # final_features = [x for x in final_features]
            # # print(type(final_features))
            # # df = pd.DataFrame(final_features)
            # # print("#result", result)

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
            randomForestLossFav = outputRandForest[0][0]
            randomForestWinFav = outputRandForest[0][1]
            randomForestLossTwoUnd = outputRandForestTwo[0][0]
            randomForestWinTwoUnd = outputRandForestTwo[0][1]

            # xvg boost prediction
            xgbLossFav = xgbPrediction[0][0]
            xgbWinFav = xgbPrediction[0][1]
            xgbLossTwoUnd = xgbPredictionTwo[0][0]
            xgbWinTwoUnd = xgbPredictionTwo[0][1]

            # pytorch prediction
            pyt_pred = pyt
            pyt_predTwo = pytTwo

            ####### Voting System #############
            fav = (randomForestWinFav + xgbWinFav) / 2
            favloss = (randomForestLossFav + xgbLossFav) / 2
            und = (randomForestWinTwoUnd + xgbWinTwoUnd) / 2
            undLoss = (randomForestLossTwoUnd + xgbLossTwoUnd) / 2
            fav_Score = 0
            und_score = 0

            # Random Forest Vote
            if randomForestWinFav > randomForestWinTwoUnd:
                fav_Score += 1

            elif randomForestWinTwoUnd > randomForestWinFav:
                und_score += 1
            else:
                fav_Score += 0.5
                und_score += 0.5
            # Xgb Vote
            if xgbWinFav > xgbWinTwoUnd:
                fav_Score += 1
            elif xgbWinTwoUnd > xgbWinFav:
                und_score += 1
            else:
                fav_Score += 0.5
                und_score += 0.5
            # Pytorch Vote
            if pyt_pred > pyt_predTwo:
                fav_Score += 1
            elif pyt_predTwo > pyt_pred:
                und_score += 1
            else:
                fav_Score += 0.5
                und_score += 0.5

            if fav_Score > und_score:
                print("fav", fav_Score)
                print(und_score)
                return render_template('index.html', UNDERDOG="{} %".format(round(favloss * 100)),
                                       FAVOURITE="{} %".format(round(fav * 100)))

            elif und_score > fav_Score:
                print("under", und_score)
                print(fav_Score)
                return render_template('index.html', UNDERDOG="{} %".format(round(und * 100)),
                                       FAVOURITE="{} %".format(round(undLoss * 100)))

            else:
                print("under", und_score)
                print("fav", fav_Score)
                return render_template('index.html', UNDERDOG="{} %".format("Draw"),
                                       FAVOURITE="{} %".format("Draw"))

        else:
            print("Did not get dataset", flush=True)

            # outputRandForest = (round(1000, 2) * 100 / 1)
            #
            # print(outputRandForest, flush=True)

        return render_template('index.html')
    else:
        return render_template('index.html')


@app.route('/predict_api', methods=['POST'])
def predict_api():
    '''
    for direct api call through request
    :return:
    '''
    data = request.get_json(force=True)
    prediction = model.predict_([np.array(list(data.values))])
    output = prediction[0]
    return jsonify(output)

    # return jsonify(output)


@app.route("/fighterDataset2.json", methods=["GET"])
@cross_origin(supports_credentials=True)
def get_example():
    """GET in server"""
    response = jsonify(message="Simple server is running")

    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route('/react_api', methods=['POST'])
@cross_origin(supports_credentials=True)

def react_api():
    global randomForestWinFav, randomForestWinTwoUnd

    if request.method == 'POST':
        if request.data:
            data = request.data.decode('UTF-8')
            # print(request.data)
            # print(len(request.data))
            print("data",data)

            # after receiving data
            print("receiving data", flush=True)
            data = data.replace("[", "")            # dataset = [x for x in data] stored in a list
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

            # df = pd.DataFrame(dataset)
            # # df.replace(stance)
            # df.replace(regex=['Orthodox'], value=1, inplace=True)
            # df.replace(regex=['Southpaw'], value=3, inplace=True)
            # df.replace(regex=['Switch'], value=4, inplace=True)
            # df.replace(regex=['Open Stance'], value=1, inplace=True)
            # df.replace(regex=['Sideways'], value=1, inplace=True)
            # print("Datasets", df, flush=True)
            # print(df, flush=True)
            # final_features = df[0:].values.tolist()
            # result = np.array(final_features)
            # result = result.T
            # print("result", result.T, flush=True)
            # result = result.astype(float)
            # result = result[0]
            # print('final feature *** ', result, flush=True)

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
            print("system check")
            print(toPredict)
            print("length")
            print(len(toPredict[0]))
            toPredictReverseOne = UFC_data.iloc[-1][0:13]
            toPredictReverseTwo = UFC_data.iloc[-1][13:]
            topredictTwo = []
            ######## revresing the Data for Fav and underdog ########
            [topredictTwo.append(x) for x in toPredictReverseTwo]
            [topredictTwo.append(x) for x in toPredictReverseOne]
            topredictTwo = np.asarray(topredictTwo).reshape(1, -1)
            # topredictTwo = np.asarray(topredictTwo)
            print("Testing ")
            print(topredictTwo)

            # print("to predict 2", toPredictTwo, flush=True)
            # print("Prediction  Data Processed ", flush=True)
            # print("testing!!!!!!!!!!!!",toPredictReverseOne)
            # print("testing!!!!!!!!!!!!",toPredictReverseTwo)

            # Pytorch Probabilities
            pyt = getPrediction(toPredict)
            pytTwo = getPrediction(topredictTwo)
            print("!!!!!!!!!!!pytorch", pyt.round(), flush=True)

            # XGB Prediction
            xgbPredictionTwo = xgbModel.predict_proba(topredictTwo)
            xgbPrediction = xgbModel.predict_proba(toPredict)
            print("XGB Boost prediction", xgbPrediction, flush=True)
            print("XGB Boost prediction Two", xgbPredictionTwo, flush=True)

            # # result = result.apply(lambda x: (x - x.min()) / (x.max() - x.min()))
            # print("Datasets2", df, flush=True)
            # # final_features = np.hstack(df)
            # # final_features = [x for x in final_features]
            # # print(type(final_features))
            # # df = pd.DataFrame(final_features)
            # # print("#result", result)

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
            randomForestLossFav = outputRandForest[0][0]
            randomForestWinFav = outputRandForest[0][1]
            randomForestLossTwoUnd = outputRandForestTwo[0][0]
            randomForestWinTwoUnd = outputRandForestTwo[0][1]

            # xvg boost prediction
            xgbLossFav = xgbPrediction[0][0]
            xgbWinFav = xgbPrediction[0][1]
            xgbLossTwoUnd = xgbPredictionTwo[0][0]
            xgbWinTwoUnd = xgbPredictionTwo[0][1]

            # pytorch prediction
            pyt_pred = pyt
            pyt_predTwo = pytTwo

            ####### Voting System #############
            fav = (randomForestWinFav + xgbWinFav) / 2
            favloss = (randomForestLossFav + xgbLossFav) / 2
            und = (randomForestWinTwoUnd + xgbWinTwoUnd) / 2
            undLoss = (randomForestLossTwoUnd + xgbLossTwoUnd) / 2
            fav_Score = 0
            und_score = 0

            # Random Forest Vote
            if randomForestWinFav > randomForestWinTwoUnd:
                fav_Score += 1

            elif randomForestWinTwoUnd > randomForestWinFav:
                und_score += 1
            else:
                fav_Score += 0.5
                und_score += 0.5
            # Xgb Vote
            if xgbWinFav > xgbWinTwoUnd:
                fav_Score += 1
            elif xgbWinTwoUnd > xgbWinFav:
                und_score += 1
            else:
                fav_Score += 0.5
                und_score += 0.5
            # Pytorch Vote
            if pyt_pred > pyt_predTwo:
                fav_Score += 1
            elif pyt_predTwo > pyt_pred:
                und_score += 1
            else:
                fav_Score += 0.5
                und_score += 0.5

            if fav_Score > und_score:
                print("fav", fav_Score)
                print(und_score)
                # return render_template('index.html', UNDERDOG="{} %".format(round(favloss * 100)),
                #                        FAVOURITE="{} %".format(round(fav * 100)))
                score = str(fav_Score)
                return (score)

            elif und_score > fav_Score:
                print("under", und_score)
                print(fav_Score)
                # return render_template('index.html', UNDERDOG="{} %".format(round(und * 100)),
                #                        FAVOURITE="{} %".format(round(undLoss * 100)))
                score = str(und_score)


                return str(score)


            else:
                print("under", und_score)
                print("fav", fav_Score)
                # return render_template('index.html', UNDERDOG="{} %".format("Draw"),
                #                        FAVOURITE="{} %".format("Draw"))
                #
                return ('Draw')
            # return()

        else:
            print("Did not get dataset", flush=True)

            # outputRandForest = (round(1000, 2) * 100 / 1)
            #
            # print(outputRandForest, flush=True)
            request.headers.add("Access-Control-Allow-Origin", "*")

        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
