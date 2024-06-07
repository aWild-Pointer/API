import base64
import io
import qrcode
import redis
from PIL import Image
from pyzbar.pyzbar import decode
from flask import Flask, request, render_template, jsonify, make_response, abort

app = Flask(__name__)
redis_client = redis.StrictRedis(host='106.14.13.36', port=6379, db=0, password='123456')


# img = qrcode.make("2469560148468971")
def QR(data):
    qr = qrcode.QRCode(version=2, error_correction=qrcode.constants.ERROR_CORRECT_L
                       , box_size=20, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    # img.save("qrcode.png")

    # 将图像保存到内存中
    img_buffer = io.BytesIO()
    img.save(img_buffer, format='PNG')
    img_buffer.seek(0)

    # 将图像数据编码为Base64字符串
    base64_image = base64.b64encode(img_buffer.getvalue()).decode('utf-8')

    return base64_image
    # img = Image.open("bee46daea4676ab30a9c1c86e1e9877.jpg")
    # img = Image.open("qrcode.png")

    # qr_data = decode(img)
    # print(qr_data)


@app.route('/', methods=['GET'])
@app.route('/', methods=['GET'])
def index():
    user_ip = request.remote_addr
    user_ip_cookie = request.cookies.get('user_ip')

    # 如果Cookie存在，则返回拒绝访问的响应
    if user_ip_cookie:
        abort(503)
    else:
        # 设置用户IP对应的Cookie
        resp = make_response(render_template("web.html"))
        resp.set_cookie('user_ip', user_ip, max_age=30)
        return resp


# @app.errorhandler(403)
# def forbidden(error):
#     return "对不起，您没有权限访问。", 403


@app.route('/web.html', methods=['POST'])
def getQr():
    code = request.form['verification_code']
    print(code)
    img = QR(code)
    return render_template('web.html', qr=img)


if __name__ == '__main__':
    # app.run(debug=True, host='106.14.13.36', port=5000)
    ssl_cert = 'cert.pem'
    ssl_key = 'private.key'
    # 加载SSL证书和密钥
    context = (ssl_cert, ssl_key)

    app.run(debug=True, ssl_context=context)
