import pathlib

from dataset_generator import DatasetGenerator

POTH = pathlib.Path(__file__).parent.__str__() + '/'

if __name__ == "__main__":
    ds_gen = DatasetGenerator()

    dataset_path = POTH + '../data/training_faces'
    for user_id, dataset in enumerate(pathlib.Path(dataset_path).iterdir()):
        ds_gen.set_input_images(dataset, str(user_id))