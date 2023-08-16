# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createuserwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CreateUserWindow(object):
    def setupUi(self, CreateUserWindow):
        CreateUserWindow.setObjectName("CreateUserWindow")
        CreateUserWindow.resize(1281, 820)
        CreateUserWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(CreateUserWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gpbox_user_data = QtWidgets.QGroupBox(self.centralwidget)
        self.gpbox_user_data.setGeometry(QtCore.QRect(10, 10, 500, 150))
        self.gpbox_user_data.setObjectName("gpbox_user_data")
        self.txt_user_name = QtWidgets.QLineEdit(self.gpbox_user_data)
        self.txt_user_name.setGeometry(QtCore.QRect(55, 30, 425, 25))
        self.txt_user_name.setText("")
        self.txt_user_name.setObjectName("txt_user_name")
        self.date_user_birthday = QtWidgets.QDateEdit(self.gpbox_user_data)
        self.date_user_birthday.setGeometry(QtCore.QRect(175, 60, 130, 25))
        self.date_user_birthday.setObjectName("date_user_birthday")
        self.lbl_user_name = QtWidgets.QLabel(self.gpbox_user_data)
        self.lbl_user_name.setGeometry(QtCore.QRect(0, 30, 50, 25))
        self.lbl_user_name.setObjectName("lbl_user_name")
        self.lbl_user_birthday = QtWidgets.QLabel(self.gpbox_user_data)
        self.lbl_user_birthday.setGeometry(QtCore.QRect(0, 60, 170, 25))
        self.lbl_user_birthday.setObjectName("lbl_user_birthday")
        self.btn_cancel = QtWidgets.QPushButton(self.gpbox_user_data)
        self.btn_cancel.setGeometry(QtCore.QRect(0, 100, 80, 25))
        self.btn_cancel.setObjectName("btn_cancel")
        self.btn_input_rfid = QtWidgets.QPushButton(self.gpbox_user_data)
        self.btn_input_rfid.setGeometry(QtCore.QRect(100, 100, 125, 25))
        self.btn_input_rfid.setObjectName("btn_input_rfid")
        self.txt_user_rfid = QtWidgets.QLineEdit(self.gpbox_user_data)
        self.txt_user_rfid.setEnabled(False)
        self.txt_user_rfid.setGeometry(QtCore.QRect(360, 60, 120, 25))
        self.txt_user_rfid.setText("")
        self.txt_user_rfid.setObjectName("txt_user_rfid")
        self.lbl_user_rfid = QtWidgets.QLabel(self.gpbox_user_data)
        self.lbl_user_rfid.setGeometry(QtCore.QRect(315, 60, 50, 25))
        self.lbl_user_rfid.setObjectName("lbl_user_rfid")
        self.btn_capture_faces = QtWidgets.QPushButton(self.gpbox_user_data)
        self.btn_capture_faces.setGeometry(QtCore.QRect(250, 100, 130, 25))
        self.btn_capture_faces.setObjectName("btn_capture_faces")
        self.btn_save = QtWidgets.QPushButton(self.gpbox_user_data)
        self.btn_save.setGeometry(QtCore.QRect(400, 100, 80, 25))
        self.btn_save.setObjectName("btn_save")

        self.qpbox_create_instructions = QtWidgets.QGroupBox(self.centralwidget)
        self.qpbox_create_instructions.setGeometry(QtCore.QRect(550, 10, 601, 126))
        self.qpbox_create_instructions.setObjectName("qpbox_create_instructions")
        self.txt_instructions_to_create = QtWidgets.QTextEdit(self.qpbox_create_instructions)
        self.txt_instructions_to_create.setGeometry(QtCore.QRect(0, 30, 600, 95))
        self.txt_instructions_to_create.setReadOnly(True)
        self.txt_instructions_to_create.setObjectName("txt_instructions_to_create")
        self.gpbox_faces = QtWidgets.QGroupBox(self.centralwidget)
        self.gpbox_faces.setGeometry(QtCore.QRect(10, 150, 1161, 581))
        self.gpbox_faces.setObjectName("gpbox_faces")
        
        self.gpbox_face_normal = QtWidgets.QGroupBox(self.gpbox_faces)
        self.gpbox_face_normal.setGeometry(QtCore.QRect(0, 20, 221, 271))
        self.gpbox_face_normal.setObjectName("gpbox_face_normal")
        self.label_face_normal = QtWidgets.QLabel(self.gpbox_face_normal)
        self.label_face_normal.setGeometry(QtCore.QRect(0, 30, 210, 150))
        self.label_face_normal.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_face_normal.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_face_normal.setObjectName("label_face_normal")
        self.btn_face_normal_clear = QtWidgets.QPushButton(self.gpbox_face_normal)
        self.btn_face_normal_clear.setGeometry(QtCore.QRect(0, 190, 100, 25))
        self.btn_face_normal_clear.setObjectName("btn_face_normal_clear")
        self.btn_face_normal_capture = QtWidgets.QPushButton(self.gpbox_face_normal)
        self.btn_face_normal_capture.setGeometry(QtCore.QRect(104, 190, 105, 25))
        self.btn_face_normal_capture.setObjectName("btn_face_normal_capture")
        
        self.gpbox_face_rightlight = QtWidgets.QGroupBox(self.gpbox_faces)
        self.gpbox_face_rightlight.setGeometry(QtCore.QRect(0, 300, 221, 271))
        self.gpbox_face_rightlight.setObjectName("gpbox_face_rightlight")
        self.label_face_rightlight = QtWidgets.QLabel(self.gpbox_face_rightlight)
        self.label_face_rightlight.setGeometry(QtCore.QRect(0, 30, 210, 150))
        self.label_face_rightlight.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_face_rightlight.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_face_rightlight.setObjectName("label_face_rightlight")
        self.btn_face_rightlight_clear = QtWidgets.QPushButton(self.gpbox_face_rightlight)
        self.btn_face_rightlight_clear.setGeometry(QtCore.QRect(0, 190, 100, 25))
        self.btn_face_rightlight_clear.setObjectName("btn_face_rightlight_clear")
        self.btn_face_rightlight_capture = QtWidgets.QPushButton(self.gpbox_face_rightlight)
        self.btn_face_rightlight_capture.setGeometry(QtCore.QRect(105, 190, 105, 25))
        self.btn_face_rightlight_capture.setObjectName("btn_face_rightlight_capture")

        self.gpbox_face_leftlight = QtWidgets.QGroupBox(self.gpbox_faces)
        self.gpbox_face_leftlight.setGeometry(QtCore.QRect(240, 300, 221, 271))
        self.gpbox_face_leftlight.setObjectName("gpbox_face_leftlight")
        self.label_face_leftlight = QtWidgets.QLabel(self.gpbox_face_leftlight)
        self.label_face_leftlight.setGeometry(QtCore.QRect(0, 30, 210, 150))
        self.label_face_leftlight.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_face_leftlight.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_face_leftlight.setObjectName("label_face_leftlight")
        self.btn_face_leftlight_clear = QtWidgets.QPushButton(self.gpbox_face_leftlight)
        self.btn_face_leftlight_clear.setGeometry(QtCore.QRect(0, 190, 100, 25))
        self.btn_face_leftlight_clear.setObjectName("btn_face_leftlight_clear")
        self.btn_face_leftlight_capture = QtWidgets.QPushButton(self.gpbox_face_leftlight)
        self.btn_face_leftlight_capture.setGeometry(QtCore.QRect(104, 190, 105, 25))
        self.btn_face_leftlight_capture.setObjectName("btn_face_leftlight_capture")
    
        self.gpbox_face_sleepy = QtWidgets.QGroupBox(self.gpbox_faces)
        self.gpbox_face_sleepy.setGeometry(QtCore.QRect(240, 20, 221, 271))
        self.gpbox_face_sleepy.setObjectName("gpbox_face_sleepy")
        self.label_face_sleepy = QtWidgets.QLabel(self.gpbox_face_sleepy)
        self.label_face_sleepy.setGeometry(QtCore.QRect(0, 30, 210, 150))
        self.label_face_sleepy.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_face_sleepy.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_face_sleepy.setObjectName("label_face_sleepy")
        self.btn_face_sleepy_clear = QtWidgets.QPushButton(self.gpbox_face_sleepy)
        self.btn_face_sleepy_clear.setGeometry(QtCore.QRect(0, 190, 100, 25))
        self.btn_face_sleepy_clear.setObjectName("btn_face_sleepy_clear")
        self.btn_face_sleepy_capture = QtWidgets.QPushButton(self.gpbox_face_sleepy)
        self.btn_face_sleepy_capture.setGeometry(QtCore.QRect(105, 190, 105, 25))
        self.btn_face_sleepy_capture.setObjectName("btn_face_sleepy_capture")

        self.gpbox_face_happy = QtWidgets.QGroupBox(self.gpbox_faces)
        self.gpbox_face_happy.setGeometry(QtCore.QRect(470, 20, 221, 271))
        self.gpbox_face_happy.setObjectName("gpbox_face_happy")
        self.label_face_happy = QtWidgets.QLabel(self.gpbox_face_happy)
        self.label_face_happy.setGeometry(QtCore.QRect(0, 30, 210, 150))
        self.label_face_happy.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_face_happy.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_face_happy.setObjectName("label_face_happy")
        self.btn_face_happy_clear = QtWidgets.QPushButton(self.gpbox_face_happy)
        self.btn_face_happy_clear.setGeometry(QtCore.QRect(0, 190, 100, 25))
        self.btn_face_happy_clear.setObjectName("btn_face_happy_clear")
        self.btn_face_happy_capture = QtWidgets.QPushButton(self.gpbox_face_happy)
        self.btn_face_happy_capture.setGeometry(QtCore.QRect(105, 190, 105, 25))
        self.btn_face_happy_capture.setObjectName("btn_face_happy_capture")
    
        self.gpbox_face_sad = QtWidgets.QGroupBox(self.gpbox_faces)
        self.gpbox_face_sad.setGeometry(QtCore.QRect(470, 300, 221, 271))
        self.gpbox_face_sad.setObjectName("gpbox_face_sad")
        self.label_face_sad = QtWidgets.QLabel(self.gpbox_face_sad)
        self.label_face_sad.setGeometry(QtCore.QRect(0, 30, 210, 150))
        self.label_face_sad.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_face_sad.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_face_sad.setObjectName("label_face_sad")
        self.btn_face_sad_clear = QtWidgets.QPushButton(self.gpbox_face_sad)
        self.btn_face_sad_clear.setGeometry(QtCore.QRect(0, 190, 100, 25))
        self.btn_face_sad_clear.setObjectName("btn_face_sad_clear")
        self.btn_face_sad_capture = QtWidgets.QPushButton(self.gpbox_face_sad)
        self.btn_face_sad_capture.setGeometry(QtCore.QRect(105, 190, 105, 25))
        self.btn_face_sad_capture.setObjectName("btn_face_sad_capture")

        self.gpbox_face_surprised = QtWidgets.QGroupBox(self.gpbox_faces)
        self.gpbox_face_surprised.setGeometry(QtCore.QRect(930, 20, 221, 271))
        self.gpbox_face_surprised.setStyleSheet("")
        self.gpbox_face_surprised.setFlat(False)
        self.gpbox_face_surprised.setObjectName("gpbox_face_surprised")
        self.label_face_surprised = QtWidgets.QLabel(self.gpbox_face_surprised)
        self.label_face_surprised.setGeometry(QtCore.QRect(0, 30, 210, 150))
        self.label_face_surprised.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_face_surprised.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_face_surprised.setObjectName("label_face_surprised")
        self.btn_face_surprised_clear = QtWidgets.QPushButton(self.gpbox_face_surprised)
        self.btn_face_surprised_clear.setGeometry(QtCore.QRect(0, 190, 100, 25))
        self.btn_face_surprised_clear.setObjectName("btn_face_surprised_clear")
        self.btn_face_surprised_capture = QtWidgets.QPushButton(self.gpbox_face_surprised)
        self.btn_face_surprised_capture.setGeometry(QtCore.QRect(104, 190, 105, 25))
        self.btn_face_surprised_capture.setObjectName("btn_face_surprised_capture")

        self.gpbox_face_glasses = QtWidgets.QGroupBox(self.gpbox_faces)
        self.gpbox_face_glasses.setGeometry(QtCore.QRect(930, 300, 221, 271))
        self.gpbox_face_glasses.setFlat(False)
        self.gpbox_face_glasses.setCheckable(False)
        self.gpbox_face_glasses.setChecked(False)
        self.gpbox_face_glasses.setObjectName("gpbox_face_glasses")
        self.label_face_glasses = QtWidgets.QLabel(self.gpbox_face_glasses)
        self.label_face_glasses.setGeometry(QtCore.QRect(0, 30, 210, 150))
        self.label_face_glasses.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_face_glasses.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_face_glasses.setObjectName("label_face_glasses")
        self.btn_face_glasses_clear = QtWidgets.QPushButton(self.gpbox_face_glasses)
        self.btn_face_glasses_clear.setGeometry(QtCore.QRect(0, 190, 100, 25))
        self.btn_face_glasses_clear.setObjectName("btn_face_glasses_clear")
        self.btn_face_glasses_capture = QtWidgets.QPushButton(self.gpbox_face_glasses)
        self.btn_face_glasses_capture.setGeometry(QtCore.QRect(104, 190, 105, 25))
        self.btn_face_glasses_capture.setObjectName("btn_face_glasses_capture")

        self.gpbox_face_centerlight = QtWidgets.QGroupBox(self.gpbox_faces)
        self.gpbox_face_centerlight.setGeometry(QtCore.QRect(700, 300, 221, 271))
        self.gpbox_face_centerlight.setObjectName("gpbox_face_centerlight")
        self.label_face_centerlight = QtWidgets.QLabel(self.gpbox_face_centerlight)
        self.label_face_centerlight.setGeometry(QtCore.QRect(0, 30, 210, 150))
        self.label_face_centerlight.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_face_centerlight.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_face_centerlight.setObjectName("label_face_centerlight")
        self.btn_face_centerlight_clear = QtWidgets.QPushButton(self.gpbox_face_centerlight)
        self.btn_face_centerlight_clear.setGeometry(QtCore.QRect(0, 190, 100, 25))
        self.btn_face_centerlight_clear.setObjectName("btn_face_centerlight_clear")
        self.btn_face_centerlight_capture = QtWidgets.QPushButton(self.gpbox_face_centerlight)
        self.btn_face_centerlight_capture.setGeometry(QtCore.QRect(104, 190, 105, 25))
        self.btn_face_centerlight_capture.setObjectName("btn_face_centerlight_capture")

        self.gpbox_face_wink = QtWidgets.QGroupBox(self.gpbox_faces)
        self.gpbox_face_wink.setGeometry(QtCore.QRect(700, 20, 221, 271))
        self.gpbox_face_wink.setObjectName("gpbox_face_wink")
        self.label_face_wink = QtWidgets.QLabel(self.gpbox_face_wink)
        self.label_face_wink.setGeometry(QtCore.QRect(0, 30, 210, 150))
        self.label_face_wink.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_face_wink.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_face_wink.setObjectName("label_face_wink")
        self.btn_face_wink_clear = QtWidgets.QPushButton(self.gpbox_face_wink)
        self.btn_face_wink_clear.setGeometry(QtCore.QRect(0, 190, 100, 25))
        self.btn_face_wink_clear.setObjectName("btn_face_wink_clear")
        self.btn_face_wink_capture = QtWidgets.QPushButton(self.gpbox_face_wink)
        self.btn_face_wink_capture.setGeometry(QtCore.QRect(104, 190, 105, 25))
        self.btn_face_wink_capture.setObjectName("btn_face_wink_capture")
        CreateUserWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(CreateUserWindow)
        self.statusbar.setObjectName("statusbar")
        CreateUserWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CreateUserWindow)
        QtCore.QMetaObject.connectSlotsByName(CreateUserWindow)
        
        SrcSize = QtGui.QScreen.availableGeometry(QtWidgets.QApplication.primaryScreen())
        frmX = (SrcSize.width() - CreateUserWindow.width())/2
        frmY = (SrcSize.height() - CreateUserWindow.height())/2
        CreateUserWindow.move(frmX, frmY)

    def retranslateUi(self, CreateUserWindow):
        _translate = QtCore.QCoreApplication.translate
        CreateUserWindow.setWindowTitle(_translate("CreateUserWindow", "Criar usuário"))
        self.gpbox_user_data.setTitle(_translate("CreateUserWindow", "Dados do usuário"))
        self.txt_user_name.setPlaceholderText(_translate("CreateUserWindow", "Nome do Usuário"))
        self.lbl_user_name.setText(_translate("CreateUserWindow", "Nome"))
        self.lbl_user_birthday.setText(_translate("CreateUserWindow", "Data de nascimento"))
        self.date_user_birthday.setDisplayFormat("dd/MM/yyyy")
        self.btn_cancel.setText(_translate("CreateUserWindow", "Cancelar"))
        self.btn_input_rfid.setText(_translate("CreateUserWindow", "Ler tag RFID"))
        self.txt_user_rfid.setPlaceholderText(_translate("CreateUserWindow", "Tag RFID"))
        self.lbl_user_rfid.setText(_translate("CreateUserWindow", "RFID"))
        self.btn_capture_faces.setText(_translate("CreateUserWindow", "Carregar faces"))
        self.btn_save.setText(_translate("CreateUserWindow", "Salvar"))
        self.qpbox_create_instructions.setTitle(_translate("CreateUserWindow", "Instruções para cadastro"))
        
        self.gpbox_faces.setTitle(_translate("CreateUserWindow", "Faces"))
        self.gpbox_face_normal.setTitle(_translate("CreateUserWindow", "Normal - olhos abertos"))
        self.btn_face_normal_clear.setText(_translate("CreateUserWindow", "Limpar"))
        self.btn_face_normal_capture.setText(_translate("CreateUserWindow", "Carregar"))
        self.gpbox_face_rightlight.setTitle(_translate("CreateUserWindow", "Olhar para a esquerda"))
        self.btn_face_rightlight_clear.setText(_translate("CreateUserWindow", "Limpar"))
        self.btn_face_rightlight_capture.setText(_translate("CreateUserWindow", "Carregar"))
        self.gpbox_face_leftlight.setTitle(_translate("CreateUserWindow", "Levemente para a direita"))
        self.btn_face_leftlight_clear.setText(_translate("CreateUserWindow", "Limpar"))
        self.btn_face_leftlight_capture.setText(_translate("CreateUserWindow", "Carregar"))
        self.gpbox_face_sleepy.setTitle(_translate("CreateUserWindow", "Normal - olhos fechados"))
        self.btn_face_sleepy_clear.setText(_translate("CreateUserWindow", "Limpar"))
        self.btn_face_sleepy_capture.setText(_translate("CreateUserWindow", "Carregar"))
        self.gpbox_face_happy.setTitle(_translate("CreateUserWindow", "Sorrir - olhos abertos"))
        self.btn_face_happy_clear.setText(_translate("CreateUserWindow", "Limpar"))
        self.btn_face_happy_capture.setText(_translate("CreateUserWindow", "Carregar"))
        self.gpbox_face_sad.setTitle(_translate("CreateUserWindow", "Triste"))
        self.btn_face_sad_clear.setText(_translate("CreateUserWindow", "Limpar"))
        self.btn_face_sad_capture.setText(_translate("CreateUserWindow", "Carregar"))
        self.gpbox_face_surprised.setTitle(_translate("CreateUserWindow", "Surpreso(a)"))
        self.btn_face_surprised_clear.setText(_translate("CreateUserWindow", "Limpar"))
        self.btn_face_surprised_capture.setText(_translate("CreateUserWindow", "Carregar"))
        self.gpbox_face_glasses.setTitle(_translate("CreateUserWindow", "Normal com óculos"))
        self.btn_face_glasses_clear.setText(_translate("CreateUserWindow", "Limpar"))
        self.btn_face_glasses_capture.setText(_translate("CreateUserWindow", "Carregar"))
        self.gpbox_face_centerlight.setTitle(_translate("CreateUserWindow", "Raiva"))
        self.btn_face_centerlight_clear.setText(_translate("CreateUserWindow", "Limpar"))
        self.btn_face_centerlight_capture.setText(_translate("CreateUserWindow", "Carregar"))
        self.gpbox_face_wink.setTitle(_translate("CreateUserWindow", "Sorrir - olhos fechados"))
        self.btn_face_wink_clear.setText(_translate("CreateUserWindow", "Limpar"))
        self.btn_face_wink_capture.setText(_translate("CreateUserWindow", "Carregar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreateUserWindow = QtWidgets.QMainWindow()
    ui = Ui_CreateUserWindow()
    ui.setupUi(CreateUserWindow)
    CreateUserWindow.show()
    sys.exit(app.exec_())
