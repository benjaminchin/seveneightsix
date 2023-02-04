from flask import Flask, request, render_template
from browsermobproxy import Server
from selenium import webdriver

server = Server(
    "eco-website/venv/Lib/site-packages/browsermob-proxy-2.1.4-bin/browsermob-proxy-2.1.4/bin/")
server.start()
proxy = server.create_proxy()

profile = webdriver.FirefoxProfile()
profile.set_proxy(proxy.selenium_proxy())
driver = webdriver.Firefox(firefox_profile=profile)

proxy.new_har("google")
driver.get("https://google.com")
har = proxy.har

server.stop()
driver.quit()

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
