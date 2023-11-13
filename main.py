# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "computo en la nube sabado 9:00 am - FINAL!"

app.run(host="0.0.0.0")