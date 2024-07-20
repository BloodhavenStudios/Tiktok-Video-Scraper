/*
© 2024 Bloodhaven Studios. All rights reserved.
This code is part of https://github.com/BloodhavenStudios/Tiktok-Video-Scraper.

Licensed under the MIT License. See LICENSE file in the project root for full license information.

Script to get all videos.
*/

const class_name = "css-hz5yk3-DivVideoFeedV2 ecyq5ls0";
let l = [];

try {
    const video_feed_div = document.getElementsByClassName(class_name)[0];
    const elements = video_feed_div.querySelectorAll("#main-content-others_homepage > div > div.css-833rgq-DivShareLayoutMain.ee7zj8d4 > div.css-1qb12g8-DivThreeColumnContainer.eegew6e2 > div > div > div.css-x6f6za-DivContainer-StyledDivContainerV2.eq741c50 > div > div > a");

    elements.forEach(element => {
        try {
            const link = element.getAttribute("href");
            if (link) {
                l.push(link);
            }
        } catch (error) {
            console.error("Error processing element:", error);
        }
    });
} catch (error) {
    console.error("Error retrieving video feed div:", error);
}

return l;
