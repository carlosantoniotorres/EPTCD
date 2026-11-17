import os
from twilio.rest import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, PHONE_NUMBER, API_KEY_WAPI
import time
from requests import Recuest, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

from datetime import datatime


query = "Estado de Mexico"
api_key = API_KEY_WAPI

url_clima = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={query}&days=1&aqi=no&alerts=no"

