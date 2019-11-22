#!-*- coding:utf-8 -*-
import sys

import Image
import qrcode
import request
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QPushButton, QTextEdit, QLabel, QDesktopWidget


class QRCode(QWidget):
    "二维码生成器"
    def __init__(self):
        super(QRCode, self).__init__()
        self.initUI()

    # UI界面
    def initUI(self):
        self.setWindowTitle("二维码生成器") # 窗口名称设置
        self.setWindowIcon(QIcon('TUBIAO.jpg')) # 窗口图标
        self.setFixedSize(700,900)  # 窗口大小定义
        self.show_qrcode=QLabel(self)  # 定义二维码产生窗口
        self.show_qrcode.setGeometry(20, 20, 600, 600)  # 设置窗口大小位置
        self.show_qrcode.setStyleSheet("background-color:while")  # 设置窗口背景颜色
        self.input_msg=QTextEdit(self) # 创建一个文本框
        self.input_msg.setPlaceholderText("请输你的个人信息:")  # 设置文本框浮动文字
        self.input_msg.setGeometry(100, 650, 400, 100)  # 设置文本框大小位置
        self.setMouseTracking(True)  # 鼠标设置
        self.name=QLabel("姓名:", self)  # 创建姓名提示框
        self.name.setGeometry(60, 610, 400, 100)  # 设置大小位置
        self.setStyleSheet("QLabel{color:rgb(0,0,0,255);font-size:18px;font-weight:normal;font-family:Arial;}")   # 设置提示框格式
        self.age=QLabel("年龄:",self)
        self.age.setGeometry(60, 630, 400, 100)
        self.setStyleSheet("QLabel{color:rgb(0,0,0,255);font-size:18px;font-weight:normal;font-family:Arial;}")
        self.phone=QLabel("电话:", self)
        self.phone.setGeometry(60, 650, 400, 100)
        self.setStyleSheet("QLabel{color:rgb(0,0,0,255);font-size:18px;font-weight:normal;font-family:Arial;}")
        self.email=QLabel("邮箱:", self)
        self.email.setGeometry(60, 670, 400, 100)
        self.setStyleSheet("QLabel{color:rgb(0,0,0,255);font-size:18px;font-weight:normal;font-family:Arial;}")
        self.btn=QPushButton(self)  # 生成按钮
        self.btn.setText("生成二维码")  # 按钮文本设置
        self.btn.setGeometry(100,780,260,30)  # 设置大小位置
        self.btn.clicked.connect(self.make)   # 这只按钮响应，按下按键响应make函数
        #self.center()
        #self.btn.clicked.connect(creat.close)

    # 控制窗口显示在屏幕中心
    def center(self):

        # 获得窗口
        qr = self.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)  # 中心显示
        self.move(qr.topLeft())  #  中心移动

    def make(self):
        '''生成二维码'''
        text=self.input_msg.toPlainText().strip()  # 读取输入的文本信息，存入text
        print(text)
        list=[]
        for info in text:
            list.append(info)
            # 储存姓名，方便寻找
        print(list)
        namestr=[]
        for info in list:
            if info !="\n":
                namestr.append(info)
            else:
                break
        length1=len(namestr)
        print(length1)
        name=''
        for i in range(0, length1):
            name=name+namestr[i]
        del list[0:length1+1]
        print(name)
        print(list)

        # 储存年龄
        agestr=[]
        for info in list:
            if info !="\n":
                agestr.append(info)
            else:
                break
        length2=len(agestr)

        age=''
        for i in range(0, length2):
            age=age+agestr[i]
        del list[0:length2+1]

        # 储存电话
        phonestr=[]
        for info in list:
            if info !="\n":
                phonestr.append(info)
            else:
                break
        length3=len(phonestr)
        phone=''
        for i in range(0, length3):
            phone=phone+phonestr[i]
        del list[0:length3+1]
        print(list)

        # 储存邮箱
        emailstr=[]
        for info in list:
            if info !="\n":
                emailstr.append(info)
            else:break
        length4=len(emailstr)
        email=''
        for i in range(0, length4):
            email=email+emailstr[i]
        del list[0:length4+1]
        #  打印调试
        print(self.input_msg.toPlainText().strip())
        print(name)
        print(age)
        print(phone)
        print(email)
        name1="姓名："+name
        print(name1)
        age="年龄："+age
        print(age)
        phone="电话："+phone
        print(phone)
        email="邮件："+email
        print(email)
        text0=name1+'\n'+age+'\n'+phone+'\n'+email
        if text == "":  # 输入为空则推出函数
            QMessageBox.warning(self, '提示',
                                '输入不能为空!')
            return
        qr = qrcode.QRCode(
            version=1,                                             #  二维码属性设置，控制二维码的大小，取值范围从1到40
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,                                        #  控制二维码中每个格子的像素数，默认为 10
            border=4,                                           #  控制二维码四周留白包含的格子数，默认为4
        )  # 设置二维码属性
        qr.add_data(text0)  # 添加文本
        qr.make(fit=True)  # 生成二维码 fit参数自适应二维码大小
        img=qr.make_image()
        # 改变颜色
        img = img.convert("RGBA")  #  为32位彩色图像，它的每个像素用32个bit表示，其中24bit表示红色、绿色和蓝色三个通道，另外8bit表示alpha通道，即透明通道
        datas = img.getdata()
        newData = []
        for item in datas:
            if item[0] == 0 and item[1] == 0 and item[2] == 0:  #  默认黑色
                newData.append((8, 99, 190, 255))
            else:
                newData.append(item)
        img.putdata(newData)
        # 改变颜色结束
        '''中间带LOGO'''
        # img = img.convert("RGBA")
        # icon=Image.open("logo.JPG")
        # img_w,img_h=img.size
        # factor=4
        # size_w=int(img_w/factor)
        # size_h=int(img_h/factor)
        # icon_w,icon_h=icon.size
        # if icon_w > size_w:
        #     icon_w = size_w
        # if icon_h > size_h:
        #     icon_h = size_h
        # icon = icon.resize((icon_w, icon_h), Image.ANANIAS)
        # w = int((img_w - icon_w) / 2)
        # h = int((img_h - icon_h) / 2)
        # icon = icon.convert("RGBA")
        # img.paste(icon, (w, h), icon)
        img.save('test.png')  # 保存二维码
        img.save('E:/imge/%s.png'%name)  # 保存到指定路径
        pixmap=QPixmap('test.png')  # 加载二维码
        self.show_qrcode.setScaledContents(True)  # 适应Label大小
        self.show_qrcode.setPixmap(pixmap)  # 显示二维码


    def closeEvent(self, event):
        '''退出界面提示'''
        reply = QMessageBox.question(self, 'Message',
                                     "你确定要退出吗？", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app=QApplication(sys.argv)
    # 每一pyqt5应用程序必须创建一个应用程序对象。sys.argv参数是一个列表，从命令行输入参数。
    # QWidget部件是pyqt5所有用户界面对象的基类。他为QWidget提供默认构造函数。默认构造函数没有父类。
    ex=QRCode()
    ex.show()
    # if ex.btn.isChecked():
    #     ex.closeEvent()
    #     QApplication.processEvents() # 刷新界面.
    sys.exit(app.exec_())   # 关闭窗口