import feedparser, time

URL="https://v2.velog.io/rss/ctdlog"
RSS_FEED = feedparser.parse(URL)
MAX_POST=5

markdown_text = """
<h3 align="center">

![header](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=260&section=header&text=&fontAlign=80&fontAlignY=50&fontSize=80&fontColor=ffffff)

</h3>

---

### 📕 Latest Blog Posts </h3> 
""" # list of blog posts will be appended here


for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"

f = open("README.md",mode="w", encoding="utf-8")
f.write(markdown_text)
f.close() 
