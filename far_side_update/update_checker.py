import urllib.request
import ssl
from bs4 import BeautifulSoup

def checker():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    target_url = "https://www.thefarside.com/new-stuff"

    html = urllib.request.urlopen(target_url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    for tag in tags:
        tag_look = tag.get('href', None)
        if tag_look.startswith("https://www.thefarside.com/new-stuff"):
            print("This is the one", tag_look)
            return tag_look
