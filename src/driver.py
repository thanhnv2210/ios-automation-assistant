from appium import webdriver
import json

def init_driver(config_path="config/capabilities.json"):
    with open(config_path) as f:
        caps = json.load(f)
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
    return driver
