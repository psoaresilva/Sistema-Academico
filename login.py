from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QFrame
)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt, pyqtSignal

class TelaLogin(QWidget):
    login_sucesso = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login - Sistema Acadêmico")
        self.resize(1000, 600)
        self.init_ui()

    def init_ui(self):
        self.background = QLabel(self)
        self.background.setPixmap(QPixmap("assets/background.png"))
        self.background.setScaledContents(False)
        self.update_background()

        self.box = QFrame(self)
        self.box.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 20px;
                border: 1px solid #ccc;
            }
        """)
        self.box.setFixedSize(400, 480)
        self.centralizar_box()

        layout = QVBoxLayout(self.box)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)

        logo = QLabel()
        logo.setPixmap(QPixmap("assets/logo.png").scaled(80, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        logo.setAlignment(Qt.AlignCenter)
        layout.addWidget(logo)

        titulo = QLabel("Sistema Acadêmico")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-size: 18px; font-weight: bold; color: #333;")
        layout.addWidget(titulo)

        self.input_user = QLineEdit()
        self.input_user.setPlaceholderText("Usuário")
        self.input_user.setStyleSheet("""
            QLineEdit {
                padding: 10px; font-size: 14px;
                border-radius: 8px; border: 1px solid #ccc;
                background-color: #f7f7f7;
            }
            QLineEdit:focus {
                border: 1px solid #6A5ACD; background-color: #fff;
            }
        """)
        layout.addWidget(self.input_user)

        self.input_pass = QLineEdit()
        self.input_pass.setPlaceholderText("Senha")
        self.input_pass.setEchoMode(QLineEdit.Password)
        self.input_pass.setStyleSheet(self.input_user.styleSheet())
        layout.addWidget(self.input_pass)

        self.label_erro = QLabel("")
        self.label_erro.setStyleSheet("color: #D32F2F; font-size: 13px;")
        self.label_erro.setAlignment(Qt.AlignCenter)
        self.label_erro.setVisible(False)
        layout.addWidget(self.label_erro)

        self.btn_login = QPushButton("Entrar")
        self.btn_login.setCursor(Qt.PointingHandCursor)
        self.btn_login.setStyleSheet("""
            QPushButton {
                background-color: #6A5ACD; color: white;
                font-size: 15px; padding: 12px; border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #5a4ccf;
            }
        """)
        self.btn_login.clicked.connect(self.verificar_login)
        layout.addWidget(self.btn_login)

        rodape = QLabel("© 2025 Sistema Acadêmico")
        rodape.setAlignment(Qt.AlignCenter)
        rodape.setStyleSheet("color: #aaa; font-size: 11px;")
        layout.addWidget(rodape)

        self.setFont(QFont("Segoe UI", 10))

    def update_background(self):
        pixmap = QPixmap("assets/background.png")
        if not pixmap.isNull():
            pixmap = pixmap.scaled(self.width(), self.height(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
            self.background.setPixmap(pixmap)
            self.background.setGeometry(0, 0, self.width(), self.height())

    def centralizar_box(self):
        self.box.move(
            (self.width() - self.box.width()) // 2,
            (self.height() - self.box.height()) // 2
        )

    def resizeEvent(self, event):
        self.update_background()
        self.centralizar_box()

    def verificar_login(self):
        usuario = self.input_user.text().strip()
        senha = self.input_pass.text().strip()

        if usuario == "" or senha == "":
            self.label_erro.setText("Preencha todos os campos.")
            self.label_erro.setVisible(True)
            return

        if (usuario == "aluno" and senha == "123") or \
        (usuario == "professor" and senha == "123") or \
        (usuario == "secretaria" and senha == "123"):
            self.label_erro.setVisible(False)
            self.login_sucesso.emit()  # <---- IMPORTANTE
        else:
            self.label_erro.setText("Usuário ou senha inválidos.")
            self.label_erro.setVisible(True)

