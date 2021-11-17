from flask import Flask, render_template , request
import diabetes
# from flask.wrappers import Request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method=="POST":
        Pregnancies = request.form['Preg']
        Glucose = request.form['glc']
        BloodPressure = request.form['bp']
        SkinThickness = request.form['skinc']
        Insulin = request.form['insulin']
        BMI = float(request.form['bmi'])
        DiabetesPedigreeFunction = float(request.form['dpf'])
        Age = request.form['age']
        data = (Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)
        result = diabetes.diabetes_prediction(data)
        return render_template("submit.html", res = result)
    else:
        return render_template("index.html")

@app.route("/submit", methods=['GET', 'POST'])
def submit():
    if request.method == "POST":
        return render_template('index.html')

if __name__ == "__main__":
    app.run()