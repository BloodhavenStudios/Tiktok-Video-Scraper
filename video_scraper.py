# Local Library import
from data import return_data

# Standard library imports
import threading
import time
from urllib.request import urlopen

# Third-party library imports
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from dataclasses import dataclass
from colorama import Fore

@dataclass
class ScraperSettings:

    # Scrolling Page
    scroll_speed: type[float] = 1.5

    # Classname of video feed div inside [script.js]

    # Download Settings
    account_link: type[str] = "https://www.tiktok.com/@codewithvincent"
    download_files_to: type[str] = "videos/"
    download_most_recent_videos_first: type[bool] = False
    threading_delay: type[float] = 13

    # Bypass Account Login/ Something went wrong
    wait_before_login: type[int] = 15
    wait_before_refresh: type[int] = 5



def download_video(link: type[str], id: type[int]) -> None:
    """
    Download the tiktok video as a mp4

    Args:
        link (type[str]): tiktok video link
        id (type[int]): the id of the video
    """
    
    cookies, headers, params = return_data()

    data = {
        "id": link,
        "locale": "en",
        "tt": "cjhDVEdl"
    }

    response = requests.post('https://ssstik.io/abc', params=params, cookies=cookies, headers=headers, data=data)
    download_soup = BeautifulSoup(response.text, "html.parser")

    try:
        download_link = download_soup.a["href"]
        video_title = download_soup.p.getText().strip()

        mp4_file = urlopen(download_link)
        with open(f"{ScraperSettings.download_files_to}{id}-{video_title}.mp4", "wb") as output:
            while(True):
                data = mp4_file.read(4096)
                if data:    output.write(data)
                else:
                    print("\r", end="")
                    print(f"Video download: {id} " + Fore.GREEN + "[Success]" + Fore.RESET)
                    break
    except:
        print("\r", end="")
        print(f"Video download: {id} " + Fore.RED + "[Failed]" + Fore.RESET + " (Try increasing ScraperSettings.threading_delay)")



# Create driver instance and options
options = Options()
options.add_argument("start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(options=options)
driver.get(ScraperSettings.account_link)



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
    driver.execute_script("window.scrollTo(0, {screen_height}*({i}*2));".format(screen_height=screen_height, i=i))  
    i += 1
    time.sleep(ScraperSettings.scroll_speed)
    scroll_height = driver.execute_script("return document.body.scrollHeight;")  
    if (screen_height) * i > scroll_height:
        break 


# Get all video links

with open("script.js", "r") as file:
    script = file.read()

urls_to_download = driver.execute_script(script)

print(f"Found: {len(urls_to_download)} videos.")

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
