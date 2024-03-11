# Local imports
from data import return_data
from scraper_settings import ScraperSettings

# Standard library imports
from urllib.request import urlopen

# Third-party library imports
import requests
from bs4 import BeautifulSoup
from colorama import Fore

def download_video(link: str, id: int) -> None:
    """
    Download the tiktok video as a mp4

    Args:
        link (str): tiktok video link
        id (int): the id of the video
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
                if data:    
                    output.write(data)
                else:
                    print("\r", end="")
                    print(f"Video download: {id} " + Fore.GREEN + "[Success]" + Fore.RESET)
                    break
    except:
        print("\r", end="")
        print(f"Video download: {id} " + Fore.RED + "[Failed]" + Fore.RESET + " (Try increasing ScraperSettings.threading_delay)")
