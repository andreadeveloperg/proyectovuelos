import sqlite3
from PyQt6 import QtWidgets, uic
import sys


class LoginApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoginApp, self).__init__()
        uic.loadUi('login.ui', self)
        self.login_button.clicked.connect(self.login)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if self.check_credentials(username, password):
            self.show_message(" Inicio de session exitoso ")
        else:
            self.show_message(" Credenciales invalidas")

    def check_credentials(self, username, password):
        conn = sqlite3.connect('db.db')
        cursor = conn.cursor()

        query = "SELECT * FROM usuarios WHERE nombre_usuario=? AND contraseña=? "
        cursor.execute(query(username, password))
        result = cursor.fetchone()
        conn.close()
        return result

    def show_message(self, message):
        msg = QtWidgets.QMessageBox()
        msg.setText(message)
        msg.exec_()


app = QtWidgets.QApplication([])
windows = LoginApp()
windows.show()
sys.exit(app.exec_())
