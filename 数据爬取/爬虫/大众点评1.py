import requests
import parsel

url = 'https://www.dianping.com/search/keyword/344/0_%E7%81%AB%E9%94%85/p2'
headers = {
    'Cookie': 'navCtgScroll=0; fspop=test; _lxsdk_cuid=18c77b5980ac8-0ba92e63ba3413-26001951-144000-18c77b5980ac8; _lxsdk=18c77b5980ac8-0ba92e63ba3413-26001951-144000-18c77b5980ac8; _hc.v=f1f0f111-6592-fe12-95bc-785e6d2c40aa.1702815439; WEBDFPID=81x4z3xu558350y5yu4569uv28y5091781x22y4x9uy979586uxzu455-2018175449745-1702815449745OYSKMQIfd79fef3d01d5e9aadc18ccd4d0c95074025; qruuid=e56606b6-5c8d-4a71-be76-5646a438d0a8; dplet=67c03bc6c4fba435892c88c72f878676; dper=86a62966ea5501dcb2ec3685d57cc29dd6912555f891c0910c155627e497f9e195313d55a4f88febb9f5c37714a2c8fcd5f8002fdbe314f7abd8a8548cb5b8c4; ua=Smile%E7%88%B1%E4%B9%B0%E6%97%BA%E4%BB%94%E7%89%88; ctu=51f4e619c348e432e2d4c483d61ee2552977534289a9707ff1de01ffe10b1d86; cy=23; cye=haikou; s_ViewType=10; ll=7fd06e815b796be3df069dec7836c3df; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1702815443,1702969189; _lx_utm=utm_source%3Dgoogle%26utm_medium%3Dorganic; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1702984259; _lxsdk_s=18c81c16871-f69-70e-ccd%7C%7C266',
    'Host': 'www.dianping.com',
    'Referer': 'https://www.dianping.com/haikou/ch10/p2',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}

response = requests.get(url=url, headers=headers)
selector = parsel.Selector(response.text)
href = selector.css('.shop-list ul li .pic a::attr(href)').getall()
print(href)
for index in href:
    html_data = requests.get(url=index, headers=headers).text
    selector_1 = parsel.Selector(html_data)
    title = selector_1.css('.shop-name::text').get()  # 店名
    count = selector_1.css('#reviewCount::text').get()  # 评论
    Price = selector_1.css('#avgPriceTitle::text').get()  # 人均消费
    item_list = selector_1.css('#comment_score .item::text').getall()  # 评价
    taste = item_list[0].split(': ')[-1]  # 口味评分
    environment = item_list[1].split(': ')[-1]  # 环境评分
    service = item_list[-1].split(': ')[-1]  # 服务评分
    address = selector_1.css('#address::text').get()  # 地址
    tel = selector_1.css('.tel ::text').getall()[-1]  # 电话
    dit = {
        '店名': title,
        '评论': count,
        '人均消费': Price,
        '口味': taste,
        '环境': environment,
        '服务': service,
        '地址': address,
        '电话': tel,
        '详情页': index,
    }
    print(dit)
