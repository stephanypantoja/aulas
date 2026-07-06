from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Stephany Hanna Estrão Pantoja"

if __name__ == "__main__":
    app.run(debug=True)