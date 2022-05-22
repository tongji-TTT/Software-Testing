import pandas as pd
def get_per(data: pd.DataFrame):
    a = 0
    for index in data.index:
        if (data.at[index,'isSame'] == True):
            a = a + 1
    return round(a/len(data),2)
