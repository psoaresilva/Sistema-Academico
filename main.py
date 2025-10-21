import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget
from login import TelaLogin
from dashboard import Dashboard
from aluno import AlunoWindow
from professor import TelaProfessor
from secretaria import SecretariaWindow


class AppController(QStackedWidget):
    def __init__(self):
        super().__init__()

        self.login = TelaLogin()
        self.dashboard = Dashboard()
        self.area_aluno = AlunoWindow()
        self.area_professor = TelaProfessor()
        self.area_secretaria = SecretariaWindow()

        self.addWidget(self.login)
        self.addWidget(self.dashboard)
        self.addWidget(self.area_aluno)
        self.addWidget(self.area_professor)
        self.addWidget(self.area_secretaria)

        # Conexões
        self.login.login_sucesso.connect(lambda: self.setCurrentWidget(self.dashboard))

        self.dashboard.ir_para_aluno.connect(lambda: self.setCurrentWidget(self.area_aluno))
        self.dashboard.ir_para_professor.connect(lambda: self.setCurrentWidget(self.area_professor))
        self.dashboard.ir_para_secretaria.connect(lambda: self.setCurrentWidget(self.area_secretaria))
        self.dashboard.voltar_login.connect(lambda: self.setCurrentWidget(self.login))

        self.area_aluno.sair.connect(lambda: self.setCurrentWidget(self.dashboard))
        self.area_professor.sair.connect(lambda: self.setCurrentWidget(self.dashboard))
        self.area_secretaria.sair.connect(lambda: self.setCurrentWidget(self.dashboard))

        self.setCurrentWidget(self.login)

    def ir_para_dashboard(self):
        usuario = self.login.input_user.text().strip().lower()
        if usuario == "aluno":
            self.setCurrentWidget(self.area_aluno)
        elif usuario == "professor":
            self.setCurrentWidget(self.area_professor)
        elif usuario == "secretaria":
            self.setCurrentWidget(self.area_secretaria)
        else:
            self.setCurrentWidget(self.dashboard)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = AppController()
    controller.show()
    sys.exit(app.exec_())
