import requests
from bs4 import BeautifulSoup


def scrape_daily_news(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            news_elements = soup.find_all(class_="ddd")

            for news in news_elements:
                print(news.get_text())
        else:
            print("Veb-sahifani olib bo‘lmadi. Status kodi:", response.status_code)
    except Exception as e:
        print("xato", e)



url = "https://tribuna.uz/"


scrape_daily_news(url)
