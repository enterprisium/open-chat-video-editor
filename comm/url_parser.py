from bs4 import BeautifulSoup
import requests
import json

def get_paragraph_texts(url: str):
    html: str = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    pes = soup.findAll('p')
    texts: list[str] = [e.get_text() for e in pes]
    return texts