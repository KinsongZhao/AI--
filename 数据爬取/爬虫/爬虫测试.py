import requests
import parsel

# Common headers for requests
headers = {
    'Cookie': 'navCtgScroll=0; fspop=test; _lxsdk_cuid=18c77b5980ac8-0ba92e63ba3413-26001951-144000-18c77b5980ac8; _lxsdk=18c77b5980ac8-0ba92e63ba3413-26001951-144000-18c77b5980ac8; _hc.v=f1f0f111-6592-fe12-95bc-785e6d2c40aa.1702815439; WEBDFPID=81x4z3xu558350y5yu4569uv28y5091781x22y4x9uy979586uxzu455-2018175449745-1702815449745OYSKMQIfd79fef3d01d5e9aadc18ccd4d0c95074025; qruuid=e56606b6-5c8d-4a71-be76-5646a438d0a8; dplet=67c03bc6c4fba435892c88c72f878676; dper=86a62966ea5501dcb2ec3685d57cc29dd6912555f891c0910c155627e497f9e195313d55a4f88febb9f5c37714a2c8fcd5f8002fdbe314f7abd8a8548cb5b8c4; ua=Smile%E7%88%B1%E4%B9%B0%E6%97%BA%E4%BB%94%E7%89%88; ctu=51f4e619c348e432e2d4c483d61ee2552977534289a9707ff1de01ffe10b1d86; cy=23; cye=haikou; s_ViewType=10; ll=7fd06e815b796be3df069dec7836c3df; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1702815443,1702969189; _lx_utm=utm_source%3Dgoogle%26utm_medium%3Dorganic; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1702984259; _lxsdk_s=18c81c16871-f69-70e-ccd%7C%7C266',
    'Host': 'www.dianping.com',
    'Referer': 'https://www.dianping.com/haikou/ch10/p2',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}

# Get user input for the maximum page number to scrape
max_page = int(input("Enter the maximum page number to scrape: "))

# Loop through pages starting from p2 up to the specified maximum page
for page_number in range(1, max_page + 1):
    url = f'https://www.dianping.com/haikou/ch10/p{page_number}'

    response = requests.get(url=url, headers=headers)
    selector = parsel.Selector(response.text)
    href = selector.css('.shop-list ul li .pic a::attr(href)').getall()

    for index in href:
        html_data = requests.get(url=index, headers=headers).text
        selector_1 = parsel.Selector(html_data)
        title = selector_1.css('.shop-name::text').get()
        count = selector_1.css('#reviewCount::text').get()
        Price = selector_1.css('#avgPriceTitle::text').get()
        item_list = selector_1.css('#comment_score .item::text').getall()
        restaurant_type = selector_1.css("div.breadcrumb>a::text")[1].get()
        business_time = selector_1.css("div.basic-info > div.other.J-other>p>span::text")[1].get()

        if len(item_list) > 0:
            taste = item_list[0].split(': ')[-1]
        else:
            taste = "N/A"

        if len(item_list) > 1:
            environment = item_list[1].split(': ')[-1]
        else:
            environment = "N/A"

        if len(item_list) > 2:
            service = item_list[2].split(': ')[-1]
        else:
            service = "N/A"

        address = selector_1.css('#address::text').get()
        tel = selector_1.css('.tel ::text').getall()[-1]

        # Write data to the file in the desired format
        with open('scraped_data.txt', 'a', encoding='utf-8') as file:
            file.write(f"在这个璀璨的城市角落，有一家名为{title}的{restaurant_type}，营业时间为:{business_time}，"
                       f"它拥有着口味: {taste}环境: {environment}服务: {service}的大众评价，人均消费为{Price}元。"
                       f"不仅口味精致，环境优雅，服务周到，更位于{address}。如果您想体验一场味觉盛宴不妨拨打电话{tel}提前咨询预订，"
                       f"节省您排队的时间，在来场美妙的味觉之旅的同时也最大限度的提高您的游玩体验！\n\n")

    print(f"Page {page_number} completed.")

print("Scraping and writing to file completed.")




# import requests
# import parsel
#
# # Common headers for requests
# headers = {
#     'Cookie': 'navCtgScroll=0; fspop=test; _lxsdk_cuid=18c77b5980ac8-0ba92e63ba3413-26001951-144000-18c77b5980ac8; _lxsdk=18c77b5980ac8-0ba92e63ba3413-26001951-144000-18c77b5980ac8; _hc.v=f1f0f111-6592-fe12-95bc-785e6d2c40aa.1702815439; WEBDFPID=81x4z3xu558350y5yu4569uv28y5091781x22y4x9uy979586uxzu455-2018175449745-1702815449745OYSKMQIfd79fef3d01d5e9aadc18ccd4d0c95074025; qruuid=e56606b6-5c8d-4a71-be76-5646a438d0a8; dplet=67c03bc6c4fba435892c88c72f878676; dper=86a62966ea5501dcb2ec3685d57cc29dd6912555f891c0910c155627e497f9e195313d55a4f88febb9f5c37714a2c8fcd5f8002fdbe314f7abd8a8548cb5b8c4; ua=Smile%E7%88%B1%E4%B9%B0%E6%97%BA%E4%BB%94%E7%89%88; ctu=51f4e619c348e432e2d4c483d61ee2552977534289a9707ff1de01ffe10b1d86; cy=23; cye=haikou; s_ViewType=10; ll=7fd06e815b796be3df069dec7836c3df; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1702815443,1702969189; _lx_utm=utm_source%3Dgoogle%26utm_medium%3Dorganic; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1702984259; _lxsdk_s=18c81c16871-f69-70e-ccd%7C%7C266',
#     'Host': 'www.dianping.com',
#     'Referer': 'https://www.dianping.com/haikou/ch10/p2',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
# }
#
# # Get user input for the maximum page number to scrape
# max_page = int(input("Enter the maximum page number to scrape: "))
#
# # Loop through pages starting from p2 up to the specified maximum page
# for page_number in range(1, max_page + 1):
#     url = f'https://www.dianping.com/haikou/ch10/p{page_number}'
#
#     response = requests.get(url=url, headers=headers)
#     selector = parsel.Selector(response.text)
#     href = selector.css('.shop-list ul li .pic a::attr(href)').getall()
#
#     for index in href:
#         html_data = requests.get(url=index, headers=headers).text
#         selector_1 = parsel.Selector(html_data)
#         title = selector_1.css('.shop-name::text').get()
#         count = selector_1.css('#reviewCount::text').get()
#         Price = selector_1.css('#avgPriceTitle::text').get()
#         item_list = selector_1.css('#comment_score .item::text').getall()
#         type = selector_1.css("div.breadcrumb>a::text")[1].get()
#         Time = selector_1.css("div.basic-info > div.other.J-other>p>span::text")[1].get()
#
#         if len(item_list) > 0:
#             taste = item_list[0].split(': ')[-1]
#         else:
#             taste = "N/A"
#
#         if len(item_list) > 1:
#             environment = item_list[1].split(': ')[-1]
#         else:
#             environment = "N/A"
#
#         if len(item_list) > 2:
#             service = item_list[-1].split(': ')[-1]
#         else:
#             service = "N/A"
#
#         if len(item_list) > 2:
#             type = item_list[-1].split(': ')[-1]
#         else:
#             type = "N/A"
#
#         if len(item_list) > 2:
#             Time = item_list[-1].split(': ')[-1]
#         else:
#             Time = "N/A"
#
#         address = selector_1.css('#address::text').get()
#         tel = selector_1.css('.tel ::text').getall()[-1]
#
#         # Write data to the file in the desired format
#         with open('scraped_data.txt', 'a', encoding='utf-8') as file:
#             file.write(f"在这个璀璨的城市角落，有一家名为{title}的{type}，营业时间为:{Time}，它拥有着口味: {taste}环境: {environment}服务: {service}的大众评价，人均消费为{Price}元。不仅口味精致，环境优雅，服务周到，更位于{address}。如果您想体验一场味觉盛宴不妨拨打电话{tel}提前咨询预订，节省您排队的时间，在来场美妙的味觉之旅的同时也最大限度的提高您的游玩体验！\n\n")
#
#     print(f"Page {page_number} completed.")
#
# print("Scraping and writing to file completed.")
#




# import requests
# import parsel
# from bs4 import BeautifulSoup
#
# # Common headers for requests
# headers = {
#     'Cookie': 'navCtgScroll=0; fspop=test; _lxsdk_cuid=18c77b5980ac8-0ba92e63ba3413-26001951-144000-18c77b5980ac8; _lxsdk=18c77b5980ac8-0ba92e63ba3413-26001951-144000-18c77b5980ac8; _hc.v=f1f0f111-6592-fe12-95bc-785e6d2c40aa.1702815439; WEBDFPID=81x4z3xu558350y5yu4569uv28y5091781x22y4x9uy979586uxzu455-2018175449745-1702815449745OYSKMQIfd79fef3d01d5e9aadc18ccd4d0c95074025; qruuid=e56606b6-5c8d-4a71-be76-5646a438d0a8; dplet=67c03bc6c4fba435892c88c72f878676; dper=86a62966ea5501dcb2ec3685d57cc29dd6912555f891c0910c155627e497f9e195313d55a4f88febb9f5c37714a2c8fcd5f8002fdbe314f7abd8a8548cb5b8c4; ua=Smile%E7%88%B1%E4%B9%B0%E6%97%BA%E4%BB%94%E7%89%88; ctu=51f4e619c348e432e2d4c483d61ee2552977534289a9707ff1de01ffe10b1d86; cy=23; cye=haikou; s_ViewType=10; ll=7fd06e815b796be3df069dec7836c3df; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1702815443,1702969189; _lx_utm=utm_source%3Dgoogle%26utm_medium%3Dorganic; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1702984259; _lxsdk_s=18c81c16871-f69-70e-ccd%7C%7C266',
#     'Host': 'www.dianping.com',
#     'Referer': 'https://www.dianping.com/haikou/ch10/p2',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
# }
#
# # Get user input for the maximum page number to scrape
# max_page = int(input("Enter the maximum page number to scrape: "))
#
# # Loop through pages starting from p2 up to the specified maximum page
# for page_number in range(1, max_page + 1):
#     url = f'https://www.dianping.com/haikou/ch10/p{page_number}'
#
#     response = requests.get(url=url, headers=headers)
#     selector = parsel.Selector(response.text)
#     href = selector.css('.shop-list ul li .pic a::attr(href)').getall()
#
#     for index in href:
#         html_data = requests.get(url=index, headers=headers).text
#         selector_1 = parsel.Selector(html_data)
#         title = selector_1.css('.shop-name::text').get()
#         count = selector_1.css('#reviewCount::text').get()
#         Price = selector_1.css('#avgPriceTitle::text').get()
#         item_list = selector_1.css('#comment_score .item::text').getall()
#         type = selector_1.css("div.breadcrumb>a::text")[1].get()
#         Time = selector_1.css("div.basic-info > div.other.J-other>p>span::text")[1].get()
#         # feeling = selector_1.css("div.content>p::text").get()
#         res = requests.get(url=index, headers=headers)
#         html = res.content.decode('utf-8')
#         soup = BeautifulSoup(html, 'lxml')
#         # ss = soup.select("div.comment>ul>li.comment-item")
#         # print(ss)
#         # try:
#         #     for i in range(3):
#         #         cc = ss[i].get_text()
#         #         print(cc)
#         # except:
#         #     print(0)
#
#
#         if len(item_list) > 0:
#             taste = item_list[0].split(': ')[-1]
#         else:
#             taste = "N/A"
#
#         if len(item_list) > 1:
#             environment = item_list[1].split(': ')[-1]
#         else:
#             environment = "N/A"
#
#         if len(item_list) > 2:
#             service = item_list[-1].split(': ')[-1]
#         else:
#             service = "N/A"
#
#         address = selector_1.css('#address::text').get()
#         # tel = selector_1.css('.tel ::text').getall()[-1]
#         tel_list = selector_1.css('.tel ::text').getall()
#         if tel_list:
#             tel = tel_list[-1]
#         else:
#             tel = "No telephone number found"
#
#         # Write data to the file
#         with open('scraped_data.txt', 'a', encoding='utf-8') as file:
#             file.write(
#                 f"类型：{type}\n店名: {title}\n营业时间：{Time}\n评论: {count}\n人均消费: {Price}\n口味: {taste}\n环境: {environment}\n服务: {service}\n地址: 海口市{address}\n电话: {tel}\n详情页: {index}\n\n")
#
#     print(f"Page {page_number} completed.")
#
# print("Scraping and writing to file completed.")
