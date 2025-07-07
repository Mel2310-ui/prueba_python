import pandas as pd

import feedparser
print("Feedpaser is installed")
# Opcional: Probar a parsear un feed de ejemplo
try:
    feed = feedparser.parse('http://www.nasa.gov/rss/dyn/breaking_news.rss')
    print(f"Título del feed: {feed.feed.title}")
    if feed.entries:
        print(f"Primer artículo: {feed.entries[0].title}")
except Exception as e:
    print(f"Error al intentar parsear el feed: {e}")

# ---------------------
# ETAPA 1: EXTRACT
# ---------------------

import requests

response = requests.get("https://api.github.com/users/octocat")
data = response.json()
print(data['name'])
