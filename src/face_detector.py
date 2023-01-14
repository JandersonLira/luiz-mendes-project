""" face_detector
"""
import cv2
import pathlib

import numpy as np

from typing import List, Union

# path of this file
POTH = pathlib.Path(__file__).parent.__str__()


class FaceDetector:
    """ FaceDetector
    """
    def __init__(self):
        """__init__ FaceDetector constructor
        """
        self.cascade_classifier = None

    def set_cascade_classifier(self, haar_cascade_path: str):
        """set_cascade_classifier set the c

        Args:
            haar_cascade_path (str): path of xml file with
            Haar Cascade informations
        """
        self.cascade_classifier = cv2.CascadeClassifier(
            haar_cascade_path
        )
    
    def get_face(self, src_path: str) -> Union[bool, List[np.array]]:
        """get_face Get sub-images in image with faces identifieds

        Args:
            src_path (str): Path of image

        Returns:
            Union[bool, List[np.array]]:
                bool: True if exist any face in image, False for other
                List[np.array]: List with cropped faces.
                Images are gray scale.
        """
        face_list = []

        color_img = cv2.imread(filename=src_path)
        gray_img = cv2.cvtColor(src=color_img, code=cv2.COLOR_BGR2GRAY)

        faces = self.cascade_classifier.detectMultiScale(
            image=gray_img, scaleFactor=1.03, minNeighbors=5
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
