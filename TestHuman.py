import unittest
from Human import Human
import xmlrunner

class TestHuman(unittest.TestCase):
    def setUp(self):
        self.test_name="Ihor"
        self.test_surname="Kandyba"
        self.test_gat=25
        self.human = Human(self.test_name,self.test_surname,self.test_gat)
    def test_get_name(self):
        self.assertEqual(self.human.get_name(),self.test_name)
    def test_get_surname(self):
        pass
        self.assertEqual(self.human.get_surname(),self.test_surname)
    def test_get_age(self):
        self.assertEqual(self.human.get_age(),self.test_gat)

if __name__ == '__main__':
        with open('results.xml', 'wb') as output:
            unittest.main(
                testRunner=xmlrunner.XMLTestRunner(output=output),
                failfast=False, buffer=False, catchbreak=False)