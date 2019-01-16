import unittest
from srcPY.person.consciousness.knowledge import Knowledge

class KnowledgeTestCase(unittest.TestCase):
    def setUp(self):
        self._level = Knowledge(51)

    def test_init(self):
        level = self._level
        self.assertEqual(level._level, 51)
