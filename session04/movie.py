import requests
from bs4 import BeautifulSoup
notebook_html = requests.get('https://search.shopping.naver.com/search/all?pagingIndex=2&pagingSize=80&query=노트북')
notebook_soup = BeautifulSoup(notebook_html.text,"html.parser")

notebook_list_box = notebook_soup.find("ul", {"class" : "list_basis"})
notebook_list = notebook_list_box.find_all('li', {"class" : "basicList_item__2XT81"})
result = []

for notebook in notebook_list:
    title = notebook.find("div",{"class":"basicList_title__3P9Q7"}).find("a").string
    price = notebook.find("div",{"class":"basicList_price_area__1UXXR"}).find("span",{"class":"price_num__2WUXn"}).text
    notebook_info = {
        'title' : title,
        'price' : price
    }
    result.append(notebook_info)

print(result)

# notebook_list = notebook_soup.select_one('#__next > div > div.style_container__1YjHN > div.style_inner__18zZX > div.style_content_wrap__1PzEo > div.style_content__2T20F > ul > div > div:nth-child(1) > li > div > div.basicList_info_area__17Xyo > div.basicList_title__3P9Q7 > a').string
notebook_list = notebook_soup.select_one('#__next > div > div.style_container__1YjHN > div.style_inner__18zZX > div.style_content_wrap__1PzEo > div.style_content__2T20F > ul > div > div:nth-child(1) > li > div > div.basicList_info_area__17Xyo > div.basicList_title__3P9Q7 > a')





