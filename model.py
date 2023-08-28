import pandas as pd
import numpy as np

df=pd.read_excel('prere_esc_raw_data.xlsx')

df=df.copy()

df['MATURITY'] = pd.to_datetime(df['MATURITY'])


df['Analysis']= 0

def prere_esc(df):
    #Pre refunded bonds spread

    df.loc[(df['Analysis'] == 0) & (df['RATING'] == 'Pre refunded') & (df['COUPON'] == 0),['Analysis']] = 'new pref, spread 20.'
    df.loc[(df['Analysis'] == 0) & (df['RATING'] == 'Pre refunded') & (df['TAXSTATUS'] == 'AMT'),['Analysis']] = 'new pref, spread 20.'
    df.loc[(df['Analysis'] == 0) & (df['RATING'] == 'Pre refunded') & (df['COUPON'] == 0) & (df['TAXSTATUS'] == 'AMT'),['Analysis']] = 'new pref, spread 40.'
    df.loc[(df['Analysis'] == 0) & (df['RATING'] == 'Pre refunded') & (df['USEOFPROCEEDS'].isin(['Hospitals','Healthcare'])),['Analysis']] = 'new pref, spread 20.'
    df.loc[(df['Analysis'] == 0) & (df['RATING'] == 'Pre refunded') & (df['USEOFPROCEEDS'].isin(['Retirement Centers','Charter School'])),['Analysis']] = 'new pref, spread 30.'
    df.loc[(df['Analysis'] == 0) & (df['RATING'] == 'Pre refunded') & (df['COUPON'] != 0) & (df['TAXSTATUS'] != 'AMT') & (df['USEOFPROCEEDS'].isin(['Hospitals','Healthcare','Retirement Centers','Charter School']) == False),['Analysis']] = 'new pref, spread 0.'

    #Escrowed bonds spread

    df.loc[(df['Analysis'] == 0) & (df['RATING'] == 'Escrowed') & (df['COUPON'] == 0) & (df['MATURITY'].between('01/01/2022','12/31/2022')),['Analysis']] = 'new etm, spread 15.'
    df.loc[(df['Analysis'] == 0) & (df['RATING'] == 'Escrowed') & (df['COUPON'] == 0) & (df['MATURITY'] >= '01/01/2023'),['Analysis']] = 'new etm, spread 20.'
    df.loc[(df['Analysis'] == 0) & (df['RATING'] == 'Escrowed') & (df['USEOFPROCEEDS'].isin(['Hospitals','Healthcare'])),['Analysis']] = 'new etm, spread 20.'
    df.loc[(df['Analysis'] == 0) & (df['RATING'] == 'Escrowed') & (df['USEOFPROCEEDS'].isin(['Retirement Centers','Charter School'])),['Analysis']] = 'new etm, spread 30.'
    df.loc[(df['Analysis'] == 0) & (df['RATING'] == 'Escrowed') & (df['COUPON'] != 0) & (df['TAXSTATUS'] != 'AMT') & (df['USEOFPROCEEDS'].isin(['Hospitals','Healthcare','Retirement Centers','Charter School']) == False),['Analysis']] = 'new etm, spread 0.'
    
    return df

prere_esc(df)

