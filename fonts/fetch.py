"""Download the latin subsets of the two faces from Google Fonts (both SIL OFL). Run once."""
import os, re, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"}
URL = "https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..800&family=Reenie+Beanie&display=swap"


def get(u):
    return urllib.request.urlopen(urllib.request.Request(u, headers=UA)).read()


css = get(URL).decode()
for name, block in re.findall(r"/\*\s*([\w-]+)\s*\*/\s*@font-face\s*\{(.*?)\}", css, re.S):
    if name != "latin":
        continue
    fam = re.search(r"font-family:\s*'([^']+)'", block).group(1).replace(" ", "")
    url = re.search(r"url\(([^)]+)\)", block).group(1)
    data = get(url)
    open(os.path.join(HERE, fam + ".woff2"), "wb").write(data)
    print(fam, len(data))
