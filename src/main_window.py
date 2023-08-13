import os
import sys

from PyQt5 import QtWidgets, uic

execution_dir = os.getcwd()
sys.path.append(execution_dir)

from training_logs_window import StartTrainingNetworkWindow
from create_user_window import CreateUserWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('ui/mainwindow.ui', self)
        self.init_ui()

        self.show()
    
    def init_ui(self):
        self.btn_train_network.clicked.connect(self.start_train_network)
        self.action_user_create.triggered.connect(self.start_create_user)
    
    def start_train_network(self):
        self.start_train_network_window = StartTrainingNetworkWindow(self)
        self.start_train_network_window.show()
        self.hide()
    
    def start_create_user(self):
        self.start_create_user_window = CreateUserWindow(self)
        self.start_create_user_window.show()
        self.hide()


app = QtWidgets.QApplication([])
window = MainWindow()
app.exec_()