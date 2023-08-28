import pandas as pd
import numpy as np
from flask import Flask,request,render_template, jsonify
from model import prere_esc

app = Flask(__name__,template_folder='Templates')

df=pd.read_excel('prere_esc_raw_data.xlsx')

df=df.copy()

@app.route('/')

def model_op(df):

    df['MATURITY'] = pd.to_datetime(df['MATURITY'])

    df['Analysis']= 0
    
    prere_esc(df)
    
    return render_template('index.html',tables = [df.to_html()],titles =[''] )

model_op(df)
    



if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=9696)

