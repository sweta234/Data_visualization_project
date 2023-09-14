import requests

url = "https://credit-card-number-validator.p.rapidapi.com/v1/validatecard"

querystring = {"cardnumber":"4682776017589385"}

headers = {
	"X-RapidAPI-Key": "d32f6b4dbemsh9ecf76c99f432b8p1a7dd0jsn1085ecdd8d9c",
	"X-RapidAPI-Host": "credit-card-number-validator.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)


