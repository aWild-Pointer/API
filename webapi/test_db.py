import unittest
import redis

# 假设 RedisCon 类定义在 redis_con.py 文件中
from DBconnect import RedisCon


class TestRedisCon(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 创建 RedisCon 实例
        cls.redis_con = RedisCon()

    def test_connection(self):
        # 测试是否成功连接到 Redis 服务器
        try:
            self.redis_con.conn.ping()
            connection_successful = True
        except redis.ConnectionError:
            connection_successful = False

        self.assertTrue(connection_successful, "Unable to connect to the Redis server.")

    def test_set_and_get(self):
        # 测试 set 和 get 操作
        self.redis_con.conn.set('test_key', 'test_value')
        value = self.redis_con.conn.get('test_key')
        self.assertEqual(value, 'test_value', "The value retrieved from Redis does not match the expected value.")

    def test_delete(self):
        # 测试 delete 操作
        self.redis_con.conn.set('test_key', 'test_value')
        self.redis_con.conn.delete('test_key')
        value = self.redis_con.conn.get('test_key')
        self.assertIsNone(value, "The key should have been deleted but it still exists.")


if __name__ == '__main__':
    unittest.main()
