import requests
from bs4 import BeautifulSoup
page = requests.get('http://www.donbest.com/nfl/injuries/')
soup = BeautifulSoup(page.text, 'html.parser')
print(len(soup))
mytable = soup.findAll("td", {"class": "otherStatistics_table_alternateRow"})
#tr = mytable.findAll("tr",{"class":"otherStatistics_table_alternateRow statistics_cellrightborder"})
("div", {"class": "_1Y3rN _308Yc"})
dataTable = mytable[0]
print(len(mytable))
for dataPiece in list(mytable):
    print('Data Piece')
    print(dataPiece).contents[0]