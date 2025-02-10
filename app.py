from flask import Flask, render_template, request, send_file
import qrcode

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def abc():
    qrc = ""
    qrcpath = ""
    if request.method == "POST":
        data = request.form["data"]
        qrc = qrcode.make(data)
        
        qrcpath = "static/qrcode.png"
        qrc.save(qrcpath)

    return render_template("index.html", qrc=qrcpath)

if __name__ == "__main__":
    app.run(debug=True)