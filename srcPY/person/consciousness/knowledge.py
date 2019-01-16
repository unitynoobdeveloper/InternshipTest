
class Knowledge:

    def __init__(self, level: int):
        if 100 < level < 50:
            raise ValueError('Knowledge cant to be more then 100 and lower then 50')
        self._level = level

