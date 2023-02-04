from flask import Flask, request, render_template

app = Flask(__name__)

url = ""
dummy_value = 128


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        url = request.form.get("url")
        return "The requested URL is: " + str(url) + "\n the data usage is: " + str(calculate(dummy_value))
    return render_template("template.html")


@app.route('/about/')
def about():
    return render_template("About.html")


def calculate(dummy_value):
    return dummy_value * 10


if __name__ == "__main__":
    app.run()
