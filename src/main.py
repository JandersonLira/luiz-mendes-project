import pathlib

from dataset_manager import DatasetManager
from face_detector import FaceDetector

POTH = pathlib.Path(__file__).parent.__str__() + '/'

if __name__ == "__main__":
    face_detector = FaceDetector()
    ds_gen = DatasetManager(face_detector)

    # dataset_path = POTH + '../data/training_faces'
    # for user_id, dataset in enumerate(pathlib.Path(dataset_path).iterdir()):
    #     ds_gen.set_input_images(dataset, str(user_id))
    
    faces, user_ids = ds_gen.load_faces()
    if face_detector.start_training(user_ids=user_ids, faces=faces):
        print('Success')
    else:
        print('Fail')