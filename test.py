import pandas as pd
def test_a(a,b,c):
    if(a+b>=c):
        return True
    else:
        return False

# dict=[[1,2,3,4,5,11],[2,3,4,5,6,7],[3,4,5,6,7,8],[4,5,6,7,8,9],[5,6,7,8,9,10]]
# data=pd.DataFrame(dict)
# data_1 = data.copy()
# data_1.at[0,0]=10
# print(data)
# for indexs in data.index:
#     print(data.at[indexs,'result'])