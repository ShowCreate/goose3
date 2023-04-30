from goose3 import Goose
from goose3.text import StopWordsKorean

url='http://news.donga.com/3/all/20131023/58406128/1'

g = Goose({'stopwords_class':StopWordsKorean})

article = g.extract(url=url)

print(article.cleaned_text[:150])