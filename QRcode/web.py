import base64
import io
import qrcode
from PIL import Image
from pyzbar.pyzbar import decode
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

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
def index():
    return render_template("web.html")

@app.route('/web.html', methods=['POST'])
def getQr():
    code = request.form['verification_code']
    print(code)
    img = QR(code)
    return render_template('web.html', qr=img)

if __name__ == '__main__':
    app.run(debug=True)