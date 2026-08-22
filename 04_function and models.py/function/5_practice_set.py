


'''Import the math module and use it to:

Find the square root of 144'''
import math
import requests

print(math.sqrt(144))

'''Calculate sin(90°) (hint: use math.radians())'''
print(math.sin(math.radians(90)))


'''Install and import the requests module (if available) and use it to fetch data from "https://api.github.com".'''

r = requests.get("https://api.github.com")
print(r.status_code)
print(r.text)

