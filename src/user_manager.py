import os
import cv2
import sys
import json
from pathlib import Path

execution_dir = os.getcwd()
sys.path.append(execution_dir)

TRAIN_DATASET_DIR = "data/new_yale_faces"


class UserManager:
    def __init__(self) -> None:
        self.users_file = 'src/users.json'
        users_file_path = Path(self.users_file)
        self.user_db = {}
        if not users_file_path.is_file():
            self.users_data = {}
            with open(self.users_file, 'w') as file:
                json.dump(self.user_db, file, indent=4)
        else:
            with open(self.users_file) as file:
                self.user_db = json.load(file)
    
    def create_user(self, user_data):
        unformatted_user_name = user_data['user_name']
        user_birthday = user_data['user_birthday']
        user_faces = user_data['user_faces']

        formatted_user_name = ""
        for part_name in unformatted_user_name.split(" "):
            formatted_user_name += part_name[0].upper()+part_name[1:].lower()
        if formatted_user_name in self.user_db.keys():
            return (False, "ERRO: Usuário já registrado no sistema.")
        
        user_faces_paths = []
        for user_face in user_faces.keys():
            filename = f"{TRAIN_DATASET_DIR}/{formatted_user_name}_{user_face}.png"
            user_faces_paths.append(filename)
            frame = user_faces[user_face]
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
            cv2.imwrite(filename, frame)
        
        self.user_db[formatted_user_name] = {
            'user_birthday': user_birthday,
            'user_faces': user_faces_paths
        }
        self.commit_changes()
        return True, "INFO: Usuário registrado com sucesso."
    
    def commit_changes(self):
        with open(self.users_file, 'w') as file:
            json.dump(self.user_db, file, indent=4)
