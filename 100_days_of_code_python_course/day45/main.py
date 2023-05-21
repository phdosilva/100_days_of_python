from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

scores = soup.find_all(name='span', class_="score")

upvotes = [int(score.getText().split()[0]) for score in scores]

article_index = upvotes.index(max(upvotes))

articles = soup.find_all(name='span', class_="titleline")
articles_text = [article_tag.getText() for article_tag in articles]
articles_ref = [article_tag.find_next(name="a").get("href") for article_tag in articles]

print(articles_text[article_index], articles_ref[article_index], upvotes[article_index])