import requests

r = requests.get(url="https://github.com/benjaminchin")
print(str(len(r.content)) + " bytes")
print(r.content)
