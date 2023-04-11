from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')            #网页1
#获取网页内容
bs = BeautifulSoup(html.read(), 'html.parser')     #获取网页内容
print(bs)
print('-'*200)

#提取只包含在 <span class="green"></span> 标签里的文字
nameList = bs.findAll('span', {'class':'green'})
for name in nameList:
    print(name.get_text())
print('-'*200)

#提取只包含在 <span class="red"></span> 标签里的文字
talkList = bs.findAll('span', {'class': 'red'})
for talk in talkList:
    print(talk.get_text())
print('-'*200)

#返回一个包含 HTML 文档中所有标题标签的列表：
hList=bs.findAll(['h1','h2','h3','h4','h5','h6',])
print(hList)
print('-'*200)

#找出子标签:父标签的下一级
html2 = urlopen('http://www.pythonscraping.com/pages/page3.html')      #网页2
bs = BeautifulSoup(html2, 'html.parser')
for child in bs.find('table',{'id':'giftList'}).children:
    print(child)            #tr 标签是 table 标签的子标签
print('-'*200)

#找出兄弟标签
for sibling in bs.find('table', {'id': 'giftList'}).tr.next_siblings:
    print(sibling)
print('-'*200)

#处理父标签
#选择图片标签的父标签(td)——td 标签的前一个兄弟标签 previous_sibling（包含美元价格的父标签）
print("该商品的价格是:")
print(bs.find('img',{'src':'../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())
