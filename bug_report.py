# -*- coding: utf-8 -*-

from qmessage import Qmessage
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_bug_report(object):
    def send(self):
        cargo = str(self.comboBox.currentText())
        password = self.lineEdit.text()
        conn = sqlite3.connect("login.db")
        cursor = conn.cursor()
        query = "SELECT * FROM users WHERE cargo = ? and senha = ?"
        data = cursor.execute(query, (cargo, password))


        if (len(cursor.fetchall()) > 0):
            # dedicar esse espaço a chamada de tela

            Qmessage.report_sent(self)
            pass
            print("foi")
        else:

            Qmessage.warning(self)
            print("foi não")
            pass


    def setupUi(self, bug_report):
        bug_report.setObjectName("bug_report")
        bug_report.resize(335, 546)
        bug_report.setMinimumSize(QtCore.QSize(335, 546))
        bug_report.setMaximumSize(QtCore.QSize(530, 596))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconteste/icons/Ativo 16@2x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        bug_report.setWindowIcon(icon)
        bug_report.setStyleSheet("background-color:white;")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(bug_report)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_3 = QtWidgets.QFrame(bug_report)
        self.frame_3.setStyleSheet("border-radius:15px;\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.frame_3)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMinimumSize(QtCore.QSize(281, 51))
        self.label.setMaximumSize(QtCore.QSize(281, 51))
        self.label.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_8 = QtWidgets.QFrame(self.frame_4)
        self.frame_8.setMinimumSize(QtCore.QSize(206, 40))
        self.frame_8.setMaximumSize(QtCore.QSize(300, 40))
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
        self.comboBox.setMinimumSize(QtCore.QSize(200, 20))
        self.comboBox.setMaximumSize(QtCore.QSize(200, 16777215))
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
"\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_2.addWidget(self.frame_8)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame_7 = QtWidgets.QFrame(self.frame_3)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame_7)
        self.label_2.setMinimumSize(QtCore.QSize(60, 20))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.frame_7)
        self.plainTextEdit.setStyleSheet("border:1px solid black;\n"
"border-radius:20px;")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_3.addWidget(self.plainTextEdit)
        self.verticalLayout_2.addWidget(self.frame_7)
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setContentsMargins(9, -1, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_10 = QtWidgets.QFrame(self.frame_5)
        self.frame_10.setMinimumSize(QtCore.QSize(206, 40))
        self.frame_10.setMaximumSize(QtCore.QSize(300, 40))
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
        self.horizontalLayout_4.addWidget(self.label_4, 0, QtCore.Qt.AlignLeft)
        self.line_2 = QtWidgets.QFrame(self.frame_10)
        self.line_2.setMinimumSize(QtCore.QSize(0, 40))
        self.line_2.setMaximumSize(QtCore.QSize(1, 16777215))
        self.line_2.setStyleSheet("margin-top:0px;")
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_4.addWidget(self.line_2)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_10)
        self.lineEdit.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit.setMaximumSize(QtCore.QSize(130, 16777215))
        self.lineEdit.setStyleSheet("border: 0px;")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.horizontalLayout_5.addWidget(self.frame_10)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_6.setMinimumSize(QtCore.QSize(140, 30))
        self.pushButton_6.setMaximumSize(QtCore.QSize(145, 25))
        self.pushButton_6.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_6.setStyleSheet("\n"
"\n"
"\n"
"QPushButton{\n"
"border:1px;\n"
"background-color: qlineargradient(spread:pad, x1:0.0227727, y1:0.557, x2:1, y2:0.551, stop:0.181818 rgba(116, 0, 239, 255), stop:0.903409 rgba(48, 252, 194, 255));\n"
"border-radius:15px;\n"
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/iconteste/icons/plus-xxl.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon1)
        self.pushButton_6.clicked.connect(self.send)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_6.addWidget(self.pushButton_6)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.frame_14 = QtWidgets.QFrame(self.frame_3)
        self.frame_14.setMaximumSize(QtCore.QSize(16777215, 25))
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_11.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_9 = QtWidgets.QLabel(self.frame_14)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_11.addWidget(self.label_9, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_2.addWidget(self.frame_14)
        self.horizontalLayout_7.addWidget(self.frame_3)

        self.retranslateUi(bug_report)
        QtCore.QMetaObject.connectSlotsByName(bug_report)

    def retranslateUi(self, bug_report):
        _translate = QtCore.QCoreApplication.translate
        bug_report.setWindowTitle(_translate("bug_report", "Bug Report"))
        self.label.setText(_translate("bug_report", "Reportar um Bug"))
        self.label_3.setText(_translate("bug_report", "Usuário"))
        self.comboBox.setItemText(0, _translate("bug_report", "Admin"))
        self.comboBox.setItemText(1, _translate("bug_report", "T.i"))
        self.comboBox.setItemText(2, _translate("bug_report", "Vendedor"))
        self.comboBox.setItemText(3, _translate("bug_report", "Gerência"))
        self.label_2.setText(_translate("bug_report", "Descrição"))
        self.plainTextEdit.setPlaceholderText(_translate("bug_report", "Diga o que aconteceu"))
        self.label_4.setText(_translate("bug_report", "Senha:"))
        self.pushButton_6.setText(_translate("bug_report", "      Enviar Bug Report"))
        self.label_9.setText(_translate("bug_report", "Andrade Esquadrias ID USER: #0001"))

import source_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    bug_report = QtWidgets.QWidget()
    ui = Ui_bug_report()
    ui.setupUi(bug_report)
    bug_report.show()
    sys.exit(app.exec_())

