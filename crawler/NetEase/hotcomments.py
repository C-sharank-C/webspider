import requests
import json

def get_res(url):
    headers = {'User-agent': 'Mozilla/5.0'}
    params = 'K9KG7jK/+V/9DRJgcYkDitNwTZYwfTzYxo9oN8Y+5NG7OCwF4ELmE/uSsSbYM2kh0oKVFBbXn6Z/TtkSLNyZMCRBDWgeVN0ZHppmG82nTwn3au8QZG0DkBW8ETsAlLbxgqLTWmPJN3cm009lGHnScQZaZSZvgCS3RO2q/eP1gIXwZxY/zvwYWBpn+HO758/kqMSBCjM9lyE6bvOi2c76b4fDOAd1r8baiMschpzSw7Zdc452+6HagFjD0JvgE0JuaP/oIi6uF1izf0Pm6dtYLQ=='
    encSecKey = 'a5a841b14c585230fc3fa4592bdb6c828f0c24faf3599ee24f2a3ec0ba194abe44082f69ca27402ed49d1da2b03ab2887170a51bacf26512fe8c74f623d5d0ea7480be34a4c3e5f418b750d438c1539fb59dc5572088e2a1074ad624d51b1ddb5a42c54c48ad4a881ee2d3b3ebe011bce3c086dc5538f5a6fc2a1306e14cccc2'
    data = {
            'params': params,
            'encSecKey': encSecKey
            }

    name_id = url.split('=')[1]
    target_url = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_{}?csrf_token='.format(name_id)
    
    res = requests.post(target_url, headers=headers, data=data)

    return res

def main():
    url = 'https://music.163.com/#/song?id=4875626'
    res = get_res(url)
    print(res.text)

    data = json.loads(res.text)

    
    with open('hotcomments.txt', 'w', encoding='utf-8') as file:
        for each_comment in data['hotComments']:
            file.write(each_comment['user']['nickname'])
            file.write(': ')
            file.write(each_comment['content'])
            file.write('\n')
            file.write('-------------------------------------')
            file.write('\n')
            

if __name__ == '__main__':
    main()
