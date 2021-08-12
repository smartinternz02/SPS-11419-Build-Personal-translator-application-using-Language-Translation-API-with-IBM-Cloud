# returns a list of languages supported by the translator service
import requests
import json
import config

url = "https://language-translation.p.rapidapi.com/translateLanguage/supported-language"
headers = { 
    'x-rapidapi-key': config.apikey,
    'x-rapidapi-host': "language-translation.p.rapidapi.com" 
    } 
response = requests.request("GET", url, headers=headers) 
print(response.text)
