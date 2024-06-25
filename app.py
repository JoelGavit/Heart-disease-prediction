from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/your_server_script', methods=['POST'])
def index():
    if request.method == 'POST':
        # Extract form data
        name = request.form['name']
        sex = request.form['sex']
        age = int(request.form['age'])
        BMI = float(request.form['BMI'])
        smoking = request.form['smoking']
        smoking_years = int(request.form.get('smokingYears', 0))  # default to 0 if not provided
        alcohol = request.form['Alcohol']
        alcohol_years = int(request.form.get('AlcoholAddictyears', 0))  # default to 0 if not provided
        stroke = request.form['Stroke']
        physical_health = int(request.form['PhysicalHealth'])
        mental_health = int(request.form['MentalHealth'])
        blood_pressure = int(request.form['bloodPressure'])
        cholesterol = int(request.form['cholesterol'])
        diabetes = request.form['diabetes']
        fasting_blood_sugar = request.form['fastingBloodSugar']
        walking = request.form['DiffWalking']
        physical_activity = request.form['PhysicalActivity']
        sleep_time = int(request.form['Sleeptime'])
        asthma = request.form['Asthma']
        kidney_disease = request.form['Kidneydisease']
        skin_cancer = request.form['Skincancer']

        # Call the function to predict cardiac risk
        # prediction = predict_cardiac_risk(name, sex, age, BMI, smoking, smoking_years, alcohol, alcohol_years,
        #                                    stroke, physical_health, mental_health, blood_pressure, cholesterol,
        #                                    diabetes, fasting_blood_sugar, walking, physical_activity, sleep_time,
        #                                    asthma, kidney_disease, skin_cancer)

    #     return f'The predicted cardiac risk for {name} is: {prediction}'
    # else:
    #     return 'Invalid request method'
        print(name)
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
