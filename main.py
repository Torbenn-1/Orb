# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1273, 913)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconteste/icons/Ativo 16@2x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color:#403749 ;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_16 = QtWidgets.QFrame(self.centralwidget)
        self.frame_16.setStyleSheet("background-color: rgb(40, 28, 53);\n"
"color:white;")
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_16)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(self.frame_16)
        self.frame.setStyleSheet("background-color: #281c35;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMinimumSize(QtCore.QSize(25, 25))
        self.frame_4.setMaximumSize(QtCore.QSize(25, 25))
        self.frame_4.setStyleSheet("border-image: url(:/iconteste/icons/ba812f4a-b112-4fa5-96d0-dccd574e3a86.jpg);\n"
"border-radius:12px;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout.setContentsMargins(-1, -1, 9, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3.addWidget(self.frame_4)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMinimumSize(QtCore.QSize(714, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(6546545, 16777215))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setContentsMargins(0, -1, 134, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setMinimumSize(QtCore.QSize(80, 30))
        self.pushButton.setToolTip("")
        self.pushButton.setStyleSheet("QPushButton{\n"
"border:0px;\n"
"border-radius:12px;\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"\n"
"background-color:#403749;\n"
"\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"border-style: outset;\n"
"border-width: 3px;\n"
"border-color: #30fcc2;\n"
"background-color:625f66\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/iconteste/icons/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(20, 20))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setMaximumSize(QtCore.QSize(25, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"border:0px;\n"
"border-radius:12px;\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"\n"
"background-color:#403749;\n"
"\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"border-style: outset;\n"
"border-width: 3px;\n"
"border-color: #30fcc2;\n"
"background-color:625f66\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/iconteste/icons/store.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2, 0, QtCore.Qt.AlignHCenter)
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setMaximumSize(QtCore.QSize(25, 16777215))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_3.setMinimumSize(QtCore.QSize(80, 30))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"border:0px;\n"
"border-radius:12px;\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"\n"
"background-color:#403749;\n"
"\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"border-style: outset;\n"
"border-width: 3px;\n"
"border-color: #30fcc2;\n"
"background-color:625f66\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/iconteste/icons/box.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setMaximumSize(QtCore.QSize(25, 16777215))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_5.setMinimumSize(QtCore.QSize(80, 30))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"border:0px;\n"
"border-radius:12px;\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"\n"
"background-color:#403749;\n"
"\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"border-style: outset;\n"
"border-width: 3px;\n"
"border-color: #30fcc2;\n"
"background-color:625f66\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/iconteste/icons/graph.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.pushButton_5.raise_()
        self.horizontalLayout_3.addWidget(self.frame_3, 0, QtCore.Qt.AlignLeft)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(500, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6, 0, QtCore.Qt.AlignRight)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_6.setMinimumSize(QtCore.QSize(96, 25))
        self.pushButton_6.setMaximumSize(QtCore.QSize(96, 25))
        self.pushButton_6.setStyleSheet("\n"
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
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.horizontalLayout_3.addWidget(self.frame_2)
        self.verticalLayout_3.addWidget(self.frame)
        self.label_23 = QtWidgets.QLabel(self.frame_16)
        self.label_23.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.0227727, y1:0.557, x2:1, y2:0.551, stop:0.181818 rgba(116, 0, 239, 255), stop:0.903409 rgba(48, 252, 194, 255));")
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.verticalLayout_3.addWidget(self.label_23)
        self.verticalLayout_5.addWidget(self.frame_16)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("QTabBar::tab {\n"
"height: 40px;\n"
"width: 93px; \n"
"background-color:#403749; \n"
"color:white;\n"
"border-right:2px solid #ffffff;\n"
"padding-left:7px;\n"
" }\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-bottom:3px solid #39fdc5;\n"
"}\n"
"")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(24, 24))
        self.tabWidget.setObjectName("tabWidget")
        self.Tab_2 = QtWidgets.QWidget()
        self.Tab_2.setObjectName("Tab_2")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.Tab_2)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.frame_22 = QtWidgets.QFrame(self.Tab_2)
        self.frame_22.setStyleSheet("background-color:#625f66;\n"
"color:white;")
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_22)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame_23 = QtWidgets.QFrame(self.frame_22)
        self.frame_23.setStyleSheet("\n"
"color: white;\n"
"background-color:#625f66;\n"
"border-radius:15px;")
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_23)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_24 = QtWidgets.QFrame(self.frame_23)
        self.frame_24.setMinimumSize(QtCore.QSize(0, 28))
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_24)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_17 = QtWidgets.QLabel(self.frame_24)
        self.label_17.setMinimumSize(QtCore.QSize(75, 25))
        self.label_17.setObjectName("label_17")
        self.verticalLayout_15.addWidget(self.label_17)
        self.verticalLayout_7.addWidget(self.frame_24)
        self.frame_25 = QtWidgets.QFrame(self.frame_23)
        self.frame_25.setMinimumSize(QtCore.QSize(0, 72))
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_25)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_18 = QtWidgets.QLabel(self.frame_25)
        self.label_18.setMinimumSize(QtCore.QSize(55, 50))
        self.label_18.setMaximumSize(QtCore.QSize(55, 50))
        self.label_18.setStyleSheet("border-image: url(:/iconteste/icons/user-g.png);")
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_15.addWidget(self.label_18)
        self.frame_26 = QtWidgets.QFrame(self.frame_25)
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.frame_26)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.frame_39 = QtWidgets.QFrame(self.frame_26)
        self.frame_39.setMinimumSize(QtCore.QSize(0, 75))
        self.frame_39.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_39.setObjectName("frame_39")
        self.formLayout_6 = QtWidgets.QFormLayout(self.frame_39)
        self.formLayout_6.setObjectName("formLayout_6")
        self.clientenome = QtWidgets.QLabel(self.frame_39)
        self.clientenome.setMinimumSize(QtCore.QSize(75, 25))
        self.clientenome.setObjectName("clientenome")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.clientenome)
        self.rua = QtWidgets.QLabel(self.frame_39)
        self.rua.setMinimumSize(QtCore.QSize(75, 25))
        self.rua.setObjectName("rua")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.rua)
        self.telefone = QtWidgets.QLabel(self.frame_39)
        self.telefone.setMinimumSize(QtCore.QSize(75, 25))
        self.telefone.setObjectName("telefone")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.telefone)
        self.citycep = QtWidgets.QLabel(self.frame_39)
        self.citycep.setMinimumSize(QtCore.QSize(75, 25))
        self.citycep.setObjectName("citycep")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.citycep)
        self.horizontalLayout_20.addWidget(self.frame_39)
        self.frame_50 = QtWidgets.QFrame(self.frame_26)
        self.frame_50.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_50.setObjectName("frame_50")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout(self.frame_50)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.label_5 = QtWidgets.QLabel(self.frame_50)
        self.label_5.setMinimumSize(QtCore.QSize(111, 25))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_29.addWidget(self.label_5)
        self.comboBox_7 = QtWidgets.QComboBox(self.frame_50)
        self.comboBox_7.setStyleSheet("QComboBox {\n"
"    border: transparent;\n"
"\n"
"}\n"
"QComboBox::drop-down:button{\n"
"border:transparent; background:transparent;\n"
"border-image: url(:/iconteste/icons/arrow-white.png);\n"
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
"}")
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.horizontalLayout_29.addWidget(self.comboBox_7)
        self.horizontalLayout_20.addWidget(self.frame_50)
        self.frame_40 = QtWidgets.QFrame(self.frame_26)
        self.frame_40.setMaximumSize(QtCore.QSize(450, 16777215))
        self.frame_40.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_40.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_40.setObjectName("frame_40")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frame_40)
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.frame_47 = QtWidgets.QFrame(self.frame_40)
        self.frame_47.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_47.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_47.setObjectName("frame_47")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.frame_47)
        self.horizontalLayout_26.setContentsMargins(152, 0, 0, 0)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_47)
        self.pushButton_13.setMinimumSize(QtCore.QSize(170, 30))
        self.pushButton_13.setMaximumSize(QtCore.QSize(170, 16777215))
        self.pushButton_13.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_13.setStyleSheet("\n"
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
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/iconteste/icons/right white arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_13.setIcon(icon5)
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_26.addWidget(self.pushButton_13)
        self.verticalLayout_21.addWidget(self.frame_47)
        self.horizontalLayout_20.addWidget(self.frame_40)
        self.horizontalLayout_15.addWidget(self.frame_26)
        self.verticalLayout_7.addWidget(self.frame_25)
        self.frame_27 = QtWidgets.QFrame(self.frame_23)
        self.frame_27.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_27)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.frame_28 = QtWidgets.QFrame(self.frame_27)
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_28)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_38 = QtWidgets.QFrame(self.frame_28)
        self.frame_38.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_38.setObjectName("frame_38")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frame_38)
        self.horizontalLayout_19.setContentsMargins(-1, -1, -1, 8)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.frame_30 = QtWidgets.QFrame(self.frame_38)
        self.frame_30.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_30.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_30.setStyleSheet("background-color:white;\n"
"color:black;")
        self.frame_30.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_30.setObjectName("frame_30")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_30)
        self.horizontalLayout_18.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_33 = QtWidgets.QLabel(self.frame_30)
        self.label_33.setMinimumSize(QtCore.QSize(20, 20))
        self.label_33.setMaximumSize(QtCore.QSize(20, 20))
        self.label_33.setStyleSheet("border-image: url(:/iconteste/icons/loupe (1).png);\n"
"border-radius:12px;")
        self.label_33.setText("")
        self.label_33.setObjectName("label_33")
        self.horizontalLayout_18.addWidget(self.label_33)
        self.line = QtWidgets.QFrame(self.frame_30)
        self.line.setMinimumSize(QtCore.QSize(1, 25))
        self.line.setMaximumSize(QtCore.QSize(1, 16777215))
        self.line.setStyleSheet("background-color:black;    ")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_18.addWidget(self.line)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_30)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit.setStyleSheet("background-color:white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color:black;\n"
"border-radius:10px;")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_18.addWidget(self.lineEdit)
        self.horizontalLayout_19.addWidget(self.frame_30)
        self.comboBox_4 = QtWidgets.QComboBox(self.frame_38)
        self.comboBox_4.setMinimumSize(QtCore.QSize(125, 25))
        self.comboBox_4.setStyleSheet("QComboBox {\n"
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
        self.comboBox_4.setObjectName("comboBox_4")
        self.horizontalLayout_19.addWidget(self.comboBox_4)
        self.verticalLayout_6.addWidget(self.frame_38)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.frame_28)
        self.tableWidget_3.setStyleSheet("background-color:white;\n"
"color:black;")
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.verticalLayout_6.addWidget(self.tableWidget_3)
        self.frame_48 = QtWidgets.QFrame(self.frame_28)
        self.frame_48.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_48.setObjectName("frame_48")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.frame_48)
        self.horizontalLayout_27.setContentsMargins(-1, -1, -1, 8)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.frame_49 = QtWidgets.QFrame(self.frame_48)
        self.frame_49.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_49.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_49.setStyleSheet("background-color:white;\n"
"color:black;")
        self.frame_49.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_49.setObjectName("frame_49")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout(self.frame_49)
        self.horizontalLayout_28.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.label_47 = QtWidgets.QLabel(self.frame_49)
        self.label_47.setMinimumSize(QtCore.QSize(20, 20))
        self.label_47.setMaximumSize(QtCore.QSize(20, 20))
        self.label_47.setStyleSheet("border-image: url(:/iconteste/icons/loupe (1).png);\n"
"border-radius:12px;")
        self.label_47.setText("")
        self.label_47.setObjectName("label_47")
        self.horizontalLayout_28.addWidget(self.label_47)
        self.line_3 = QtWidgets.QFrame(self.frame_49)
        self.line_3.setMinimumSize(QtCore.QSize(1, 25))
        self.line_3.setMaximumSize(QtCore.QSize(1, 16777215))
        self.line_3.setStyleSheet("background-color:black;    ")
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_28.addWidget(self.line_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_49)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_3.setStyleSheet("background-color:white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color:black;\n"
"border-radius:10px;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_28.addWidget(self.lineEdit_3)
        self.horizontalLayout_27.addWidget(self.frame_49)
        self.comboBox_5 = QtWidgets.QComboBox(self.frame_48)
        self.comboBox_5.setMinimumSize(QtCore.QSize(125, 25))
        self.comboBox_5.setStyleSheet("QComboBox {\n"
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
        self.comboBox_5.setObjectName("comboBox_5")
        self.horizontalLayout_27.addWidget(self.comboBox_5)
        self.verticalLayout_6.addWidget(self.frame_48)
        self.listWidget = QtWidgets.QListWidget(self.frame_28)
        self.listWidget.setStyleSheet("background-color:white;\n"
"color:black;")
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_6.addWidget(self.listWidget)
        self.horizontalLayout_16.addWidget(self.frame_28)
        self.frame_29 = QtWidgets.QFrame(self.frame_27)
        self.frame_29.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_29.setMaximumSize(QtCore.QSize(350, 16777215))
        self.frame_29.setStyleSheet("color: white;\n"
"background-color:#625f66;\n"
"border-radius:15px;")
        self.frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_29)
        self.verticalLayout_8.setContentsMargins(-1, 0, 9, 21)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_37 = QtWidgets.QFrame(self.frame_29)
        self.frame_37.setMaximumSize(QtCore.QSize(16777215, 400))
        self.frame_37.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_37.setObjectName("frame_37")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frame_37)
        self.verticalLayout_18.setContentsMargins(0, 26, 0, 0)
        self.verticalLayout_18.setSpacing(17)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label = QtWidgets.QLabel(self.frame_37)
        self.label.setMaximumSize(QtCore.QSize(400, 25))
        self.label.setObjectName("label")
        self.verticalLayout_18.addWidget(self.label)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.frame_37)
        self.plainTextEdit.setMaximumSize(QtCore.QSize(400, 200))
        self.plainTextEdit.setStyleSheet("background-color: rgb(147, 147, 147);\n"
"border-radius:0px;")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_18.addWidget(self.plainTextEdit)
        self.verticalLayout_8.addWidget(self.frame_37, 0, QtCore.Qt.AlignTop)
        self.frame_31 = QtWidgets.QFrame(self.frame_29)
        self.frame_31.setMinimumSize(QtCore.QSize(0, 300))
        self.frame_31.setMaximumSize(QtCore.QSize(16777215, 4000))
        self.frame_31.setStyleSheet("background-color:#403749;")
        self.frame_31.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_31)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_36 = QtWidgets.QFrame(self.frame_31)
        self.frame_36.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_36.setObjectName("frame_36")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_36)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.frame_32 = QtWidgets.QFrame(self.frame_36)
        self.frame_32.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_32.setObjectName("frame_32")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_32)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_28 = QtWidgets.QLabel(self.frame_32)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_16.addWidget(self.label_28, 0, QtCore.Qt.AlignRight)
        self.label_26 = QtWidgets.QLabel(self.frame_32)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_16.addWidget(self.label_26, 0, QtCore.Qt.AlignRight)
        self.label_7 = QtWidgets.QLabel(self.frame_32)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_16.addWidget(self.label_7, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout_17.addWidget(self.frame_32)
        self.frame_35 = QtWidgets.QFrame(self.frame_36)
        self.frame_35.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_35.setObjectName("frame_35")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_35)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_9 = QtWidgets.QLabel(self.frame_35)
        self.label_9.setStyleSheet("color:#39fdc5;")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_17.addWidget(self.label_9)
        self.label_30 = QtWidgets.QLabel(self.frame_35)
        self.label_30.setStyleSheet("color:#39fdc5;")
        self.label_30.setObjectName("label_30")
        self.verticalLayout_17.addWidget(self.label_30)
        self.label_29 = QtWidgets.QLabel(self.frame_35)
        self.label_29.setStyleSheet("color:#cb7efb;")
        self.label_29.setObjectName("label_29")
        self.verticalLayout_17.addWidget(self.label_29)
        self.horizontalLayout_17.addWidget(self.frame_35)
        self.verticalLayout_10.addWidget(self.frame_36)
        self.frame_33 = QtWidgets.QFrame(self.frame_31)
        self.frame_33.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_33.setObjectName("frame_33")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_33)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_31 = QtWidgets.QLabel(self.frame_33)
        self.label_31.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_31.setObjectName("label_31")
        self.verticalLayout_11.addWidget(self.label_31, 0, QtCore.Qt.AlignHCenter)
        self.label_32 = QtWidgets.QLabel(self.frame_33)
        self.label_32.setStyleSheet("color:#39fdc5;\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.label_32.setObjectName("label_32")
        self.verticalLayout_11.addWidget(self.label_32, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_10.addWidget(self.frame_33)
        self.frame_34 = QtWidgets.QFrame(self.frame_31)
        self.frame_34.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_34.setObjectName("frame_34")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_34)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_34)
        self.pushButton_10.setMinimumSize(QtCore.QSize(170, 30))
        self.pushButton_10.setMaximumSize(QtCore.QSize(300, 16777215))
        self.pushButton_10.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_10.setStyleSheet("\n"
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
        self.pushButton_10.setIcon(icon5)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_12.addWidget(self.pushButton_10)
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_34)
        self.pushButton_11.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_11.setStyleSheet("QPushButton{\n"
"border:0px;\n"
"border-radius:5px;\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"\n"
"background-color:#281c35;\n"
"\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"border-style: outset;\n"
"border-width: 3px;\n"
"border-color: #30fcc2;\n"
"background-color:#625f66;\n"
"}")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/iconteste/icons/invoice.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_11.setIcon(icon6)
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_12.addWidget(self.pushButton_11)
        self.verticalLayout_10.addWidget(self.frame_34, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_8.addWidget(self.frame_31)
        self.horizontalLayout_16.addWidget(self.frame_29)
        self.verticalLayout_7.addWidget(self.frame_27)
        self.verticalLayout_13.addWidget(self.frame_23)
        self.verticalLayout_14.addWidget(self.frame_22)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/iconteste/icons/cart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.Tab_2, icon7, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.frame_20 = QtWidgets.QFrame(self.tab)
        self.frame_20.setStyleSheet("color:white;")
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_20)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_17 = QtWidgets.QFrame(self.frame_20)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.frame_18 = QtWidgets.QFrame(self.frame_17)
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_18)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_18)
        self.pushButton_9.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton_9.setMaximumSize(QtCore.QSize(200, 16777215))
        self.pushButton_9.setStyleSheet("QPushButton{\n"
"border:0px;\n"
"border-radius:12px;\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"\n"
"background-color:#281c35;\n"
"\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"border-style: outset;\n"
"border-width: 3px;\n"
"border-color: #30fcc2;\n"
"background-color:281c35;\n"
"}")
        self.pushButton_9.setIcon(icon2)
        self.pushButton_9.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_11.addWidget(self.pushButton_9)
        self.comboBox = QtWidgets.QComboBox(self.frame_18)
        self.comboBox.setStyleSheet("background-color:transparent;\n"
"color:white;")
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_11.addWidget(self.comboBox)
        self.horizontalLayout_12.addWidget(self.frame_18)
        self.frame_19 = QtWidgets.QFrame(self.frame_17)
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_19)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_24 = QtWidgets.QLabel(self.frame_19)
        self.label_24.setMinimumSize(QtCore.QSize(20, 20))
        self.label_24.setMaximumSize(QtCore.QSize(20, 20))
        self.label_24.setStyleSheet("border-image: url(:/iconsteste/user.png);")
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_10.addWidget(self.label_24)
        self.label_25 = QtWidgets.QLabel(self.frame_19)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_10.addWidget(self.label_25)
        self.comboBox_3 = QtWidgets.QComboBox(self.frame_19)
        self.comboBox_3.setStyleSheet("background-color:transparent;\n"
"color:white;")
        self.comboBox_3.setObjectName("comboBox_3")
        self.horizontalLayout_10.addWidget(self.comboBox_3)
        self.label_27 = QtWidgets.QLabel(self.frame_19)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_10.addWidget(self.label_27)
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_19)
        self.comboBox_2.setStyleSheet("background-color:transparent;\n"
"color:white;")
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_10.addWidget(self.comboBox_2)
        self.horizontalLayout_12.addWidget(self.frame_19)
        self.verticalLayout_4.addWidget(self.frame_17)
        self.frame_21 = QtWidgets.QFrame(self.frame_20)
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_21)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.frame_21)
        self.tableWidget_2.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget_2.setStyleSheet("\n"
"QTableWidget::item { \n"
"background-color: #625f66; }\n"
"QTableWidget::item:alternate {\n"
" background-color: #403749; } \n"
"\n"
"QTableWidget{\n"
"color:white;\n"
"border:0px;\n"
"}")
        self.tableWidget_2.setAlternatingRowColors(True)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(6)
        self.tableWidget_2.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        self.tableWidget_2.horizontalHeader().setVisible(False)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(103)
        self.tableWidget_2.horizontalHeader().setHighlightSections(False)
        self.tableWidget_2.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(48)
        self.tableWidget_2.verticalHeader().setHighlightSections(False)
        self.tableWidget_2.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget_2.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout_13.addWidget(self.tableWidget_2)
        self.verticalLayout_4.addWidget(self.frame_21)
        self.horizontalLayout_14.addWidget(self.frame_20)
        self.frame_5 = QtWidgets.QFrame(self.tab)
        self.frame_5.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_5.setStyleSheet("color: white;\n"
"background-color:#625f66;\n"
"border-radius:15px;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.current_date = QtWidgets.QLabel(self.frame_7)
        self.current_date.setObjectName("current_date")
        self.horizontalLayout_8.addWidget(self.current_date)
        self.horizontalLayout_9.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_6)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_7.setMinimumSize(QtCore.QSize(40, 25))
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"border:0px;\n"
"border-radius:5px;\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"\n"
"background-color:#403749;\n"
"\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"border-style: outset;\n"
"border-width: 3px;\n"
"border-color: #30fcc2;\n"
"background-color:625f66;\n"
"}")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/iconteste/icons/send-file-icon-18-256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon8)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_7.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_8.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"border:0px;\n"
"border-radius:5px;\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"\n"
"background-color:#403749;\n"
"\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"border-style: outset;\n"
"border-width: 3px;\n"
"border-color: #30fcc2;\n"
"background-color:625f66;\n"
"}")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/iconteste/icons/printer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon9)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_7.addWidget(self.pushButton_8)
        self.horizontalLayout_9.addWidget(self.frame_8)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.frame_9 = QtWidgets.QFrame(self.frame_5)
        self.frame_9.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_10 = QtWidgets.QFrame(self.frame_9)
        self.frame_10.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.formLayout_3 = QtWidgets.QFormLayout(self.frame_10)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_8 = QtWidgets.QLabel(self.frame_10)
        self.label_8.setMinimumSize(QtCore.QSize(20, 20))
        self.label_8.setMaximumSize(QtCore.QSize(20, 20))
        self.label_8.setStyleSheet("border-image: url(:/iconteste/icons/user.png);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.client_name_label = QtWidgets.QLabel(self.frame_10)
        self.client_name_label.setObjectName("client_name_label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.client_name_label)
        self.label_11 = QtWidgets.QLabel(self.frame_10)
        self.label_11.setMinimumSize(QtCore.QSize(20, 20))
        self.label_11.setMaximumSize(QtCore.QSize(20, 20))
        self.label_11.setStyleSheet("border-image: url(:/iconteste/icons/phone.png);")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.client_tell_label = QtWidgets.QLabel(self.frame_10)
        self.client_tell_label.setObjectName("client_tell_label")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.client_tell_label)
        self.horizontalLayout_6.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.frame_9)
        self.frame_11.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.formLayout_4 = QtWidgets.QFormLayout(self.frame_11)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_13 = QtWidgets.QLabel(self.frame_11)
        self.label_13.setMinimumSize(QtCore.QSize(20, 20))
        self.label_13.setMaximumSize(QtCore.QSize(20, 20))
        self.label_13.setStyleSheet("border-image: url(:/iconteste/icons/truck.png);")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.delicery_place_label = QtWidgets.QLabel(self.frame_11)
        self.delicery_place_label.setObjectName("delicery_place_label")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.delicery_place_label)
        self.label_14 = QtWidgets.QLabel(self.frame_11)
        self.label_14.setObjectName("label_14")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_14)
        self.horizontalLayout_6.addWidget(self.frame_11)
        self.verticalLayout_2.addWidget(self.frame_9)
        self.frame_12 = QtWidgets.QFrame(self.frame_5)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_12)
        self.tableWidget.setStyleSheet("QTableWidget{\n"
"background-color: white;\n"
"color:black;\n"
"border-bottom: 2px solid white;\n"
"border-right: 2px solid white;\n"
"}\n"
"\n"
"QTableView::item {\n"
"border-bottom: 1px solid #d6d9dc;\n"
"border-top: 1px solid #d6d9dc;\n"
"margin-bottom:5px;\n"
"border-radius:10px;\n"
"\n"
"\n"
"\n"
"\n"
"}\n"
"QTableView::section{\n"
"color:blue;\n"
"}")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideRight)
        self.tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 5, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout_5.addWidget(self.tableWidget)
        self.verticalLayout_2.addWidget(self.frame_12)
        self.frame_15 = QtWidgets.QFrame(self.frame_5)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_13 = QtWidgets.QFrame(self.frame_15)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.formLayout_2 = QtWidgets.QFormLayout(self.frame_13)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_15 = QtWidgets.QLabel(self.frame_13)
        self.label_15.setObjectName("label_15")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.subtotal = QtWidgets.QLabel(self.frame_13)
        self.subtotal.setStyleSheet("color:#39fdc5;")
        self.subtotal.setObjectName("subtotal")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.subtotal)
        self.label_16 = QtWidgets.QLabel(self.frame_13)
        self.label_16.setObjectName("label_16")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.desconto = QtWidgets.QLabel(self.frame_13)
        self.desconto.setStyleSheet("color:#cb7efb;")
        self.desconto.setObjectName("desconto")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.desconto)
        self.horizontalLayout_4.addWidget(self.frame_13)
        self.frame_14 = QtWidgets.QFrame(self.frame_15)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.formLayout = QtWidgets.QFormLayout(self.frame_14)
        self.formLayout.setObjectName("formLayout")
        self.label_19 = QtWidgets.QLabel(self.frame_14)
        self.label_19.setObjectName("label_19")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.totalgeral = QtWidgets.QLabel(self.frame_14)
        self.totalgeral.setStyleSheet("color:#39fdc5;")
        self.totalgeral.setObjectName("totalgeral")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.totalgeral)
        self.label_20 = QtWidgets.QLabel(self.frame_14)
        self.label_20.setObjectName("label_20")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.cartodecredito = QtWidgets.QLabel(self.frame_14)
        self.cartodecredito.setStyleSheet("color:#cb7efb;")
        self.cartodecredito.setObjectName("cartodecredito")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cartodecredito)
        self.horizontalLayout_4.addWidget(self.frame_14)
        self.verticalLayout_2.addWidget(self.frame_15)
        self.horizontalLayout_14.addWidget(self.frame_5)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/iconteste/icons/clipboard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon10, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setStyleSheet("")
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.frame_46 = QtWidgets.QFrame(self.tab_3)
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
        self.frame_44 = QtWidgets.QFrame(self.frame_46)
        self.frame_44.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_44.setObjectName("frame_44")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.frame_44)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_44)
        self.pushButton_12.setMinimumSize(QtCore.QSize(170, 30))
        self.pushButton_12.setMaximumSize(QtCore.QSize(180, 16777215))
        self.pushButton_12.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_12.setStyleSheet("\n"
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
        self.pushButton_12.setIcon(icon5)
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_25.addWidget(self.pushButton_12)
        self.verticalLayout_20.addWidget(self.frame_44)
        self.horizontalLayout_30.addWidget(self.frame_46)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/iconteste/icons/group.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_3, icon11, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.frame_52 = QtWidgets.QFrame(self.tab_4)
        self.frame_52.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_52.setObjectName("frame_52")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_52)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_53 = QtWidgets.QFrame(self.frame_52)
        self.frame_53.setStyleSheet("border-radius:15px;")
        self.frame_53.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_53.setObjectName("frame_53")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.frame_53)
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.frame_54 = QtWidgets.QFrame(self.frame_53)
        self.frame_54.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_54.setObjectName("frame_54")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.frame_54)
        self.horizontalLayout_31.setContentsMargins(-1, -1, 0, 0)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.frame_55 = QtWidgets.QFrame(self.frame_54)
        self.frame_55.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_55.setObjectName("frame_55")
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout(self.frame_55)
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.frame_56 = QtWidgets.QFrame(self.frame_55)
        self.frame_56.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_56.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_56.setStyleSheet("background-color:white;\n"
"color:black;")
        self.frame_56.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_56.setObjectName("frame_56")
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout(self.frame_56)
        self.horizontalLayout_33.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.label_35 = QtWidgets.QLabel(self.frame_56)
        self.label_35.setMinimumSize(QtCore.QSize(20, 20))
        self.label_35.setMaximumSize(QtCore.QSize(20, 20))
        self.label_35.setStyleSheet("border-image: url(:/iconteste/icons/loupe (1).png);\n"
"border-radius:12px;")
        self.label_35.setText("")
        self.label_35.setObjectName("label_35")
        self.horizontalLayout_33.addWidget(self.label_35)
        self.line_4 = QtWidgets.QFrame(self.frame_56)
        self.line_4.setMinimumSize(QtCore.QSize(1, 25))
        self.line_4.setMaximumSize(QtCore.QSize(1, 16777215))
        self.line_4.setStyleSheet("background-color:black;    ")
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_33.addWidget(self.line_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_56)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_4.setStyleSheet("background-color:white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color:black;\n"
"border-radius:10px;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_33.addWidget(self.lineEdit_4)
        self.horizontalLayout_32.addWidget(self.frame_56)
        self.comboBox_8 = QtWidgets.QComboBox(self.frame_55)
        self.comboBox_8.setMinimumSize(QtCore.QSize(125, 25))
        self.comboBox_8.setStyleSheet("QComboBox {\n"
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
        self.comboBox_8.setObjectName("comboBox_8")
        self.horizontalLayout_32.addWidget(self.comboBox_8)
        self.horizontalLayout_31.addWidget(self.frame_55)
        self.verticalLayout_22.addWidget(self.frame_54)
        self.frame_57 = QtWidgets.QFrame(self.frame_53)
        self.frame_57.setMinimumSize(QtCore.QSize(700, 0))
        self.frame_57.setMaximumSize(QtCore.QSize(16515165, 16777215))
        self.frame_57.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_57.setObjectName("frame_57")
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout(self.frame_57)
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.tableWidget_6 = QtWidgets.QTableWidget(self.frame_57)
        self.tableWidget_6.setStyleSheet("background-color:white;\n"
"color:black;")
        self.tableWidget_6.setObjectName("tableWidget_6")
        self.tableWidget_6.setColumnCount(0)
        self.tableWidget_6.setRowCount(0)
        self.horizontalLayout_34.addWidget(self.tableWidget_6)
        self.verticalLayout_22.addWidget(self.frame_57)
        self.frame_58 = QtWidgets.QFrame(self.frame_53)
        self.frame_58.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_58.setObjectName("frame_58")
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout(self.frame_58)
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.pushButton_14 = QtWidgets.QPushButton(self.frame_58)
        self.pushButton_14.setMinimumSize(QtCore.QSize(170, 30))
        self.pushButton_14.setMaximumSize(QtCore.QSize(180, 16777215))
        self.pushButton_14.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_14.setStyleSheet("\n"
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
        self.pushButton_14.setIcon(icon5)
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout_35.addWidget(self.pushButton_14)
        self.verticalLayout_22.addWidget(self.frame_58)
        self.verticalLayout_9.addWidget(self.frame_53)
        self.horizontalLayout_36.addWidget(self.frame_52)
        self.tabWidget.addTab(self.tab_4, icon6, "")
        self.verticalLayout_5.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tela Principal"))
        self.pushButton.setText(_translate("MainWindow", "Vendedor"))
        self.label_2.setText(_translate("MainWindow", "   |"))
        self.pushButton_2.setText(_translate("MainWindow", "   Caixa"))
        self.label_3.setText(_translate("MainWindow", "|"))
        self.pushButton_3.setText(_translate("MainWindow", "   Estoque"))
        self.label_4.setText(_translate("MainWindow", "   |"))
        self.pushButton_5.setText(_translate("MainWindow", "   Estatísticas"))
        self.label_6.setText(_translate("MainWindow", "Andrade Esquadrias | ID USER: #0001"))
        self.pushButton_6.setText(_translate("MainWindow", "Bug Report"))
        self.label_17.setText(_translate("MainWindow", "Current Date"))
        self.clientenome.setText(_translate("MainWindow", "Nome:"))
        self.rua.setText(_translate("MainWindow", "Rua:"))
        self.telefone.setText(_translate("MainWindow", "Telefone:"))
        self.citycep.setText(_translate("MainWindow", "Cidade e CEP:"))
        self.label_5.setText(_translate("MainWindow", "Tipo de Processo:"))
        self.comboBox_7.setItemText(0, _translate("MainWindow", "Venda"))
        self.comboBox_7.setItemText(1, _translate("MainWindow", "Troca"))
        self.comboBox_7.setItemText(2, _translate("MainWindow", "Devolução"))
        self.pushButton_13.setText(_translate("MainWindow", "             Escolher Cliente"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Adcionar produtos"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Produtos Adicionados"))
        self.label.setText(_translate("MainWindow", "Descrição Adcional :"))
        self.label_28.setText(_translate("MainWindow", "Frete:"))
        self.label_26.setText(_translate("MainWindow", "Sub-total:"))
        self.label_7.setText(_translate("MainWindow", "Desconto:"))
        self.label_9.setText(_translate("MainWindow", "R$ "))
        self.label_30.setText(_translate("MainWindow", "R$"))
        self.label_29.setText(_translate("MainWindow", "R$"))
        self.label_31.setText(_translate("MainWindow", "Total Geral"))
        self.label_32.setText(_translate("MainWindow", "R$"))
        self.pushButton_10.setText(_translate("MainWindow", "                Concluir Venda"))
        self.pushButton_11.setText(_translate("MainWindow", "Gerar Orçamento"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab_2), _translate("MainWindow", "Nova Venda"))
        self.pushButton_9.setText(_translate("MainWindow", "Caixa atual"))
        self.label_25.setText(_translate("MainWindow", "Periodo"))
        self.label_27.setText(_translate("MainWindow", "Até"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "New Column"))
        self.current_date.setText(_translate("MainWindow", "01/12/2020"))
        self.pushButton_7.setText(_translate("MainWindow", "Enviar"))
        self.pushButton_8.setText(_translate("MainWindow", "Imprimir"))
        self.client_name_label.setText(_translate("MainWindow", "John Lennon"))
        self.client_tell_label.setText(_translate("MainWindow", "1197670-0598"))
        self.delicery_place_label.setText(_translate("MainWindow", "Av. Atlantica -5808 - Pq Atlantica"))
        self.label_14.setText(_translate("MainWindow", "São Paulo - Sp 04805000"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "New Column"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(1, 5)
        item.setText(_translate("MainWindow", "da"))
        item = self.tableWidget.item(2, 5)
        item.setText(_translate("MainWindow", "sd"))
        item = self.tableWidget.item(4, 5)
        item.setText(_translate("MainWindow", "a"))
        item = self.tableWidget.item(5, 5)
        item.setText(_translate("MainWindow", "sda"))
        item = self.tableWidget.item(6, 5)
        item.setText(_translate("MainWindow", "sdas"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_15.setText(_translate("MainWindow", "Sub Total   R$"))
        self.subtotal.setText(_translate("MainWindow", "5000,00"))
        self.label_16.setText(_translate("MainWindow", "Desconto   R$"))
        self.desconto.setText(_translate("MainWindow", "500,00"))
        self.label_19.setText(_translate("MainWindow", "Total Geral:               R$"))
        self.totalgeral.setText(_translate("MainWindow", " 5000,00"))
        self.label_20.setText(_translate("MainWindow", "Cartão de Crédito     R$"))
        self.cartodecredito.setText(_translate("MainWindow", " 500,00"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Pedidos"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Pesquise os clientes"))
        self.pushButton_12.setText(_translate("MainWindow", "          Adcionar novo Cliente"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Clientes"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "pesquise por orçamentos "))
        self.pushButton_14.setText(_translate("MainWindow", "                 Exportar em PDF"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Orçamento"))

import source_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

