import csv

clean_data = []
csv_rows = ['NAME', 'HEIGHT', 'WEIGHT', 'REACH', 'STANCE', 'DOB', 'SLpM', 'StrAcc', 'SApM', 'StrDef', 'TDAvg',
            'TDAcc', 'TDDef', 'SubAvg',
            'NAME1', 'HEIGHT1', 'WEIGHT1', 'REACH1', 'STANCE1', 'DOB1', 'SLpM1', 'StrAcc1', 'SApM1',
            'StrDef1', 'TDAvg1', 'TDAcc1', 'TDDef1', 'SubAvg1', 'WIN'
            ]
result = ['1', '0']

with open('/home/rotimi/Documents/FYP/ProfessorM.M.A/ufc_data/not_clean.csv', 'r+') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        clean_data.append(row[0:14])

with open('clean.csv', 'w+', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    spamwriter.writerow(csv_rows)
    data = clean_data[1:]
    win = result[0:1]
    lose = result[1:]
    print(len(data) / 2)
    for row in range(int(len(data) / 2)):

        if (row % 2) != 0:
            spamwriter.writerow(data[row - 1] + data[row] + win)

    for row in range(int(len(data) / 2), len(data)):

        if (row % 2) != 0:
            spamwriter.writerow(data[row] + data[row - 1] + lose)

    pass


