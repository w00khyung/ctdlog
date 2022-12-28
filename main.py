import feedparser, time

URL="https://v2.velog.io/rss/ctdlog"
RSS_FEED = feedparser.parse(URL)
MAX_POST=7

markdown_text = """
<h3 align="center">

![header](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=260&section=header&text=Fragment&fontAlign=75&fontAlignY=50&fontSize=80&fontColor=ffffff)

</h3>


<h3 align="center">🚀 Follow Me 🚀</h3>
<p align="center">
  <a href="https://velog.io/@ctdlog"><img src="https://img.shields.io/badge/Tech%20Blog-11B48A?style=flat-square&logo=Vimeo&logoColor=white&link=https://velog.io/@ctdlog"/></a>&nbsp
  <a href="mailto:qpflapffhs76@gmail.com"><img src="https://img.shields.io/badge/Email-44A833?style=flat-square&logo=Mail.Ru&logoColor=white&link=qpflapffhs76@gmail.com"/></a>&nbsp
</p>

<h3 align="center">📚 Tech Stack 📚</h3>
<p align="center">
  <img src="https://img.shields.io/badge/HTML-E34F26?style=flat-square&logo=HTML5&logoColor=white"/>
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=CSS3&logoColor=white"/>
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=white"/>
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white"/><br/>
  <img src="https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=node.js&logoColor=white"/>
  <img src="https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=white"/>
  <img src="https://img.shields.io/badge/Next-000000?style=flat-square&logo=next.js&logoColor=white"/>
  <img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=Git&logoColor=white"/>&nbsp
  <img src="https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=AmazonAWS&logoColor=white"/></a>&nbsp

</p>

📌 Latest Blog Posts
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

