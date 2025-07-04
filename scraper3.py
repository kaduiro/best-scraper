import os
import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore
from urllib.parse import urljoin

# 対象のWebページ
TARGET_URL = "https://momon-ga.com/fanzine/mo3232571/"  # 任意の画像を含むページに変更する

# 保存先ディレクトリ
SAVE_DIR = "D:\steganography\manga\玉子房"
os.makedirs(SAVE_DIR, exist_ok=True)

# HTML取得
response = requests.get(TARGET_URL)
soup = BeautifulSoup(response.content, "html.parser")

# 画像タグをすべて取得
img_tags = soup.find_all("img")

# 画像URLごとに処理
for i, img in enumerate(img_tags, start=1):
    img_url = img.get("src")
    if not img_url:
        continue  # src属性がない場合はスキップ

    # 相対URLを絶対URLに変換
    img_url = urljoin(TARGET_URL, img_url)

    # 画像データ取得
    try:
        img_data = requests.get(img_url).content
        filename = os.path.join(SAVE_DIR, f"image_{i}.jpg")

        # 書き込み
        with open(filename, "wb") as f:
            f.write(img_data)
        print(f"Saved: {filename}")
    except Exception as e:
        print(f"Failed to save {img_url}: {e}")
