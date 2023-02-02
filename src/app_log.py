import pathlib
import logging


# path of this file
POTH = pathlib.Path(__file__).parent.__str__() + '/'

APP_LOG_FILE = POTH + '../data/app.log'

pathlib.Path(APP_LOG_FILE).touch(exist_ok=True)

logging.root.setLevel(logging.NOTSET)

logging.basicConfig(
    filename=APP_LOG_FILE, filemode='a',
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
    datefmt='%d-%m-%y %H:%M:%S', level=logging.NOTSET
)