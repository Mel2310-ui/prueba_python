import feedparser
url = "https://www.20minutos.es/rss/"
feed = feedparser.parse(url)
print(f"Título del feed: {feed.feed.title}\n")
for entry in feed.entries[:5]:
    print("Título:", entry.title)
    print("Publicado:", entry.published)
    print("Enlace:", entry.link)
    print("Resumen:", entry.summary)
    print("-" * 40)

palabras_clave = ["guerra", "ataques", "politica"]

print("Noticias filtradas por palabra clave:\n")

for entry in feed.entries:
    texto = (entry.title + entry.summary).lower()
    if any(palabra in texto for palabra in palabras_clave):
        print("Título:", entry.title)
        print("Publicado:", entry.published)
        print("Enlace:", entry.link)
        print("-" * 40)