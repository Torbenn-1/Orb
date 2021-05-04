from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtGui

class Qmessage(object):
    def warning(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(":(")
        msg.setInformativeText(
            'Credêciais incorretas, caso você não tenha um cadastro contate um administrador e ele fará seu cadastro')
        msg.setWindowTitle("Ops")
        msg.exec_()

    def report_sent(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowIcon(QtGui.QIcon(':/iconteste/icons/Ativo 16@2x.png'))

        msg.setText(":)")
        msg.setInformativeText(
            'Seu report foi enviado com sucesso, Já vamos colocar nossos programadores para consertar esse defeito. Pode fechar essa tela e usar o sistema, assim que o erro for corrigido avisaremos.')
        msg.setWindowTitle("Enviado")
        msg.exec_()

    def warning2(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(":(")
        msg.setWindowIcon(QtGui.QIcon(':/iconteste/icons/Ativo 16@2x.png'))

        msg.setInformativeText('Opa, Parece que você esqueceu de completar algum campo, verifique e tente de novo.')
        msg.setWindowTitle("Ops")
        msg.exec_()

    def great(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowIcon(QtGui.QIcon(':/iconteste/icons/Ativo 16@2x.png'))

        msg.setText(":)")
        msg.setInformativeText(
            'Seu Cadastro foi efetuado com sucesso, agora é só retornar para a tela de Login e já pode usar o Orb a vontande.')
        msg.setWindowTitle("Sucesso")
        msg.exec_()