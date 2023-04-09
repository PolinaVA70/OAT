import unittest
import Dog

class TestDogMethods(unittest.TestCase):

    def setUp(self):
        self.dogTest = Dog.Dog()

    def test_init(self):
        self.assertEqual(self.dogTest.mood, 50)
        self.assertEqual(self.dogTest.hunger, 50)
        self.assertEqual(self.dogTest.vivacity, 50)

    def test_sleep(self):
        self.dogTest.sleep()
        self.assertEqual(self.dogTest.hunger, 25)
        self.assertEqual(self.dogTest.vivacity, 100)

    def test_play(self):
        self.dogTest.play()
        self.assertEqual(self.dogTest.mood, 100)
        self.assertEqual(self.dogTest.vivacity, 25)
        self.assertEqual(self.dogTest.hunger, 25)

    def test_eat(self):
        self.dogTest.eat()
        self.assertEqual(self.dogTest.hunger, 100)
        self.assertEqual(self.dogTest.vivacity, 75)





