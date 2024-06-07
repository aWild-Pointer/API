import base64
import io
import requests
from PIL import Image
from pyzbar.pyzbar import decode

# url = 'http://localhost:5000/api/generate_qr'
url = 'http://106.14.13.36:5000/api/generate_qr'
data = {'data': 'test-Linux'}
response = requests.post(url, json=data)
response_data = response.json()

# 从响应中获取Base64编码字符串
base64_string = response_data['qr_image']

def save_image_from_base64(base64_string, filename):
    # 将Base64字符串解码为二进制数据
    image_data = base64.b64decode(base64_string)

    # 将二进制数据读入PIL的Image对象
    image = Image.open(io.BytesIO(image_data))

    # 保存图片到文件
    image.save(filename)

# 保存图像到文件
filename = "decoded_image.png"  # 图片保存的文件名
save_image_from_base64(base64_string, filename)
img = Image.open("decoded_image.png")
qr_data = decode(img)
print(qr_data)



