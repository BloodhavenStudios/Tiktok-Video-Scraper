const class_name = "css-wjuodt-DivVideoFeedV2 ecyq5ls0"

let l = [];
const video_feed_div = document.getElementsByClassName(class_name)[0];
const elements = video_feed_div.querySelectorAll("#main-content-others_homepage > div > div.css-833rgq-DivShareLayoutMain.ee7zj8d4 > div.css-1qb12g8-DivThreeColumnContainer.eegew6e2 > div > div");

elements.forEach(element => {
    const descriptor = element.querySelector("div.css-vi46v1-DivDesContainer.eih2qak4 > div > a");
    const link = descriptor.getAttribute("href");
    if (link) {
        l.push(link);
    }
});

return l;
