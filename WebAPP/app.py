import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder as encoder, MinMaxScaler



app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


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
    if request.method == 'POST':
        print("test1", flush=True)

        if 'form' in request.form:

            # after receving data
            print("recived data", flush=True)
            data = request.form['form']
            # dataset = [x for x in data]
            dataset = lambda x: list(x.split(","))
            dataset = dataset(data)
            print("Datasets", dataset, flush=True)
            print("Datasets", dataset[0], flush=True)
            # idex not to conver = 0,4,14,18
            # Convert for adding to data frame
            for x in range(0, len(dataset)):
                if (x == 0) or (x == 4) or (x == 14) or (x == 18):
                    pass
                else:
                    dataset[x] = float(dataset[x])
                    print(dataset[x])
            # apppend one for extra column for dataframe to be dropped later 
            dataset.append(1)
            print("Datasets", dataset, flush=True)
            print("Datasets", type(dataset[1]), flush=True)

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
            # print(UFC_data.iloc[-1])
            toPredict = np.asarray(UFC_data.iloc[-1]).reshape(1, -1)

            # # result = result.apply(lambda x: (x - x.min()) / (x.max() - x.min()))
            # print("Datasets2", df, flush=True)
            # # final_features = np.hstack(df)
            # # final_features = [x for x in final_features]
            # # print(type(final_features))
            # # df = pd.DataFrame(final_features)
            # # print("#result", result)
            prediction = model.predict_proba(toPredict)
            output = prediction
            # print(prediction[0].round(), flush=True)
            output = (prediction [0]* 100 )
            print(output, flush=True)
            return render_template('index.html', UNDERDOG= "{} %".format(output[0]),FAVOURITE = "{} %".format(output[1]))

        else:
            print("Did not get dataset", flush=True)

            # output = (round(1000, 2) * 100 / 1)
            #
            # print(output, flush=True)

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


if __name__ == "__main__":
    app.run(debug=True)
