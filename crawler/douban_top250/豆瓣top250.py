import requests
from bs4 import BeautifulSoup
import re

def open_url(url):
    headers = {'User-agent': 'Mozilla/5.0'}
    res = requests.get(url, headers=headers)

    return res

def get_pages(res):
    soup = BeautifulSoup(res.text, 'html.parser')

    depth = soup.find('span', class_='next').previous_sibling.previous_sibling.text  #有趣的是，一个previous_sibling定位的是'\n'

    return int(depth)

def find_result(res2):
    soup = BeautifulSoup(res2.text, 'html.parser')

    #电影名
    movies = []
    m_target = soup.find_all('div', class_='hd')
    for each in m_target:
        movies.append(each.a.span.text)
        
    #评分
    rates = []
    r_target = soup.find_all('span', class_='rating_num')
    for each in r_target:
        rates.append("电影评分:" + each.text)
        
    #信息
    info = []
    i_target = soup.find_all('div', class_='bd')
    for each in i_target:
        try:
            info.append(each.p.text.split('\n')[1].strip() + each.p.text.split('\n')[2].strip())
        except:
            continue

    result = []
    length = len(movies)
    for i in range(length):
        result.append(movies[i] + rates[i] + info[i] + '\n')

    return result

def main():
    #打开网站
    url = "http://movie.douban.com/top250"
    res = open_url(url)

    #print(res.text)
    
    #获取页码数
    pages = get_pages(res)

    #print(pages)
    #遍历每页，打印结果
    result = []
    for i in range(pages):
        url2 = ''.join([url, '/?start=', str(i*25), '&filter='])    #为什么是'/?'而不是'\?'
        res2 = open_url(url2)
        #print(res2.text)
        result.extend(find_result(res2))
    #print(1)

    #print(result)
        
    #保存在文件中
    with open("豆瓣TOP250电影2.0.txt", 'w', encoding='utf-8') as f:
        #f.writelines(result)
        for each in result:
            f.write(each)
    

if __name__ == '__main__':
    main()
