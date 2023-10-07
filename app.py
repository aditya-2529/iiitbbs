from distutils.log import debug
import pickle
from flask import Flask , render_template, request

app= Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/heart')
def heart():
    return render_template('heartform.html')

@app.route('/diabetes')
def diabetes():
    return render_template('diabetesform.html')

@app.route('/heartform', methods=['GET','POST'])
def heartform():
    model=pickle.load(open('model.pkl','rb'))
    age = int(request.form.get('age'))
    sex = int(request.form.get('gender'))
    cp = int(request.form.get('chestPain'))
    trestbps = int(request.form.get('trestbps'))
    chol = int(request.form.get('chol'))
    fbs = int(request.form.get('fastingSugar'))
    restecg = int(request.form.get('restecg'))
    thalach = int(request.form.get('thalach'))
    exeng = int(request.form.get('exerciseAngina'))
    oldpeak = int(request.form.get('STDepression'))
    slope = int(request.form.get('slope'))
    ca = int(request.form.get('ca'))
    thal = int(request.form.get('thal'))
    pre = model.predict([[(age),(sex),(cp),(trestbps),(chol),(fbs),(restecg),(thalach),(exeng),(oldpeak),(slope),(ca),(thal)]])
    # pre = model.predict([[1,20,15,13,46,78,97,55,84,66,3,12,153]])
    output = round(pre[0],2)
    return render_template('result.html',out=output)

@app.route('/diabetesform', methods=['GET','POST'])
def diabetesform():
    model=pickle.load(open('modelD.pkl','rb'))
    pregnancies = int(request.form.get('pregnancies'))
    glucose = int(request.form.get('glucose'))
    bloodPressure = int(request.form.get('bloodPressure'))
    skinThickness = int(request.form.get('skinThickness'))
    insulin = int(request.form.get('insulin'))
    bmi = int(request.form.get('bmi'))
    diabetesPedigree = int(request.form.get('diabetesPedigree'))
    age = int(request.form.get('age'))
    # print((pregnancies),(glucose),(bloodPressure),(skinThickness),(insulin),(bmi),(diabetesPedigree),(age))
    pre=model.predict([[(pregnancies),(glucose),(bloodPressure),(skinThickness),(insulin),(bmi),(diabetesPedigree),(age)]])
    # pre = model.predict([[1,23,24,15,26,79,48,75]])
    output=round(pre[0],2)
    return render_template('result.html',out1=output)

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