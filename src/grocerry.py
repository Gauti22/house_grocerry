import pandas as pd
import numpy as np

def data_read(path):
    data=pd.read_csv(path)
    return(data)

def processing(data):
    data['Finished']=data['Finished'].str.strip()
    data=data[data['Finished']=='Yes']
    data['Item'] = data['Item'].str.split('(').str[0].str.strip()
    return(data)


if __name__=='__main__':
    path='/Users/gautammehta/Downloads/GroceryList.xlsx - Grocery list.csv'
    data=data_read(path)
    processing(data)