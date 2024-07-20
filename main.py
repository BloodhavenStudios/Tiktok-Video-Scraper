""" 
© 2024 Bloodhaven Studios. All rights reserved.
This code is part of https://github.com/BloodhavenStudios/Tiktok-Video-Scraper.

Licensed under the MIT License. See LICENSE file in the project root for full license information.

Main Module for Scraper.
"""
import logging
import threading
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from data import ScraperSettings
from scraper_functions import download_video

# Logging Configuration
# DO NOT TOUCH
logging.getLogger("selenium").setLevel(logging.CRITICAL)
logging.getLogger("urllib3").setLevel(logging.CRITICAL)

logging.basicConfig(
    filename="output.log",
    filemode="w",
    level=logging.DEBUG,
    format='[%(levelname)s] %(message)s'
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(levelname)s] %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

__all__ = [
    "ScraperSettings"
]

# Create driver instance and options
options = Options()
options.add_argument("start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options)
driver.get(ScraperSettings.account_link)

logging.info("Scraping Account: %s", ScraperSettings.account_link)

# Check for login popup/ something went wrong button
# Continue as Guest
time.sleep(ScraperSettings.wait_before_login)

try:
    if driver.find_element(By.ID, "loginContainer"):
        guest_button = driver.find_element(By.CSS_SELECTOR, "#loginContainer > div > div > div.css-txolmk-DivGuestModeContainer.exd0a435 > div")
        guest_button.click()
except:
    pass

# Something Went Wrong.
try:
    while(True):
        time.sleep(ScraperSettings.wait_before_refresh)
        if driver.find_element(By.CSS_SELECTOR, "#main-content-others_homepage > div > div.css-833rgq-DivShareLayoutMain.ee7zj8d4 > main > div"):
            refresh_button = driver.find_element(By.CSS_SELECTOR, "#main-content-others_homepage > div > div.css-833rgq-DivShareLayoutMain.ee7zj8d4 > main > div > button")
            refresh_button.click()
        else:
            break
except:
    pass

# Autoscroll through page
screen_height = driver.execute_script("return window.screen.height")
i = 1
while(True):
    driver.execute_script(f"window.scrollTo(0, {screen_height}*({i}*2));")
    i += 1
    time.sleep(ScraperSettings.scroll_speed)
    scroll_height = driver.execute_script("return document.body.scrollHeight;")  
    if (screen_height) * i > scroll_height:
        break

# Get all video links
with open(file="script.js", mode="r", encoding="UTF-8") as file:
    script = file.read()

urls_to_download = driver.execute_script(script)

print(f"Found: {len(urls_to_download)} videos.")
logging.info("Found: %s videos.", len(urls_to_download))

if not ScraperSettings.download_most_recent_videos_first:
    urls_to_download = reversed(urls_to_download)

# Download all videos
for index, url in enumerate(urls_to_download):
    try:
        print(f"Starting video download: {index+1}", end="")
        threading.Thread(target=download_video, args=(url, index+1,), daemon=True).start()
        time.sleep(ScraperSettings.threading_delay)
    except:
        continue
