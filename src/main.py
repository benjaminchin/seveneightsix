from flask import Flask, request, render_template

app = Flask(__name__)

url = ""
@app.route('/', methods=["GET", "POST"])
def get():
    if request.method == "POST":
        url = request.form.get("url")
        return "The requested URL is: " + str(url)
    return render_template("template.html")


if __name__ == "__main__":
    app.run()
