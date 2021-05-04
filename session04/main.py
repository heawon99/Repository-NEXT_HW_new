import requests
from bs4 import BeautifulSoup
from note_book import extract_info
import csv

file = open('note_book.csv', mode='w', newline='')
writer = csv.writer(file)
writer.writerow(["title","price","detail"])

final_result = []
for page in range(30):
    NOTEBOOK_URL = f'https://search.shopping.naver.com/search/all?pagingIndex={page}&pagingSize=80&query=노트북'
    notebook_html = requests.get(NOTEBOOK_URL)
    notebook_soup = BeautifulSoup(notebook_html.text,"html.parser")

    notebook_list_box = notebook_soup.find("ul", {"class" : "list_basis"})
    notebook_list = notebook_list_box.find_all('li', {"class" : "basicList_item__2XT81"})
    final_result += extract_info(notebook_list)

for result in final_result:
    row = []
    row.append(result['title'])
    row.append(result['price'])
    row.append(result['detail'])
    writer.writerow(row)
print(final_result)