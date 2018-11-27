from flask import Flask, request, render_template 
from sklearn.externals import joblib
import pandas as pd

app = Flask(__name__)

model = None


def load_model():

    global model

    model = joblib.load('KNN_Model.joblib')


@app.route('/') 
def my_form():
	load_model()
	return render_template('main.html')

@app.route('/main') 
def main_form():
	load_model()
	return render_template('main.html')

@app.route('/about')
def about_us():
    return render_template('about.html')


@app.route('/result', methods=['GET', 'POST'])
def result():
    height = 1
    width = 40
    pred_data = pd.DataFrame(0, index=range(height), columns=range(width))
    
    # Untuk data umur
    age = int(request.form['age'])
    pred_data[0] = [age]
    if (age < 30):
        pred_data[38] = 1
    elif (age < 40):
        pred_data[34] = 1
    elif (age < 50):
        pred_data[35] = 1
    elif (age < 60):
        pred_data[36] = 1
    elif (age < 70):
        pred_data[37] = 1
    else:
        pred_data[39] = 1
            
    pred_data[1] = [int(request.form['blood_pressure'])]
    pred_data[2] = [int(request.form['cholestrol'])]
    pred_data[3] = [int(request.form['heart_rate'])]
    pred_data[4] = [int(request.form['st_depression'])]
    
    # Untuk data jenis kelamin
    gender = int(request.form['gender'])
    if (gender == 0):
        pred_data[5] = 1
    else:
        pred_data[6] = 1
    
    # Untuk data jenis sakit dada
    chest_pain = int(request.form['chest_pain'])
    if (chest_pain == 1):
        pred_data[10] = 1
    elif (chest_pain == 2):
        pred_data[8] = 1
    elif (chest_pain == 3):
        pred_data[9] = 1
    else:
        pred_data[7] = 1

    blood_sugar = int(request.form['blood_sugar'])
    if (blood_sugar == 0):
        pred_data[11] = 1
    else:
        pred_data[12] = 1
    
    ecg = int(request.form['ecg'])
    if (ecg == 1):
        pred_data[17] = 1
    elif (ecg == 2):
        pred_data[15] = 1
    else:
        pred_data[16] = 1

    exercise = int(request.form['exercise'])
    if (exercise == 0):
        pred_data[19] = 1
    else:
        pred_data[20] = 1

    peak_exercise = int(request.form['peak_exercise'])
    if (peak_exercise == 1):
        pred_data[24] = 1
    elif (peak_exercise == 2):
        pred_data[23] = 1
    else:
        pred_data[22] = 1
    
    vessels = int(request.form['vessels'])
    if (vessels == 0):
        pred_data[25] = 1
    elif (vessels == 1):
        pred_data[26] = 1
    elif (vessels == 2):
        pred_data[27] = 1
    else:
        pred_data[28] = 1
    
    thal = int(request.form['thal'])
    if (thal == 3):
        pred_data[32] = 1
    elif (thal == 6):
        pred_data[31] = 1
    else:
        pred_data[33] = 1

    pred = model.predict(pred_data)
    return render_template('result.html', hasil=pred[0])

# if __name__ == '__main__':

#     try:
#         load_model()
#         print("Model loaded")

#     except Exception as e:
#         print("Model loading failed")
#         print(str(e))
		

#     app.run()