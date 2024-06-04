from flask import Flask,render_template,request
import pickle
import numpy as np

#create flask app
app=Flask(__name__)

#load the pickle model
with open('model2.pkl','rb') as model_file:
    model=pickle.load(model_file)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    # Get user input from the form 
    
    crop_names=request.form['Crop Names'].title()
    if crop_names=="Maize":
     crop_names=0
    if crop_names=="Rice":
     crop_names=1
    if crop_names=="Sugarcane":
     crop_names=2
    elif crop_names=='Wheat':
     crop_names=3
    

    state_names=request.form['State Name'].title()
    if state_names=="Andaman and Nicobar Islands":
     state_names=0
    if state_names=="Andhra Pradesh":
     state_names=1
    if state_names=="Arunachal Pradesh":
     state_names=2
    if state_names=="Assam":
     state_names=3
    if state_names=="Bihar":
     state_names=4
    if state_names=="Chandigarh":
     state_names=5
    if state_names=="Chhattisgarh":
     state_names=6
    if state_names=="Dadra and Nagar Haveli":
     state_names=7
    if state_names=="Goa":
     state_names=8
    if state_names=="Gujarat":
     state_names=9
    if state_names=="Haryana":
     state_names=10
    if state_names=="Himachal Pradesh":
     state_names=11
    if state_names=="Jammu and Kashmir ":
     state_names=12
    if state_names=="Jharkhand":
     state_names=13
    if state_names=="Karnataka":
     state_names=14
    if state_names=="Kerala":
     state_names=15
    if state_names=="Madhya Pradesh":
     state_names=16
    if state_names=="Maharashtra":
     state_names=17
    if state_names=="Manipur":
     state_names=18
    if state_names=="Meghalaya":
     state_names=19
    if state_names=="Mizoram":
     state_names=20
    if state_names=="Nagaland":
     state_names=21
    if state_names=="Odisha":
     state_names=22
    if state_names=="Puducherry":
     state_names=23
    if state_names=="Punjab":
     state_names=24
    if state_names=="Rajasthan":
     state_names=25
    if state_names=="Sikkim":
     state_names=26
    if state_names=="Tamil Nadu":
     state_names=27
    if state_names=="Telangana":
     state_names=28
    if state_names=="Tripura":
     state_names=29
    if state_names=="Uttar Pradesh":
     state_names=30
    if state_names=="Uttarakhand":
     state_names=31
    elif state_names=='West Bengal':
     state_names=32


    season_names=request.form['Season Name'].title()
    if season_names=="Autumn":
     season_names=0
    if season_names=="Kharif":
     season_names=1
    if season_names=="Rabi":
     season_names=2
    if season_names=="Summer":
     season_names=3
    if season_names=="Whole Year":
     season_names=4
    elif season_names=='Winter':
     season_names=5
    
    area = float(request.form['Area'])
    crop_year = int(request.form['Crop Year'])
    temprature = float(request.form['Temprature'])
    humidity = float(request.form['Humidity'])
    pressure = float(request.form['Pressure'])



    # Make prediction

    prediction = model.predict([[crop_names,state_names,season_names,area,crop_year,temprature,humidity,pressure]])

    return f"The predicted crop yield is: {prediction[0]}"


if __name__=="__main__":
    app.run(debug=True)

    