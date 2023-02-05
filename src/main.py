from flask import Flask, request, render_template
import requests

EMISSION_CONST = 0.00086638382

app = Flask(__name__)

url = ""


@app.route('/home/')
@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        url = request.form.get("url")
        visitors = request.form.get("visitors")
        
        data = calculate(url, visitors)
        return render_template("display.html", data=data)
    return render_template("template.html")


@app.route('/about/')
def about():
    return render_template("About.html")


def calculate(url: str, visitors: int) -> int:
    response = requests.get(url)
    size = len(response.content)
    mb = size/1024/1024
    netdata = mb*float(visitors)
    return round(EMISSION_CONST*netdata, 5)


if __name__ == "__main__":
    app.run(port=80)
