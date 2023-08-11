import cv2
import copy
import time

from PyQt5 import QtCore, QtWidgets, QtGui, QtTest, uic

from opencv_qt import realTimeVideo


class CreateUserWindow(QtWidgets.QMainWindow):
    def __init__(self, parent):
        super(CreateUserWindow, self).__init__()
        uic.loadUi('ui/createuserwindow.ui', self)
        self.main_window = parent
        
        self.capture = realTimeVideo()
        
        self.capture.signals.stop.connect(lambda: print("stop camera"))
        self.capture.signals.new_frame.connect(self.show_image)

        self.current_face_label = None
        self.current_btn_capture = None
        self.current_btn_clear = None
        self.current_face = None
        
        self.image = None
        self.frame = None
        self.capturing = False
        
        self.init_ui()
        self.show()
    
    def reset_label_faces(self):
        self.label_faces = [
            {
				'face': 'normal',
                'label': self.label_face_normal,
                'frame': None,
                'capture': self.btn_face_normal_capture,
                'clear': self.btn_face_normal_clear
            },
            {
				'face': 'sleep',
                'label': self.label_face_sleep,
                'frame': None,
                'capture': self.btn_face_sleep_capture,
                'clear': self.btn_face_sleep_clear
            },
            {
				'face': 'smiling',
                'label': self.label_face_smiling,
                'frame': None,
                'capture': self.btn_face_smiling_capture,
                'clear': self.btn_face_smiling_clear
            },
            {
				'face': 'closed_eyes',
                'label': self.label_face_closed_eyes,
                'frame': None,
                'capture': self.btn_face_closed_eyes_capture,
                'clear': self.btn_face_closed_eyes_clear
            },
            {
				'face': 'surprised',
                'label': self.label_face_surprised,
                'frame': None,
                'capture': self.btn_face_surprised_capture,
                'clear': self.btn_face_surprised_clear
            },
            {
				'face': 'left',
                'label': self.label_face_left,
                'frame': None,
                'capture': self.btn_face_left_capture,
                'clear': self.btn_face_left_clear
            },
            {
				'face': 'right',
                'label': self.label_face_right,
                'frame': None,
                'capture': self.btn_face_right_capture,
                'clear': self.btn_face_right_clear
            },
            {
				'face': 'sad',
                'label': self.label_face_sad,
                'frame': None,
                'capture': self.btn_face_sad_capture,
                'clear': self.btn_face_sad_clear
            },
            {
				'face': 'anger',
                'label': self.label_face_anger,
                'frame': None,
                'capture': self.btn_face_anger_capture,
                'clear': self.btn_face_anger_clear
            },
            {
				'face': 'glasses',
                'label': self.label_face_glasses,
                'frame': None,
                'capture': self.btn_face_glasses_capture,
                'clear': self.btn_face_glasses_clear
            }
		]
        for face in self.label_faces:
            face['capture'].clicked.connect(self.capture_face)
            face['clear'].clicked.connect(self.clear_face)

            face['capture'].setEnabled(False)
            face['clear'].setEnabled(False)
    
    def set_current_face(self):
        for face in self.label_faces:
            if face['frame'] is None:
                self.current_face_label = face['label']
                self.current_btn_capture = face['capture']
                self.current_btn_clear = face['clear']
                self.current_face = face['face']
                self.current_btn_capture.setEnabled(True)
                return
        self.stop_camera()

    def init_ui(self):
        self.reset_label_faces()
        self.set_current_face()

        regex = QtCore.QRegExp("[a-z-A-Z_]+")
        validator = QtGui.QRegExpValidator(regex)
        self.txt_user_name.setValidator(validator)
        self.txt_user_name.setMaxLength(100)

        self.btn_capture_faces.setEnabled(False)
        # self.btn_cancel.clicked.connect(self.stop_camera)
    
    def start_camera(self):
        self.capture.start()
    
    def stop_camera(self):
        # self.capture.stop()
        pass
        
    def show_image(self, image, frame):
        if not self.capturing:
            self.current_face_label.clear()
            self.current_face_label.setPixmap(QtGui.QPixmap.fromImage(image))
            self.frame = frame
            self.image = image

    def capture_face(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            for face in self.label_faces:
                if self.current_face == face['face']:
                    frame = cv2.imread(fileName, cv2.IMREAD_GRAYSCALE)
                    
                    face['frame'] = copy.copy(frame)
                    self.set_current_face()

                    pixmap = QtGui.QPixmap(fileName)
                    pixmap = pixmap.scaled(200, 200, QtCore.Qt.KeepAspectRatio)
                    
                    face['label'].setPixmap(pixmap)
                    face['capture'].setEnabled(False)
                    face['clear'].setEnabled(True)
                    return

    def clear_face(self):
        pass
    
    def closeEvent(self, event) -> None:
        self.stop_camera()
        self.main_window.show()
        self.hide()