import requests

#Get Request

url = "https://checkip.amazonaws.com"
response = requests.request("GET", url)
print(response.status_code)
print(response.text)

#You can use POSTMAN to create the Code for you