from os import path
from os.path import abspath

ROOT_PATH = path.dirname(__file__)


class Config:
    DATA_PATH = abspath(path.join(ROOT_PATH, "data"))
