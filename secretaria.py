import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QLineEdit, QScrollArea, QFrame, QDialog, QComboBox, QStackedLayout
)
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal


class EditarUsuarioDialog(QDialog):
    def __init__(self, usuario, callback_confirmar, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Editar Usuário")
        self.setFixedSize(400, 400)
        self.usuario = usuario
        self.callback_confirmar = callback_confirmar

        self.setStyleSheet("""
            QDialog {
                background-color: white;
                border-radius: 10px;
            }
            QLabel {
                font-size: 14px;
            }
            QLineEdit, QComboBox {
                padding: 6px;
                font-size: 13px;
            }
            QPushButton {
                padding: 8px;
                font-size: 14px;
                border-radius: 6px;
            }
        """)

        layout = QVBoxLayout(self)

        logo = QLabel()
        logo.setPixmap(QPixmap("assets/logo.png").scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        logo.setAlignment(Qt.AlignCenter)
        layout.addWidget(logo)

        self.nome_edit = QLineEdit(usuario['nome'])
        layout.addWidget(QLabel("Nome Completo"))
        layout.addWidget(self.nome_edit)

        self.usuario_edit = QLineEdit(usuario['usuario'])
        layout.addWidget(QLabel("Usuário"))
        layout.addWidget(self.usuario_edit)

        self.senha_edit = QLineEdit(usuario['senha'])
        self.senha_edit.setEchoMode(QLineEdit.Password)
        layout.addWidget(QLabel("Senha"))
        layout.addWidget(self.senha_edit)

        self.divisao_combo = QComboBox()
        self.divisao_combo.addItems(["aluno", "professor", "secretaria"])
        self.divisao_combo.setCurrentText(usuario['divisao'])
        layout.addWidget(QLabel("Divisão"))
        layout.addWidget(self.divisao_combo)

        botoes = QHBoxLayout()

        confirmar = QPushButton("Confirmar")
        confirmar.setStyleSheet("background-color: #2E7D32; color: white;")
        confirmar.clicked.connect(self.confirmar)
        botoes.addWidget(confirmar)

        sair = QPushButton("Sair")
        sair.setStyleSheet("background-color: #D32F2F; color: white;")
        sair.clicked.connect(self.reject)
        botoes.addWidget(sair)

        layout.addLayout(botoes)

    def confirmar(self):
        self.usuario['nome'] = self.nome_edit.text()
        self.usuario['usuario'] = self.usuario_edit.text()
        self.usuario['senha'] = self.senha_edit.text()
        self.usuario['divisao'] = self.divisao_combo.currentText()
        self.callback_confirmar()
        self.accept()

class AvisosWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: white;")
        layout_principal = QVBoxLayout(self)
        layout_principal.setContentsMargins(30, 30, 30, 30)
        layout_principal.setSpacing(20)

        titulo = QLabel("📢 Avisos Gerais")
        titulo.setStyleSheet("font-size: 24px; font-weight: bold; color: #333;")
        layout_principal.addWidget(titulo)

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
        layout_principal.addWidget(scroll)

class MatriculaWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout_principal = QVBoxLayout(self)
        layout_principal.setContentsMargins(30, 30, 30, 30)
        layout_principal.setSpacing(20)

        titulo = QLabel("📝 Definir Matrícula")
        titulo.setStyleSheet("font-size: 24px; font-weight: bold; color: #333;")
        layout_principal.addWidget(titulo)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        conteudo = QWidget()
        layout_scroll = QVBoxLayout(conteudo)
        layout_scroll.setSpacing(15)

        instrucoes = QLabel(
            "Aqui você pode definir a matrícula dos alunos por turma.\n"
            "Exemplo: mover aluno de uma turma para outra, ou atualizar seus dados acadêmicos."
        )
        instrucoes.setWordWrap(True)
        instrucoes.setStyleSheet("font-size: 14px; color: #555;")
        layout_scroll.addWidget(instrucoes)

        aviso = QLabel("⚠️ Funcionalidade visual. Integração com banco de dados ainda não implementada.")
        aviso.setStyleSheet("font-size: 13px; color: #c0392b;")
        layout_scroll.addWidget(aviso)

        # Simulação de formulário de matrícula
        for aluno in [
            "Ana Paula", "Carlos Lima", "Fernanda Souza",
            "Amanda Costa Santos", "Rafael Teixeira"
        ]:
            card = QFrame()
            card.setStyleSheet("""
                QFrame {
                    background-color: #f4f4f4;
                    border: 1px solid #ccc;
                    border-radius: 8px;
                    padding: 12px;
                }
            """)
            layout_card = QVBoxLayout(card)
            nome = QLabel(f"Aluno: <b>{aluno}</b>")
            combo = QComboBox()
            combo.addItems(["A1", "B1", "B2", "C1"])
            combo.setStyleSheet("padding: 6px; font-size: 13px;")
            layout_card.addWidget(nome)
            layout_card.addWidget(QLabel("Nova turma:"))
            layout_card.addWidget(combo)
            layout_scroll.addWidget(card)

        scroll.setWidget(conteudo)
        layout_principal.addWidget(scroll)
    
    # Botão de confirmar alterações
        btn_confirmar = QPushButton("💾 Confirmar Alterações")
        btn_confirmar.setStyleSheet("""
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
        btn_confirmar.setCursor(Qt.PointingHandCursor)
        btn_confirmar.clicked.connect(self.confirmar_alteracoes)
        layout_scroll.addWidget(btn_confirmar)

        # Label de feedback oculto
        self.feedback_label = QLabel("")
        self.feedback_label.setStyleSheet("color: green; font-size: 13px;")
        layout_scroll.addWidget(self.feedback_label)

    
    def confirmar_alteracoes(self):
        self.feedback_label.setText("✅ Alterações salvas com sucesso!")





class SecretariaWindow(QWidget):
    sair = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Área da Secretaria")
        self.resize(1280, 700)
        self.usuarios = self.carregar_usuarios()
        self.usuario_selecionado = self.usuarios[0]
        self.init_ui()

    def init_ui(self):
            layout_geral = QHBoxLayout(self)
            layout_geral.setContentsMargins(0, 0, 0, 0)

            # === SIDEBAR ===
            sidebar = QFrame()
            sidebar.setFixedWidth(200)
            sidebar.setStyleSheet("background-color: #5A4CCF; border-right: 2px solid #888;")
            layout_sidebar = QVBoxLayout(sidebar)
            layout_sidebar.setContentsMargins(15, 20, 15, 15)

            avatar = QLabel()
            avatar.setPixmap(QPixmap("assets/user.png").scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            avatar.setAlignment(Qt.AlignCenter)
            layout_sidebar.addWidget(avatar)

            nome_label = QLabel("Usuário: <b>julia.silva</b><br>Cargo: secretaria")
            nome_label.setAlignment(Qt.AlignCenter)
            nome_label.setStyleSheet("color: white; font-size: 13px;")
            layout_sidebar.addWidget(nome_label)

            self.btn_avisos = self.criar_botao("Avisos", "📢", callback=lambda: self.trocar_tela("avisos"))
            self.btn_usuarios = self.criar_botao("Administrar Usuários", "👥", destaque=True, callback=lambda: self.trocar_tela("usuarios"))
            self.btn_periodo = self.criar_botao("Período Letivo", "📆", callback=lambda: self.trocar_tela("periodo"))
            self.btn_matricula = self.criar_botao("Definir Matrícula", "📝", callback=lambda: self.trocar_tela("matricula"))
            
            layout_sidebar.addWidget(self.btn_periodo)
            layout_sidebar.addWidget(self.btn_matricula)
            layout_sidebar.addWidget(self.btn_avisos)
            layout_sidebar.addWidget(self.btn_usuarios)
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

            # === ÁREA CENTRAL COM STACK ===
            conteudo = QHBoxLayout()
            conteudo.setContentsMargins(20, 20, 20, 20)

            self.stack = QStackedLayout()

            # === TELA DE USUÁRIOS ===
            self.widget_usuarios = QWidget()
            self.widget_usuarios_layout = QVBoxLayout(self.widget_usuarios)

            self.busca = QLineEdit()
            self.busca.setPlaceholderText("🔍 Pesquisar")
            self.busca.setStyleSheet("padding: 10px; font-size: 14px; border: 1px solid #ccc; border-radius: 6px;")
            self.widget_usuarios_layout.addWidget(self.busca)

            scroll = QScrollArea()
            scroll.setWidgetResizable(True)
            self.lista_widget = QWidget()
            self.lista_layout = QVBoxLayout(self.lista_widget)
            self.lista_layout.setSpacing(10)
            scroll.setWidget(self.lista_widget)
            self.widget_usuarios_layout.addWidget(scroll)

            self.stack.addWidget(self.widget_usuarios)

            # === TELA DE AVISOS ===
            self.avisos_widget = AvisosWidget()
            self.stack.addWidget(self.avisos_widget)

            # === TELA PERÍODO LETIVO ===
            self.widget_periodo = QWidget()
            layout_periodo = QVBoxLayout(self.widget_periodo)
            layout_periodo.setContentsMargins(30, 30, 30, 30)
            layout_periodo.setSpacing(20)

            titulo_periodo = QLabel("📆 Calendário Letivo")
            titulo_periodo.setStyleSheet("font-size: 24px; font-weight: bold;")
            layout_periodo.addWidget(titulo_periodo)

            scroll_periodo = QScrollArea()
            scroll_periodo.setWidgetResizable(True)
            scroll_area_conteudo = QWidget()
            layout_scroll = QVBoxLayout(scroll_area_conteudo)
            layout_scroll.setSpacing(20)

            for i in range(1, 13):
                img = QLabel()
                img.setPixmap(QPixmap(f"assets/periodo-{i}.png").scaledToWidth(900, Qt.SmoothTransformation))
                layout_scroll.addWidget(img)

            scroll_periodo.setWidget(scroll_area_conteudo)
            layout_periodo.addWidget(scroll_periodo)
            self.stack.addWidget(self.widget_periodo)

            # === TELA DEFINIR MATRÍCULA ===
            self.widget_matricula = QWidget()
            layout_matricula = QVBoxLayout(self.widget_matricula)
            layout_matricula.setContentsMargins(30, 30, 30, 30)
            layout_matricula.setSpacing(20)

            titulo_matricula = QLabel("📝 Definir Matrícula")
            titulo_matricula.setStyleSheet("font-size: 24px; font-weight: bold;")
            layout_matricula.addWidget(titulo_matricula)

            # Aqui você pode personalizar o conteúdo da matrícula depois (formulários, opções etc)
            mensagem = QLabel("Funcionalidade em construção.")
            mensagem.setStyleSheet("font-size: 16px; color: #666;")
            layout_matricula.addWidget(mensagem)

            self.stack.addWidget(self.widget_matricula)
            self.matricula_widget = MatriculaWidget()
            self.stack.addWidget(self.matricula_widget)

            conteudo.addLayout(self.stack, 2)

            # === PAINEL LATERAL DE DETALHES ===
            self.painel = QFrame()
            self.painel.setFixedWidth(220)
            self.painel.setMaximumHeight(350)
            self.painel.setStyleSheet("""
                QFrame {
                    background-color: #5A4CCF;
                    border-radius: 10px;
                    border-left: 2px solid #888;
                    margin-right: 10px;
                    color: white;
                }
            """)
            self.layout_detalhes = QVBoxLayout(self.painel)
            self.layout_detalhes.setContentsMargins(16, 16, 16, 16)
            self.layout_detalhes.setSpacing(8)
            conteudo.addWidget(self.painel)

            layout_geral.addLayout(conteudo)

            self.popular_lista()
            self.atualizar_painel(self.usuario_selecionado)


    

    def limpar_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)
            else:
                sublayout = item.layout()
                if sublayout is not None:
                    self.limpar_layout(sublayout)

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

    def criar_card_usuario(self, usuario):
        card = QFrame()
        card.setStyleSheet("background-color: #6A5ACD; border-radius: 8px;")
        layout = QHBoxLayout(card)
        layout.setContentsMargins(10, 10, 10, 10)

        avatar = QLabel()
        avatar.setPixmap(QPixmap("assets/user.png").scaled(36, 36, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        layout.addWidget(avatar)

        info = QVBoxLayout()
        nome = QLabel(f"<b>{usuario['nome']}</b>  <span style='color:#ccc'>@{usuario['usuario']}</span>")
        nome.setStyleSheet("color: white;")
        turma = QLabel(f"{usuario['cargo']}")
        turma.setStyleSheet("color: white; font-size: 12px;")
        info.addWidget(nome)
        info.addWidget(turma)
        layout.addLayout(info)

        layout.addStretch()

        btn_edit = QPushButton()
        btn_edit.setIcon(QIcon("assets/editar.png"))
        btn_edit.setStyleSheet("background-color: white; border-radius: 4px; padding: 6px;")
        btn_edit.clicked.connect(lambda: self.abrir_edicao(usuario))
        layout.addWidget(btn_edit)

        btn_del = QPushButton()
        btn_del.setIcon(QIcon("assets/lixeira.png"))
        btn_del.setStyleSheet("background-color: white; border-radius: 4px; padding: 6px;")
        btn_del.clicked.connect(lambda: self.excluir_usuario(usuario, card))
        layout.addWidget(btn_del)

        card.mousePressEvent = lambda event: self.atualizar_painel(usuario)
        return card

    def atualizar_painel(self, usuario):
        self.usuario_selecionado = usuario
        self.limpar_layout(self.layout_detalhes)

        foto = QLabel()
        foto.setPixmap(QPixmap("assets/user.png").scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        foto.setAlignment(Qt.AlignCenter)
        self.layout_detalhes.addWidget(foto)

        nome = QLabel(f"<b>{usuario['nome']}</b>")
        nome.setAlignment(Qt.AlignCenter)
        nome.setStyleSheet("color: white; font-size: 15px;")
        self.layout_detalhes.addWidget(nome)

        usuario_tag = QLabel(f"@{usuario['usuario']}")
        usuario_tag.setAlignment(Qt.AlignCenter)
        usuario_tag.setStyleSheet("color: white; font-size: 13px;")
        self.layout_detalhes.addWidget(usuario_tag)

        cargo = QLabel(usuario['divisao'])
        cargo.setAlignment(Qt.AlignCenter)
        cargo.setStyleSheet("color: white; font-size: 13px;")
        self.layout_detalhes.addWidget(cargo)

        turma = QLabel(usuario['cargo'])
        turma.setAlignment(Qt.AlignCenter)
        turma.setStyleSheet("color: white; font-size: 13px;")
        self.layout_detalhes.addWidget(turma)

        senha = QLabel(f"<b>Senha:</b> {usuario['senha']}")
        senha.setAlignment(Qt.AlignCenter)
        senha.setStyleSheet("color: white; font-size: 13px;")
        self.layout_detalhes.addWidget(senha)

        botoes = QHBoxLayout()
        editar = QPushButton()
        editar.setIcon(QIcon("assets/editar.png"))
        editar.setToolTip("Editar")
        editar.setStyleSheet("background: white; border-radius: 6px; padding: 8px;")
        editar.clicked.connect(lambda: self.abrir_edicao(usuario))

        excluir = QPushButton()
        excluir.setIcon(QIcon("assets/lixeira.png"))
        excluir.setToolTip("Excluir")
        excluir.setStyleSheet("background: white; border-radius: 6px; padding: 8px;")
        excluir.clicked.connect(lambda: self.excluir_usuario(usuario))

        botoes.addWidget(editar)
        botoes.addWidget(excluir)
        self.layout_detalhes.addLayout(botoes)

    def abrir_edicao(self, usuario):
        dialog = EditarUsuarioDialog(usuario, self.recarregar_lista, self)
        dialog.exec_()

    def excluir_usuario(self, usuario, card=None):
        self.usuarios.remove(usuario)
        self.recarregar_lista()

    def recarregar_lista(self):
        for i in reversed(range(self.lista_layout.count())):
            widget = self.lista_layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)
        self.popular_lista()
        self.atualizar_painel(self.usuarios[0] if self.usuarios else {})

    def popular_lista(self):
        for usuario in self.usuarios:
            card = self.criar_card_usuario(usuario)
            self.lista_layout.addWidget(card)

    def carregar_usuarios(self):
            return sorted([
                {"nome": "Ana Paula", "usuario": "ana", "turma": "A1", "senha": "1234", "divisao": "aluno", "cargo": "Turma: A1"},
                {"nome": "Carlos Lima", "usuario": "carlos", "turma": "A1", "senha": "1234", "divisao": "aluno", "cargo": "Turma: A1"},
                {"nome": "Fernanda Souza", "usuario": "fernanda", "turma": "A1", "senha": "1234", "divisao": "aluno", "cargo": "Turma: A1"},
                {"nome": "Rafael Teixeira", "usuario": "rafael", "turma": "A1", "senha": "1234", "divisao": "aluno", "cargo": "Turma: A1"},
                {"nome": "Vitória Martins", "usuario": "vitoria", "turma": "A1", "senha": "1234", "divisao": "aluno", "cargo": "Turma: A1"},
                {"nome": "Amanda Costa Santos", "usuario": "amanda", "turma": "B2", "senha": "1234", "divisao": "aluno", "cargo": "Turma: B2"},
                {"nome": "André Luiz Ramos", "usuario": "andre", "turma": "B2", "senha": "1234", "divisao": "aluno", "cargo": "Turma: B2"},
                {"nome": "Andréia Santos Silva", "usuario": "andreia", "turma": "B2", "senha": "1234", "divisao": "aluno", "cargo": "Turma: B2"},
                {"nome": "Beatrice Unknown", "usuario": "beatrice", "turma": "A1", "senha": "1234", "divisao": "aluno", "cargo": "Turma: A1"},
                {"nome": "Bruna Oliveira Silva", "usuario": "bruna", "turma": "B2", "senha": "1234", "divisao": "aluno", "cargo": "Turma: B2"},
            ], key=lambda u: u['nome'])

    def trocar_tela(self, nome):
        self.set_destaque(self.btn_avisos, False)
        self.set_destaque(self.btn_usuarios, False)
        self.set_destaque(self.btn_periodo, False)
        self.set_destaque(self.btn_matricula, False)

        if nome == "avisos":
            self.stack.setCurrentWidget(self.avisos_widget)
            self.painel.hide()
            self.set_destaque(self.btn_avisos, True)
        elif nome == "usuarios":
            self.stack.setCurrentWidget(self.widget_usuarios)
            self.painel.show()
            self.set_destaque(self.btn_usuarios, True)
        elif nome == "periodo":
            self.stack.setCurrentWidget(self.widget_periodo)
            self.painel.hide()
            self.set_destaque(self.btn_periodo, True)
        elif nome == "matricula":
            self.stack.setCurrentWidget(self.matricula_widget)
            self.painel.hide()
            self.set_destaque(self.btn_avisos, False)
            self.set_destaque(self.btn_usuarios, False)
            self.set_destaque(self.btn_periodo, False)
            self.set_destaque(self.btn_matricula, True)



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
    win = SecretariaWindow()
    win.show()
    sys.exit(app.exec_())
