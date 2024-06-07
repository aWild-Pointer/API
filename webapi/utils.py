import base64
import io
import random
import string
import qrcode


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


def generate_random_username(length=8):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))