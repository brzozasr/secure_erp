from model.model_dict.model_json import *
from view.view import *


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
