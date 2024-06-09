import random
import requests
from pymongo.server_api import ServerApi
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from pymongo import MongoClient
import datetime
import json
from bson import ObjectId

class MongoJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super().default(obj)


# Twitter credentials
TWITTER_USERNAME = "baraja7378@jadsys.com"
TWITTER_PASSWORD = "thisismypasswordfortheinternshiptask"

# MongoDB credentials
MONGO_USERNAME = "testassignment"
MONGO_PASSWORD = "nuzjyc-kijfyG-xesce7"
MONGO_URI = f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@cluster0.ondxvyb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# MongoDB setup
client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
db = client['twitter_trends']
collection = db['trends']

# List of user agents to rotate
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.68",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.68",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.68",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36 Edg/89.0.774.68",
]


import requests

# Webshare.io API credentials
WEBSHARE_API_KEY = "ycil7i4615six3qf7k81eshu1nimkmcnozeo6c3h"
WEBSHARE_API_URL = "https://proxy.webshare.io/api/v2/proxy/list/?mode=direct&page=1&page_size=25"

# Function to get a proxy from Webshare.io
def get_free_proxy():
    params = {
        "api_key": WEBSHARE_API_KEY,
        "protocol": "http",
        "format": "json"
    }
    response = requests.get(WEBSHARE_API_URL, headers={"Authorization": "Token my-token-got-used-up" })
    if response.status_code == 200:
        proxy_list = response.json()["results"]
        if proxy_list:
            proxy = random.choice(proxy_list)
            proxy_url = f"http://{proxy['username']}:{proxy['password']}@{proxy['proxy_address']}:{proxy['port']}"
            return {"http": proxy_url}
    return None

def fetch_trending_topics():
    # Choose a random user-agent
    user_agent = random.choice(USER_AGENTS)
    #proxy = get_free_proxy()

    options = webdriver.ChromeOptions()
    options.add_argument(f'user-agent={user_agent}')
    #options.add_argument(f'--proxy-server={proxy["http"]}')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    trend_names = []
    try:
        # Log into Twitter
        driver.get('https://x.com/i/flow/login')
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input').send_keys(TWITTER_USERNAME)
        driver.find_element(By.XPATH,
                            '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]').send_keys(
            Keys.ENTER)
        time.sleep(2)

        driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input').send_keys('codetester1263')

        #press enter
        driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button').send_keys(Keys.ENTER)

        time.sleep(4)
        #enter password
        driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(TWITTER_PASSWORD)

        #press enter
        driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button').send_keys(Keys.ENTER)

        # sends the email to the email input
        #email.send_keys(TWITTER_USERNAME)
        # sends the password to the password input
        #password.send_keys(TWITTER_PASSWORD)
        # executes RETURN key action
        #password.send_keys(Keys.RETURN)

        time.sleep(2)
        driver.get('https://x.com/explore/tabs/keyword')

        time.sleep(5)
        #trends = driver.find_elements(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div')[1:6]
        trend_names.append(driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div/div/div[3]/div/div/div/div/div[2]/span/span').text)
        trend_names.append(driver.find_element(By.XPATH,
                                             '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div/div/div[4]/div/div/div/div/div[2]/span').text)
        trend_names.append(driver.find_element(By.XPATH,
                                             '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div/div/div[5]/div/div/div/div/div[2]/span').text)
        trend_names.append(driver.find_element(By.XPATH,
                                             '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div/div/div[6]/div/div/div/div/div[2]/span').text)
        trend_names.append(driver.find_element(By.XPATH,
                                             '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div/div/div[7]/div/div/div/div/div[2]/span').text)
    except Exception as e:
        trend_names = [f"Error fetching trends: ${e}"]
    finally:
        driver.quit()

    # Store in MongoDB
    record = {
        "trend1": trend_names[0] if len(trend_names) > 0 else "N/A",
        "trend2": trend_names[1] if len(trend_names) > 1 else "N/A",
        "trend3": trend_names[2] if len(trend_names) > 2 else "N/A",
        "trend4": trend_names[3] if len(trend_names) > 3 else "N/A",
        "trend5": trend_names[4] if len(trend_names) > 4 else "N/A",
        "timestamp": str(datetime.datetime.now()),  # Convert to string
        "ip_address": proxy
    }
    collection.insert_one(record)

    # Print the result as JSON string
    print(json.dumps(record, cls=MongoJSONEncoder))

if __name__ == "__main__":
    fetch_trending_topics()
