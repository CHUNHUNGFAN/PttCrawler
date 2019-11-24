import requests,json
import urllib3
from bs4 import BeautifulSoup as bs
urllib3.disable_warnings()
rs = requests.session()
web_str = "https://www.ptt.cc/bbs/index.html"
res = rs.get(web_str,verify=False)

soup = bs(res.text,"lxml")
time = 1
for entry in soup.find_all('div',class_='b-ent'):
    title = entry.find(class_='board-name').text
    web_str2 = "https://www.ptt.cc/bbs/" + str(title) + "/search?q=%E5%8F%B0%E6%B3%A5"
    payload = {
        'from': '/bbs/'+str(title) + '/index.html',
        'yes': 'yes'
    }
    rs2 = requests.session()
    res2 = rs2.post('https://www.ptt.cc/ask/over18', verify = False,data = payload)
    res2 = rs2.get(web_str2,verify=False)
    soup2 = bs(res2.text,"lxml")
    for entry2 in soup2.find_all('div',class_='r-ent'):
        title2 = entry2.find(class_="title").text
        href = 'https://www.ptt.cc'+ entry2.find('a')['href']
        print(time,title2)
        print(href)
        time += 1
