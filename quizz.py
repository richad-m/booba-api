# Retrieve a quote from API
# Stock response
# display phrase in template
import requests
import json


def fetch_quote():
    response = requests.get('https://booba-api.herokuapp.com/api/quotes')
    return response.json()
