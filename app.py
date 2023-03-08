from flask import Flask,render_template,request
from joblib import load
import numpy as np
import sklearn
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')
@app.route("/play",methods=['POST'])
def play():
    gender = request.form['gender']
    age = request.form['age']
    currentSmoker = request.form['currentSmoker']
    cigsPerDay = request.form['cigsPerDay']
    BPMeds = request.form['BPMeds']
    prevalentStroke = request.form['prevalentStroke']
    prevalentHyp = request.form['prevalentHyp']
    diabetes = request.form['diabetes']
    totChol = request.form['totChol']
    sysBP = request.form['sysBP']
    diaBP = request.form['diaBP']
    BMI = request.form['BMI']
    heartRate = request.form['heartRate']
    glucose = request.form['glucose']
    model = load("model/model_heart")
    a=[gender,age,currentSmoker,cigsPerDay,BPMeds,prevalentStroke,prevalentHyp,diabetes,totChol,sysBP,diaBP,BMI,heartRate,glucose]
    b = np.array(a,dtype=float)
    prediction = model.predict([b])
    print(prediction)
    if(prediction[0]==1):
        result= "Yes you are suffering with cronical heart disease"
        return render_template('result.html',result = result)
    else:
        result= "You dont have any heart disease ! dont worry about it"
        return render_template("result.html",result=result)
app.run(debug=True)
   