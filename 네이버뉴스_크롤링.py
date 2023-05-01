from goose3 import Goose
from goose3.text import StopWordsKorean
import requests
from bs4 import BeautifulSoup

# 네이버 뉴스 URL
url_format = 'https://search.naver.com/search.naver?where=news&sm=tab_pge&query={query}&start={start}'

query = '마약' # 키워드 입력

start_page = 1 
end_page = 1
count = 0
g = Goose({'stopwords_class':StopWordsKorean})

# 파일 열기
with open('네이버뉴스_크롤링_결과.txt', 'w', encoding='utf-8') as f:
    for page in range(start_page, end_page + 1):
        url = url_format.format(query=query, start=(page - 1) * 10 + 1)
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        for link in soup.select('.bx .news_area [title]'):
            try:
                article = {}
                article['link'] = link['href']
                article['title'] = link.text.strip()
                article['date'] = link.find_next('span', class_='info').text
                content = g.extract(url=article['link'])
                article['text'] = content.cleaned_text
                article['authors'] = content.authors
                count = count + 1
                # 파일에 쓰기
                f.write(f"Number: {count}째 기사\n")
                f.write(f"Link: {article['link']}\n")
                f.write(f"Title: {article['title']}\n")
                f.write(f"Date: {article['date']}\n")
                f.write(f"Text: {article['text']}\n")
                f.write(f"Authors: {article['authors']}\n")
                f.write(f"\nㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n\n")

            except:
                pass