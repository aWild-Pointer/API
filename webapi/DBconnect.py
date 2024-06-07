import pymysql
import redis


class RedisCon:
    def __init__(self):
        self.conn = redis.Redis(host='106.14.13.36', port=6379, db=0, decode_responses=True, password='123456')


class MysqlCon:
    def __init__(self):
        self.conn = pymysql.connect(host='106.14.13.36', port=3306, user='root', passwd='123456', db='TicketHub')
        self.cursor = self.conn.cursor()

    def close_conn(self):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()

    def select(self, sql, param=None):
        if param is None:
            self.cursor.execute(sql)
        else:
            self.cursor.execute(sql, param)
        result = self.cursor.fetchall()
        if len(result) == 0:
            return None
        result_str = ', '.join([str(row[0]) for row in result])
        return result_str

    def select2(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        result_str = ', '.join([str(row) for row in result])
        return result_str

    def insert(self, sql, data):
        try:
            # 执行插入操作
            self.cursor.execute(sql, data)
            # 提交事务
            self.conn.commit()
            return True
        except pymysql.Error as e:
            self.conn.rollback()
            return False





mysqlcon = MysqlCon()
sql1 = 'SELECT eventname,eventinfo,eventresource FROM event '
# sql1 = 'SELECT * FROM user WHERE userphone = %s'
# sql2 = 'INSERT INTO user (userphone, username, userinfo) VALUES (%s, %s, %s)'
# sql1 = 'SELECT eventresource FROM event WHERE eventid = 5'
# sql2 = 'SELECT eventname FROM event WHERE eventid = 5'
# sql2 = 'SELECT * FROM event'
print(type(mysqlcon.select(sql1)))
# print(mysqlcon.select(sql2))
# mysqlcon.insert(sql2, ('1234567890', 'zx', '已实名'))


