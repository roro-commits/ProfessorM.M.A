import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url, json={"HEIGHT": 0.5, "WEIGHT": 0.2666666667, "REACH": 0.6153846154, "STANCE": 0.2,
                             "DOB": 0.7222222222, "SLpM": 0.1947469571, "StrAcc": 0.6, "SApM": 0.2406779661,
                             "StrDef": 0.5423728814, "TDAvg": 0.1860465116, "TDAcc": 0.44, "TDDef": 0.57,
                             "SubAvg": 0.3783783784, "HEIGHT1": 0.05, "WEIGHT1": 0.2666666667, "REACH1": 0.6666666667,
                             "STANCE1": 0.2, "DOB1": 0.5833333333, "SLpM1": 0.4901256732, "StrAcc1": 0.5421686747,
                             "SApM1": 0.1653034869, "StrDef1": 0.7142857143, "TDAvg1": 0.0530035336, "TDAcc1": 0.42,
                             "TDDef1": 0.7, "SubAvg1": 0.0379310345})

# print(r.json())