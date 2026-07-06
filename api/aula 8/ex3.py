from flask import Flask
from datetime import date

app = Flask(__name__)

@app.route("/saudacao")
def saudacao():
    return "Bom dia!"

@app.route("/data")
def data():
    hoje = date.today()
    return f"Data: {hoje}"


if __name__ == "__main__":
    app.run(debug=True)