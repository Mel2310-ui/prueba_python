import feedparser
d = feedparser.parse('https://www.20minutos.es/')
print(d.feed.title())