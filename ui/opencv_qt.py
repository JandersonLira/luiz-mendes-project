import cv2
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.uic import loadUi
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cv2

class Signals(QtCore.QObject):
    started = QtCore.pyqtSignal()
    stop = QtCore.pyqtSignal()
    new_frame = QtCore.pyqtSignal(QtGui.QImage, np.ndarray)

class realTimeVideo(QThread):
    def __init__(self):
        super(realTimeVideo, self).__init__()
        self.signals = Signals()

    def run(self):
        print('start')
        #fourcc = cv2.VideoWriter_fourcc(*'DIVX')
        #self.out = cv2.VideoWriter('output.avi', fourcc, 25.0, (640, 480))
        
        self.cap = cv2.VideoCapture(0)
        cont = 0
        while (self.cap.isOpened()):
            ret, frame = self.cap.read()
            if ret == True:
                frame = cv2.flip(frame, 180)

                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = cv2.resize(frame, (311, 221))

                image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
                print(f"frame {cont}")
                self.signals.new_frame.emit(image, frame)
            else:
                break
            cont += 1

    @QtCore.pyqtSlot()
    def stop(self):
        print('stop')
        self.cap.release()    