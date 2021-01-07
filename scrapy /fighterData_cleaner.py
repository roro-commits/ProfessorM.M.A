import pandas as pd
import matplotlib.pyplot as mpl
from multiprocessing import Process

df = pd.read_csv('FighterData/fighterData.csv')
dateOfBith = df['DOB']
date_list = []  # dates substring to removed/cleaned
height_list = []
height_list1 = []
heightOfFigters = df['HEIGHT']
# heightOfFigters1 = df['HEIGHT1']

df.replace(regex=['%', 'lbs.', '"', '--'], value='', inplace=True)
heightOfFigters.replace(regex=[' '], value='', inplace=True)
# heightOfFigters1.replace(regex=[' '], value='', inplace=True)


# checks data len if greater than example (Jan28, 1998) -> takes first 6 ('Jan28, ')
def dateClean():
    for dates in dateOfBith:
        if len(dates) > 5:
            date_list.append(dates[:7])

    # replace 1st 6 with '' (Jan28, 1998) -> (1998)
    for i in range(len(date_list)):
        df.replace(regex=[str(date_list[i])], value='', inplace=True)
        print(len(date_list), date_list[i], i)

    # print("********************************************************** one")


def test():
    for height in heightOfFigters:
        if len(height) > 0:
            height_list.append(height)
            # df.to_csv('clean_dataset.csv', index=False)
            # print(height)

    for i in range(len(height_list)):
        height = height_list[i].split("'")
        feet = int(height[0])
        inches = int(height[1])
        # feet1 = int(height1[0])
        # inches1 = int(height1[1])
        tot_inches = feet * 12 + inches
        meters = tot_inches * 0.0254
        df.replace(regex=[str(height_list[i])], value=meters, inplace=True)
        print(len(height_list), height_list[i], i)



dateClean()
test()

df.to_csv('fighter_clean_Dataset.csv', index=False)

print(True)



# if __name__ == '__main__':
#     p1 = Process(target=dateClean)
#     p1.start()
