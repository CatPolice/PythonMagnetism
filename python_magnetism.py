# coding=utf-8
import urllib.request
from urllib.request import urlopen
import chardet
from bs4 import BeautifulSoup

# ==================================================================
# ==================================================================
# ==================================================================

def _getData():
    urlHead = "http://www.zhongziso.com"
    url_list = []
    keyword = "搜索关键词"  # 搜索关键词
    keyword = urllib.request.quote(keyword)  # 编码
    url = "http://www.zhongziso.com/list/" + keyword + "/1"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/51.0.2704.63 Safari/537.36'}
    req = urllib.request.Request(url=url, headers=headers)
    try:
        #     data = opener.open(url,timeout=10).read().decode("utf-8")
        res = urllib.request.urlopen(req)
        data = res.read()
        bs4 = BeautifulSoup(data)
        span_class = bs4.find_all('table',{'class':'table table-bordered table-striped'})
        for at in span_class:
            # print(at.a.get('href'))
            url_list.append(urlHead+at.a.get('href'))
    # print(bs4)
    except Exception as er:
        print("异常概要：")
        print(er)

    return url_list

def _getHtml(url = ""):
    magnet = ""
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/51.0.2704.63 Safari/537.36'}
    req = urllib.request.Request(url=url, headers=headers)
    try:
        #     data = opener.open(url,timeout=10).read().decode("utf-8")
        res = urllib.request.urlopen(req)
        data = res.read()
        bs4 = BeautifulSoup(data)
        span_class = bs4.find_all('textarea', {'class': 'magnetlink form-control'})
        for at in span_class:
            magnet = at.text
            magnet_replace = magnet.replace('\r\n','')
            print(magnet)
    # print(bs4)
    except Exception as er:
        print("异常概要：")
        print(er)

    return magnet_replace


if __name__ == "__main__":
    magnet_list = []
    url_list = _getData()
    print('==========begin============')
    for url in  url_list:
        magnet = _getHtml(url)
        # print(magnet)
        magnet_list.append(magnet)

    print(magnet_list)
    print("===========end============")

