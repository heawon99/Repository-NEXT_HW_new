import requests
from bs4 import BeautifulSoup
import csv

file = open('notebook.csv', mode='w', newline='')
#notebook.csv라는 파일 만들고 오픈하겠다. 
writer = csv.writer(file)
writer.writerow(["상품 제품명","상품 가격명","상품 상세설명"])


# 우리가 정보를 얻고 싶어 하는 URL
NOTEBOOK_URL = f'https://search.shopping.naver.com/search/all?pagingIndex=&pagingSize=80&query=노트북'
# get 요청을 통해 해당 페이지 정보를 저장
notebook_html = requests.get(NOTEBOOK_URL)
# bs4 라이브러리를 통해 불러온 html을 우리가 원하는 형태로 파싱
notebook_soup = BeautifulSoup(notebook_html.text,"html.parser")

notebook_list_box = notebook_soup.find("ul",{"class":"list_basis"})
notebook_list=notebook_list_box.find_all("li",{"class":"basicList_item__2XT81"})

final_result =[]
for notebook_item in notebook_list:
    title= notebook_item.find("div",{"class":"basicList_title__3P9Q7"}).find("a").text
    price=notebook_item.find("div",{"class":"basicList_price_area__1UXXR"}).find("span",{"class":"price_num__2WUXn"}).text
    detail=notebook_item.find_all("a",{"class":"basicList_detail__27Krk"})

 

temp = []
for detail_item in detail:
    temp.append(detail_item.text)
print(temp)


result = {
    'title': title,
    'price': price,
    'detail': temp
}
final_result.append(result)
for result in final_result:
    row =[]
    row.append(result['title'])
    row.append(result['price'])
    row.append(result['detail'])
    writer.writerow(row)

print(final_result)

# print(len(notebook_items))
# print(type(notebook_items))

#find 매칭된 첫번째 태그만 가져오는거 
#find all 모든 태그를 가져오는거 
#notebook_list_box items 5개를 가지고 있는 부모 요소 
#notebook_items 5개 있음. 5개의 배열을 의미함. 
#string을 붙인이유는 a태그 전체가 출력이 된다.string은 
#우리가 텍스트만 출력하고 싶었기에 붙여진것 그래서 .text로 해도 괜찮음.

