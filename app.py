from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Ola, Flask"


if __name__ == '__main__':
    app.run(debug=True)
