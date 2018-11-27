from flask import Flask, request, render_template 
from sklearn.externals import joblib
import pandas as pd

app = Flask(__name__)

model = None


def load_model():

    global model

    model = joblib.load("model_knn.joblib")


@app.route('/') 
def my_form():
	load_model()
	return render_template('main.html')


@app.route('/result', methods=['GET', 'POST'])
def result():
    pred_data = pd.DataFrame({})
    pred_data[0] = [int(request.form['age'])]
    pred_data[1] = [int(request.form['gender'])]
    pred_data[2] = [int(request.form['chest_pain'])]
    pred_data[3] = [int(request.form['blood_pressure'])]
    pred_data[4] = [int(request.form['cholestrol'])]
    pred_data[5] = [int(request.form['blood_sugar'])]
    pred_data[6] = [int(request.form['ecg'])]
    pred_data[7] = [int(request.form['heart_rate'])]
    pred_data[8] = [int(request.form['exercise'])]
    pred_data[9] = [int(request.form['st_depression'])]
    pred_data[10] = [int(request.form['peak_exercise'])]
    pred_data[11] = [int(request.form['vessels'])]
    pred_data[12] = [int(request.form['thal'])]

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