# -*- coding: utf-8 -*-

import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from bug_report import Ui_bug_report
from qmessage import Qmessage

class Ui_cadastro(object):


    def bug_report_call(self):
        self.bug_report = QtWidgets.QWidget()
        self.ui = Ui_bug_report()
        self.ui.setupUi(self.bug_report)
        self.bug_report.show()


    def insertData(self):
        username = self.lineEdit_3.text()
        email = self.lineEdit.text()
        cargo = str(self.comboBox.currentText())
        senha = self.lineEdit_2.text()
        if (username == '' or email == '' or senha == ''):



            Qmessage.warning2(self)
        else:
            conn = sqlite3.connect("login.db")
            cursor = conn.cursor()
            cursor.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                            nome TEXT NOT NULL,
                            email TEXT NOT NULL,
                            cargo TEXT NOT NULL,
                            senha TEXT NOT NULL

                    );
                    
                    """)
            cursor.execute("INSERT INTO users VALUES(?,?,?,?)", (username, email, cargo, senha))
            conn.commit()
            conn.close()
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()

            Qmessage.great(self)
            pass




    def setupUi(self, cadastro):
        cadastro.setObjectName("cadastro")
        cadastro.resize(1377, 697)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconteste/icons/Ativo 16@2x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        cadastro.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(cadastro)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_3.setStyleSheet("background-color: #281c35;\n"
"color:#fff;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setContentsMargins(6, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame_6)
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
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.frame_4 = QtWidgets.QFrame(self.frame_6)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_6)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2.addWidget(self.frame_5)
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout.setContentsMargins(20, 0, 23, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_7)
        self.label_2.setMinimumSize(QtCore.QSize(200, 0))
        self.label_2.setMaximumSize(QtCore.QSize(200, 30))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.bugreport = QtWidgets.QPushButton(self.frame_7)
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
        self.horizontalLayout_2.addWidget(self.frame_7, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_3.addWidget(self.frame_6)
        self.label_24 = QtWidgets.QLabel(self.frame_3)
        self.label_24.setMinimumSize(QtCore.QSize(0, 15))
        self.label_24.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_24.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.0227727, y1:0.557, x2:1, y2:0.551, stop:0.181818 rgba(116, 0, 239, 255), stop:0.903409 rgba(48, 252, 194, 255));")
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.verticalLayout_3.addWidget(self.label_24)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_17 = QtWidgets.QFrame(self.centralwidget)
        self.frame_17.setStyleSheet("background-color: rgb(98, 95, 102);")
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_17)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setVerticalSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame_15 = QtWidgets.QFrame(self.frame_17)
        self.frame_15.setMinimumSize(QtCore.QSize(341, 446))
        self.frame_15.setMaximumSize(QtCore.QSize(700, 550))
        self.frame_15.setStyleSheet("background-color: #f7f7f7;\n"
"border:1px;\n"
"border-radius:10px;")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_5.setContentsMargins(-1, 4, -1, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_18 = QtWidgets.QFrame(self.frame_15)
        self.frame_18.setMaximumSize(QtCore.QSize(16777215, 55))
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_18)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_13 = QtWidgets.QFrame(self.frame_18)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.retotologin = QtWidgets.QPushButton(self.frame_13)
        self.retotologin.setMinimumSize(QtCore.QSize(0, 25))
        self.retotologin.setStyleSheet("\n"
"QPushButton{\n"
"border-radius: 12px;\n"
"background-color: transparent;\n"
"color: black;\n"
"\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"\n"
"border-width: 2px;\n"
"border-bottom:1px;\n"
"border-color: black;\n"
"\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"border-bottom:1px;\n"
"border:1px solid black;\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/iconteste/icons/arrow-left-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.retotologin.setIcon(icon1)
        self.retotologin.setObjectName("retotologin")
        self.horizontalLayout_9.addWidget(self.retotologin, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout_8.addWidget(self.frame_13)
        self.frame_20 = QtWidgets.QFrame(self.frame_18)
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.horizontalLayout_8.addWidget(self.frame_20)
        self.frame_19 = QtWidgets.QFrame(self.frame_18)
        self.frame_19.setMaximumSize(QtCore.QSize(150, 16777215))
        self.frame_19.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_19)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_10 = QtWidgets.QLabel(self.frame_19)
        self.label_10.setMaximumSize(QtCore.QSize(110, 16777215))
        self.label_10.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_7.addWidget(self.label_10)
        self.horizontalLayout_8.addWidget(self.frame_19)
        self.verticalLayout_5.addWidget(self.frame_18)
        self.label_8 = QtWidgets.QLabel(self.frame_15)
        self.label_8.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8)
        self.frame_16 = QtWidgets.QFrame(self.frame_15)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_16)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.frame_16)
        self.frame.setMinimumSize(QtCore.QSize(226, 198))
        self.frame.setMaximumSize(QtCore.QSize(226, 198))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_12 = QtWidgets.QFrame(self.frame)
        self.frame_12.setMinimumSize(QtCore.QSize(206, 40))
        self.frame_12.setMaximumSize(QtCore.QSize(206, 40))
        self.frame_12.setStyleSheet("border: 1px solid black;\n"
"border-radius:20px;\n"
"background-color: white;")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.frame_12)
        self.label_6.setMinimumSize(QtCore.QSize(40, 20))
        self.label_6.setMaximumSize(QtCore.QSize(25, 20))
        self.label_6.setStyleSheet("border:0px;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.line_4 = QtWidgets.QFrame(self.frame_12)
        self.line_4.setMinimumSize(QtCore.QSize(0, 40))
        self.line_4.setMaximumSize(QtCore.QSize(1, 16777215))
        self.line_4.setStyleSheet("margin-top:0px;")
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_6.addWidget(self.line_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_12)
        self.lineEdit_3.setMaximumSize(QtCore.QSize(130, 16777215))
        self.lineEdit_3.setStyleSheet("border: 0px;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_6.addWidget(self.lineEdit_3)
        self.verticalLayout_4.addWidget(self.frame_12)
        self.frame_10 = QtWidgets.QFrame(self.frame)
        self.frame_10.setMinimumSize(QtCore.QSize(206, 40))
        self.frame_10.setMaximumSize(QtCore.QSize(206, 40))
        self.frame_10.setStyleSheet("border: 1px solid black;\n"
"border-radius:20px;\n"
"background-color: white;")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.frame_10)
        self.label_4.setMinimumSize(QtCore.QSize(40, 20))
        self.label_4.setMaximumSize(QtCore.QSize(25, 20))
        self.label_4.setStyleSheet("border:0px;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.line_2 = QtWidgets.QFrame(self.frame_10)
        self.line_2.setMinimumSize(QtCore.QSize(0, 40))
        self.line_2.setMaximumSize(QtCore.QSize(1, 16777215))
        self.line_2.setStyleSheet("margin-top:0px;")
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_4.addWidget(self.line_2)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_10)
        self.lineEdit.setMaximumSize(QtCore.QSize(130, 16777215))
        self.lineEdit.setStyleSheet("border: 0px;")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.verticalLayout_4.addWidget(self.frame_10)
        self.frame_8 = QtWidgets.QFrame(self.frame)
        self.frame_8.setMinimumSize(QtCore.QSize(206, 40))
        self.frame_8.setMaximumSize(QtCore.QSize(206, 40))
        self.frame_8.setStyleSheet("border: 1px solid black;\n"
"border-radius:20px;\n"
"background-color: white;")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frame_8)
        self.label_3.setMinimumSize(QtCore.QSize(40, 20))
        self.label_3.setMaximumSize(QtCore.QSize(25, 20))
        self.label_3.setStyleSheet("border:0px;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.line = QtWidgets.QFrame(self.frame_8)
        self.line.setMinimumSize(QtCore.QSize(0, 40))
        self.line.setMaximumSize(QtCore.QSize(1, 16777215))
        self.line.setStyleSheet("margin-top:0px;")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)
        self.comboBox = QtWidgets.QComboBox(self.frame_8)
        self.comboBox.setMinimumSize(QtCore.QSize(130, 20))
        self.comboBox.setStyleSheet("QComboBox {\n"
"    border: transparent;\n"
"\n"
"}\n"
"QComboBox::drop-down:button{\n"
"border:transparent; background:transparent;\n"
"border-image: url(:/iconteste/icons/arrow-black.png);\n"
"width: 14px;\n"
"height: 14px;\n"
"padding-top:1px;\n"
"margin-top:3px;\n"
"\n"
"}\n"
"\n"
"QComboBox QAbstractItemView{\n"
"    \n"
"    border:1px solid black;\n"
"    border-radius:0px;\n"
" \n"
"    \n"
"}\n"
"")
        self.comboBox.setIconSize(QtCore.QSize(16, 16))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.horizontalLayout_3.addWidget(self.comboBox, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.verticalLayout_4.addWidget(self.frame_8)
        self.frame_11 = QtWidgets.QFrame(self.frame)
        self.frame_11.setMinimumSize(QtCore.QSize(206, 40))
        self.frame_11.setMaximumSize(QtCore.QSize(206, 40))
        self.frame_11.setStyleSheet("border: 1px solid black;\n"
"border-radius:20px;\n"
"background-color: white;")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.frame_11)
        self.label_5.setMinimumSize(QtCore.QSize(40, 20))
        self.label_5.setMaximumSize(QtCore.QSize(25, 20))
        self.label_5.setStyleSheet("border:0px;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.line_3 = QtWidgets.QFrame(self.frame_11)
        self.line_3.setMinimumSize(QtCore.QSize(0, 40))
        self.line_3.setMaximumSize(QtCore.QSize(1, 16777215))
        self.line_3.setStyleSheet("margin-top:0px;")
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_5.addWidget(self.line_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_11)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(130, 16777215))
        self.lineEdit_2.setStyleSheet("border: 0px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_5.addWidget(self.lineEdit_2)
        self.verticalLayout_4.addWidget(self.frame_11)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.frame_16)
        self.frame_22 = QtWidgets.QFrame(self.frame_15)
        self.frame_22.setMaximumSize(QtCore.QSize(16777213, 16777215))
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_22)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.adduser = QtWidgets.QPushButton(self.frame_22)
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
        self.adduser.clicked.connect(self.insertData)

        self.gridLayout_4.addWidget(self.adduser, 0, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.frame_22)
        self.frame_21 = QtWidgets.QFrame(self.frame_15)
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_21)
        self.horizontalLayout_10.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame_14 = QtWidgets.QFrame(self.frame_21)
        self.frame_14.setMaximumSize(QtCore.QSize(16777215, 25))
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_11.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_9 = QtWidgets.QLabel(self.frame_14)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_11.addWidget(self.label_9)
        self.horizontalLayout_10.addWidget(self.frame_14)
        self.frame_23 = QtWidgets.QFrame(self.frame_21)
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.horizontalLayout_10.addWidget(self.frame_23)
        self.frame_24 = QtWidgets.QFrame(self.frame_21)
        self.frame_24.setMaximumSize(QtCore.QSize(150, 16777215))
        self.frame_24.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_24)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_11 = QtWidgets.QLabel(self.frame_24)
        self.label_11.setMinimumSize(QtCore.QSize(100, 70))
        self.label_11.setMaximumSize(QtCore.QSize(110, 16777215))
        self.label_11.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_11.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"border-image: url(:/iconteste/icons/bc618214-251e-4c1c-9617-52f5a49d45b0.jpg);\n"
"border-radius:0px;")
        self.label_11.setText("")
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_12.addWidget(self.label_11)
        self.horizontalLayout_10.addWidget(self.frame_24)
        self.verticalLayout_5.addWidget(self.frame_21)
        self.gridLayout_5.addWidget(self.frame_15, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_17)
        cadastro.setCentralWidget(self.centralwidget)

        self.retranslateUi(cadastro)
        QtCore.QMetaObject.connectSlotsByName(cadastro)

    def retranslateUi(self, cadastro):
        _translate = QtCore.QCoreApplication.translate
        cadastro.setWindowTitle(_translate("cadastro", "Cadastro"))
        self.label_2.setText(_translate("cadastro", "andrade esquadrias id user #8774"))
        self.bugreport.setText(_translate("cadastro", "Bug Report"))
        self.retotologin.setText(_translate("cadastro", "Retornar para login"))
        self.label_10.setText(_translate("cadastro", "Andráde esquadrias"))
        self.label_8.setText(_translate("cadastro", "Cadastro"))
        self.label_6.setText(_translate("cadastro", "Nome"))
        self.label_4.setText(_translate("cadastro", "E-Mail"))
        self.label_3.setText(_translate("cadastro", "Cargo"))
        self.comboBox.setItemText(0, _translate("cadastro", "Admin"))
        self.comboBox.setItemText(1, _translate("cadastro", "T.i"))
        self.comboBox.setItemText(2, _translate("cadastro", "Vendedor"))
        self.comboBox.setItemText(3, _translate("cadastro", "Gerência"))
        self.label_5.setText(_translate("cadastro", "Senha:"))
        self.adduser.setText(_translate("cadastro", "Adicionar novo usuário"))
        self.label_9.setText(_translate("cadastro", "Orb powered by Evolcco Versão BETA 0.1"))

import source_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cadastro = QtWidgets.QMainWindow()
    ui = Ui_cadastro()
    ui.setupUi(cadastro)
    cadastro.show()
    cadastro.showMaximized()

    sys.exit(app.exec_())

