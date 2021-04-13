'''
1. 数据位置   网址
2. 数据定位   照片
3. 数据匹配   标签
4. 数据下载   下载
'''

import requests
from bs4 import BeautifulSoup
import re

def open_url(url):
    headers = {"User-agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    return res

def find_result(res):
    soup = BeautifulSoup(res.text, 'html.parser')
    target = soup.find_all("img", class_="pic")

    return target
    
def save_images(res2):
    num = 0
    for each in res2:
        #print(each['data-original'].split("?")[0])
        img = requests.get(each['data-original'].split("?")[0])
        #print(img_wb)
        with open("./images/%s.jpg" % each['alt'], "wb") as f:
            f.write(img.content)    # 保存图片

# 目标网址
def main():
    main_page_url = "https://www.huya.com/g/4079"
    res = open_url(main_page_url)
    
    res2 = find_result(res)
    #print(res2)
    save_images(res2)

if __name__ == "__main__":
    main()

'''
运行成功
2021年4月12日01:27:46
keys: 获取BeautifulSoup对象的属性值，直接用字典的方式获取。
      保存图片：访问图片url，以"wb"格式写入返回内容的content
