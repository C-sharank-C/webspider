import requests
from bs4 import BeautifulSoup
import re
import json
import openpyxl

def save2excel(data):
    wb = openpyxl.Workbook()
    wb.guess_types = True
    ws = wb.active

    ws.column_dimensions['B'].width = 15
    ws.column_dimensions['C'].width = 15
    ws.column_dimensions['D'].width = 10
    
    ws.append(['城市', '平均房价', '平均工资', '房价工资比'])
    for each in data:
        ws.append(each)
    
    wb.save('2017年中国主要城市房价工资比排行榜.xlsx')

def find_data(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    target = soup.find_all('p', style="TEXT-INDENT: 2em")
    print(target)
    target = iter(target)
    #print(target)

    data = []
    with open('test.txt', 'w', encoding='utf-8') as file:
        for each in target:
            if each.text.isnumeric():
                data.append([
                        re.search(r'\[(.+)\]', next(target).text).group(1),
                        re.search(r'\d.*', next(target).text).group(),
                        re.search(r'\d.*', next(target).text).group(),
                        re.search(r'\d.*', next(target).text).group()
                    ])

    return data
    

def get_hosprisalrate(url):
    headers = {"User-agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)

    return res

def main():
    url = 'https://news.house.qq.com/a/20170702/003985.htm'
    #get_hosprisalrate(url)

    res = get_hosprisalrate(url)

    data = find_data(res)
    
    #save2excel(data)

if __name__ == "__main__":
    main()

