# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication,QWidget,QTextEdit,QVBoxLayout,QPushButton
import sys
from PIL import Image
from pyzbar import pyzbar


class TextEditDemo(QWidget):
    def __init__(self,parent=None):
        super(TextEditDemo, self).__init__(parent)
        self.setWindowTitle('联系人')

        # 定义窗口的初始大小
        self.resize(400,300)
        # 创建多行文本框
        self.textEdit=QTextEdit()
        #self.textEdit.setGeometry(20, 20, 60, 60)
        #self.textEdit.setStyleSheet("background-color:while")
        # 创建两个按钮
        self.btnPress1=QPushButton('显示联系人信息') # 实例化垂直布局
        # self.btnPress2=QPushButton('点击')
        layout=QVBoxLayout()
        # 相关控件添加到垂直布局中
        layout.addWidget(self.textEdit)
        layout.addWidget(self.btnPress1)
        # layout.addWidget(self.btnPress2)
        # 设置布局
        self.setLayout(layout)
        # 将按钮的点击信号与相关的槽函数进行绑定，点击即触发
        self.btnPress1.clicked.connect(self.btnPress1_clicked)
        # self.btnPress2.clicked.connect(self.get_ewm)
    def btnPress1_clicked(self):
        #以文本的形式输出到多行文本框
        name=(input("请输入查找的联系人："))
        a=self.get_ewm('E:\\imge\\%s.png'%name)
        self.textEdit.setPlainText('%s'%a)
    # def btnPress2_clicked(self):
    #     self.textEdit.setPlainText("你好啊")

    def get_ewm(self,img_adds):
        img = Image.open(img_adds)
        txt_list = pyzbar.decode(img)
        for txt in txt_list:
            # barcodeData = txt.data.decode('utf-8')
            a = txt.data
            str_from_utf_8 = a.decode(encoding="utf-8")
            #print(str_from_utf_8)
            return str_from_utf_8
if __name__ == '__main__':
    #name=(input("请输入查找的联系人："))
    #get_ewm('E:\\imge\\%s.png'%name)
    #print(a)
    app=QApplication(sys.argv)
    win=TextEditDemo()
    win.show()
    sys.exit(app.exec_())

