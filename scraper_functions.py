""" 
© 2024 Bloodhaven Studios. All rights reserved.
This code is part of https://github.com/BloodhavenStudios/Tiktok-Video-Scraper.

Licensed under the MIT License. See LICENSE file in the project root for full license information.

Main Module for Scraper.
"""
import os
import logging
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
from colorama import Fore
from data import ScraperSettings, return_data

logging.basicConfig(
    filename="output.log",
    filemode="w",
    level=logging.DEBUG,
    format='[%(levelname)s] %(message)s'
)

__all__ = [
    "download_video"
]

def save_video_as_mp4(response: requests.Response, id: int) -> None:
    """ Saves the downloaded video as a .mp4

    Args:
        response (str): requests.Response object
        link (str): string
        id (int): int
    """
    download_soup = BeautifulSoup(response.text, "html.parser")

    download_link = download_soup.a["href"]
    video_title = download_soup.p.getText().strip()

    mp4_file = urlopen(download_link)
    with open(f"{ScraperSettings.download_files_to}{id}-{video_title}.mp4", "wb") as output:
        while(True):
            data = mp4_file.read(4096)
            if data:    
                output.write(data)
            else:
                print("\r", end="")
                print(f"Video download: {id} " + Fore.GREEN + "[Success]" + Fore.RESET)
                break

def download_video(link: str, id: int) -> None:
    """ Downloads a video

    Args:
        link (str): string
        id (int): int
    """
    cookies, headers, params = return_data()

    data = {"id": link, "locale": "en", "tt": "WlRVNk1j"}

    response = requests.post("https://ssstik.io/abc", data=data, params=params, headers=headers, cookies=cookies)

    if "not a valid TikTok link." in response.text:
        logging.error(f"Video: {id} - POST request failure to get download link.")

    try:
        save_video_as_mp4(response, id)
    except FileNotFoundError:
        os.mkdir("videos/")
        ScraperSettings.download_files_to = "videos/"
        save_video_as_mp4(response, id)
    except Exception as e:
        print(e)
        print("\r", end="")
        print(f"Video download: {id} " + Fore.RED + "[Failed]" + Fore.RESET + " (Try increasing ScraperSettings.threading_delay)")
        logging.error(f"Failed to download video: {id}")
