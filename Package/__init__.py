from bs4 import BeautifulSoup
import requests


def data_extraction():
    content = requests.get("https://twitter.com/i/trends")
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, "html.parser")
        result = soup.find("div", {"Class": "css-901oao r-1nao33i r-1qd0xha r-a023e6 "
                                            "r-b88u0q r-rjixqe r-1bymd8e r-bcqeeo r-qvutc0"})
        print(result)
