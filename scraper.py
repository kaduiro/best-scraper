import requests # type: ignore

from bs4 import BeautifulSoup # type: ignore


TARGET_URL = "https://shikaku-mafia.com/" # スクレイピングしたいURLをここに書く

html = requests.get(TARGET_URL)  # HTMLを取ってくる
soup = BeautifulSoup(html.content, "html.parser")  # HTMLを解析する
title = soup.find("title")  # データを抽出する
print(title)