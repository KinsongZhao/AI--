import pymysql


def open():
    """
    建立数据库连接
    :return: 数据数据
    """
    db = pymysql.connect(host="127.0.0.1", user="root", password="Zxy20041226", database="test", charset="utf8")
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
    cursor.execute(sql, values)# 执行sql数据修改语句
    db.commit() # 提交数据
    cursor.close() # 关闭游标
    db.close() # 关闭数据库连接
    return cursor.rowcount





if __name__ == "__main__":
    try:
        sql = "insert into user (username,email) values (%s,%s)"
        val = ("小米", "4185156@163.com")
        r = query(sql,val)
        print(r)
    except:
        print("数据操作错误！")

    # try:
    #     sql = "insert into user_info (userName,userPwd) values (%s,%s)"
    #     val = ("bob", "bob")
    #     print(insert(sql,val),"条数据添加成功")
    # except:
    #     print("数据操作错误！")


    # try:
    #     sql1 = "insert into user_info (userName,userPwd) values (%s,%s)"
    #     val = [("bob", "bob"),("tom", "tom")]
    #     print(insert_p(sql,val),"条数据添加成功")
    # except:
    #     print("数据操作错误！")

    # try:
    #     sql_update = "update user_info set userName = %s where userPwd=%s"
    #     val = ('test', '123456')
    #     print(update(sql_update, val), "条数据被修改！")
    # except:
    #     print("数据读取错误！")
