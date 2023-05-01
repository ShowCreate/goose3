"""
사용방식은 간단합니다.

1. start_page, end_page를 통해 특정 페이지를 지정할 수 있습니다.
2. 키워드 입력으로 찾고 싶은 뉴스를 크롤링할 수 있습니다.
3. "python 네이버뉴스_크롤링.py"를 입력하여 실행하면 됩니다.
4. "네이버뉴스_크롤링_결과.txt"라는 이름으로 결과가 나옵니다.

주의! 조선일보 기사들은 크롤링되지 않습니다.
"""

from goose3 import Goose
from goose3.text import StopWordsKorean
import requests
from bs4 import BeautifulSoup

# 네이버 뉴스 URL
url_format = 'https://search.naver.com/search.naver?where=news&sm=tab_pge&query={query}&start={start}'

query = '마약' # 키워드 입력

start_page = 1 # 시작 
end_page = 2 # 끝
count = 0
g = Goose({'stopwords_class':StopWordsKorean})

# 파일 열기
with open('네이버뉴스_크롤링_결과.txt', 'w', encoding='utf-8') as f:
    for page in range(start_page, end_page + 1):
        url = url_format.format(query=query, start=(page - 1) * 10 + 1)
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        for link in soup.select('.news_area [title]'):
            try:
                article = {}
                article['link'] = link['href']
                article['titles'] = link.text.strip()
                article['date'] = link.find_next('span', class_='info').text
                content = g.extract(url=article['link'])
                article['text'] = content.cleaned_text[:150]
                article['authors'] = content.authors
                count = count + 1
                # 파일에 쓰기
                f.write(f"Number: {count}째 기사\n")
                f.write(f"Link: {article['link']}\n")
                f.write(f"Title: {article['titles']}\n")
                f.write(f"Date: {article['date']}\n")
                f.write(f"Text: {article['text']}\n")
                f.write(f"Authors: {article['authors']}\n")
                f.write(f"\nㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n\n")

            except:
                pass