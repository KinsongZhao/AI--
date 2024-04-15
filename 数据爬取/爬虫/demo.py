import requests
from bs4 import BeautifulSoup
import time
import pymysql

# 读取url内容
url = 'https://www.dianping.com/haikou/ch10'
def read_url(url,headers):
    # 发送网页请求
    res = requests.get(url,headers=headers)
    time.sleep(0.8)
    # res.content 获取内容
    # 对返回的内容设置编码
    html = res.content.decode('utf-8')
    return html

def soup_html(html_str):
    # pip install lxml -i https://pypi.tuna.tsinghua.edu.cn/simple
    # 解析HTML文本数据 ，lxml库更实用与HTML
    soup = BeautifulSoup(html_str,"lxml")
    #逐步定位到目标标签
    div_lsit = soup.select("ul>li>div.txt>div.tit>a")
    for a in div_lsit:
        try:
            a_url = a.get("href")
            name = a.select("h4")[0].get_text()
            print(a_url,name)
        except:
            print(a_url,"异常！！！")




# def txt_def(info_list):
#     import json
#     with open(r'C:\Users\Default\Desktop\sentence.txt', 'a', encoding='utf-8') as df:
#         for one in info_list[1]:
#             df.write(json.dumps(one, ensure_ascii=False) + '\n\n')



# def soup_zi_html(html_str):
#     # pip install lxml
#     soup = BeautifulSoup(html_str,"lxml")
#     zi_wen = soup.select("div.contson")[0].get_text().replace("\n","")
#     return zi_wen


#def txt_def(info_list):
#    import json
#    with open(r'C:\Users\admin\Desktop\sentence.txt', 'a', encoding='utf-7') as df:
#        for one in info_list[2]:
#            df.write(json.dumps(one, ensure_ascii=False) + '\n\n')

def open():
    """
    建立数据库连接
    :return: 数据数据
    """
    db = pymysql.connect(host="127.0.0.1", port=3306, user="KingsongZhao", password="Zxy20041226", database="travel", charset="utf8")
    return db

if __name__ == '__main__':
    headers = {
        "Cookie": "fspop=test; _lx_utm=utm_source%3Dgoogle%26utm_medium%3Dorganic; _lxsdk_cuid=18c77b5980ac8-0ba92e63ba3413-26001951-144000-18c77b5980ac8; _lxsdk=18c77b5980ac8-0ba92e63ba3413-26001951-144000-18c77b5980ac8; _hc.v=f1f0f111-6592-fe12-95bc-785e6d2c40aa.1702815439; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1702815443; WEBDFPID=81x4z3xu558350y5yu4569uv28y5091781x22y4x9uy979586uxzu455-2018175449745-1702815449745OYSKMQIfd79fef3d01d5e9aadc18ccd4d0c95074025; qruuid=e56606b6-5c8d-4a71-be76-5646a438d0a8; dplet=67c03bc6c4fba435892c88c72f878676; dper=86a62966ea5501dcb2ec3685d57cc29dd6912555f891c0910c155627e497f9e195313d55a4f88febb9f5c37714a2c8fcd5f8002fdbe314f7abd8a8548cb5b8c4; ll=7fd06e815b796be3df069dec7836c3df; ua=Smile%E7%88%B1%E4%B9%B0%E6%97%BA%E4%BB%94%E7%89%88; ctu=51f4e619c348e432e2d4c483d61ee2552977534289a9707ff1de01ffe10b1d86; cy=23; cye=haikou; s_ViewType=10; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1702818100; _lxsdk_s=18c77b5980a-007-1bf-ff1%7C%7C297",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    # n = int(input("你要爬取多少页"))
    # for i in range(1,n+1):
    #     html_str = read_url('https://www.dianping.com/haikou/ch10{}'.format(i), headers=headers)

        # html_str = read_url('https://www.dianping.com/haikou/ch10{}/'%i,headers=headers)
#         print("开始读取第"+str(i)+"主页面。。。。-------------------------------------------------------------------------------------------")
#         data_list,data_url = soup_html(html_str)
#         print("主页面——————解析中！！！")
#         data_zi_list = []
#         for zi_url in data_url:
#             print("开始读取字面。。。。。")
#             html_zi_str = read_url(zi_url, headers=headers)
#             zi_wen = soup_zi_html(html_zi_str)
#             print("子页面——————解析中！！！")
#             data_zi_list.append(zi_wen)
#         print(data_list)
#         print(data_zi_list)
# #       数据存储
#         print("数据入库------------------。")


    str_html = read_url("https://www.dianping.com/haikou/ch10",headers=headers)
    soup_html(str_html)