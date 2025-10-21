from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QFrame
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt, pyqtSignal


class Dashboard(QWidget):
    ir_para_aluno = pyqtSignal()
    ir_para_professor = pyqtSignal()
    ir_para_secretaria = pyqtSignal()
    voltar_login = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dashboard - Sistema Acadêmico")
        self.resize(960, 600)
        self.init_ui()

    def init_ui(self):
        self.background = QLabel(self)
        self.background.setPixmap(QPixmap("assets/background.png"))
        self.background.setScaledContents(False)
        self.update_background()

        layout_geral = QVBoxLayout(self)
        layout_geral.setContentsMargins(0, 0, 0, 0)
        layout_geral.setSpacing(0)

        box = QFrame()
        box.setStyleSheet("""
            QFrame {
                background-color: rgba(255, 255, 255, 0.94);
                border-radius: 16px;
            }
        """)
        box.setFixedSize(600, 480)
        self.centralizar_box(box)

        layout_box = QVBoxLayout(box)
        layout_box.setContentsMargins(30, 30, 30, 30)
        layout_box.setSpacing(25)

        logo = QLabel()
        logo.setPixmap(QPixmap("assets/logo.png").scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        logo.setAlignment(Qt.AlignCenter)
        layout_box.addWidget(logo)

        titulo = QLabel("Bem-vindo ao Sistema Acadêmico")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-size: 20px; font-weight: bold; color: #333;")
        layout_box.addWidget(titulo)

        botoes_layout = QVBoxLayout()
        botoes_layout.setSpacing(15)

        self.btn_aluno = QPushButton("👨‍🎓 Acessar como Aluno")
        self.btn_professor = QPushButton("👨‍🏫 Acessar como Professor")
        self.btn_secretaria = QPushButton("🏫 Acessar como Secretaria")
        self.btn_voltar_login = QPushButton("↩️ Voltar ao Login")

        for btn in [self.btn_aluno, self.btn_professor, self.btn_secretaria, self.btn_voltar_login]:
            btn.setCursor(Qt.PointingHandCursor)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #6A5ACD;
                    color: white;
                    font-size: 15px;
                    padding: 12px;
                    border-radius: 10px;
                }
                QPushButton:hover {
                    background-color: #5a4ccf;
                }
            """)
            botoes_layout.addWidget(btn)

        layout_box.addLayout(botoes_layout)
        layout_geral.addWidget(box, alignment=Qt.AlignCenter)

        # Conexões
        self.btn_aluno.clicked.connect(self.ir_para_aluno.emit)
        self.btn_professor.clicked.connect(self.ir_para_professor.emit)
        self.btn_secretaria.clicked.connect(self.ir_para_secretaria.emit)
        self.btn_voltar_login.clicked.connect(self.voltar_login.emit)

        self.setFont(QFont("Segoe UI", 10))

    def centralizar_box(self, widget):
        screen_width = self.width()
        screen_height = self.height()
        widget.move((screen_width - widget.width()) // 2, (screen_height - widget.height()) // 2)

    def resizeEvent(self, event):
        self.update_background()
        self.centralizar_box(self.findChild(QFrame))

    def update_background(self):
        full_pixmap = QPixmap("assets/background.png")
        if not full_pixmap.isNull():
            pixmap = full_pixmap.scaled(self.width(), self.height(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
            self.background.setPixmap(pixmap)
            self.background.setGeometry(0, 0, self.width(), self.height())
