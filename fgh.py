import requests

url = "https://fidelity-investments.p.rapidapi.com/v3/auto-complete"

querystring = {"q":"apple"}

headers = {
	"X-RapidAPI-Key": "d32f6b4dbemsh9ecf76c99f432b8p1a7dd0jsn1085ecdd8d9c",
	"X-RapidAPI-Host": "fidelity-investments.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
