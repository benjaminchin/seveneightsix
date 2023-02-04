import requests
response = requests.get('https://ecofriendlyweb.org/eco-friendly-website-accreditation/')
x = len(response.content)
print(x)
print('word')