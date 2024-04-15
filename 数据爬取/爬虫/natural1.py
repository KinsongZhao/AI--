import requests
from bs4 import BeautifulSoup
import time



def read_url(url, headers):
    # print(url)
    requests.packages.urllib3.disable_warnings()
    res = requests.get(url, headers=headers, verify=False)
    html = res.content.decode('utf-8')
    time.sleep(2)
    # print(html)
    return html


def soup_html(html_str):
    soup = BeautifulSoup(html_str, "lxml")
    div_list = soup.select("ul > li> div.txt > div.tit")
    data_list = []
    data_url = []
    for div in div_list:
        wen = div.select("a")[0].get('title')
        url = div.select("a")[0].get('href')
        data_list.append(wen)
        data_url.append(url)
    print(data_list)
    print(data_url)
    return data_list, data_url



def soup_zi_html(html_str):
    print('************')
    soup = BeautifulSoup(html_str, "lxml")
    # print(soup.prettify())
    try:
        la = soup.select("div.brief-info>span.item")
        Price = la[1].get_text()
        print(Price)
        lb = soup.select("#basic-info > div.expand-info.address > span")
        Address = lb[0].get_text()
        lb1 = soup.select("#address")
        Address += lb1[0].get_text()
        print(Address)
        lc = soup.select("#basic-info > div.other.J-other > p:nth-child(1) > span.info-name")
        Time = lc[0].get_text()
        lc1 = soup.select("#basic-info > div.other.J-other > p:nth-child(1) > span.item")
        Time += lc1[0].get_text()
        print(Time)
        return Price, Address
    except:
        Price=''
        Address=''
        return Price, Address
    # Yonghu = "用户点评： "
    # ld = soup.select("#rev_1519362798 > div > div.info.J-info-a1ll.clearfix > p")
    # node = execjs.get()
    # print(ld)
    # for mm in range(3):
    #     a = ld[mm].get_text()
    # print(ld)



# def txt_def(info_list):
#     import json
#     with open(r"Attractions.txt", "a", encoding='utf-8') as df:
#         df.write(json.dumps(info_list, ensure_ascii=False) + '\n\n\n\n')






#
if __name__ == '__main__':
    # headers = {
    #     'Cookie': 'fspop=test; _lxsdk_cuid=18c77b5980ac8-0ba92e63ba3413-26001951-144000-18c77b5980ac8; _lxsdk=18c77b5980ac8-0ba92e63ba3413-26001951-144000-18c77b5980ac8; _hc.v=f1f0f111-6592-fe12-95bc-785e6d2c40aa.1702815439; WEBDFPID=81x4z3xu558350y5yu4569uv28y5091781x22y4x9uy979586uxzu455-2018175449745-1702815449745OYSKMQIfd79fef3d01d5e9aadc18ccd4d0c95074025; ua=Smile%E7%88%B1%E4%B9%B0%E6%97%BA%E4%BB%94%E7%89%88; ctu=51f4e619c348e432e2d4c483d61ee2552977534289a9707ff1de01ffe10b1d86; cy=23; cye=haikou; s_ViewType=10; _lx_utm=utm_source%3Dgoogle%26utm_medium%3Dorganic; qruuid=b058bdb4-219a-4c56-8109-21d5bd38ce64; dplet=c851e12691084081f1d9bda38995d600; dper=54b84d7f8bff34c0c561a80fee41ac182c056719f47aba452e6051d2fd7dcff6f86a7ae874c6f1384efb92e3f873e196c7c3bed2a5a8c92ad284a7a2ebe976cf; ll=7fd06e815b796be3df069dec7836c3df; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1702815443,1702969189,1703123523,1703253061; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1703253071; _lxsdk_s=18c91cadffa-1e4-728-44d%7C%7C45',
    #     'Host': 'www.dianping.com',
    #     'Referer': 'https://account.dianping.com/',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    # }
    headers = {
        'Cookie': '_lxsdk_cuid=18c82021149c8-0240fa2c885894-4c657b58-1fa400-18c82021149c8; _lxsdk=18c82021149c8-0240fa2c885894-4c657b58-1fa400-18c82021149c8; _hc.v=9cb82820-0c75-830f-2116-edcc971ecb30.1702988223; WEBDFPID=7601303uwzy05w761u7vy7uyx1wvwyw681x179782w697958uz5ww8vx-2018348225069-1702988222124SKAEOYUfd79fef3d01d5e9aadc18ccd4d0c95073796; fspop=test; s_ViewType=10; qruuid=9e138a3e-c24e-407a-be13-d2457088a065; dper=7889ad538b3ba4548e75e058199f8927359dfb18123b308ae5003f061d1692858658c4823c1f89e4c6b2ae49dc730bc8dfa8cf3bf0f8a4ce93bdc0b1fe6d7383; ll=7fd06e815b796be3df069dec7836c3df; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1702988532,1703248547; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1703248561; _lxsdk_s=18c9185241c-efa-c4d-892%7C%7C48',
        'Host': 'www.dianping.com',
        'Referer': 'https://account.dianping.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
    }
    n = int(input("你要爬取多少页"))
    for i in range(1, n + 1):
        if i == 1:
            html_str = read_url('https://www.dianping.com/haikou/ch10',
                                headers=headers)
        else:
            html_str = read_url('https://www.dianping.com/haikou/ch10/p%d' % i,
                                headers=headers)
        # print("开始读取第" + str(
        #     i) + "主页面。。。。-------------------------------------------------------------------------------------------")
        data_list, data_url = soup_html(html_str)
        print("DATA",data_url)
        # print("主页面——————解析中！！！")
        data_zi_list = []
        for m in range(len(data_list)):
            # ss = '景点：\n' + data_list[n] + '\n' + date_address[n][0] + '\n' + date_address[n][1] + '\n'
            # print(ss)
            # print("开始读取字面。。。。。")
            zi_url = data_url[m]
            print(zi_url)
            html_zi_str = read_url(zi_url, headers=headers)
            # print(data_list[m])
            laa, lbb = soup_zi_html(html_zi_str)
            # print("子页面——————解析中！！！")

        # print("数据入库------------------。")
        # for info_ls in data_zi_list:
        #     txt_def(info_ls)
