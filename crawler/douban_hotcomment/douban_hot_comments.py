import requests
from bs4 import BeautifulSoup
import re
import random
import time

def open_url(url):
    pro = ['223.241.79.99:8888', '220.175.144.181:8888', '223.215.6.201:8088', '60.167.119.114:8888', '49.68.210.180:8888', '222.189.191.145:9999', '220.175.144.92:8888']

    headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
    res = requests.get(url, headers=headers, proxies={"http": random.choice(pro)}, timeout=5)
    return res

def find_result(res):
    soup = BeautifulSoup(res.text, 'html.parser')

    #viewers
    viewers = []
    v_target = soup.find_all('span', class_='comment-info')
    for each in v_target:
        #print(each.contents[1].text)
        viewers.append(each.contents[1].text + ': ')

    #comments
    comments = []
    c_target = soup.find_all('span', class_='short')
    for each in c_target:
        #print(each.contents)
        comments.append(each.text)

    #print(comments)
    #print(viewers)

    result = []
    length = len(viewers)
    for i in range(length):
        result.append(viewers[i] + comments[i] + '\n\n')

    return result

def get_next(url):
    res = open_url(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    print(soup)
    if soup.find('a', class_='next'):
        return 1
    else:
        return 0

def main():
    #open website
    target_url = "https://movie.douban.com/subject/1292052/comments?start={}&limit=20&status=P&sort=new_score"
    page_start = 0

    #go through each page
    result = []
    while True:
        start_num = page_start * 20
        url = target_url.format(start_num)
        is_next = get_next(url)
        print(is_next)
        if not is_next:
            break
        else:
            res = open_url(url)
            #print(res.text)
            result.extend(find_result(res))
        page_start += 1

    #save to douban_HC.txt
    with open("douban_HC.txt", 'w', encoding='utf-8') as f:
        for each in result:
            f.write(each)
            

if __name__ == '__main__':
    main()
