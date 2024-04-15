import requests
import parsel

# Common headers for requests
headers = {
    'Cookie': '_lxsdk_cuid=18c82021149c8-0240fa2c885894-4c657b58-1fa400-18c82021149c8; _lxsdk=18c82021149c8-0240fa2c885894-4c657b58-1fa400-18c82021149c8; _hc.v=9cb82820-0c75-830f-2116-edcc971ecb30.1702988223; WEBDFPID=7601303uwzy05w761u7vy7uyx1wvwyw681x179782w697958uz5ww8vx-2018348225069-1702988222124SKAEOYUfd79fef3d01d5e9aadc18ccd4d0c95073796; fspop=test; s_ViewType=10; qruuid=9e138a3e-c24e-407a-be13-d2457088a065; dper=7889ad538b3ba4548e75e058199f8927359dfb18123b308ae5003f061d1692858658c4823c1f89e4c6b2ae49dc730bc8dfa8cf3bf0f8a4ce93bdc0b1fe6d7383; ll=7fd06e815b796be3df069dec7836c3df; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1702988532,1703248547; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1703248561; _lxsdk_s=18c9185241c-efa-c4d-892%7C%7C48',
    'Host': 'www.dianping.com',
    'Referer': 'https://account.dianping.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
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

        if len(item_list) > 0:
            taste = item_list[0].split(': ')[-1]
        else:
            taste = "N/A"

        if len(item_list) > 1:
            environment = item_list[1].split(': ')[-1]
        else:
            environment = "N/A"

        if len(item_list) > 2:
            service = item_list[-1].split(': ')[-1]
        else:
            service = "N/A"

        address = selector_1.css('#address::text').get()
        tel_elements = selector_1.css('.tel ::text').getall()

        if tel_elements:
            tel = tel_elements[-1]
        else:
            tel = "N/A"  # or any default value you want to assign when the list is empty

        # Write data to the file
        with open('scraped_data.txt', 'a', encoding='utf-8') as file:
            file.write(f"店名: {title}\n评论: {count}\n人均消费: {Price}\n口味: {taste}\n环境: {environment}\n服务: {service}\n地址: {address}\n电话: {tel}\n详情页: {index}\n\n")

    print(f"Page {page_number} completed.")

print("Scraping and writing to file completed.")
