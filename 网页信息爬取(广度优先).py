#广度优先
from urllib. request import urlopen
from urllib. parse import quote
from bs4 import BeautifulSoup
import re, time

#全局取消证书验证
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

domain='https://baike.baidu.com'
start='/item/林徽因/236792'

start = quote(start, safe=";/?:@&=+$,", encoding="utf-8")        #转码("林徽因"中文  需转码 )    #设定安全字符，让冒号不转码
PersonList=[['林徽因',start]]
print(PersonList)
print('-' * 100)

index=0
while index<len(PersonList) and index<2:     #限定爬取的上限人数
    print('访问 '+PersonList[index][0])       #PersonList[index][0]为人名
    str=PersonList[index][1]                 #取url
    print(str)
    print('-'*100)
    url = domain + str       #合并为完整网址
    print(url)
    print('-' * 100)
    html = urlopen(url)          #网页下载器   构造 HTTP 请求
    #print(html.read()
    bs = BeautifulSoup(html, 'html.parser')                                #网页解析器      获取网页内容
    result = bs.find_all("a", {'href': re.compile('/item/.*/\d+$')})       #a标签  找出符合正则表达式的信息
    for r in result:
        subspan = r.find('span', {'class': 'title'})         #找出<span class=”title“></span>标签  （人名）
        # 对林徽因页面的解析
        if subspan is not None:
            print('发现' + subspan.get_text().strip())       #.strip()为移除字符串头尾指定的字符（默认为空格或换行符）
            sign = True                             #发现
            for p in PersonList:
                if r.attrs['href'] == p[1]:       #p[1]为 url
                    sign = False                  #不发现
            if sign == True:
                PersonList.append([subspan.get_text().strip(), r.attrs['href']])
                print('加入', subspan.get_text().strip() + r.attrs['href'])
    index += 1                #下一层
    time.sleep(1)            #sleep() 函数推迟调用线程的运行   此处为推迟1秒执行
    print('-' * 100)

print(PersonList)
