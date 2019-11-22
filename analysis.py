# -*- coding: utf-8 -*-

from PIL import Image
from pyzbar import pyzbar


def get_ewm(img_adds):
    img = Image.open(img_adds)

    txt_list = pyzbar.decode(img)

    for txt in txt_list:
        #barcodeData = txt.data.decode('utf-8')
        a=txt.data
        str_from_utf_8 = a.decode(encoding="utf-8")
        print(str_from_utf_8)
        #print(barcodeData)
        #print(type(txt.data))

if __name__ == '__main__':
    # 解析本地二维码
    name=(input("请输入查找的联系人："))
    get_ewm('E:\\imge\\%s.png'%name)

    # 解析网络二维码
    # get_ewm('https://gqrcode.alicdn.com/img?type=cs&shop_id=445653319&seller_id=3035998964&w=140&h=140&el=q&v=1')
