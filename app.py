# Importing essential libraries
from flask import Flask, render_template, request
import elements as e

app = Flask(__name__)

global diabetes


@app.route('/', methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        pregnancies = request.form["pregnancies"]
        glucose = request.form["glucose"]
        blood_pressure = request.form["bloodpressure"]
        skin_thickness = request.form["skinthickness"]
        insulin = request.form["insulin"]
        bmi = request.form["bmi"]
        dpf = request.form["dpf"]
        age = request.form["age"]
        diabetes = e.predict(pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf,
                             age)
        return render_template('index.html', db_pred=diabetes)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
