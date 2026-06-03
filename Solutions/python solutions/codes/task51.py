import hashlib

class URLShortener:
    def __init__(self):
        self.url_map = {}

    def shorten(self, original_url):
        url_hash = hashlib.md5(original_url.encode()).hexdigest()[:6]
        self.url_map[url_hash] = original_url
        return f"http://short.ly/{url_hash}"

    def lookup(self, short_url):
        url_hash = short_url.split("/")[-1]
        return self.url_map.get(url_hash, "URL not found")

shortener = URLShortener()
short_url = shortener.shorten("https://www.google.com")
print(f"Shortened: {short_url}")
original = shortener.lookup(short_url)
print(f"Original: {original}")
