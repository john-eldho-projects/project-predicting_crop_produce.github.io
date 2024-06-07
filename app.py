from flask import Flask, render_template, request
import pickle
import numpy as np


#create flask app
app = Flask(__name__)

# Load the pickle model
with open('model (4).pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':

        # Get user input from the form 
        crop_names = request.form['crop_names']
        crop_mapping = {"Maize": 0, "Rice": 1, "Sugarcane": 2, "Wheat": 3}
        crop_names = crop_mapping[crop_names]
    
        area = float(request.form['area'])  
        scaled_area = (area - 23764.333872) / 32899.371585

        crop_year = float(request.form['crop_year'])
        scaled_cy = (crop_year - 2005.675439) / 5.069206

        temprature = float(request.form['temprature'])
        scaled_temp = (temprature - 303.297517) / 4.558251

        humidity = float(request.form['humidity'])
        scaled_hum = (humidity - 66.467829) / 16.363367

        pressure = float(request.form['pressure'])
        scaled_pre = (pressure - 1003.704828) / 3.838096

        state_names = request.form['state_name']
        state_mapping = {
            "Andaman and Nicobar Islands": 0, "Andhra Pradesh": 1, "Arunachal Pradesh": 2, 
            "Assam": 3, "Bihar": 4, "Chandigarh": 5, "Chhattisgarh": 6, 
            "Dadra and Nagar Haveli": 7, "Goa": 8, "Gujarat": 9, "Haryana": 10, 
            "Himachal Pradesh": 11, "Jammu and Kashmir": 12, "Jharkhand": 13, 
            "Karnataka": 14, "Kerala": 15, "Madhya Pradesh": 16, "Maharashtra": 17, 
            "Manipur": 18, "Meghalaya": 19, "Mizoram": 20, "Nagaland": 21, 
            "Odisha": 22, "Puducherry": 23, "Punjab": 24, "Rajasthan": 25, 
            "Sikkim": 26, "Tamil Nadu": 27, "Telangana": 28, "Tripura": 29, 
            "Uttar Pradesh": 30, "Uttarakhand": 31, "West Bengal": 32
        }
        state_names = state_mapping[state_names]

        season_names = request.form['season_name']
        season_mapping = {
            "Autumn": 0, "Kharif": 1, "Rabi": 2, "Summer": 3, 
            "Whole Year": 4, "Winter": 5
        }
        season_names = season_mapping[season_names]

        # Make prediction
        feature = np.array([[scaled_cy, scaled_area, scaled_temp, scaled_hum, scaled_pre, state_names, season_names, crop_names]])
        prediction = model.predict(feature)
        num = float(prediction)
        result = (num * 99840.976746) + 71988.387684
    
        return render_template('prediction.html', pred_res=int(result))

if __name__ == "__main__":
    app.run(debug=True)
