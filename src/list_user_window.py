from PyQt5 import QtCore, QtWidgets, QtGui, QtGui, uic

from create_user_window import CreateUserWindow
from user_manager import UserManager

INSTRUCTIONS = """O nome do usuário deve ter entre 10 e 100 caracteres.
Todas as 10 imagens de faces devem ser preenchidas.

"""


class ListUserWindow(QtWidgets.QMainWindow):
    def __init__(self, parent):
        super(ListUserWindow, self).__init__()
        uic.loadUi('ui/listuserwindow.ui', self)
        self.main_window = parent
        self.user_manager = UserManager()
        self.focused_user_name = None
        self.init_ui()
    
    def init_ui(self):
        self.fill_user_table()
        self.table_user_list.cellClicked.connect(self.update_focused_user_name)
        self.btn_user_update.clicked.connect(self.update_user)
    
    def fill_user_table(self):
        user_data = self.user_manager.read_user_data()
        self.table_user_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_user_list.setRowCount(len(user_data.keys()))
        
        header = self.table_user_list.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)

        for row, user_name in enumerate(user_data.keys()):
            item_user_name = QtWidgets.QTableWidgetItem(user_name)
            self.table_user_list.setItem(row, 0, item_user_name)

            item_user_birthday = QtWidgets.QTableWidgetItem(user_data[user_name])
            self.table_user_list.setItem(row, 1, item_user_birthday)

    def update_focused_user_name(self, row, column):
        user_name_item = self.table_user_list.item(row, 0)
        self.focused_user_name = user_name_item.text() if user_name_item is not None else None

    def update_user(self):
        if self.focused_user_name is not None:
            self.create_user_window = CreateUserWindow(
                parent=self.main_window, new_user=False, user_name=self.focused_user_name
            )
            self.create_user_window.show()
            self.hide()

