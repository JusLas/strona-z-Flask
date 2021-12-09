from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "It's home page"

@app.route ("/mypage/me")
def about_me():
    return render_template("1stronawww.html")

@app.route("/mypage/contact", methods = ["GET","POST"])
def contact():
    print("Działam")
    if request.method == "POST":
        print("Działam2")
        my_data = request.form.get("aboutyou")
        print (my_data)

    return render_template("2stonawww.html")

app.run(debug = True)
#uruchomienie flaska z VC bez konieczności dodawania komend#

