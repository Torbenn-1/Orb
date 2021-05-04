import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from bug_report import Ui_bug_report
from qmessage import Qmessage
from cadastro import Ui_cadastro


class Ui_MainWindow(object):
    ###### chamada de QDialog
    def bug_report_call(self):
        self.bug_report = QtWidgets.QWidget()
        self.ui = Ui_bug_report()
        self.ui.setupUi(self.bug_report)
        self.bug_report.show()


    ###### chamada de QMainWindow

    def cad_cadastro(self):
        self.cadastro = QtWidgets.QMainWindow()
        self.ui = Ui_cadastro()
        self.ui.setupUi(self.cadastro)
        self.cadastro.show()


    def login(self):
        cargo = str(self.comboBox.currentText())
        password = self.senha.text()
        conn = sqlite3.connect("login.db")
        cursor = conn.cursor()
        query = "SELECT * FROM users WHERE cargo = ? and senha = ?"
        data = cursor.execute(query, (cargo, password))


        if (len(cursor.fetchall()) > 0):
            # dedicar esse espaço a chamada de tela
            print("foi")
        else:

            Qmessage.warning(self)
            print("foi não")


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1110, 758)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconteste/icons/Ativo 16@2x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_3.setStyleSheet("background-color: #281c35;\n"
"color:#ffffff;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame_6)
        self.frame_2.setMaximumSize(QtCore.QSize(30, 30))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setMinimumSize(QtCore.QSize(25, 25))
        self.label.setMaximumSize(QtCore.QSize(25, 25))
        self.label.setStyleSheet("border-image: url(:/iconteste/icons/ba812f4a-b112-4fa5-96d0-dccd574e3a86.jpg);\n"
"border-radius:12px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
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
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_7)
        self.label_2.setMaximumSize(QtCore.QSize(165, 30))
        self.label_2.setObjectName("label_2")

        ##bug report button
        self.horizontalLayout.addWidget(self.label_2)
        self.bug = QtWidgets.QPushButton(self.frame_7)
        self.bug.setMaximumSize(QtCore.QSize(96, 25))
        self.bug.setStyleSheet("\n"
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
        self.bug.setObjectName("bug")
        self.bug.clicked.connect(self.bug_report_call)
        self.horizontalLayout.addWidget(self.bug)


        self.horizontalLayout_2.addWidget(self.frame_7)
        self.verticalLayout_3.addWidget(self.frame_6)
        self.label_23 = QtWidgets.QLabel(self.frame_3)
        self.label_23.setMinimumSize(QtCore.QSize(0, 15))
        self.label_23.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_23.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.0227727, y1:0.557, x2:1, y2:0.551, stop:0.181818 rgba(116, 0, 239, 255), stop:0.903409 rgba(48, 252, 194, 255));")
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.verticalLayout_3.addWidget(self.label_23)
        self.verticalLayout_9.addWidget(self.frame_3)
        self.frame_13 = QtWidgets.QFrame(self.centralwidget)
        self.frame_13.setMinimumSize(QtCore.QSize(501, 0))
        self.frame_13.setStyleSheet("background-color: rgb(98, 95, 102);")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_17 = QtWidgets.QFrame(self.frame_13)
        self.frame_17.setMaximumSize(QtCore.QSize(600, 450))
        self.frame_17.setStyleSheet("background-color:white;\n"
"background-color: rgb(247, 247, 247);")
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_17)
        self.verticalLayout_8.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_12 = QtWidgets.QFrame(self.frame_17)
        self.frame_12.setEnabled(True)
        self.frame_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_5.setContentsMargins(-1, 9, -1, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_18 = QtWidgets.QFrame(self.frame_12)
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_18)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_20 = QtWidgets.QFrame(self.frame_18)
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.deucerto = QtWidgets.QLabel(self.frame_20)
        self.deucerto.setMinimumSize(QtCore.QSize(0, 20))
        self.deucerto.setText("")
        self.deucerto.setObjectName("deucerto")
        self.verticalLayout_2.addWidget(self.deucerto)
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
        self.frame_11 = QtWidgets.QFrame(self.frame_12)
        self.frame_11.setMinimumSize(QtCore.QSize(141, 111))
        self.frame_11.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.frame_11)
        self.label_6.setMinimumSize(QtCore.QSize(180, 100))
        self.label_6.setMaximumSize(QtCore.QSize(180, 16777215))
        self.label_6.setStyleSheet("border-image: url(:/iconteste/icons/bc618214-251e-4c1c-9617-52f5a49d45b0.jpg);")
        self.label_6.setText("")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.verticalLayout_5.addWidget(self.frame_11, 0, QtCore.Qt.AlignHCenter)
        self.frame = QtWidgets.QFrame(self.frame_12)
        self.frame.setMinimumSize(QtCore.QSize(301, 221))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_21 = QtWidgets.QFrame(self.frame)
        self.frame_21.setMaximumSize(QtCore.QSize(225, 16777215))
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_21)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_8 = QtWidgets.QFrame(self.frame_21)
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
        self.comboBox.setMinimumSize(QtCore.QSize(120, 20))
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
        self.verticalLayout_10.addWidget(self.frame_8)
        self.frame_10 = QtWidgets.QFrame(self.frame_21)
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
        self.senha = QtWidgets.QLineEdit(self.frame_10)
        self.senha.setMaximumSize(QtCore.QSize(130, 16777215))
        self.senha.setStyleSheet("border: 0px;")
        self.senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.senha.setObjectName("senha")
        self.horizontalLayout_4.addWidget(self.senha)
        self.verticalLayout_10.addWidget(self.frame_10)
        self.frame_22 = QtWidgets.QFrame(self.frame_21)
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_22)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.iniciar = QtWidgets.QPushButton(self.frame_22)
        self.iniciar.setMinimumSize(QtCore.QSize(100, 30))
        self.iniciar.setMaximumSize(QtCore.QSize(100, 30))
        self.iniciar.setStyleSheet("\n"
"\n"
"QPushButton{\n"
"border: 1px solid black;\n"
"border-radius: 15px;\n"
"color:white;\n"
"background-color: qlineargradient(spread:pad, x1:0.0227727, y1:0.557, x2:1, y2:0.551, stop:0.181818 rgba(116, 0, 239, 255), stop:0.903409 rgba(48, 252, 194, 255));\n"
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
"\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/iconteste/icons/right white arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.iniciar.setIcon(icon1)
        self.iniciar.setObjectName("iniciar")
        self.horizontalLayout_9.addWidget(self.iniciar)
        self.iniciar.clicked.connect(self.login)


        self.verticalLayout_10.addWidget(self.frame_22)
        self.gridLayout_2.addWidget(self.frame_21, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setMinimumSize(QtCore.QSize(171, 20))
        self.label_5.setMaximumSize(QtCore.QSize(171, 20))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.frame)
        self.verticalLayout_8.addWidget(self.frame_12)
        self.frame_14 = QtWidgets.QFrame(self.frame_17)
        self.frame_14.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_6.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_15 = QtWidgets.QFrame(self.frame_14)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_9 = QtWidgets.QLabel(self.frame_15)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_7.addWidget(self.label_9)
        self.horizontalLayout_6.addWidget(self.frame_15)
        self.frame_16 = QtWidgets.QFrame(self.frame_14)
        self.frame_16.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_16)
        self.verticalLayout_6.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")

        #New user Button


        self.nuser = QtWidgets.QPushButton(self.frame_16)
        self.nuser.setMinimumSize(QtCore.QSize(0, 25))
        self.nuser.setMaximumSize(QtCore.QSize(150, 16777215))
        self.nuser.setStyleSheet("\n"
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/iconteste/icons/plus-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nuser.setIcon(icon2)
        self.nuser.setObjectName("nuser")
        self.nuser.clicked.connect(self.cad_cadastro)

        self.verticalLayout_6.addWidget(self.nuser)
        self.horizontalLayout_6.addWidget(self.frame_16)
        self.verticalLayout_8.addWidget(self.frame_14)
        self.horizontalLayout_5.addWidget(self.frame_17)
        self.verticalLayout_9.addWidget(self.frame_13)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.label_2.setText(_translate("MainWindow", "andrade esquadrias id user #8774"))
        self.bug.setText(_translate("MainWindow", "Bug Report"))
        self.label_10.setText(_translate("MainWindow", "Andrade esquadrias"))
        self.label_3.setText(_translate("MainWindow", "Login"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Admin"))
        self.comboBox.setItemText(1, _translate("MainWindow", "T.i"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Vendedor"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Gerência"))
        self.label_4.setText(_translate("MainWindow", "Senha:"))
        self.iniciar.setText(_translate("MainWindow", "Iniciar"))
        self.label_9.setText(_translate("MainWindow", "Orb Powered by Evolcco Versão Beta 0.1"))
        self.nuser.setText(_translate("MainWindow", "cadastrar novo usuario"))

import source_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    MainWindow.showMaximized()

    sys.exit(app.exec_())

