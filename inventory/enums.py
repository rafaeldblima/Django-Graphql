from common.enums import BaseEnum


class ReasonsEnum(BaseEnum):
    NEW_STOCK = ('ns', "New Stock")
    USABLE_RETURN = ('ur', "Usable Return")
    UNUSABLE_RETURN = ('nr', "Unusable Return")

    def __init__(self, cod, desc):
        self.cod = cod
        self.desc = desc
