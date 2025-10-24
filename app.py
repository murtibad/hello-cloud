from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Merhaba, Buluttan Selam!"

if __name__ == "__main__":
    app.run(debug=True)
