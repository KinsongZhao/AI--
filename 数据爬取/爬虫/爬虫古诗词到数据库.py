import requests
from bs4 import BeautifulSoup
import time
import pymysql
import pymysql
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding



def open():
    """
    建立数据库连接
    :return: 数据数据
    """
    db = pymysql.connect(host="localhost", port=3306, user="root", password="Zxy20041226",
                         database="test", charset="utf8")
    return db


def query1(sql):
    """
    不带参数查询
    :param sql:
    :return:
    """
    db = open()
    cursor = db.cursor()  # 使用cursor（）方法获取游标
    cursor.execute(sql)  # 执行sql查询语句
    result = cursor.fetchall()  # 记录查询结果
    cursor.close()  # 关闭游标
    db.close()  # 关闭数据库连接
    return result  # 返回查询结果


def query(sql, *keys):
    """
    带参数查询数据库数据
    :return:
    """
    db = open()  # 连接数据库
    cursor = db.cursor()  # 使用cursor()方法获取操作游标
    cursor.execute(sql, keys)  # 执行查询sql 语句
    result = cursor.fetchall()  # 记录查询结果
    cursor.close()  # 关闭游标
    db.close()  # 关闭数据库连接
    return result  # 返回查询结果


def insert(sql, values):
    """
    向数据库插入数据,插入的values是一个tuple
    :param sql: 运行sql插入语句
    :return: 返回插入结果
    """
    db = open()  # 打开数据库连接
    cursor = db.cursor()  # 使用cursor（）方法获取游标
    cursor.execute(sql, values)
    db.commit()
    cursor.close()
    db.close()
    return cursor.rowcount


def insert_p(sql, values):
    """
    向数据库插入数据,插入的values是一个tuple
    :param sql: 运行sql插入语句
    :return: 返回插入结果
    """
    db = open()  # 打开数据库连接
    cursor = db.cursor()  # 使用cursor（）方法获取游标
    cursor.executemany(sql, values)
    db.commit()
    cursor.close()
    db.close()
    return cursor.rowcount


def delete(sql, values):
    """
    删除数据库数据
    :param sql:
    :return:
    """
    db = open()  # 打开数据库连接
    cursor = db.cursor()  # 使用cursor()方法获取游标
    cursor.execute(sql, values)
    db.commit()  # 执行修改
    cursor.close()
    db.close()
    return cursor.rowcount


def update(sql, values):
    """
    更新数据库数据
    :param sql:
    :param values:
    :return:
    """
    db = open()  # 打开数据库连接
    cursor = db.cursor()  # 使用cursor()方法获取游标
    cursor.execute(sql, values)  # 执行sql数据修改语句
    db.commit()  # 提交数据
    cursor.close()  # 关闭游标
    db.close()  # 关闭数据库连接
    return cursor.rowcount






# 读取url内容
def read_url(url,headers):
    # 发送网页请求
    res = requests.get(url,headers=headers)
    time.sleep(0.0001)
    # res.content 获取内容
    # 对返回的内容设置编码
    html = res.content.decode('utf-8')
    return html

def soup_html(html_str):
    # pip install lxml -i https://pypi.tuna.tsinghua.edu.cn/simple
    # 解析HTML文本数据 ，lxml库更实用与HTML
    soup = BeautifulSoup(html_str,"lxml")
    #逐步定位到目标标签
    div_lsit = soup.select("div.left>div.sons>div.cont")
    data_list = []
    data_url = []
    for div in div_lsit:
        # < div
        #
        # class ="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;" >
        #
        # < a
        # href = "/mingju/juv_d898ba69839d.aspx"
        # style = " float:left;"
        # target = "_blank" > 东北看惊诸葛表，西南更草相如檄。 < / a >
        # < span
        # style = " color:#65645F; float:left; margin-left:5px; margin-right:10px;" >—— < / span > < a
        # href = "/shiwenv_6684e95c8744.aspx"
        # style = " float:left;"
        # target = "_blank" > 辛弃疾《满江红·送李正之提刑入蜀》 < / a >
        # < / div >   东北看惊诸葛表，西南更草相如檄。——辛弃疾《满江红·送李正之提刑入蜀》
        #数据清洗与标准化
        wen = div.get_text().replace("\n","")
        url = div.select("a")[0].get('href')
        url = "https://so.gushiwen.cn"+url
        data_list.append(wen)
        data_url.append(url)
    # print(data_list)
    # print(data_url)

    return data_list,data_url

def txt_def(info_list):
    import json
    with open(r"E:\课业\AIGC大语言模型\畅游\爬虫\sentence.txt", 'a', encoding='utf-8') as df:
        for one in info_list:
            df.write(json.dumps(one, ensure_ascii=False) + '\n\n')



def soup_zi_html(html_str):
    # pip install lxml
    soup = BeautifulSoup(html_str,"lxml")
    zi_wen = soup.select("div.contson")[0].get_text().replace("\n","")
    return zi_wen


# def txt_def(info_list):
#     import json
#     with open(r'D:\sentence.txt', 'a', encoding='utf-8') as df:
#         for one in info_list[1]:
#             df.write(json.dumps(one, ensure_ascii=False) + '\n\n')


if __name__ == '__main__':
    headers = {
        "Cookie": "acw_tc=7043f21d17029011203475468e778f4d0f404aab45a29099849cc92940; cdn_sec_tc=7043f21d17029011203475468e778f4d0f404aab45a29099849cc92940; login=flase; Hm_lvt_9007fab6814e892d3020a64454da5a55=1702901121; Hm_lpvt_9007fab6814e892d3020a64454da5a55=1702901121",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    n = int(input("你要爬取多少页"))
    for i in range(1,n+1):
        html_str = read_url('https://so.gushiwen.cn/mingjus/default.aspx?page=%d&tstr=&astr=&cstr=&xstr='%i,headers=headers)
        print("开始读取第"+str(i)+"主页面。。。。-------------------------------------------------------------------------------------------")
        data_list,data_url = soup_html(html_str)
        print("主页面——————解析中！！！")
        data_zi_list = []
        for zi_url in data_url:
            print("开始读取字面。。。。。")
            html_zi_str = read_url(zi_url, headers=headers)
            zi_wen = soup_zi_html(html_zi_str)
            print("子页面——————解析中！！！")
            data_zi_list.append(zi_wen)
        # print(data_list)
        # print(data_zi_list)
#       数据存储
        print("数据入库------------------。")

        data = {}
        for i in range(len(data_list)):
            data[data_list[i]] = data_zi_list[i]


        # txt_def(data)




        for i in range(len(data_list)):
            sql = "insert into train_ (content,summary) values (%s,%s)"
            va1 = data_list[i]
            va2 = data_zi_list[i]
            val = (va1, va2)
            print(insert(sql, val), f"第{i + 1}条数据添加成功")
