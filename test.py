from bs4 import BeautifulSoup as BS

file = open("index.html", "r", encoding="utf-8")

html = file.read()

soup = BS(html, "html.parser")

main = soup.find("div", class_="main-container")
navigations = main.find("div", class_="navigations")
titles = navigations.find_all("h1", class_="nav")
# for title in titles:
#     print(title.text)

content = main.find("div", class_="content-container")
post = content.find_all("div", class_="post")
# for p in post:
#     title = p.find("h2", class_="title")
#     print(title.text)


footer = main.find("div", class_="footer-box")
box = footer.find_all("div", class_="box")
for b in box:
    title = b.find("p", class_="title")  
    print(title.text.strip())


































