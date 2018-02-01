#快速生成二维码
#安装：pip install qrcode

"""import qrcode
img = qrcode.make('h')
img.save('test.png')

a=qrcode.make("http://www.baidu.com")
a.save("百度.png")
"""

import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.ERROR_CORRECT_Q,
    box_size=4,
    border=2
)
qr.add_data("https://user.qzone.qq.com/1447866357/infocenter")
qr.make(fit=True)
img=qr.make_image(fill_color="yellow",back_color="blue")
img.save("东城爵.png")
