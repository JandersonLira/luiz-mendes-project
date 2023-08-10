import cv2
import pathlib

from dataset_manager import DatasetManager
from face_detector import FaceDetector

POTH = pathlib.Path(__file__).parent.__str__() + '/'

if __name__ == "__main__":
    face_detector = FaceDetector()
    ds_gen = DatasetManager(face_detector)
    
    dataset_path = POTH + '../data/training_faces'
    for user_id, dataset in enumerate(pathlib.Path(dataset_path).iterdir(), start=1):
        ds_gen.set_input_images(dataset, str(user_id))
    
    faces, user_ids = ds_gen.load_faces()
    face_detector.start_training(user_ids=user_ids, faces=faces)
    
    trained_model_path = POTH + '../data/trained_model.yml'
    user_list = ['None', 'Obama', 'Trump', 'Janderson', 'Biden']
    if face_detector.load_model(model_path=trained_model_path):
        for folder in pathlib.Path(str(POTH)+'../data/validation_faces').iterdir():
            for image in pathlib.Path(str(folder)).iterdir():
                print(image)
                src_image = cv2.imread(str(image))
                face_detector.search_user(user_list, src_image)
                print('\n\n')
    