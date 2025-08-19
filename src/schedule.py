import pandas as pd
import numpy as np

def data_read1(path):
    data=pd.read_csv(path)
    return(data)

def processing1(data):
    data.drop(columns=['DATE','Days'],inplace=True)
    df=data[['Breakfast_Assigned','lunch_Assigned','dinner_Assigned']]
    df.rename(columns={'Breakfast_Assigned':'Breakfast','lunch_Assigned':'Lunch','dinner_Assigned':'Dinner'},inplace=True)
    long = df.melt(var_name='Meal', value_name='Assigned')
    pivot = pd.crosstab(long['Assigned'], long['Meal']) 
    pivot = pivot.reindex(index=['Gautam','Jatin','Vanshika'],
                        columns=['Breakfast','Lunch','Dinner'],
                        fill_value=0)
    return pivot

def processing2(data):
    df1=data[['Breakfast','Lunch','Dinner']]
    df1=df1.melt()
    df1=df1[~df1['value'].isnull()]
    # assumes your column is 'value'
    df1[['dish1','dish2']] = df1['value'].str.split(r'\s*\+\s*', n=1, expand=True)
    df1.drop(columns='value',inplace=True)
    df2 = df1[['variable', 'dish1']].rename(columns={'dish1': 'dish'})
    df3 = df1[['variable', 'dish2']].rename(columns={'dish2': 'dish'})
    df3=df3[~df3['dish'].isna()]
    union_all = pd.concat([df2, df3], ignore_index=True)
    union_all['dish'] = union_all['dish'].astype(str).str.capitalize().str.strip()
    dt=pd.crosstab(columns=union_all['variable'],index=union_all['dish'])
    return dt

def processing3(data1):
    df1=data1[['Breakfast','Lunch','Dinner']]
    df1=df1.melt()
    df1=df1[~df1['value'].isnull()]
    # assumes your column is 'value'
    df1[['dish1','dish2']] = df1['value'].str.capitalize().str.split(r'\s*\+\s*', n=1, expand=True)
    df1.drop(columns='value',inplace=True)
    df2 = df1[['variable', 'dish1']].rename(columns={'dish1': 'dish'})
    df3 = df1[['variable', 'dish2']].rename(columns={'dish2': 'dish'})
    df3=df3[~df3['dish'].isna()]
    union_all = pd.concat([df2, df3], ignore_index=True)
    union_all['dish']=pd.Series(union_all['dish'].str.capitalize())
    a=union_all['dish'].value_counts().reset_index()
    return a

if __name__=='__main__':
    path='/Users/gautammehta/Downloads/GroceryList.xlsx - Daily meal plan.csv'
    data=data_read1(path)
    pivot=processing1(data)
    dt=processing2(data)