from flask import Flask, request, render_template

app = Flask(__name__)

url = ""

@app.route('/home/')
@app.route('/', methods=["GET", "POST"])
def get():
    if request.method == "POST":
        url = request.form.get("url")
        visitors = request.form.get("visitors")
        '''return "The requested URL is: " + str(url) + "\n The emissions for the given site is: " + str(calculate(url, visitors)) + " kilograms of CO2 per month."'''
        data = calculate(url, visitors)
        return render_template("display.html", data=data)
    return render_template("template.html")


if __name__ == "__main__":
    app.run()
