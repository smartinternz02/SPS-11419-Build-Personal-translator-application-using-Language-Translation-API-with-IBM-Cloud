# for testing the detect language service
import requests 
import config

url = "https://language-translation.p.rapidapi.com/translateLanguage/detect-language"
querystring = {"text":"Привет, мой дорогой друг!"} 
headers = {
    'x-rapidapi-key': config.apikey,
    'x-rapidapi-host': "language-translation.p.rapidapi.com"
    } 

response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)

