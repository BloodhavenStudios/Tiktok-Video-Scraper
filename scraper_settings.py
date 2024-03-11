from dataclasses import dataclass

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
