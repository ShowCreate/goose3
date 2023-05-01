from goose3 import Goose
url = 'http://edition.cnn.com/2012/02/22/world/europe/uk-occupy-london/index.html?hpt=ieu_c2'
g = Goose()
article = g.extract(url=url)
print(article.title)
print(article.meta_description)
print(article.cleaned_text[:150])