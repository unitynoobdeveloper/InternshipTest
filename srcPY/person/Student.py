from srcPY.person.consciousness.Knowledge import Knowledge
import  random

class Student():
    def __init__(self, name):
        self.name = name
        self.knowledge=0
        self.SetKnowledge()

    def SetKnowledge(self):
        knowledge=Knowledge(random.randint(0,100))
        self.knowledge= knowledge.level







