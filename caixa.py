# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_caixa(object):
    def setupUi(self, caixa):
        caixa.setObjectName("caixa")
        caixa.resize(1200, 829)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconteste/icons/ba812f4a-b112-4fa5-96d0-dccd574e3a86.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        caixa.setWindowIcon(icon)
        caixa.setStyleSheet("background-color:#403749;\n"
"color:white;")
        self.centralwidget = QtWidgets.QWidget(caixa)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
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
        self.frame_3.setMinimumSize(QtCore.QSize(450, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(6546545, 16777215))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setContentsMargins(15, -1, 134, 0)
        self.horizontalLayout.setSpacing(44)
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
        icon1.addPixmap(QtGui.QPixmap(":/iconteste/icons/calculator.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        icon2.addPixmap(QtGui.QPixmap(":/iconteste/icons/bill.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setMaximumSize(QtCore.QSize(25, 16777215))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
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
        self.verticalLayout_2.addWidget(self.frame_16)
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
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_5 = QtWidgets.QFrame(self.tab)
        self.frame_5.setStyleSheet("border-radius:10px;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setContentsMargins(14, 0, 14, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_41 = QtWidgets.QFrame(self.frame_5)
        self.frame_41.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_41.setObjectName("frame_41")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.frame_41)
        self.horizontalLayout_23.setContentsMargins(0, -1, 0, 0)
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
        self.verticalLayout_4.addWidget(self.frame_41)
        self.tableclientes = QtWidgets.QTableWidget(self.frame_5)
        self.tableclientes.setStyleSheet("\n"
"QTableWidget::item { \n"
"background-color: #625f66;\n"
"border-radius:0px;\n"
"}\n"
"QTableWidget::item:alternate {\n"
" background-color: #403749;\n"
"border-radius:0px;\n"
"} \n"
"\n"
"QTableWidget{\n"
"color:white;\n"
"border:0px;\n"
"}")
        self.tableclientes.setObjectName("tableclientes")
        self.tableclientes.setColumnCount(0)
        self.tableclientes.setRowCount(0)
        self.tableclientes.horizontalHeader().setVisible(False)
        self.tableclientes.horizontalHeader().setHighlightSections(False)
        self.tableclientes.verticalHeader().setVisible(False)
        self.verticalLayout_4.addWidget(self.tableclientes)
        self.verticalLayout_5.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.tab)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_15 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_15.setMinimumSize(QtCore.QSize(170, 30))
        self.pushButton_15.setMaximumSize(QtCore.QSize(180, 16777215))
        self.pushButton_15.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_15.setStyleSheet("\n"
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
        self.pushButton_15.setObjectName("pushButton_15")
        self.horizontalLayout_4.addWidget(self.pushButton_15)
        self.pushButton_14 = QtWidgets.QPushButton(self.frame_6)
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
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout_4.addWidget(self.pushButton_14)
        self.verticalLayout_5.addWidget(self.frame_6)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_7 = QtWidgets.QFrame(self.tab_2)
        self.frame_7.setStyleSheet("border-radius:10px;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setContentsMargins(18, 0, 14, 0)
        self.verticalLayout_6.setSpacing(21)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_44 = QtWidgets.QFrame(self.frame_7)
        self.frame_44.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_44.setObjectName("frame_44")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.frame_44)
        self.horizontalLayout_24.setContentsMargins(0, -1, 0, 0)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.frame_45 = QtWidgets.QFrame(self.frame_44)
        self.frame_45.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_45.setObjectName("frame_45")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.frame_45)
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.frame_46 = QtWidgets.QFrame(self.frame_45)
        self.frame_46.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_46.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_46.setStyleSheet("background-color:white;\n"
"color:black;")
        self.frame_46.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_46.setObjectName("frame_46")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.frame_46)
        self.horizontalLayout_26.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.label_35 = QtWidgets.QLabel(self.frame_46)
        self.label_35.setMinimumSize(QtCore.QSize(20, 20))
        self.label_35.setMaximumSize(QtCore.QSize(20, 20))
        self.label_35.setStyleSheet("border-image: url(:/iconteste/icons/loupe (1).png);\n"
"border-radius:12px;")
        self.label_35.setText("")
        self.label_35.setObjectName("label_35")
        self.horizontalLayout_26.addWidget(self.label_35)
        self.line_3 = QtWidgets.QFrame(self.frame_46)
        self.line_3.setMinimumSize(QtCore.QSize(1, 25))
        self.line_3.setMaximumSize(QtCore.QSize(1, 16777215))
        self.line_3.setStyleSheet("background-color:black;    ")
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_26.addWidget(self.line_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_46)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_3.setStyleSheet("background-color:white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color:black;\n"
"border-radius:10px;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_26.addWidget(self.lineEdit_3)
        self.horizontalLayout_25.addWidget(self.frame_46)
        self.comboBox_7 = QtWidgets.QComboBox(self.frame_45)
        self.comboBox_7.setMinimumSize(QtCore.QSize(125, 25))
        self.comboBox_7.setStyleSheet("QComboBox {\n"
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
        self.comboBox_7.setObjectName("comboBox_7")
        self.horizontalLayout_25.addWidget(self.comboBox_7)
        self.horizontalLayout_24.addWidget(self.frame_45)
        self.verticalLayout_6.addWidget(self.frame_44)
        self.tabletransac = QtWidgets.QTableWidget(self.frame_7)
        self.tabletransac.setMinimumSize(QtCore.QSize(0, 0))
        self.tabletransac.setStyleSheet("\n"
"QTableWidget::item { \n"
"background-color: #625f66;\n"
"border-radius:0px;\n"
"}\n"
"QTableWidget::item:alternate {\n"
" background-color: #403749;\n"
"border-radius:0px;\n"
"} \n"
"\n"
"QTableWidget{\n"
"color:white;\n"
"border:0px;\n"
"}")
        self.tabletransac.setAlternatingRowColors(True)
        self.tabletransac.setObjectName("tabletransac")
        self.tabletransac.setColumnCount(0)
        self.tabletransac.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tabletransac.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabletransac.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabletransac.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabletransac.setVerticalHeaderItem(3, item)
        self.tabletransac.horizontalHeader().setVisible(False)
        self.tabletransac.horizontalHeader().setCascadingSectionResizes(False)
        self.tabletransac.horizontalHeader().setDefaultSectionSize(103)
        self.tabletransac.horizontalHeader().setHighlightSections(False)
        self.tabletransac.horizontalHeader().setSortIndicatorShown(False)
        self.tabletransac.horizontalHeader().setStretchLastSection(False)
        self.tabletransac.verticalHeader().setVisible(False)
        self.tabletransac.verticalHeader().setCascadingSectionResizes(False)
        self.tabletransac.verticalHeader().setDefaultSectionSize(48)
        self.tabletransac.verticalHeader().setHighlightSections(False)
        self.tabletransac.verticalHeader().setSortIndicatorShown(False)
        self.tabletransac.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_6.addWidget(self.tabletransac)
        self.verticalLayout_7.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.tab_2)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_17 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_17.setMinimumSize(QtCore.QSize(170, 30))
        self.pushButton_17.setMaximumSize(QtCore.QSize(180, 16777215))
        self.pushButton_17.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_17.setStyleSheet("\n"
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
        self.pushButton_17.setObjectName("pushButton_17")
        self.horizontalLayout_5.addWidget(self.pushButton_17)
        self.verticalLayout_7.addWidget(self.frame_8)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        caixa.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(caixa)
        self.statusBar.setObjectName("statusBar")
        caixa.setStatusBar(self.statusBar)

        self.retranslateUi(caixa)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(caixa)

    def retranslateUi(self, caixa):
        _translate = QtCore.QCoreApplication.translate
        caixa.setWindowTitle(_translate("caixa", "Caixa"))
        self.pushButton.setText(_translate("caixa", "Ajustar valor do caixa"))
        self.label_2.setText(_translate("caixa", "   |"))
        self.pushButton_2.setText(_translate("caixa", "Adcionar e remover transações "))
        self.label_3.setText(_translate("caixa", "   |"))
        self.label_6.setText(_translate("caixa", "Andrade Esquadrias | ID USER: #0001"))
        self.pushButton_6.setText(_translate("caixa", "Bug Report"))
        self.lineEdit_2.setPlaceholderText(_translate("caixa", "Vendas finalizadas"))
        self.pushButton_15.setText(_translate("caixa", "Fechar caixa"))
        self.pushButton_14.setText(_translate("caixa", "Resumo financeiro"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("caixa", "Total"))
        self.lineEdit_3.setPlaceholderText(_translate("caixa", "Pesquise pelas transações efetuadas"))
        item = self.tabletransac.verticalHeaderItem(0)
        item.setText(_translate("caixa", "New Row"))
        item = self.tabletransac.verticalHeaderItem(1)
        item.setText(_translate("caixa", "New Row"))
        item = self.tabletransac.verticalHeaderItem(2)
        item.setText(_translate("caixa", "New Row"))
        item = self.tabletransac.verticalHeaderItem(3)
        item.setText(_translate("caixa", "New Row"))
        self.pushButton_17.setText(_translate("caixa", "Adcionar Transação"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("caixa", "Transações"))

import source_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    caixa = QtWidgets.QMainWindow()
    ui = Ui_caixa()
    ui.setupUi(caixa)
    caixa.show()
    sys.exit(app.exec_())

