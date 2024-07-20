""" 
© 2024 Bloodhaven Studios. All rights reserved.
This code is part of https://github.com/BloodhavenStudios/Tiktok-Video-Scraper.

Licensed under the MIT License. See LICENSE file in the project root for full license information.

Data Module for Scraper.
"""
from dataclasses import dataclass

__all__ = [
    "ScraperSettings",
    "return_data"
]

# Settings for scraper change account, speed etc here
@dataclass
class ScraperSettings:
    # Scrolling Page
    scroll_speed: float = 1.5

    # Download Settings
    account_link: str = "https://www.tiktok.com/@codewithvincent"
    download_files_to: str = "videos/"
    download_most_recent_videos_first: bool = False
    threading_delay: float = 13

    # Bypass Account Login/ Something went wrong
    wait_before_login: int = 15
    wait_before_refresh: int = 5

cookies = {
    # Please get this data from the console network activity tool
    # This is explained in the video :)
}

headers = {
    # Please get this data from the console network activity tool
    # This is explained in the video :)
}

params = {
    "url": "dl"
}

def return_data() -> tuple[dict, dict, dict]:
    """ Returns a Tuple containing dictionarys for cookies, headers, and parameters"""
    return cookies, headers, params
