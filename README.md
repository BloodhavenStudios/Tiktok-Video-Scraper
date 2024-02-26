# Tiktok-Video-Scraper
A simple scraper using selenium and bs4 to download tiktok videos without the watermark!

This is the updated code that follows the tutorial [here](https://www.youtube.com/watch?v=UsT11sOD1JA)
# Use this to get headers, cookies, etc

Common errors / issues:
1. Crashes after opening
- Increase wait time in (ScraperSettings.wait_before_login) to allow things to load (slow network)
2. Doesn't scroll all the way to the bottom of the page
- Increase (ScraperSettings.scroll_speed) or you changed the web browser resoulution (minimizing/ maximizing).
3. If you get an error for downloading the video
- Make sure to check your cookies / headers or increase (ScraperSettings.threading_delay)

If you get stuck and need help, make sure to join the [CodeWithVincent Discord](https://discord.gg/codewithvincent-920882891024629790), and drop your question in the questions channel pinging matthewyt.
