from distutils.log import debug
import pickle
from flask import Flask , render_template,request

app= Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/heartform', methods=['GET','POST'])
def heartform():
    # prediction=model.predict([[float(request.form.get('age'))]])
    # output=round(prediction[0],2)
    model=pickle.load(open('model.pkl','rb'))
    age = request.form.get('age')
    sex = request.form.get('gender')
    cp = request.form.get('chestPain')
    trestbps = request.form.get('trestbps')
    chol = request.form.get('chol')
    fbs = request.form.get('fastingSugar')
    restecg = request.form.get('restecg')
    thalach = request.form.get('thalach')
    exeng = request.form.get('exerciseAngina')
    oldpeak = request.form.get('STDepression')
    slope = request.form.get('slope')
    ca = request.form.get('ca')
    thal = request.form.get('thal')
    pre = model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exeng,oldpeak,slope,ca,thal]])
    output = round(pre[0],2)
    return render_template('heartform.html',out=output)

@app.route('/diabetesform', methods=['GET','POST'])
def diabetesform():
    model=pickle.load(open('modelD.pkl','rb'))
    pregnancies = request.form.get('pregnancies')
    glucose = int(request.form.get('glucose'))
    bloodPressure = request.form.get('bloodPressure')
    skinThickness = request.form.get('skinThickness')
    insulin = request.form.get('insulin')
    bmi = request.form.get('bmi')
    diabetesPedigree = request.form.get('diabetesPedigree')
    age = request.form.get('age')
    # print((pregnancies),(glucose),(bloodPressure),(skinThickness),(insulin),(bmi),(diabetesPedigree),(age))
    prediction=model.predict([[(pregnancies),(glucose),(bloodPressure),(skinThickness),(insulin),(bmi),(diabetesPedigree),(age)]])
    output=round(prediction[0],2)
    return render_template('diabetesform.html',out=output)

@app.route('/parkinson', methods=['GET','POST'])
def predict():
    model = pickle.load(open('modelP.pkl','rb'))
    fo = request.form.get('age')
    # fhi = int(request.form.get('glucose'))
    # flo = request.form.get('bloodPressure')
    # jit = request.form.get('skinThickness')
    # rap = request.form.get('insulin')
    # ppq = request.form.get('bmi')
    # ddp = request.form.get('diabetesPedigree')
    # age = request.form.get('age')
    prediction=model.predict([[8]])
    output=round(prediction[0],2)
    return render_template('parkinsonform.html', out=output)
if __name__ == '__main__':
    app.run(debug=True)