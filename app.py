from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!doctype html>
    <html lang="tr">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Buluttan Selam ☁️</title>
        <style>
            * { box-sizing: border-box; }
            body {
                margin: 0;
                font-family: 'Poppins', sans-serif;
                background: radial-gradient(circle at 20% 20%, #5c6cff, #282c34);
                color: white;
                height: 100vh;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                overflow: hidden;
                text-align: center;
            }
            h1 {
                font-size: 3rem;
                margin-bottom: 0.3em;
                animation: fadeIn 2s ease-out;
            }
            p {
                font-size: 1.2rem;
                color: #cfd9ff;
                animation: fadeIn 3s ease-in;
            }
            a.button {
                display: inline-block;
                margin-top: 25px;
                padding: 12px 25px;
                border-radius: 25px;
                border: 2px solid #fff;
                color: #fff;
                text-decoration: none;
                font-weight: 500;
                transition: 0.3s;
                animation: fadeInUp 2.5s ease;
            }
            a.button:hover {
                background: #fff;
                color: #282c34;
            }
            footer {
                position: absolute;
                bottom: 20px;
                font-size: 0.9rem;
                color: #aab6ff;
                animation: fadeIn 4s ease;
            }

            /* animasyonlar */
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(20px); }
                to { opacity: 1; transform: translateY(0); }
            }
            @keyframes fadeInUp {
                from { opacity: 0; transform: translateY(50px); }
                to { opacity: 1; transform: translateY(0); }
            }

            /* yıldız arka plan */
            .stars {
                position: absolute;
                top: 0; left: 0;
                width: 100%; height: 100%;
                background: transparent url('https://raw.githubusercontent.com/jusleg/stars-background/master/stars.svg') repeat;
                animation: moveStars 60s linear infinite;
                z-index: 0;
            }
            @keyframes moveStars {
                from { background-position: 0 0; }
                to { background-position: 10000px 10000px; }
            }
            .content { z-index: 1; }
        </style>
    </head>
    <body>
        <div class="stars"></div>
        <div class="content">
            <h1>☁️ Buluttan Selam</h1>
            <p>Flask ile yapılmış küçük ama havalı bir bulut sitesi.</p>
            <a href="https://github.com/murattokac" target="_blank" class="button">GitHub Profilim</a>
        </div>
        <footer>© 2025 Murat Tokaç • Flask + Bulut</footer>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
