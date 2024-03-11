const class_name = "css-wjuodt-DivVideoFeedV2 ecyq5ls0";
let l = [];

try {
    const video_feed_div = document.getElementsByClassName(class_name)[0];
    const elements = video_feed_div.querySelectorAll("#main-content-others_homepage > div > div.css-833rgq-DivShareLayoutMain.ee7zj8d4 > div.css-1qb12g8-DivThreeColumnContainer.eegew6e2 > div > div");

    elements.forEach(element => {
        try {
            const descriptor = element.querySelector("div.css-vi46v1-DivDesContainer.eih2qak4 > div > a");
            const link = descriptor.getAttribute("href");
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
