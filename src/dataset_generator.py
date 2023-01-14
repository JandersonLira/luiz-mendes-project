""" dataset_generator
"""


class DatasetGenerator:
    """ DatasetGenerator
    """
    def __init__(self) -> None:
        """__init__ DatasetGenerator constructor
        """
        self.input_images = {}
        self.__dataset_info = {}

    def set_input_images(self, src_path: str, user_id: int) -> None:
        """set_input_images Define image path of a specific
        face to be inserted in dataset

        Args:
            src_path (str): Path of images
            user_id (int): The unique ID of user
        """
        pass

    def __load_users_images(self):
        """__load_users_images Load informations about
        the user faces already registered
        """
        pass
