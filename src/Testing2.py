import requests

link = "https://observablehq.com/@mrchrisadams/carbon-footprint-of-sending-data-around"

# Have field where variable called "link" = user input, and
response = requests.get(link)
size = len(response.content)

KB = int(size)/1024
MB = KB/1024

# Have users enter the amount of monthly visitors = variable "visitors"
visitors = 10000

# Equation for Total data used by website and users
netdata = MB*visitors
emissions = 0.00086638382*netdata
print('The monthly emissions associated with your website amounts to ' +
      str(emissions) + ' kilograms of CO2')
