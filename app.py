# Flask app
from flask import Flask, request, render_template
import re
import requests
from gevent.pywsgi import WSGIServer
import os
import config

app = Flask(__name__)


#load home page
@app.route("/")
def home():
    return render_template('index.html')

#translate button
@app.route("/translator")
def translator():
    return render_template('translator.html')

#take language input from user
@app.route("/translate",methods=["POST"])
def translate():
    lang = request.form['type']
    out = request.form['output']
    ttext = findLang(lang,out)
    return render_template('translate.html',translated = ttext)

#function to call api, fetch results
def findLang(lang,out):
    url = "https://language-translation.p.rapidapi.com/translateLanguage/translate"

    payload = "{\r\"text\":\""+out+"\"," + "\r\"type\":\"plain\"," + "\r\"target\":\""+lang+"\"\r}"

    headers = {
        "content-type": "application/json",
        'x-rapidapi-key': config.apikey,
        'x-rapidapi-host': "language-translation.p.rapidapi.com"
        } 

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()['translatedText']

port = os.getenv('VCAP_APP_PORT','8080')
  
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug = True, host='0.0.0.0', port=port)

# https://github.com/IBM-Cloud/get-started-python
# helped in final deploying to ibm cloud