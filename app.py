from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Merhaba, Buluttan Selam!</h1><p>Site ayakta 🎉</p>"

if __name__ == "__main__":
    app.run(debug=True)
