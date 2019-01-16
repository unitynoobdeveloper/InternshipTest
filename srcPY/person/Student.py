from srcPY.person.consciousness.knowledge import Knowledge
from random import randint


class Student:
    def __init__(self, name):
        self.name = name
        self.knowledge = 0
        self.SetKnowledge()

    def SetKnowledge(self):
        knowledge = Knowledge(randint(0, 100))
        self.knowledge = knowledge.level







