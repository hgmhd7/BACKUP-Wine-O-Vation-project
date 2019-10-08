#importing libraries
import os
import numpy as np
import flask
import pickle
from flask_material import Material
import pandas as pd
import json
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy


#creating instance of the class
app=Flask(__name__, static_url_path='/static')
Material(app)



# Database Setup
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///wine_cellar.sqlite"


db = SQLAlchemy(app)

# reflect an existing database into a new modelapp
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)


# # Save references to each table
# Samples_Metadata = Base.classes.sample_metadata
master_wine_table = Base.classes.master_wine_table
wine_predictions = Base.classes.wine_predictions_table




#to tell flask what url shoud trigger the function index()
@app.route('/')
def index():
    return render_template('index.html')



@app.route('/story_of_wine')
def story_of_wine():
    return render_template('story_of_wine.html')


@app.route('/flavor_notes')
def flavor_notes():
    return render_template('flavor_notes.html')



@app.route('/virtual_sommelier')
def virtual_sommelier():
    return render_template('virtual_sommelier.html')



@app.route('/wine_recommender')
def wine_recommender():
    return render_template('wine_recommender.html')



@app.route('/predict_wine_score',methods=["POST"])

    
def predict_wine_score():
	# if request.method == 'POST':
	# 	petal_length = request.form['petal_length']
	# 	sepal_length = request.form['sepal_length']
	# 	petal_width = request.form['petal_width']
	# 	sepal_width = request.form['sepal_width']
	# 	model_choice = request.form['model_choice']

	# 	# Clean the data by convert from unicode to float 
	# 	sample_data = [sepal_length,sepal_width,petal_length,petal_width]
	# 	clean_data = [float(i) for i in sample_data]

	# 	# Reshape the Data as a Sample not Individual Features
	# 	ex1 = np.array(clean_data).reshape(1,-1)

	# 	# ex1 = np.array([6.2,3.4,5.4,2.3]).reshape(1,-1)

	# 	# Reloading the Model
	# 	if model_choice == 'logitmodel':
	# 	    logit_model = joblib.load('data/logit_model_iris.pkl')
	# 	    result_prediction = logit_model.predict(ex1)
	# 	elif model_choice == 'knnmodel':
	# 		knn_model = joblib.load('data/knn_model_iris.pkl')
	# 		result_prediction = knn_model.predict(ex1)
	# 	elif model_choice == 'svmmodel':
	# 		knn_model = joblib.load('data/svm_model_iris.pkl')
	# 		result_prediction = knn_model.predict(ex1)

	# return render_template('index.html', petal_width=petal_width,
	# 	sepal_width=sepal_width,
	# 	sepal_length=sepal_length,
	# 	petal_length=petal_length,
	# 	clean_data=clean_data,
	# 	result_prediction=result_prediction,
	# 	model_selected=model_choice)

    test_1 = "test_1_value..."

    return render_template('virtual_sommelier.html', testing_1=test_1)





@app.route('/recommend_wines',methods=["POST"])

def recommend_wines():

   # Use Pandas to perform the sql queryclear
    stmt = db.session.query(master_wine_table).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    wine_list = df.to_dict(orient='records')
    wine_list_jsonified = jsonify(wine_list)
    
    test_2 = "test_2_value..."

    return render_template('wine_recommender.html', testing_2=test_2, wine_list_jsonified=wine_list_jsonified)


#     #prediction function
# def WineRatingPredictor(to_predict_list):
#     to_predict = np.array(to_predict_list).reshape(1,5)
#     loaded_model = pickle.load(open("model.pkl","rb"))
#     result = loaded_model.predict(to_predict)
#     return result[0]


# @app.route('/virtual_sommelier',methods = ['POST'])
# def result():
#     if request.method == 'POST':
#         to_predict_list = request.form.to_dict()
#         to_predict_list=list(to_predict_list.values())
#         to_predict_list = list(map(int, to_predict_list))
#         result = WineRatingPredictor(to_predict_list)
         
#         if int(result)==1:
#             prediction='Income more than 50K'
#         else:
#             prediction='Income less that 50K'
            
#         return render_template("virtual_sommelier.html",prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)