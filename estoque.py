# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Estoque(object):
    def setupUi(self, Estoque):
        Estoque.setObjectName("Estoque")
        Estoque.resize(1248, 803)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconteste/icons/ba812f4a-b112-4fa5-96d0-dccd574e3a86.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Estoque.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Estoque)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
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
        self.frame_12 = QtWidgets.QFrame(self.frame_3)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_3.setContentsMargins(6, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.frame_12)
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
        self.frame_4 = QtWidgets.QFrame(self.frame_12)
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
        self.verticalLayout.addWidget(self.Logincadastro)
        self.horizontalLayout_3.addWidget(self.frame_4)
        self.frame_13 = QtWidgets.QFrame(self.frame_12)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout.setContentsMargins(20, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_13)
        self.label_2.setMinimumSize(QtCore.QSize(200, 0))
        self.label_2.setMaximumSize(QtCore.QSize(200, 30))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.horizontalLayout_3.addWidget(self.frame_13, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_3.addWidget(self.frame_12)
        self.label_24 = QtWidgets.QLabel(self.frame_3)
        self.label_24.setMinimumSize(QtCore.QSize(0, 15))
        self.label_24.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_24.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.0227727, y1:0.557, x2:1, y2:0.551, stop:0.181818 rgba(116, 0, 239, 255), stop:0.903409 rgba(48, 252, 194, 255));")
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.verticalLayout_3.addWidget(self.label_24)
        self.verticalLayout_5.addWidget(self.frame_3)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color:#403749;\n"
"color:black;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_46 = QtWidgets.QFrame(self.frame)
        self.frame_46.setStyleSheet("border-radius:15px;")
        self.frame_46.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_46.setObjectName("frame_46")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.frame_46)
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.frame_41 = QtWidgets.QFrame(self.frame_46)
        self.frame_41.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_41.setObjectName("frame_41")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.frame_41)
        self.horizontalLayout_23.setContentsMargins(-1, -1, 0, 0)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.frame_42 = QtWidgets.QFrame(self.frame_41)
        self.frame_42.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_42.setObjectName("frame_42")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.frame_42)
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.frame_43 = QtWidgets.QFrame(self.frame_42)
        self.frame_43.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_43.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_43.setStyleSheet("background-color:white;\n"
"color:black;")
        self.frame_43.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_43.setObjectName("frame_43")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.frame_43)
        self.horizontalLayout_22.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_34 = QtWidgets.QLabel(self.frame_43)
        self.label_34.setMinimumSize(QtCore.QSize(20, 20))
        self.label_34.setMaximumSize(QtCore.QSize(20, 20))
        self.label_34.setStyleSheet("border-image: url(:/iconteste/icons/loupe (1).png);\n"
"border-radius:12px;")
        self.label_34.setText("")
        self.label_34.setObjectName("label_34")
        self.horizontalLayout_22.addWidget(self.label_34)
        self.line_2 = QtWidgets.QFrame(self.frame_43)
        self.line_2.setMinimumSize(QtCore.QSize(1, 25))
        self.line_2.setMaximumSize(QtCore.QSize(1, 16777215))
        self.line_2.setStyleSheet("background-color:black;    ")
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_22.addWidget(self.line_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_43)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_2.setStyleSheet("background-color:white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color:black;\n"
"border-radius:10px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_22.addWidget(self.lineEdit_2)
        self.horizontalLayout_21.addWidget(self.frame_43)
        self.comboBox_6 = QtWidgets.QComboBox(self.frame_42)
        self.comboBox_6.setMinimumSize(QtCore.QSize(125, 25))
        self.comboBox_6.setStyleSheet("QComboBox {\n"
"    border: transparent;\n"
"\n"
"}\n"
"QComboBox::drop-down:button{\n"
"border:transparent; background:transparent;\n"
"border-image: url(:/iconteste/icons/arrow-white.png);\n"
"width: 14,px;\n"
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
        self.comboBox_6.setObjectName("comboBox_6")
        self.horizontalLayout_21.addWidget(self.comboBox_6)
        self.horizontalLayout_23.addWidget(self.frame_42)
        self.verticalLayout_20.addWidget(self.frame_41)
        self.frame_45 = QtWidgets.QFrame(self.frame_46)
        self.frame_45.setMinimumSize(QtCore.QSize(700, 0))
        self.frame_45.setMaximumSize(QtCore.QSize(16515165, 16777215))
        self.frame_45.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_45.setObjectName("frame_45")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.frame_45)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.frame_45)
        self.tableWidget_4.setStyleSheet("background-color:white;\n"
"color:black;")
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(0)
        self.tableWidget_4.setRowCount(0)
        self.horizontalLayout_24.addWidget(self.tableWidget_4)
        self.verticalLayout_20.addWidget(self.frame_45)
        self.horizontalLayout_2.addWidget(self.frame_46)
        self.frame_11 = QtWidgets.QFrame(self.frame)
        self.frame_11.setMaximumSize(QtCore.QSize(500, 700))
        self.frame_11.setStyleSheet("background-color:#625f66;\n"
"color:white;\n"
"border-radius:10px;")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.frame_11)
        self.label_3.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.frame_15 = QtWidgets.QFrame(self.frame_11)
        self.frame_15.setStyleSheet("color:black;")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_16 = QtWidgets.QFrame(self.frame_15)
        self.frame_16.setMinimumSize(QtCore.QSize(300, 40))
        self.frame_16.setMaximumSize(QtCore.QSize(206, 40))
        self.frame_16.setStyleSheet("border: 1px solid black;\n"
"border-radius:20px;\n"
"background-color: white;\n"
"color:black;")
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_14 = QtWidgets.QLabel(self.frame_16)
        self.label_14.setMinimumSize(QtCore.QSize(40, 20))
        self.label_14.setMaximumSize(QtCore.QSize(100, 20))
        self.label_14.setStyleSheet("border:0px;")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_8.addWidget(self.label_14)
        self.line_5 = QtWidgets.QFrame(self.frame_16)
        self.line_5.setMinimumSize(QtCore.QSize(0, 40))
        self.line_5.setMaximumSize(QtCore.QSize(1, 16777215))
        self.line_5.setStyleSheet("margin-top:0px;")
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_8.addWidget(self.line_5)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_16)
        self.lineEdit_5.setMaximumSize(QtCore.QSize(130, 16777215))
        self.lineEdit_5.setStyleSheet("border: 0px;")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_8.addWidget(self.lineEdit_5)
        self.verticalLayout_7.addWidget(self.frame_16)
        self.frame_20 = QtWidgets.QFrame(self.frame_15)
        self.frame_20.setMinimumSize(QtCore.QSize(300, 40))
        self.frame_20.setMaximumSize(QtCore.QSize(206, 40))
        self.frame_20.setStyleSheet("border: 1px solid black;\n"
"border-radius:20px;\n"
"background-color: white;\n"
"color:black;")
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_20)
        self.horizontalLayout_13.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_20 = QtWidgets.QLabel(self.frame_20)
        self.label_20.setMinimumSize(QtCore.QSize(40, 20))
        self.label_20.setMaximumSize(QtCore.QSize(100, 20))
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
        self.verticalLayout_7.addWidget(self.frame_20)
        self.frame_17 = QtWidgets.QFrame(self.frame_15)
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
        self.label_17.setMaximumSize(QtCore.QSize(100, 20))
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
        self.comboBox_7 = QtWidgets.QComboBox(self.frame_17)
        self.comboBox_7.setMaximumSize(QtCore.QSize(130, 16777215))
        self.comboBox_7.setStyleSheet("QComboBox {\n"
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
        self.comboBox_7.setObjectName("comboBox_7")
        self.horizontalLayout_10.addWidget(self.comboBox_7)
        self.verticalLayout_7.addWidget(self.frame_17)
        self.frame_19 = QtWidgets.QFrame(self.frame_15)
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
        self.label_19.setMaximumSize(QtCore.QSize(100, 20))
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
        self.comboBox_8 = QtWidgets.QComboBox(self.frame_19)
        self.comboBox_8.setMaximumSize(QtCore.QSize(130, 16777215))
        self.comboBox_8.setStyleSheet("QComboBox {\n"
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
        self.comboBox_8.setObjectName("comboBox_8")
        self.horizontalLayout_12.addWidget(self.comboBox_8)
        self.verticalLayout_7.addWidget(self.frame_19)
        self.frame_18 = QtWidgets.QFrame(self.frame_15)
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
        self.label_18.setMaximumSize(QtCore.QSize(100, 20))
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
        self.verticalLayout_7.addWidget(self.frame_18)
        self.verticalLayout_4.addWidget(self.frame_15, 0, QtCore.Qt.AlignHCenter)
        self.frame_7 = QtWidgets.QFrame(self.frame_11)
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 250))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_7)
        self.label.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.frame_7)
        self.plainTextEdit.setMaximumSize(QtCore.QSize(300, 200))
        self.plainTextEdit.setStyleSheet("border:1px solid white;")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_2.addWidget(self.plainTextEdit, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_4.addWidget(self.frame_7)
        self.frame_6 = QtWidgets.QFrame(self.frame_11)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_13.setMinimumSize(QtCore.QSize(170, 30))
        self.pushButton_13.setMaximumSize(QtCore.QSize(180, 16777215))
        self.pushButton_13.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_13.setStyleSheet("\n"
"\n"
"\n"
"QPushButton{\n"
"border:1px;\n"
"background-color: qlineargradient(spread:pad, x1:0.0227727, y1:0.557, x2:1, y2:0.551, stop:0.181818 rgba(116, 0, 239, 255), stop:0.903409 rgba(48, 252, 194, 255));\n"
"border-radius:10px;\n"
"color:white;\n"
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/iconteste/icons/right white arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_13.setIcon(icon2)
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_4.addWidget(self.pushButton_13)
        self.verticalLayout_4.addWidget(self.frame_6)
        self.horizontalLayout_2.addWidget(self.frame_11)
        self.verticalLayout_5.addWidget(self.frame)
        Estoque.setCentralWidget(self.centralwidget)

        self.retranslateUi(Estoque)
        QtCore.QMetaObject.connectSlotsByName(Estoque)

    def retranslateUi(self, Estoque):
        _translate = QtCore.QCoreApplication.translate
        Estoque.setWindowTitle(_translate("Estoque", "Estoque"))
        self.Logincadastro.setText(_translate("Estoque", "Login/ Cadastro"))
        self.label_2.setText(_translate("Estoque", "          Meemo user id user #0001"))
        self.lineEdit_2.setPlaceholderText(_translate("Estoque", "Pesquise os produtos"))
        self.label_3.setText(_translate("Estoque", "Cadastro de Produtos"))
        self.label_14.setText(_translate("Estoque", "Nome:"))
        self.label_20.setText(_translate("Estoque", "Quantidade:"))
        self.label_17.setText(_translate("Estoque", "Tipo:"))
        self.label_19.setText(_translate("Estoque", "Linha:"))
        self.label_18.setText(_translate("Estoque", "Definição:"))
        self.label.setText(_translate("Estoque", "          Descrição:"))
        self.pushButton_13.setText(_translate("Estoque", "     Adcionar Produto ao banco"))

import source_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Estoque = QtWidgets.QMainWindow()
    ui = Ui_Estoque()
    ui.setupUi(Estoque)
    Estoque.show()
    sys.exit(app.exec_())

