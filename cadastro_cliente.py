# -*- coding: utf-8 -*-

import sqlite3
from bug_report import Ui_bug_report
from PyQt5 import QtCore, QtGui, QtWidgets
from qmessage import Qmessage
from login import Ui_MainWindow





class Ui_Form(object):
    def fecha(self):
        pass
    def ret_login(self):
        self.login = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.login)
        self.login.show()
        self.fecha()
    def bug_report_call(self):
        self.bug_report = QtWidgets.QWidget()
        self.ui = Ui_bug_report()
        self.ui.setupUi(self.bug_report)
        self.bug_report.show()

    def cad_cliente(self):
        cname = self.lineEdit_4.text()
        cell = self.lineEdit_7.text()
        tel = self.lineEdit_8.text()
        bairro = self.lineEdit_10.text()
        cpf = self.lineEdit_5.text()
        email = self.lineEdit_6.text()
        rua = self.lineEdit_9.text()
        cidade = self.lineEdit_11.text()



        if (cname == '' or rua == '' or cell == '' or bairro == '' or cidade == ''):


            Qmessage.warning(self)
        else:
            conn = sqlite3.connect("clientel.db")
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS clientes (
                    nome TEXT NOT NULL,
                    cell TEXT NOT NULL,
                    tel TEXT NOT NULL,
                    bairro TEXT NOT NULL,
                    cpf TEXT NOT NULL,
                    email TEXT NOT NULL,
                    rua TEXT NOT NULL,
                    cidade TEXT NOT NULL

                );
            """)
            cursor.execute("INSERT INTO clientes VALUES(?,?,?,?,?,?,?,?)", (cname, cell, tel, bairro, cpf, email, rua, cidade))
            conn.commit()
            conn.close()
            self.lineEdit_4.clear()
            self.lineEdit_7.clear()
            self.lineEdit_8.clear()
            self.lineEdit_10.clear()
            self.lineEdit_5.clear()
            self.lineEdit_11.clear()
            self.lineEdit_6.clear()
            self.lineEdit_9.clear()






            Qmessage.great(self)
            pass

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1362, 1023)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconteste/icons/Ativo 16@2x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_3.setStyleSheet("background-color: #281c35;\n"
"color:#fff;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_8 = QtWidgets.QFrame(self.frame_3)
        self.frame_8.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_3.setContentsMargins(6, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.frame_8)
        self.frame_2.setMinimumSize(QtCore.QSize(31, 30))
        self.frame_2.setMaximumSize(QtCore.QSize(31, 30))
        self.frame_2.setStyleSheet("border-image: url(:/iconteste/icons/ba812f4a-b112-4fa5-96d0-dccd574e3a86.jpg);\n"
"border-radius:15px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_3.addWidget(self.frame_2)
        self.frame_4 = QtWidgets.QFrame(self.frame_8)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Logincadastro = QtWidgets.QPushButton(self.frame_4)
        self.Logincadastro.setMinimumSize(QtCore.QSize(111, 25))
        self.Logincadastro.setMaximumSize(QtCore.QSize(110, 16777215))
        self.Logincadastro.setStyleSheet("QPushButton{\n"
"border:0px;\n"
"border-radius:12px;\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"\n"
"background-color:#403749\n"
"\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"border-style: outset;\n"
"border-width: 3px;\n"
"border-color: #30fcc2;\n"
"background-color:625f66\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/iconteste/icons/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Logincadastro.setIcon(icon1)
        self.Logincadastro.setObjectName("Logincadastro")
        self.Logincadastro.clicked.connect(self.ret_login)
        self.verticalLayout.addWidget(self.Logincadastro)
        self.horizontalLayout_3.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_8)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3.addWidget(self.frame_5)
        self.frame_10 = QtWidgets.QFrame(self.frame_8)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout.setContentsMargins(20, 0, 23, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_10)
        self.label_2.setMinimumSize(QtCore.QSize(200, 0))
        self.label_2.setMaximumSize(QtCore.QSize(200, 30))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.bugreport = QtWidgets.QPushButton(self.frame_10)
        self.bugreport.setMinimumSize(QtCore.QSize(100, 0))
        self.bugreport.setMaximumSize(QtCore.QSize(96, 25))
        self.bugreport.setStyleSheet("\n"
"\n"
"\n"
"QPushButton{\n"
"border:1px;\n"
"background-color: qlineargradient(spread:pad, x1:0.0227727, y1:0.557, x2:1, y2:0.551, stop:0.181818 rgba(116, 0, 239, 255), stop:0.903409 rgba(48, 252, 194, 255));\n"
"border-radius:10px;\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"\n"
"\n"
"border-width: 2px;\n"
"\n"
"border-color: black;\n"
"\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"border-style: outset;\n"
"border-width: 3px;\n"
"border-color: #30fcc2;\n"
"}\n"
"")
        self.bugreport.setObjectName("bugreport")
        self.bugreport.clicked.connect(self.bug_report_call)

        self.horizontalLayout.addWidget(self.bugreport)
        self.horizontalLayout_3.addWidget(self.frame_10, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_3.addWidget(self.frame_8)
        self.label_24 = QtWidgets.QLabel(self.frame_3)
        self.label_24.setMinimumSize(QtCore.QSize(0, 15))
        self.label_24.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_24.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.0227727, y1:0.557, x2:1, y2:0.551, stop:0.181818 rgba(116, 0, 239, 255), stop:0.903409 rgba(48, 252, 194, 255));")
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.verticalLayout_3.addWidget(self.label_24)
        self.verticalLayout_5.addWidget(self.frame_3)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setStyleSheet("background-color: rgb(98, 95, 102);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 200)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_22 = QtWidgets.QFrame(self.frame)
        self.frame_22.setMinimumSize(QtCore.QSize(500, 761))
        self.frame_22.setMaximumSize(QtCore.QSize(700, 600))
        self.frame_22.setStyleSheet("background-color: #f7f7f7;\n"
"border:1px;\n"
"border-radius:10px;")
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_22)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 17)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_23 = QtWidgets.QFrame(self.frame_22)
        self.frame_23.setMaximumSize(QtCore.QSize(16777215, 55))
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_23)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.frame_25 = QtWidgets.QFrame(self.frame_23)
        self.frame_25.setMaximumSize(QtCore.QSize(150, 16777215))
        self.frame_25.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_25)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_10 = QtWidgets.QLabel(self.frame_25)
        self.label_10.setMaximumSize(QtCore.QSize(110, 16777215))
        self.label_10.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_17.addWidget(self.label_10)
        self.horizontalLayout_15.addWidget(self.frame_25, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_6.addWidget(self.frame_23, 0, QtCore.Qt.AlignRight)
        self.label_11 = QtWidgets.QLabel(self.frame_22)
        self.label_11.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_6.addWidget(self.label_11)
        self.frame_7 = QtWidgets.QFrame(self.frame_22)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_9 = QtWidgets.QLabel(self.frame_7)
        self.label_9.setMinimumSize(QtCore.QSize(100, 100))
        self.label_9.setMaximumSize(QtCore.QSize(100, 100))
        self.label_9.setStyleSheet("border-image: url(:/iconteste/icons/user-g.png);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_2.addWidget(self.label_9)
        self.verticalLayout_6.addWidget(self.frame_7)
        self.frame_26 = QtWidgets.QFrame(self.frame_22)
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_26)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_11 = QtWidgets.QFrame(self.frame_26)
        self.frame_11.setMinimumSize(QtCore.QSize(650, 198))
        self.frame_11.setMaximumSize(QtCore.QSize(400, 300))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_9 = QtWidgets.QFrame(self.frame_11)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.formLayout = QtWidgets.QFormLayout(self.frame_9)
        self.formLayout.setObjectName("formLayout")
        self.frame_14 = QtWidgets.QFrame(self.frame_9)
        self.frame_14.setMinimumSize(QtCore.QSize(300, 40))
        self.frame_14.setMaximumSize(QtCore.QSize(206, 40))
        self.frame_14.setStyleSheet("border: 1px solid black;\n"
"border-radius:20px;\n"
"background-color: white;")
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_14 = QtWidgets.QLabel(self.frame_14)
        self.label_14.setMinimumSize(QtCore.QSize(40, 20))
        self.label_14.setMaximumSize(QtCore.QSize(25, 20))
        self.label_14.setStyleSheet("border:0px;")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_7.addWidget(self.label_14)
        self.line_5 = QtWidgets.QFrame(self.frame_14)
        self.line_5.setMinimumSize(QtCore.QSize(0, 40))
        self.line_5.setMaximumSize(QtCore.QSize(1, 16777215))
        self.line_5.setStyleSheet("margin-top:0px;")
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_7.addWidget(self.line_5)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_14)
        self.lineEdit_4.setMaximumSize(QtCore.QSize(130, 16777215))
        self.lineEdit_4.setStyleSheet("border: 0px;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_7.addWidget(self.lineEdit_4)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.frame_14)
        self.frame_17 = QtWidgets.QFrame(self.frame_9)
        self.frame_17.setMinimumSize(QtCore.QSize(300, 40))
        self.frame_17.setMaximumSize(QtCore.QSize(206, 40))
        self.frame_17.setStyleSheet("border: 1px solid black;\n"
"border-radius:20px;\n"
"background-color: white;")
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_17 = QtWidgets.QLabel(self.frame_17)
        self.label_17.setMinimumSize(QtCore.QSize(40, 20))
        self.label_17.setMaximumSize(QtCore.QSize(25, 20))
        self.label_17.setStyleSheet("border:0px;")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_10.addWidget(self.label_17)
        self.line_8 = QtWidgets.QFrame(self.frame_17)
        self.line_8.setMinimumSize(QtCore.QSize(0, 40))
        self.line_8.setMaximumSize(QtCore.QSize(1, 16777215))
        self.line_8.setStyleSheet("margin-top:0px;")
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.horizontalLayout_10.addWidget(self.line_8)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_17)
        self.lineEdit_7.setMaximumSize(QtCore.QSize(130, 16777215))
        self.lineEdit_7.setStyleSheet("border: 0px;")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_10.addWidget(self.lineEdit_7)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.frame_17)
        self.frame_18 = QtWidgets.QFrame(self.frame_9)
        self.frame_18.setMinimumSize(QtCore.QSize(300, 40))
        self.frame_18.setMaximumSize(QtCore.QSize(206, 40))
        self.frame_18.setStyleSheet("border: 1px solid black;\n"
"border-radius:20px;\n"
"background-color: white;")
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_18)
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_18 = QtWidgets.QLabel(self.frame_18)
        self.label_18.setMinimumSize(QtCore.QSize(40, 20))
        self.label_18.setMaximumSize(QtCore.QSize(25, 20))
        self.label_18.setStyleSheet("border:0px;")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_11.addWidget(self.label_18)
        self.line_9 = QtWidgets.QFrame(self.frame_18)
        self.line_9.setMinimumSize(QtCore.QSize(0, 40))
        self.line_9.setMaximumSize(QtCore.QSize(1, 16777215))
        self.line_9.setStyleSheet("margin-top:0px;")
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.horizontalLayout_11.addWidget(self.line_9)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame_18)
        self.lineEdit_8.setMaximumSize(QtCore.QSize(130, 16777215))
        self.lineEdit_8.setStyleSheet("border: 0px;")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_11.addWidget(self.lineEdit_8)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.frame_18)
        self.frame_20 = QtWidgets.QFrame(self.frame_9)
        self.frame_20.setMinimumSize(QtCore.QSize(300, 40))
        self.frame_20.setMaximumSize(QtCore.QSize(206, 40))
        self.frame_20.setStyleSheet("border: 1px solid black;\n"
"border-radius:20px;\n"
"background-color: white;")
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_20)
        self.horizontalLayout_13.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_20 = QtWidgets.QLabel(self.frame_20)
        self.label_20.setMinimumSize(QtCore.QSize(40, 20))
        self.label_20.setMaximumSize(QtCore.QSize(25, 20))
        self.label_20.setStyleSheet("border:0px;")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_13.addWidget(self.label_20)
        self.line_11 = QtWidgets.QFrame(self.frame_20)
        self.line_11.setMinimumSize(QtCore.QSize(0, 40))
        self.line_11.setMaximumSize(QtCore.QSize(1, 16777215))
        self.line_11.setStyleSheet("margin-top:0px;")
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.horizontalLayout_13.addWidget(self.line_11)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame_20)
        self.lineEdit_10.setMaximumSize(QtCore.QSize(130, 16777215))
        self.lineEdit_10.setStyleSheet("border: 0px;")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.horizontalLayout_13.addWidget(self.lineEdit_10)
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.frame_20)
        self.frame_15 = QtWidgets.QFrame(self.frame_9)
        self.frame_15.setMinimumSize(QtCore.QSize(300, 40))
        self.frame_15.setMaximumSize(QtCore.QSize(206, 40))
        self.frame_15.setStyleSheet("border: 1px solid black;\n"
"border-radius:20px;\n"
"background-color: white;")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_15 = QtWidgets.QLabel(self.frame_15)
        self.label_15.setMinimumSize(QtCore.QSize(40, 20))
        self.label_15.setMaximumSize(QtCore.QSize(25, 20))
        self.label_15.setStyleSheet("border:0px;")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_8.addWidget(self.label_15)
        self.line_6 = QtWidgets.QFrame(self.frame_15)
        self.line_6.setMinimumSize(QtCore.QSize(0, 40))
        self.line_6.setMaximumSize(QtCore.QSize(1, 16777215))
        self.line_6.setStyleSheet("margin-top:0px;")
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout_8.addWidget(self.line_6)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_15)
        self.lineEdit_5.setMaximumSize(QtCore.QSize(130, 16777215))
        self.lineEdit_5.setStyleSheet("border: 0px;")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_8.addWidget(self.lineEdit_5)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.frame_15)
        self.frame_16 = QtWidgets.QFrame(self.frame_9)
        self.frame_16.setMinimumSize(QtCore.QSize(300, 40))
        self.frame_16.setMaximumSize(QtCore.QSize(206, 40))
        self.frame_16.setStyleSheet("border: 1px solid black;\n"
"border-radius:20px;\n"
"background-color: white;")
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_16 = QtWidgets.QLabel(self.frame_16)
        self.label_16.setMinimumSize(QtCore.QSize(40, 20))
        self.label_16.setMaximumSize(QtCore.QSize(25, 20))
        self.label_16.setStyleSheet("border:0px;")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_9.addWidget(self.label_16)
        self.line_7 = QtWidgets.QFrame(self.frame_16)
        self.line_7.setMinimumSize(QtCore.QSize(0, 40))
        self.line_7.setMaximumSize(QtCore.QSize(1, 16777215))
        self.line_7.setStyleSheet("margin-top:0px;")
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.horizontalLayout_9.addWidget(self.line_7)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_16)
        self.lineEdit_6.setMaximumSize(QtCore.QSize(130, 16777215))
        self.lineEdit_6.setStyleSheet("border: 0px;")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_9.addWidget(self.lineEdit_6)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.frame_16)
        self.frame_19 = QtWidgets.QFrame(self.frame_9)
        self.frame_19.setMinimumSize(QtCore.QSize(300, 40))
        self.frame_19.setMaximumSize(QtCore.QSize(206, 40))
        self.frame_19.setStyleSheet("border: 1px solid black;\n"
"border-radius:20px;\n"
"background-color: white;")
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_19)
        self.horizontalLayout_12.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_19 = QtWidgets.QLabel(self.frame_19)
        self.label_19.setMinimumSize(QtCore.QSize(40, 20))
        self.label_19.setMaximumSize(QtCore.QSize(25, 20))
        self.label_19.setStyleSheet("border:0px;")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_12.addWidget(self.label_19)
        self.line_10 = QtWidgets.QFrame(self.frame_19)
        self.line_10.setMinimumSize(QtCore.QSize(0, 40))
        self.line_10.setMaximumSize(QtCore.QSize(1, 16777215))
        self.line_10.setStyleSheet("margin-top:0px;")
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.horizontalLayout_12.addWidget(self.line_10)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame_19)
        self.lineEdit_9.setMaximumSize(QtCore.QSize(130, 16777215))
        self.lineEdit_9.setStyleSheet("border: 0px;")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalLayout_12.addWidget(self.lineEdit_9)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.frame_19)
        self.frame_21 = QtWidgets.QFrame(self.frame_9)
        self.frame_21.setMinimumSize(QtCore.QSize(300, 40))
        self.frame_21.setMaximumSize(QtCore.QSize(206, 40))
        self.frame_21.setStyleSheet("border: 1px solid black;\n"
"border-radius:20px;\n"
"background-color: white;")
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_21)
        self.horizontalLayout_14.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_21 = QtWidgets.QLabel(self.frame_21)
        self.label_21.setMinimumSize(QtCore.QSize(40, 20))
        self.label_21.setMaximumSize(QtCore.QSize(25, 20))
        self.label_21.setStyleSheet("border:0px;")
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_14.addWidget(self.label_21)
        self.line_12 = QtWidgets.QFrame(self.frame_21)
        self.line_12.setMinimumSize(QtCore.QSize(0, 40))
        self.line_12.setMaximumSize(QtCore.QSize(1, 16777215))
        self.line_12.setStyleSheet("margin-top:0px;")
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.horizontalLayout_14.addWidget(self.line_12)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.frame_21)
        self.lineEdit_11.setMaximumSize(QtCore.QSize(130, 16777215))
        self.lineEdit_11.setStyleSheet("border: 0px;")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.horizontalLayout_14.addWidget(self.lineEdit_11)
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.frame_21)
        self.verticalLayout_2.addWidget(self.frame_9)
        self.gridLayout_2.addWidget(self.frame_11, 0, 0, 1, 1)
        self.verticalLayout_6.addWidget(self.frame_26)
        self.frame_30 = QtWidgets.QFrame(self.frame_22)
        self.frame_30.setMaximumSize(QtCore.QSize(16777213, 16777215))
        self.frame_30.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_30.setObjectName("frame_30")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_30)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.adduser = QtWidgets.QPushButton(self.frame_30)
        self.adduser.setMinimumSize(QtCore.QSize(175, 30))
        self.adduser.setMaximumSize(QtCore.QSize(120, 30))
        self.adduser.setStyleSheet("\n"
"\n"
"\n"
"QPushButton{\n"
"border: 1px solid black;\n"
"border-radius: 15px;\n"
"background-color: qlineargradient(spread:pad, x1:0.0227727, y1:0.557, x2:1, y2:0.551, stop:0.181818 rgba(116, 0, 239, 255), stop:0.903409 rgba(48, 252, 194, 255));\n"
"color: white;\n"
"\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"\n"
"border-width: 2px;\n"
"\n"
"border-color: black;\n"
"\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"border-style: outset;\n"
"border-width: 3px;\n"
"border-color: black;\n"
"}\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/iconteste/icons/plus-xxl.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.adduser.setIcon(icon2)
        self.adduser.setObjectName("adduser")
        self.adduser.clicked.connect(self.cad_cliente)

        self.gridLayout_4.addWidget(self.adduser, 0, 0, 1, 1)
        self.verticalLayout_6.addWidget(self.frame_30)
        self.frame_31 = QtWidgets.QFrame(self.frame_22)
        self.frame_31.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frame_31)
        self.horizontalLayout_19.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.frame_32 = QtWidgets.QFrame(self.frame_31)
        self.frame_32.setMaximumSize(QtCore.QSize(16777215, 25))
        self.frame_32.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_32.setObjectName("frame_32")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.frame_32)
        self.horizontalLayout_20.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_12 = QtWidgets.QLabel(self.frame_32)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_20.addWidget(self.label_12)
        self.horizontalLayout_19.addWidget(self.frame_32)
        self.frame_33 = QtWidgets.QFrame(self.frame_31)
        self.frame_33.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_33.setObjectName("frame_33")
        self.horizontalLayout_19.addWidget(self.frame_33)
        self.frame_34 = QtWidgets.QFrame(self.frame_31)
        self.frame_34.setMaximumSize(QtCore.QSize(150, 16777215))
        self.frame_34.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.frame_34.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_34.setObjectName("frame_34")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.frame_34)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_13 = QtWidgets.QLabel(self.frame_34)
        self.label_13.setMinimumSize(QtCore.QSize(100, 70))
        self.label_13.setMaximumSize(QtCore.QSize(110, 16777215))
        self.label_13.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_13.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"border-image: url(:/iconteste/icons/bc618214-251e-4c1c-9617-52f5a49d45b0.jpg);\n"
"border-radius:0px;")
        self.label_13.setText("")
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_21.addWidget(self.label_13)
        self.horizontalLayout_19.addWidget(self.frame_34)
        self.verticalLayout_6.addWidget(self.frame_31)
        self.horizontalLayout_4.addWidget(self.frame_22)
        self.verticalLayout_5.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cadastror Cliente"))
        self.Logincadastro.setText(_translate("Form", "Login/ Cadastro"))
        self.label_2.setText(_translate("Form", "andrade esquadrias id user #8774"))
        self.bugreport.setText(_translate("Form", "Bug Report"))
        self.label_10.setText(_translate("Form", "Andráde esquadrias"))
        self.label_11.setText(_translate("Form", "Cadastro de Clientes"))
        self.label_14.setText(_translate("Form", "Nome"))
        self.label_17.setText(_translate("Form", "Cell:"))
        self.label_18.setText(_translate("Form", "Tel:"))
        self.label_20.setText(_translate("Form", "Bairro:"))
        self.label_15.setText(_translate("Form", "CPF:"))
        self.label_16.setText(_translate("Form", "E-mail:"))
        self.label_19.setText(_translate("Form", "Rua:"))
        self.label_21.setText(_translate("Form", "Cidade:"))
        self.adduser.setText(_translate("Form", "Adicionar novo usuário"))
        self.label_12.setText(_translate("Form", "Orb powered by Evolcco Versão BETA 0.1"))

import source_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    Form.showMaximized()

    sys.exit(app.exec_())

