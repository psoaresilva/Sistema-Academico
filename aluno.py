import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QScrollArea, QFrame, QStackedLayout, QComboBox
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal


class RematriculaAluno(QWidget):
    def __init__(self):
        super().__init__()
        layout_principal = QVBoxLayout(self)
        layout_principal.setContentsMargins(30, 30, 30, 30)
        layout_principal.setSpacing(20)

        titulo = QLabel("📝 Rematrícula Online")
        titulo.setStyleSheet("font-size: 24px; font-weight: bold; color: #333;")
        layout_principal.addWidget(titulo)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        conteudo = QWidget()
        layout_scroll = QVBoxLayout(conteudo)
        layout_scroll.setSpacing(15)

        info = QLabel(
            "A rematrícula está disponível até 30/06/2025.\n\n"
            "Selecione sua turma para o próximo semestre e clique em confirmar."
        )
        info.setStyleSheet("font-size: 14px; color: #555;")
        info.setWordWrap(True)
        layout_scroll.addWidget(info)

        # Card visual
        card = QFrame()
        card.setStyleSheet("""
            QFrame {
                background-color: #f9f9f9;
                border: 1px solid #ccc;
                border-radius: 8px;
                padding: 20px;
            }
        """)
        card_layout = QVBoxLayout(card)
        card_layout.setSpacing(10)

        self.combo_turma = QComboBox()
        self.combo_turma.addItems(["3º Ano A", "3º Ano B", "4º Ano A", "4º Ano B"])
        self.combo_turma.setStyleSheet("padding: 8px; font-size: 14px;")
        card_layout.addWidget(QLabel("Escolha sua turma:"))
        card_layout.addWidget(self.combo_turma)

        self.btn_confirmar = QPushButton("💾 Confirmar Matrícula")
        self.btn_confirmar.setStyleSheet("""
            QPushButton {
                background-color: #6A5ACD;
                color: white;
                font-size: 14px;
                padding: 10px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #5a4ccf;
            }
        """)
        self.btn_confirmar.clicked.connect(self.confirmar_matricula)
        card_layout.addWidget(self.btn_confirmar)

        self.feedback_label = QLabel("")
        self.feedback_label.setStyleSheet("font-size: 13px; color: green;")
        card_layout.addWidget(self.feedback_label)

        layout_scroll.addWidget(card)
        scroll.setWidget(conteudo)
        layout_principal.addWidget(scroll)

    def confirmar_matricula(self):
        turma = self.combo_turma.currentText()
        self.feedback_label.setText(f"✅ Matrícula confirmada para {turma} com sucesso!")

class AvisosAluno(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)

        titulo = QLabel("📢 Avisos Gerais")
        titulo.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(titulo)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        conteudo = QWidget()
        layout_conteudo = QVBoxLayout(conteudo)
        layout_conteudo.setSpacing(15)

        avisos = [
            "📅 As aulas do segundo semestre começam no dia 05/08.",
            "⚠️ O prazo final para rematrícula é 30/06.",
            "📢 Evento cultural dia 20/07. Participação obrigatória para todas as turmas.",
        ]

        for texto in avisos:
            card = QFrame()
            card.setStyleSheet("""
                QFrame {
                    background-color: #f9f9f9;
                    border: 1px solid #ccc;
                    border-radius: 8px;
                }
                QLabel {
                    font-size: 15px;
                    padding: 10px;
                }
            """)
            layout_card = QVBoxLayout(card)
            label = QLabel(texto)
            label.setWordWrap(True)
            layout_card.addWidget(label)
            layout_conteudo.addWidget(card)

        scroll.setWidget(conteudo)
        layout.addWidget(scroll)


class PeriodoLetivoAluno(QWidget):
    def __init__(self):
        super().__init__()

        layout_periodo = QVBoxLayout(self)
        layout_periodo.setContentsMargins(30, 30, 30, 30)
        layout_periodo.setSpacing(20)

        titulo = QLabel("📆 Calendário Letivo")
        titulo.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout_periodo.addWidget(titulo)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        container = QWidget()
        layout_scroll = QVBoxLayout(container)
        layout_scroll.setSpacing(20)

        for i in range(1, 13):
            img = QLabel()
            img.setPixmap(QPixmap(f"assets/periodo-{i}.png").scaledToWidth(900, Qt.SmoothTransformation))
            layout_scroll.addWidget(img)

        scroll.setWidget(container)
        layout_periodo.addWidget(scroll)


class NotasFaltasAluno(QWidget):
    def __init__(self):
        super().__init__()

        layout_principal = QVBoxLayout(self)
        layout_principal.setContentsMargins(30, 30, 30, 30)
        layout_principal.setSpacing(20)

        titulo = QLabel("📊 Notas e Faltas")
        titulo.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout_principal.addWidget(titulo)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        container = QWidget()
        layout_scroll = QVBoxLayout(container)
        layout_scroll.setSpacing(20)

        disciplinas = {
            "Desenvolvimento Web": {"nota": 9.0, "faltas": 2},
            "Banco de Dados": {"nota": 7.0, "faltas": 1},
            "Engenharia de Software": {"nota": 5.5, "faltas": 0},
            "Programação Mobile": {"nota": 8.8, "faltas": 3},
        }

        for nome, dados in disciplinas.items():
            card = QFrame()
            card.setStyleSheet("""
                QFrame {
                    background-color: #f9f9f9;
                    border: 1px solid #ccc;
                    border-radius: 12px;
                }
            """)
            layout_card = QVBoxLayout(card)
            layout_card.setContentsMargins(16, 16, 16, 16)
            layout_card.setSpacing(10)

            nome_disciplina = QLabel(f"<b>{nome}</b>")
            nome_disciplina.setStyleSheet("font-size: 16px;")
            layout_card.addWidget(nome_disciplina)

            # Nota com cor de status
            nota_valor = dados["nota"]
            if nota_valor < 6:
                cor_nota = "#c0392b"  # vermelho
            elif nota_valor < 7.5:
                cor_nota = "#f39c12"  # laranja
            else:
                cor_nota = "#27ae60"  # verde

            nota = QLabel(f"Nota final: {nota_valor}")
            nota.setStyleSheet(f"font-size: 14px; color: {cor_nota};")
            layout_card.addWidget(nota)

            # Faltas com alerta
            faltas_valor = dados["faltas"]
            cor_faltas = "#c0392b" if faltas_valor >= 3 else "#333"
            faltas = QLabel(f"Faltas: {faltas_valor}")
            faltas.setStyleSheet(f"font-size: 14px; color: {cor_faltas};")
            layout_card.addWidget(faltas)

            layout_scroll.addWidget(card)

        scroll.setWidget(container)
        layout_principal.addWidget(scroll)




class AtividadesAluno(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)

        titulo = QLabel("📚 Atividades Cadastradas")
        titulo.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(titulo)

        atividades = [
            "Lista de exercícios de Programação - até 21/06",
            "Resumo de Engenharia de Software",
            "Desafio de Mobile com Flutter"
        ]

        for atividade in atividades:
            card = QFrame()
            card.setStyleSheet("""
                QFrame {
                    background-color: #f4f4f4;
                    border-radius: 8px;
                    padding: 10px;
                    border: 1px solid #ccc;
                }
                QLabel {
                    font-size: 14px;
                }
            """)
            layout_card = QVBoxLayout(card)
            layout_card.addWidget(QLabel(atividade))
            layout.addWidget(card)


class AlunoWindow(QWidget):
    sair = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Área do Aluno")
        self.resize(1000, 700)
        self.init_ui()

    def init_ui(self):
        layout_geral = QHBoxLayout(self)
        layout_geral.setContentsMargins(0, 0, 0, 0)

        # Sidebar
        sidebar = QFrame()
        sidebar.setFixedWidth(200)
        sidebar.setStyleSheet("background-color: #5A4CCF;")
        layout_sidebar = QVBoxLayout(sidebar)
        layout_sidebar.setContentsMargins(15, 20, 15, 15)

        avatar = QLabel()
        avatar.setPixmap(QPixmap("assets/user.png").scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        avatar.setAlignment(Qt.AlignCenter)
        layout_sidebar.addWidget(avatar)

        info_label = QLabel("Usuário: <b>joaosilva123</b><br>Turma: <b>3º Ano A</b>")
        info_label.setAlignment(Qt.AlignCenter)
        info_label.setStyleSheet("color: white; font-size: 13px;")
        layout_sidebar.addWidget(info_label)

        self.btn_avisos = self.criar_botao("Avisos", "📢", callback=lambda: self.trocar_tela("avisos"))
        self.btn_periodo = self.criar_botao("Período Letivo", "📆", destaque=True, callback=lambda: self.trocar_tela("periodo"))
        self.btn_rematricula = self.criar_botao("Rematrícula", "📄", callback=lambda: self.trocar_tela("rematricula"))
        self.btn_notas = self.criar_botao("Nota/Falta", "📊", callback=lambda: self.trocar_tela("notas"))
        self.btn_atividades = self.criar_botao("Atividades", "📚", callback=lambda: self.trocar_tela("atividades"))

        for btn in [self.btn_avisos, self.btn_periodo, self.btn_rematricula, self.btn_notas, self.btn_atividades]:
            layout_sidebar.addWidget(btn)

        layout_sidebar.addStretch()

        btn_sair = QPushButton("↩️  Sair")
        btn_sair.clicked.connect(self.sair.emit)
        btn_sair.setStyleSheet("""
            QPushButton {
                background-color: #D32F2F;
                color: white;
                font-size: 13px;
                border-radius: 6px;
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #b71c1c;
            }
        """)
        layout_sidebar.addWidget(btn_sair)

        layout_geral.addWidget(sidebar)

        # Conteúdo central com stack
        conteudo = QVBoxLayout()
        conteudo.setContentsMargins(20, 20, 20, 20)
        self.stack = QStackedLayout()

        self.page_avisos = AvisosAluno()
        self.page_periodo = PeriodoLetivoAluno()
        self.page_matricula = RematriculaAluno()
        self.stack.addWidget(self.page_matricula)
        self.page_notas = NotasFaltasAluno()
        self.page_atividades = AtividadesAluno()

        for pagina in [self.page_avisos, self.page_periodo, self.page_matricula, self.page_notas, self.page_atividades]:
            self.stack.addWidget(pagina)

        conteudo.addLayout(self.stack)
        layout_geral.addLayout(conteudo)

        self.trocar_tela("periodo")

    def criar_botao(self, texto, icone, destaque=False, callback=None):
        cor = "#F9A825" if destaque else "#6A5ACD"
        fonte = "black" if destaque else "white"
        btn = QPushButton(f"{icone}  {texto}")
        btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {cor};
                color: {fonte};
                font-size: 13px;
                padding: 8px 12px;
                border: none;
                border-radius: 6px;
                text-align: left;
            }}
            QPushButton:hover {{
                background-color: {'#fbc02d' if destaque else '#5a4ccf'};
            }}
        """)
        if callback:
            btn.clicked.connect(callback)
        return btn

    def trocar_tela(self, nome):
        self.set_destaque(self.btn_avisos, False)
        self.set_destaque(self.btn_periodo, False)
        self.set_destaque(self.btn_rematricula, False)
        self.set_destaque(self.btn_notas, False)
        self.set_destaque(self.btn_atividades, False)

        if nome == "avisos":
            self.stack.setCurrentWidget(self.page_avisos)
            self.set_destaque(self.btn_avisos, True)
        elif nome == "periodo":
            self.stack.setCurrentWidget(self.page_periodo)
            self.set_destaque(self.btn_periodo, True)
        elif nome == "rematricula":
            self.stack.setCurrentWidget(self.page_matricula)
            self.set_destaque(self.btn_rematricula, True)
        elif nome == "notas":
            self.stack.setCurrentWidget(self.page_notas)
            self.set_destaque(self.btn_notas, True)
        elif nome == "atividades":
            self.stack.setCurrentWidget(self.page_atividades)
            self.set_destaque(self.btn_atividades, True)

    def set_destaque(self, botao, ativo):
        cor = "#F9A825" if ativo else "#6A5ACD"
        fonte = "black" if ativo else "white"
        botao.setStyleSheet(f"""
            QPushButton {{
                background-color: {cor};
                color: {fonte};
                font-size: 13px;
                padding: 8px 12px;
                border: none;
                border-radius: 6px;
                text-align: left;
            }}
            QPushButton:hover {{
                background-color: {'#fbc02d' if ativo else '#5a4ccf'};
            }}
        """)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = AlunoWindow()
    win.show()
    sys.exit(app.exec_())