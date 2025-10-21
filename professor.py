import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QStackedLayout, QFrame, QScrollArea, QLineEdit, QDateEdit, QCheckBox, QComboBox
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtCore import pyqtSignal


class AvisosProfessor(QWidget):
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
            "📅 Lançamento de atividades deve ser feito até 23/06.",
            "📢 Reunião pedagógica no dia 24/06 às 14h na sala dos professores.",
            "⚠️ Encerramento das notas será em 30/06.",
            "📚 Evento de integração docente dia 01/07 com participação obrigatória."
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


class PeriodoLetivoProfessor(QWidget):
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


class ChamadaOnlineWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.alunos_por_turma = {
            "A1": [
                "Ana Paula", "Carlos Lima", "Fernanda Souza", "João Pedro", "Mariana Silva",
                "Felipe Costa", "Laura Oliveira", "Gabriel Santos", "Camila Rocha", "Vinícius Dias",
                "Juliana Mendes", "Ricardo Almeida"
            ],
            "B2": [
                "Amanda Costa Santos", "Rafael Teixeira", "André Luiz", "Beatriz Soares", "Luan Martins",
                "Jéssica Vieira", "Bruno Castro", "Isabela Ribeiro", "Danilo Freitas", "Tatiane Lopes",
                "Murilo Lima", "Vanessa Torres"
            ],
            "C3": [
                "Lucas Oliveira", "Marina Silva", "Pedro Santos", "Larissa Gomes", "Eduardo Nunes",
                "Gabriela Monteiro", "Roberto Peixoto", "Daniela Barros", "Thiago Campos", "Nicole Xavier",
                "Caio Rezende", "Helena Cruz"
            ],
            "D4": [
                "Beatrice Unknown", "Vitória Martins", "Fernando Moura", "Paula Andrade", "Caio Neves",
                "Renata Lima", "Henrique Duarte", "Letícia Souza", "Vinícius Barreto", "Luana Sales",
                "Matheus Azevedo", "Sabrina Couto"
            ]
        }


        self.layout_principal = QVBoxLayout(self)
        self.layout_principal.setContentsMargins(30, 30, 30, 30)
        self.layout_principal.setSpacing(20)

        titulo = QLabel("🧾 Chamada Online")
        titulo.setStyleSheet("font-size: 24px; font-weight: bold; color: #333;")
        self.layout_principal.addWidget(titulo)

        # Turmas
        layout_turmas = QHBoxLayout()
        self.botoes_turma = {}
        for turma, cor in zip(["A1", "B2", "C3", "D4"], ["#7e57c2", "#536dfe", "#fbc02d", "#66bb6a"]):
            btn = QPushButton(turma)
            btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {cor};
                    color: white;
                    border-radius: 10px;
                    padding: 10px 20px;
                    font-weight: bold;
                    font-size: 14px;
                }}
                QPushButton:hover {{
                    background-color: #333;
                }}
            """)
            btn.clicked.connect(lambda checked, t=turma: self.carregar_alunos(t))
            layout_turmas.addWidget(btn)
            self.botoes_turma[turma] = btn

        self.layout_principal.addLayout(layout_turmas)

        # Botão de marcar todos
        self.btn_todos_presentes = QPushButton("✅ Marcar Todos como Presentes")
        self.btn_todos_presentes.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-size: 13px;
                padding: 8px 16px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #43A047;
            }
        """)
        self.btn_todos_presentes.clicked.connect(self.marcar_todos_presentes)
        self.layout_principal.addWidget(self.btn_todos_presentes)


        # Área de alunos com scroll
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll_area_conteudo = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_area_conteudo)
        self.scroll_layout.setSpacing(10)
        self.scroll.setWidget(self.scroll_area_conteudo)
        self.layout_principal.addWidget(self.scroll)

        # Botão de confirmar chamada
        self.btn_confirmar = QPushButton("💾 Confirmar Chamada")
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
        self.btn_confirmar.clicked.connect(self.confirmar_chamada)
        self.layout_principal.addWidget(self.btn_confirmar)

        # Feedback visual
        self.feedback_label = QLabel("")
        self.feedback_label.setStyleSheet("color: green; font-size: 13px;")
        self.layout_principal.addWidget(self.feedback_label)

        self.carregar_alunos("A1")  # Carrega a primeira turma por padrão

    def carregar_alunos(self, turma):
        for i in reversed(range(self.scroll_layout.count())):
            widget = self.scroll_layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)

        self.checkboxes = []
        for aluno in self.alunos_por_turma.get(turma, []):
            linha = QFrame()
            linha.setStyleSheet("background: white; border: 1px solid #ccc; border-radius: 6px;")
            layout_linha = QHBoxLayout(linha)
            layout_linha.setContentsMargins(10, 5, 10, 5)
            nome_label = QLabel(aluno)
            nome_label.setStyleSheet("font-size: 14px;")
            layout_linha.addWidget(nome_label)
            layout_linha.addStretch()
            chk = QCheckBox("Presente")
            layout_linha.addWidget(chk)
            self.checkboxes.append(chk)
            self.scroll_layout.addWidget(linha)

    def confirmar_chamada(self):
        presentes = sum(1 for chk in self.checkboxes if chk.isChecked())
        self.feedback_label.setText(f"✅ Chamada registrada com sucesso! {presentes} presente(s).")
    
    def marcar_todos_presentes(self):
        for chk in self.checkboxes:
            chk.setChecked(True)
        self.feedback_label.setText("✅ Todos os alunos foram marcados como presentes.")

class AtribuirNotasWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.alunos_por_turma = {
            "A1": ["Ana Paula", "Carlos Lima", "Fernanda Souza", "Rafael Teixeira", "Vitória Martins", "Beatrice Unknown"],
            "B2": ["Amanda Costa", "André Luiz", "Andréia Santos", "Bruna Oliveira", "Gabriel Lima", "Larissa Ramos"]
        }

        self.layout_principal = QVBoxLayout(self)
        self.layout_principal.setContentsMargins(30, 30, 30, 30)
        self.layout_principal.setSpacing(20)

        titulo = QLabel("📝 Atribuir Notas e Faltas")
        titulo.setStyleSheet("font-size: 24px; font-weight: bold; color: #333;")
        self.layout_principal.addWidget(titulo)

        # Seletor de turma
        self.combo_turma = QComboBox()
        self.combo_turma.addItems(self.alunos_por_turma.keys())
        self.combo_turma.setStyleSheet("padding: 8px; font-size: 14px;")
        self.combo_turma.currentTextChanged.connect(self.carregar_alunos)
        self.layout_principal.addWidget(self.combo_turma)

        # Área scrollável com os alunos
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll_area_conteudo = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_area_conteudo)
        self.scroll_layout.setSpacing(10)
        self.scroll.setWidget(self.scroll_area_conteudo)
        self.layout_principal.addWidget(self.scroll)

        # Botão de confirmação
        self.btn_confirmar = QPushButton("💾 Confirmar Notas")
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
        self.btn_confirmar.clicked.connect(self.confirmar_notas)
        self.layout_principal.addWidget(self.btn_confirmar)

        # Label de feedback
        self.feedback = QLabel("")
        self.feedback.setStyleSheet("color: green; font-size: 13px;")
        self.layout_principal.addWidget(self.feedback)

        self.carregar_alunos("A1")

    def carregar_alunos(self, turma):
        # Limpa o layout
        for i in reversed(range(self.scroll_layout.count())):
            widget = self.scroll_layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)

        self.inputs = []

        for aluno in self.alunos_por_turma[turma]:
            card = QFrame()
            card.setStyleSheet("""
                QFrame {
                    background-color: #f9f9f9;
                    border: 1px solid #ccc;
                    border-radius: 8px;
                    padding: 12px;
                }
            """)
            layout_card = QHBoxLayout(card)

            # Nome do aluno
            nome = QLabel(aluno)
            nome.setStyleSheet("font-size: 14px; font-weight: bold;")
            layout_card.addWidget(nome)
            layout_card.addStretch()

            # Layout vertical para os campos
            campos_layout = QVBoxLayout()

            # Campo de Nota
            label_nota = QLabel("Nota:")
            label_nota.setStyleSheet("font-size: 13px; color: #555;")
            nota_input = QLineEdit()
            nota_input.setPlaceholderText("0.0")
            nota_input.setFixedWidth(60)
            nota_input.setStyleSheet("padding: 6px; font-size: 13px;")

            # Campo de Faltas
            label_faltas = QLabel("Faltas:")
            label_faltas.setStyleSheet("font-size: 13px; color: #555;")
            faltas_input = QLineEdit()
            faltas_input.setPlaceholderText("0")
            faltas_input.setFixedWidth(60)
            faltas_input.setStyleSheet("padding: 6px; font-size: 13px;")

            # Agrupando os campos
            campos_layout.addWidget(label_nota)
            campos_layout.addWidget(nota_input)
            campos_layout.addSpacing(8)
            campos_layout.addWidget(label_faltas)
            campos_layout.addWidget(faltas_input)

            layout_card.addLayout(campos_layout)

            # Salva os inputs
            self.inputs.append((aluno, nota_input, faltas_input))
            self.scroll_layout.addWidget(card)


    def confirmar_notas(self):
        notas = []
        for aluno, nota_input, faltas_input in self.inputs:
            nota = nota_input.text()
            faltas = faltas_input.text()
            notas.append((aluno, nota, faltas))
        self.feedback.setText("✅ Notas e faltas registradas com sucesso!")


class LancarAtividadesWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)

        titulo = QLabel("📝 Lançar Atividades")
        titulo.setStyleSheet("font-size: 24px; font-weight: bold; color: #333;")
        layout.addWidget(titulo)

        form = QFrame()
        form.setStyleSheet("""
            QFrame {
                background-color: #f9f9f9;
                border: 1px solid #ccc;
                border-radius: 10px;
                padding: 20px;
            }
        """)
        form_layout = QVBoxLayout(form)
        form_layout.setSpacing(15)

        self.titulo_edit = QLineEdit()
        self.titulo_edit.setPlaceholderText("Título da atividade")
        self.titulo_edit.setStyleSheet("padding: 10px; font-size: 14px;")
        form_layout.addWidget(self.titulo_edit)

        self.descricao_edit = QLineEdit()
        self.descricao_edit.setPlaceholderText("Descrição")
        self.descricao_edit.setStyleSheet("padding: 10px; font-size: 14px;")
        form_layout.addWidget(self.descricao_edit)

        datas_layout = QHBoxLayout()

        self.data_abertura = QDateEdit()
        self.data_abertura.setCalendarPopup(True)
        self.data_abertura.setDate(QDate.currentDate())
        self.data_abertura.setStyleSheet("padding: 8px; font-size: 14px;")
        datas_layout.addWidget(QLabel("Data de Abertura:"))
        datas_layout.addWidget(self.data_abertura)

        self.data_fechamento = QDateEdit()
        self.data_fechamento.setCalendarPopup(True)
        self.data_fechamento.setDate(QDate.currentDate())
        self.data_fechamento.setStyleSheet("padding: 8px; font-size: 14px;")
        datas_layout.addWidget(QLabel("Data de Fechamento:"))
        datas_layout.addWidget(self.data_fechamento)

        form_layout.addLayout(datas_layout)

        self.btn_confirmar = QPushButton("Confirmar")
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
        self.btn_confirmar.clicked.connect(self.confirmar)
        form_layout.addWidget(self.btn_confirmar)

        self.feedback = QLabel("")
        self.feedback.setStyleSheet("color: green; font-size: 13px;")
        form_layout.addWidget(self.feedback)

        layout.addWidget(form)

    def confirmar(self):
        self.feedback.setText("✅ Atividade cadastrada com sucesso!")


class TelaProfessor(QWidget):
    sair = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Área do Professor")
        self.resize(1200, 700)
        self.init_ui()

    def init_ui(self):
        layout_geral = QHBoxLayout(self)
        layout_geral.setContentsMargins(0, 0, 0, 0)

        sidebar = QFrame()
        sidebar.setFixedWidth(200)
        sidebar.setStyleSheet("background-color: #5A4CCF;")
        layout_sidebar = QVBoxLayout(sidebar)
        layout_sidebar.setContentsMargins(15, 20, 15, 15)

        avatar = QLabel()
        avatar.setPixmap(QPixmap("assets/user.png").scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        avatar.setAlignment(Qt.AlignCenter)
        layout_sidebar.addWidget(avatar)

        nome_label = QLabel("Usuário: <b>professor123</b><br>Cargo: Professor")
        nome_label.setAlignment(Qt.AlignCenter)
        nome_label.setStyleSheet("color: white; font-size: 13px;")
        layout_sidebar.addWidget(nome_label)

        self.btn_avisos = self.criar_botao("Avisos", "📢", callback=lambda: self.trocar_tela("avisos"))
        self.btn_periodo = self.criar_botao("Período Letivo", "📆", callback=lambda: self.trocar_tela("periodo"))
        self.btn_notas = self.criar_botao("Atribuir Notas", "📝", callback=lambda: self.trocar_tela("notas"))
        self.btn_atividades = self.criar_botao("Lançar Atividades", "📚", callback=lambda: self.trocar_tela("atividades"))
        self.btn_chamada = self.criar_botao("Chamada Online", "📋", callback=lambda: self.trocar_tela("chamada"))

        for btn in [self.btn_avisos, self.btn_periodo, self.btn_notas, self.btn_atividades, self.btn_chamada]:
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

        conteudo = QVBoxLayout()
        conteudo.setContentsMargins(20, 20, 20, 20)

        self.stack = QStackedLayout()

        self.page_avisos = AvisosProfessor()
        self.page_avisos.setStyleSheet("font-size: 24px; font-weight: bold;")
        self.page_periodo = PeriodoLetivoProfessor()
        self.page_periodo.setStyleSheet("font-size: 24px; font-weight: bold;")
        self.page_notas = AtribuirNotasWidget()
        self.page_notas.setStyleSheet("font-size: 24px; font-weight: bold;")
        self.page_chamada = ChamadaOnlineWidget()
        self.page_chamada.setStyleSheet("font-size: 24px; font-weight: bold;")
        self.page_atividades = LancarAtividadesWidget()

        for page in [self.page_avisos, self.page_periodo, self.page_notas, self.page_chamada, self.page_atividades]:
            self.stack.addWidget(page)

        conteudo.addLayout(self.stack)
        layout_geral.addLayout(conteudo)

        self.trocar_tela("atividades")

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
        mapeamento = {
            "avisos": self.page_avisos,
            "periodo": self.page_periodo,
            "notas": self.page_notas,
            "atividades": self.page_atividades,
            "chamada": self.page_chamada
        }
        self.stack.setCurrentWidget(mapeamento[nome])
        self.set_destaque(self.btn_avisos, nome == "avisos")
        self.set_destaque(self.btn_periodo, nome == "periodo")
        self.set_destaque(self.btn_notas, nome == "notas")
        self.set_destaque(self.btn_atividades, nome == "atividades")
        self.set_destaque(self.btn_chamada, nome == "chamada")

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
    win = TelaProfessor()
    win.show()
    sys.exit(app.exec_())
