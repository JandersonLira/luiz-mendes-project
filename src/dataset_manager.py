""" dataset_generator
"""
import os
import cv2
import json
import pathlib
import numpy as np

from typing import List, Union

import app_log

from face_detector import FaceDetector

# path of this file
POTH = pathlib.Path(__file__).parent.__str__() + '/'
DATASET_CONFIG_FILE = POTH + '../data/dataset_config.json'


class DatasetManager:
    """ DatasetManager
    """
    def __init__(self, face_detector: FaceDetector) -> None:
        """__init__ DatasetManager constructor
        """
        self.input_images = {}
        self.__dataset_info = {}
        self.__face_detector = face_detector

    def set_input_images(self, src_path: pathlib.Path, user_id: str) -> None:
        """set_input_images Define image path of a specific
        face to be inserted in dataset

        Args:
            src_path (str): Path of images
            user_id (str): The unique ID of user
        """
        self.__load_users_images()
        
        user_name = src_path.name.upper()
        
        user_path = pathlib.Path(POTH + '../data/dataset/' + user_name)
        user_path.mkdir(parents=True, exist_ok=True)
        
        image_index = sum(os.path.isfile(os.path.join(user_path, f)) for f in os.listdir(user_path)) + 1

        if user_id not in self.__dataset_info.keys():
            self.__dataset_info[user_id] = {
                'user_name': user_name,
                'faces':{}
            }
            app_log.logging.info(f'Insert a new user in training dataset. ID: {user_id} - Name: {user_name}')
        
        for input_image_path in pathlib.Path(src_path).iterdir():
            if not str(input_image_path) in self.__dataset_info[user_id]['faces'].keys():
                found_faces, faces = self.__face_detector.get_face(input_image_path)
                if found_faces:
                    for face in faces:
                        img_path = str(user_path) + '/' + user_name + '.' + user_id + '.' + str(image_index) + '.jpg'
                        cv2.imwrite(img_path, face)
                        image_index += 1
                        self.__dataset_info[user_id]['faces'][str(input_image_path)] = str(img_path)
                        app_log.logging.info(f'Insert a new trainig image in dataset. USER_ID: {user_id} - IMAGE_INDEX: {str(image_index)}')
            else:
                app_log.logging.warning(f'Image already in dataset: {input_image_path}')
        
        self.__update_users_images()

    def load_faces(self) -> Union[List[str], List[str]]:
        """load_faces _summary_

        Returns:
            Union[List[str], List[str]]:
                List[np.array]: List with loaded faces
                List[str]: List with user ids of faces
        """
        self.__load_users_images()
        
        faces = []
        user_ids = []

        for user_id in self.__dataset_info.keys():
            face_paths = self.__dataset_info[user_id]['faces'].values()
            for face_path in face_paths:
                color_img = cv2.imread(filename=face_path)
                gray_img = np.array(cv2.cvtColor(src=color_img, code=cv2.COLOR_BGR2GRAY), 'uint8')
                faces.append(gray_img)
                user_ids.append(int(user_id))
        return [faces, user_ids]

    def __load_users_images(self):
        """__load_users_images Load informations about
        the user faces already registered
        """
        ds_file_name = DATASET_CONFIG_FILE.split('/')[-1]

        pathlib.Path(DATASET_CONFIG_FILE).touch(exist_ok=True)

        try:
            with open(file=DATASET_CONFIG_FILE, mode='r') as f:
                self.__dataset_info = json.loads(f.read())
            app_log.logging.info(f'Load dataset configuration file: {ds_file_name}')
        except Exception as ex:
            app_log.logging.error(f"Fail to load dataset configuration file ({ds_file_name}): {ex}")

    def __update_users_images(self):
        """__update_users_images Update informations about
        the user faces in dataset_config.json
        """
        ds_file_name = DATASET_CONFIG_FILE.split('/')[-1]
        try:
            with open(file=DATASET_CONFIG_FILE, mode='w') as f:
                f.write(json.dumps(self.__dataset_info))
            app_log.logging.info(f'Update dataset configuration file: {ds_file_name}')
        except Exception as ex:
            app_log.logging.error(f"Fail to update {ds_file_name}: {ex}")
        """
        self.__dataset_info = {
            user_id: [
                User.id.n_img.jpg
            ]
        }
        """
    
    def load_user_list(self) -> List[str]:
        """load_user_list Load list with all user names

        Returns:
            Union[str]: List of user names
        """
        self.__load_users_images()
