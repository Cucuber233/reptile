import bs4,requests
from urllib.request import quote

#把请求头伪装为谷歌浏览器
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/89.0.4389.114 Safari/537.36'}

url='https://www.xiachufang.com/explore/'

#使用get获取数据时，需要添加请求头
res   = requests.get(url, headers=headers)
bsres = bs4.BeautifulSoup(res.text, 'html.parser')

#使用find_all查找含有属性‘info pure-u’的div标签
menu = bsres.find_all('div',class_="info pure-u")

#它会生成一个列表，列表里面每个元素都是Tag对象
food_list = []
for i in menu:
    #获取菜名
    name = i.find('p', class_='name').text.strip()
    #获取地址
    url1 = 'https://www.xiachufang.com' + i.find('a').get('href')
    #获取食材
    food = i.find('p', class_='ing ellipsis').text.strip()
    #把上面三个信息打包成一个列表存入food_list
    food_list.append([name, url1, food])

food_list = []
name_list = bsres.find_all('p', class_="name")
foodlist  = bsres.find_all('p', class_="ing ellipsis")

for i in range(len(name_list)):
    food_list.append([name_list[i].text.strip() ,name_list[i].find('a').get('href'), foodlist[i].text.strip()])
    
print(food_list[0])
