from flask import Flask,render_template,request
import pickle
import numpy as np

#create flask app
app=Flask(__name__)

#load the pickle model
<<<<<<< HEAD
with open('modellr.pkl','rb') as model_file:
=======
with open('model2.pkl','rb') as model_file:
>>>>>>> 987298ad039a82ade46b3e90ec03b763f88e3749
    model=pickle.load(model_file)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/prediction',methods=['GET','POST'])
def predict():
    if request.method=='POST':
        crop_year = float(request.form['Crop Year'])
        area = float(request.form['Area'])
        temprature = float(request.form['Temprature'])
        humidity = float(request.form['Humidity'])
        pressure = float(request.form['Pressure'])
        state_names=request.form['State Name'].title()
        season_names=request.form['Season Name'].title()
        crop_names=request.form['Crop Names'].title()
    
    scaled_cy=(crop_year-2005.675439)/5.069206
    scaled_area=(area-23764.333872)/32899.371585
    scaled_temp=(temprature-303.297517)/4.558251
    scaled_hum=(humidity-66.467829)/16.363367
    scaled_pre=(pressure-1003.704828)/3.838096
    
<<<<<<< HEAD

    
    if state_names=="Andamanandnicobarislands":
        state_names=0
    elif state_names=="Andhra Pradesh":
        state_names=1
    elif state_names=="Arunachal Pradesh":
        state_names=2
    elif state_names=="Assam":
        state_names=3
    elif state_names=="Bihar":
        state_names=4
    elif state_names=="Chandigarh":
        state_names=5
    elif state_names=="Chhattisgarh":
        state_names=6
    elif state_names=="Dadraandnagarhaveli":
        state_names=7
    elif state_names=="Goa":
        state_names=8
    elif state_names=="Gujarat":
        state_names=9
    elif state_names=="Haryana":
        state_names=10
    elif state_names=="Himachal Pradesh":
        state_names=11
    elif state_names=="Jammuandkashmir":
        state_names=12
    elif state_names=="Jharkhand":
        state_names=13
    elif state_names=="Karnataka":
        state_names=14
    elif state_names=="Kerala":
        state_names=15
    elif state_names=="Madhya Pradesh":
        state_names=16
    elif state_names=="Maharashtra":
        state_names=17
    elif state_names=="Manipur":
        state_names=18
    elif state_names=="Meghalaya":
        state_names=19
    elif state_names=="Mizoram":
        state_names=20
    elif state_names=="Nagaland":
        state_names=21
    elif state_names=="Odisha":
        state_names=22
    elif state_names=="Puducherry":
        state_names=23
    elif state_names=="Punjab":
        state_names=24
    elif state_names=="Rajasthan":
        state_names=25
    elif state_names=="Sikkim":
        state_names=26
    elif state_names=="Tamil Nadu":
        state_names=27
    elif state_names=="Telangana":
        state_names=28
    elif state_names=="Tripura":
        state_names=29
    elif state_names=="Uttar Pradesh":
        state_names=30
    elif state_names=="Uttarakhand":
        state_names=31
    elif state_names=="West Bengal" :
        state_names=32
=======
    crop_names=request.form['Crop Names'].title()
    if crop_names=="Maize":
     crop_names=0
    if crop_names=="Rice":
     crop_names=1
    if crop_names=="Sugarcane":
     crop_names=2
    elif crop_names=='Wheat':
     crop_names=3
    
>>>>>>> 987298ad039a82ade46b3e90ec03b763f88e3749

    if season_names=="Autumn":
        season_names=0
    elif season_names=="Kharif":
        season_names=1
    elif season_names=="Rabi":
        season_names=2
    elif season_names=="Summer":
        season_names=3
    elif season_names=="Whole Year":
        season_names=4
    elif season_names=='Winter':
<<<<<<< HEAD
        season_names=5


    if crop_names=="Maize":
     crop_names=0
    elif crop_names=="Rice":
     crop_names=1
    elif crop_names=="Sugarcane":
     crop_names=2
    elif crop_names=='Wheat':
     crop_names=3
        

    # Make prediction
    feature=np.array([[scaled_cy,scaled_area,scaled_temp,scaled_hum,scaled_pre,state_names,season_names,crop_names]])
    print(feature)
    #prediction = model.predict(feature)
    #result=(prediction*99840.976746)+71988.387684
    
    #return render_template('prediction.html',pred_res=result)
=======
     season_names=5
    
    area = float(request.form['Area'])
    crop_year = int(request.form['Crop Year'])
    temprature = float(request.form['Temprature'])
    humidity = float(request.form['Humidity'])
    pressure = float(request.form['Pressure'])



    # Make prediction

    prediction = model.predict([[crop_names,state_names,season_names,area,crop_year,temprature,humidity,pressure]])
>>>>>>> 987298ad039a82ade46b3e90ec03b763f88e3749

    return f"The predicted crop yield is: {prediction[0]}"


if __name__=="__main__":
    app.run(debug=True)

    