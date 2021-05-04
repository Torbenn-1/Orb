# -*- coding: utf-8 -*-

from login import Ui_MainWindow
from bug_report import Ui_bug_report

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):

        ###### chamada de QDialog
    def bug_report_call(self):
        self.bug_report = QtWidgets.QWidget()
        self.ui = Ui_bug_report()
        self.ui.setupUi(self.bug_report)
        self.bug_report.show()


    def login(self):
        self.login = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.login)
        self.login.show()


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1109, 828)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconteste/icons/Ativo 16@2x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background-color:#433A4D;\n"
"color:white;")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_3 = QtWidgets.QFrame(Form)
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
        self.Logincadastro.clicked.connect(self.login)
        self.verticalLayout.addWidget(self.Logincadastro)
        self.horizontalLayout_3.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_12)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3.addWidget(self.frame_5)
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
        self.frame_11 = QtWidgets.QFrame(Form)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_11)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_8 = QtWidgets.QFrame(self.frame_11)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_22 = QtWidgets.QFrame(self.frame_8)
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_22)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_6 = QtWidgets.QFrame(self.frame_22)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_23 = QtWidgets.QFrame(self.frame_6)
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_23)
        self.horizontalLayout_9.setSpacing(7)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame_14 = QtWidgets.QFrame(self.frame_23)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_9.addWidget(self.frame_14)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_23)
        self.pushButton_7.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton_7.setMaximumSize(QtCore.QSize(100, 30))
        self.pushButton_7.setStyleSheet("\n"
"QPushButton{\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"background-color: white;\n"
"color:black;\n"
"\n"
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
"border-color: #281c35;\n"
"}\n"
"")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.bug_report_call)
        self.horizontalLayout_9.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_23)
        self.pushButton_8.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton_8.setMaximumSize(QtCore.QSize(100, 30))
        self.pushButton_8.setStyleSheet("\n"
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
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_9.addWidget(self.pushButton_8)
        self.frame_15 = QtWidgets.QFrame(self.frame_23)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_9.addWidget(self.frame_15)
        self.verticalLayout_8.addWidget(self.frame_23)
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.frame_7)
        self.label_5.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.verticalLayout_8.addWidget(self.frame_7)
        self.verticalLayout_7.addWidget(self.frame_6)
        self.frame_10 = QtWidgets.QFrame(self.frame_22)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_7.addWidget(self.frame_10)
        self.frame_9 = QtWidgets.QFrame(self.frame_22)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_7.addWidget(self.frame_9)
        self.verticalLayout_4.addWidget(self.frame_22)
        self.frame = QtWidgets.QFrame(self.frame_8)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 199)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setMinimumSize(QtCore.QSize(550, 350))
        self.label_4.setStyleSheet("image: url(:/iconteste/icons/404.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.verticalLayout_4.addWidget(self.frame)
        self.gridLayout.addWidget(self.frame_8, 0, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.frame_11)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "404"))
        self.Logincadastro.setText(_translate("Form", "Login/ Cadastro"))
        self.label_2.setText(_translate("Form", "          andrade esquadrias id user #8774"))
        self.pushButton_7.setText(_translate("Form", "Bug Report"))
        self.pushButton_8.setText(_translate("Form", "Retornar ao Inicio"))
        self.label_5.setText(_translate("Form", "Não encontramos o que você buscava :("))
import source_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
