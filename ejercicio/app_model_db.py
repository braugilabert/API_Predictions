from flask import Flask, request, jsonify
import os
import pickle
import pandas as pd
import sqlite3 
#SQL

os.chdir(os.path.dirname(__file__))

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET'])
def hello():
    return "Bienvenido a mi API del modelo advertising"

@app.route('/v2/predict', methods=['GET'])

def the_prediction(): #PREDICTS
    model = pickle.load(open('data/advertising_model','rb'))
    tv = request.args.get('tv', None)
    radio = request.args.get('radio', None)
    newspaper = request.args.get('newspaper', None)

    if tv is None or radio is None or newspaper is None:
        return "Some arguments are missing, as input values are needed to predict"
    else:
        prediction = model.predict([[tv,radio,newspaper]])
        return "Prediction of sales when you invest that money in TV, radio and newspaper is: " + str(round(prediction[0],2)) + 'k €'

@app.route('/v2/ingest_data', methods=['POST'])
def new_data_entry():
    tv = request.args.get('tv', None)
    radio = request.args.get('radio', None)
    newspaper = request.args.get('newspaper', None)
    sales = request.args.get('sales', None)

    connection = sqlite3.connect('data/Adverti.db')
    cursor = connection.cursor()
    query = '''INSERT INTO campañas VALUES (?,?,?,?)'''
    result = cursor.execute(query, (tv, radio, newspaper, sales) ).fetchall()

    query = '''SELECT * FROM campañas'''
    result = cursor.execute(query).fetchall()
    connection.commit()
    connection.close()
    return jsonify(result)

@app.route('/v2/retrain', methods=['PUT'])
def to_train_the_model():
    connection = sqlite3.connect('data/Adverti.db')
    cursor = connection.cursor()
    query = ''' SELECT * FROM inversiones'''
    result = cursor.execute(query).fetchall()
    df = pd.DataFrame(result)
    x = df.drop(columns = ["sales"])
    y = df["sales"]
    #MODEL
    model = pickle.load(open('data/advertising_model','rb'))
    model.fit(x,y)
    pickle.dump(model, open('data/advertising_model','wb'))

app.run()

