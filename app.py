from flask import Flask,render_template,request
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form values as strings
    pregn = request.form.get('pregnancies')
    glucose = request.form.get('glucose')
    bp = request.form.get('bloodpressure')
    sknThickness = request.form.get('skinthickness')
    insulin = request.form.get('insulin')
    bmi = request.form.get('bmi')
    dpf = request.form.get('dpf')
    Age = request.form.get('Age')

    # Convert form values to float
    parameter = [float(pregn), float(glucose), float(bp), float(sknThickness),
                 float(insulin), float(bmi), float(dpf), float(Age)]

    # Use the converted parameter for prediction
    
    result = model.predict([parameter])[0]

    # Returning the result
    if result==1:
        return render_template('index.html',label=1)
    else:
        return render_template('index.html',label=-1)


if __name__ == '__main__':
    app.run(debug=True)