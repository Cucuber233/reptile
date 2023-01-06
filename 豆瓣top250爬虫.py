import requests,bs4,time

url = 'https://movie.douban.com/top250'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'}

movie_lis t = []

id = 0
for i in range(10):
    res = requests.get(url + '?start=' + str(25*i) + '&filter=', headers = headers)
    bs_res = bs4.BeautifulSoup(res.text, 'html.parser')
    data = bs_res.find_all('div', class_ = 'info')
    for j in data:
        id += 1
        try:
            movie = j.find('span', class_='title').text
            star =j .find('span', class_="rating_num").text
            recommendation = j.find('p', class_='quote').text.strip()
            movie_url = j.find('a')['href']
        except:
            pass
        
        else:
            movie_list.append([id, movie, star, recommendation, movie_url])
            
for i in movie_list:
    print(i)

