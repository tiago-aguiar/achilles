from enum import Enum

class Entity(Enum):
    YT = 0
    IG = 1
    FB = 2


class Account():

    def __init__(self, id, name):
        self.id = id
        self.name = name
