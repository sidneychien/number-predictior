#-*- coding:utf-8 -*-
import json
from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify
from sklearn.linear_model import LinearRegression
import numpy as np

app = Flask(__name__)


X = [[1.7,5,0.76,1,0.5],[1.6,3.2,0.42,1,0.48],[1.5,7,0.25,1,0.36],[1.2,7.66,0.33,1,0.4],[1.87,3.72,0.24,1,0.37],[1,1.5,0.15,1,0.42]]
y = [[9],[13],[11],[4],[15],[7]]


linreg = LinearRegression()
linreg.fit(X,y)

predicy=linreg.predict([[1,1,1,1,1]])


@app.route('/' , methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        a = request.get_data()
        dict1 = json.loads(a)
        return json.dumps(dict1["data"])
    else:
        return str(predicy)


if __name__ =='__main__':
    app.run(debug=True)