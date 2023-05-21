[Beatufil soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

### First steps
```python
from bs4 import BeautifulSoup

with open('website.html') as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser") # parser helps BeatifulSoup read the content
# in some websites you can get an error involving "parser"
# you might consider using the lxml.parser instead
# import lxml

# print(soup.title.name)
# print(soup.title.string)

# print(soup.prettify())

# print(soup.find_all(name="a"))
```

### Cases
```python
soup.find_all(name="a")
soup.select("li a") # a nested in li

tag = soup.find(name="input")
max_lenght = tag.get("maxlenght")
```


**Tip:** Some websites has rules to be respected in "root/robots.txt"