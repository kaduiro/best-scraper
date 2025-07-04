import requests
from bs4 import BeautifulSoup

# スクレイピング対象のURL
url = "https://news.ycombinator.com/"

# ページのHTMLを取得
response = requests.get(url)

# レスポンスが成功した場合のみ処理を続行
if response.status_code == 200:
    # BeautifulSoupでHTMLを解析
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # ニュース記事の見出しを取得
    headlines = soup.find_all('a', class_='storylink')
    for i, headline in enumerate(headlines, 1):
        print(f"{i}: {headline.text}")
else:
    print(f"リクエスト失敗: ステータスコード {response.status_code}")