import base64
import io

import random
import utils
from PIL import Image
from flask import Flask, request, render_template, jsonify
from DBconnect import RedisCon, MysqlCon
from utils import QR

app = Flask(__name__)


# img = qrcode.make("2469560148468971")


@app.route('/', methods=['GET'])
def index():
    return render_template("web.html")


@app.route('/api/generate_qr', methods=['POST'])
def qrcode():
    data = request.form.get('data')
    if not data:
        return 'ERROR', 400

    qr_image = QR(data)
    return qr_image, 200


@app.route('/api/logcode', methods=['POST'])
def logcode():
    rediscon = RedisCon().conn
    phone = request.form.get("phone")
    if not phone:
        return 'ERROR', 400
    if rediscon.hexists('logCode', phone):
        return rediscon.hget('logCode', phone)
    else:
        code = '{:06d}'.format(random.randint(0, 999999))
        rediscon.hset('logCode', phone, code)
        rediscon.expire('logCode', 300)
    return code, 200


@app.route('/api/login', methods=['POST'])
def login():
    rediscon = RedisCon().conn
    mysqlcon = MysqlCon()
    phone = request.form.get("phone")
    code = request.form.get("code")
    if not phone or not code:
        mysqlcon.close_conn()
        return 'ERROR'

    stored_code = rediscon.hget('logCode', phone)
    if stored_code and stored_code == code:
        sql1 = 'SELECT username FROM user WHERE userphone = %s'
        sql2 = 'INSERT INTO user (userphone, username, userinfo) VALUES (%s, %s, %s)'
        sql3 = 'SELECT userinfo FROM user WHERE userphone = %s'
        if mysqlcon.select(sql1, phone) is None:
            username = utils.generate_random_username()
            mysqlcon.insert(sql2, (phone, username, '未实名'))
            mysqlcon.close_conn()
        username = mysqlcon.select(sql1, phone)
        userinfo = mysqlcon.select(sql3, phone)
        result = {
            'username': username,
            'userinfo': userinfo
        }
        return result, 200
    else:
        mysqlcon.close_conn()
        return 'ERROR', 400


@app.route('/api/eventinfo', methods=['POST'])
def eventinfo():
    mysqlcon = MysqlCon()
    choice = request.form.get("choice")
    sql1 = 'SELECT eventresource FROM event WHERE eventid = %s'
    sql2 = 'SELECT eventname FROM event WHERE eventid = %s'
    sql3 = 'SELECT eventinfo FROM event WHERE eventid = %s'
    result1 = mysqlcon.select(sql1,choice)
    result2 = mysqlcon.select(sql2, choice)
    result3 = mysqlcon.select(sql3, choice)
    result = {
        "eventname": result2,
        "eventresource": result1,
        "eventinfo": result3
    }
    result = f"{result2}.{result1}"
    mysqlcon.close_conn()
    return result, 200


@app.route('/api/eventdata', methods=['GET'])
def eventdata():
    mysqlcon = MysqlCon()
    sql = 'SELECT eventname,eventinfo,eventresource FROM event '
    result = mysqlcon.select2(sql)
    mysqlcon.close_conn()
    return result, 200


if __name__ == '__main__':
    # app.run(debug=True, host='106.14.13.36', port=5000)
    # ssl_cert = 'cert.pem'
    # ssl_key = 'private.key'
    # 加载SSL证书和密钥
    # context = (ssl_cert, ssl_key)

    # app.run(debug=True, ssl_context=context)
    app.run(debug=True)
