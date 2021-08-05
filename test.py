# for testing the detect language service
import requests 

url = "https://language-translation.p.rapidapi.com/translateLanguage/detect-language"
querystring = {"text":"Привет, мой дорогой друг!"} 
headers = {
    'x-rapidapi-key': "6baae6a51fmsha48ab291ec53a9fp1b09b7jsn9b56d5c35aa3",
    'x-rapidapi-host': "language-translation.p.rapidapi.com"
    } 

response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)

