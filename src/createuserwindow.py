import cv2
import copy
import time

from PyQt5 import QtCore, QtWidgets, QtGui, QtTest, QtGui, uic

from captureimagetocreateuser import CaptureImageToCreateUser

INSTRUCTIONS = """O nome do usuário deve ter entre 10 e 100 caracteres.
Todas as 10 imagens de faces devem ser preenchidas.

"""


class CreateUserWindow(QtWidgets.QMainWindow):
    def __init__(self, parent):
        super(CreateUserWindow, self).__init__()
        uic.loadUi('ui/createuserwindow.ui', self)
        self.main_window = parent
        
        self.face_list = {
            'normal': None,
            'sleep': None,
            'smiling': None,
            'closed_eyes': None,
            'surprised': None,
            'left': None,
            'right': None,
            'sad': None,
            'anger': None,
            'glasses': None
        }

        self.create_global_variables_access_to_widgets()
        self.init_ui()
        self.show()
    
    def create_global_variables_access_to_widgets(self):
        global btn_face_normal_capture
        btn_face_normal_capture = self.btn_face_normal_capture

        global btn_face_normal_clear
        btn_face_normal_clear = self.btn_face_normal_clear

        global label_face_normal
        label_face_normal = self.label_face_normal

        global btn_face_sleep_capture
        btn_face_sleep_capture = self.btn_face_sleep_capture

        global btn_face_sleep_clear
        btn_face_sleep_clear = self.btn_face_sleep_clear

        global label_face_sleep
        label_face_sleep = self.label_face_sleep

        global btn_face_smiling_capture
        btn_face_smiling_capture = self.btn_face_smiling_capture

        global btn_face_smiling_clear
        btn_face_smiling_clear = self.btn_face_smiling_clear

        global label_face_smiling
        label_face_smiling = self.label_face_smiling

        global btn_face_closed_eyes_capture
        btn_face_closed_eyes_capture = self.btn_face_closed_eyes_capture

        global btn_face_closed_eyes_clear
        btn_face_closed_eyes_clear = self.btn_face_closed_eyes_clear

        global label_face_closed_eyes
        label_face_closed_eyes = self.label_face_closed_eyes

        global btn_face_surprised_capture
        btn_face_surprised_capture = self.btn_face_surprised_capture

        global btn_face_surprised_clear
        btn_face_surprised_clear = self.btn_face_surprised_clear

        global label_face_surprised
        label_face_surprised = self.label_face_surprised

        global btn_face_left_capture
        btn_face_left_capture = self.btn_face_left_capture

        global btn_face_left_clear
        btn_face_left_clear = self.btn_face_left_clear

        global label_face_left
        label_face_left = self.label_face_left

        global btn_face_right_capture
        btn_face_right_capture = self.btn_face_right_capture

        global btn_face_right_clear
        btn_face_right_clear = self.btn_face_right_clear

        global label_face_right
        label_face_right = self.label_face_right

        global btn_face_sad_capture
        btn_face_sad_capture = self.btn_face_sad_capture

        global btn_face_sad_clear
        btn_face_sad_clear = self.btn_face_sad_clear

        global label_face_sad
        label_face_sad = self.label_face_sad

        global btn_face_anger_capture
        btn_face_anger_capture = self.btn_face_anger_capture

        global btn_face_anger_clear
        btn_face_anger_clear = self.btn_face_anger_clear

        global label_face_anger
        label_face_anger = self.label_face_anger

        global btn_face_glasses_capture
        btn_face_glasses_capture = self.btn_face_glasses_capture

        global btn_face_glasses_clear
        btn_face_glasses_clear = self.btn_face_glasses_clear

        global label_face_glasses
        label_face_glasses = self.label_face_glasses
    
    def configure_reset_faces(self):
        for face_name in self.face_list.keys():
            globals()[f'btn_face_{face_name}_capture'].clicked.connect(
                lambda x, face_name=face_name: self.capture_face(face_name)
            )

            globals()[f'btn_face_{face_name}_clear'].clicked.connect(
                lambda x, face_name=face_name: self.clear_face(face_name)
            )

    def init_ui(self):
        self.configure_reset_faces()
        self.txt_instructions_to_create.setText(INSTRUCTIONS)

        self.btn_input_rfid.setEnabled(False)

        self.btn_save.clicked.connect(self.save_user)

        regex = QtCore.QRegExp("[a-z-A-Z_]+")
        validator = QtGui.QRegExpValidator(regex)
        self.txt_user_name.setValidator(validator)
        self.txt_user_name.setMaxLength(100)

        self.btn_capture_faces.setEnabled(True)
        self.btn_capture_faces.clicked.connect(self.capture_process)
    
    def capture_process(self):
        faces_to_capture = []
        for face_name in self.face_list.keys():
            if self.face_list[face_name] is None:
                faces_to_capture.append(face_name)
        self.camera_window = CaptureImageToCreateUser(faces_to_capture)
        self.camera_window.signals.close.connect(self.close_camera_window)
        self.camera_window.show()
        self.hide()
    
    def close_camera_window(self, captured_images: dict):
        captured_image_names = []
        for face_name in captured_images.keys():
            if captured_images[face_name]['frame'] is not None:
                captured_image_names.append(face_name)

        for face_name in self.face_list.keys():
            if face_name in captured_image_names:
                self.face_list[face_name] = captured_images[face_name]['frame']
                
                globals()[f'btn_face_{face_name}_capture'].setEnabled(False)
                globals()[f'btn_face_{face_name}_clear'].setEnabled(True)
                
                image = QtGui.QImage(
                    self.face_list[face_name],
                    self.face_list[face_name].shape[1],
                    self.face_list[face_name].shape[0],
                    QtGui.QImage.Format_RGB888
                )

                pixmap =  QtGui.QPixmap.fromImage(image)
                pixmap = pixmap.scaled(200, 200, QtCore.Qt.KeepAspectRatio)
                globals()[f'label_face_{face_name}'].setPixmap(pixmap)

        self.show()

    def capture_face(self, face_name):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            frame = cv2.imread(fileName, cv2.IMREAD_GRAYSCALE)
            
            self.face_list[face_name] = copy.copy(frame)
            globals()[f'btn_face_{face_name}_capture'].setEnabled(False)
            globals()[f'btn_face_{face_name}_clear'].setEnabled(True)
            
            pixmap = QtGui.QPixmap(fileName)
            pixmap = pixmap.scaled(200, 200, QtCore.Qt.KeepAspectRatio)
            globals()[f'label_face_{face_name}'].setPixmap(pixmap)

    def clear_face(self, face_name):
        globals()[f'label_face_{face_name}'].clear()
        globals()[f'btn_face_{face_name}_capture'].setEnabled(True)
        globals()[f'btn_face_{face_name}_clear'].setEnabled(False)
        self.face_list[face_name] = None
    
    def save_user(self):
        error_msg = ""
        if len(self.txt_user_name.text()) < 10:
            error_msg += "ERRO: Nome curto demais. O nome do usuário deve conter, pelo menos, 10 caracteres.\n"

        if None in list(self.face_list.values()):
            error_msg += "ERRO: É necessário capturar todas 10 faces para registar usuário.\n"
        
        if error_msg:
            self.txt_user_name.setText(INSTRUCTIONS+error_msg)
            return

        
        

    def closeEvent(self, event) -> None:
        self.main_window.show()
        self.hide()