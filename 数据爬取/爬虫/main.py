import requests
from bs4 import BeautifulSoup

url = https://www.dianping.com/haikou/ch10
def scrape_tripadvisor_reviews(url):
    # 发送HTTP请求获取页面内容
    response = requests.get(url)

    # 检查请求是否成功
    if response.status_code == 200:
        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # 找到评论所在的HTML元素
        review_elements = soup.find_all('div', class_='review-container')

        # 提取评论文本并打印
        for review_element in review_elements:
            review_text = review_element.find('q',
                                              class_='location-review-review-list-parts-ExpandableReview__reviewText--gOmRC').text.strip()
            print(review_text)
    else:
        print("Failed to retrieve the page. Status code:", response.status_code)


# 指定要爬取的景点评论页面URL
url = 'https://www.tripadvisor.com/Attraction_Review-g60713-d108506-Reviews-Golden_Gate_Bridge-San_Francisco_California.html'

# 调用爬取函数
scrape_tripadvisor_reviews(url)
