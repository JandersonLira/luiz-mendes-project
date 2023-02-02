""" face_detector
"""
import cv2
import pathlib

import numpy as np

from typing import List, Union

import app_log

# path of this file
POTH = pathlib.Path(__file__).parent.__str__() + '/'
MODEL_PATH = POTH + '../data/trained_model.yml'
CASCADE_MODEL_PATH = POTH + '../files/haarcascade_frontalface_default.xml'

class FaceDetector:
    """ FaceDetector
    """
    def __init__(self):
        """__init__ FaceDetector constructor
        """
        self.cascade_classifier = cv2.CascadeClassifier(CASCADE_MODEL_PATH)
        self.__recognizer = cv2.face.LBPHFaceRecognizer_create(
            radius=2, neighbors=16, grid_x=8, grid_y=8
        )
    
    def get_face(self, src_path: pathlib.Path) -> Union[bool, List[np.array]]:
        """get_face Get sub-images in image with faces identifieds

        Args:
            src_path (pathlib.Path): Path of image

        Returns:
            Union[bool, List[np.array]]:
                bool: True if exist any face in image, False for other
                List[np.array]: List with cropped faces.
                Images are gray scale.
        """
        face_list = []

        color_img = cv2.imread(filename=str(src_path))
        gray_img = cv2.cvtColor(src=color_img, code=cv2.COLOR_BGR2GRAY)

        faces = self.cascade_classifier.detectMultiScale(
            image=gray_img, scaleFactor=1.03, minNeighbors=49
        )
        
        for (start_point_x, start_point_y, width, height) in faces:
            cropped_face = gray_img[
                start_point_y:start_point_y+height,
                start_point_x:start_point_x+width
            ]
            face_list.append(cropped_face)

        if len(face_list) != 0:
            return [True, face_list]
        else:
            return [False, []]

    def start_training(self, user_ids: List[str], faces: List[np.array]) -> bool:
        """start_training function to execute the training model

        Args:
            user_ids (List[str]): List of user ids
            faces (List[np.array]): List of loaded faces

        Returns:
            bool: Status of training
        """
        try:
            app_log.logging.info(f'Start training')
            self.__recognizer.train(faces, np.array(user_ids))
            app_log.logging.info(f'Finish training')
            app_log.logging.info(f'Model trained successfully: {MODEL_PATH}')
        except Exception as ex:
            app_log.logging.error(f'Fail to training model: {ex}')
            return False
        
        try:
            self.__recognizer.write(MODEL_PATH)
            app_log.logging.info(f'Trainded model file generated successfully: {MODEL_PATH}')
            return True
        except Exception as ex:
            app_log.logging.error(f'Fail to generate trained model file: {ex}')
