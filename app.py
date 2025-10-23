from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "change-this-key"  # flash mesajları için

@app.route("/")
def index():
    features = [
        {"icon":"rocket","title":"Hızlı ve Hafif","desc":"Flask + Bootstrap ile ışık hızında."},
        {"icon":"palette","title":"Şık Tasarım","desc":"Minimal, modern ve mobil uyumlu."},
        {"icon":"wrench","title":"Kolay Gelişim","desc":"Bileşenleri artır, sayfaları çoğalt."},
    ]
    return render_template("index.html", features=features)

@app.route("/projeler")
def projects():
    items = [
        {"name":"Bulut Selam API","desc":"Basit selam servisi (JSON).","link":"#"},
        {"name":"Döviz Çevirici","desc":"Draw.io diyagramından canlı web'e.","link":"#"},
        {"name":"Kişisel Blog","desc":"Markdown tabanlı içerik denemesi.","link":"#"},
    ]
    return render_template("projects.html", items=items)

@app.route("/iletisim", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = (request.form.get("name") or "").strip()
        email = (request.form.get("email") or "").strip()
        message = (request.form.get("message") or "").strip()

        # basit doğrulama
        if not name or not email or not message:
            flash("Lütfen tüm alanları doldur.")
            return redirect(url_for("contact"))

        # burada gelecekte e-posta/DB entegrasyonu eklenebilir
        # şimdilik teşekkür sayfasına yönlendirelim
        return redirect(url_for("thanks", n=name))
    return render_template("contact.html")

@app.route("/tesekkur")
def thanks():
    n = request.args.get("n", "Ziyaretçi")
    return render_template("thanks.html", name=n)

# Render/Heroku gibi ortamlarda gunicorn bu objeyi arar: app
if __name__ == "__main__":
    app.run(debug=True)
