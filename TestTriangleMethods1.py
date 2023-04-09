import unittest
import Triangle

class TestTriangleMethods(unittest.TestCase):

    def setUp(self):
        print("setUp")
        self.a = "3"
        self.b = "3"
        self.c = "3"
        self.test_triangle = Triangle.Triangle(self.a, self.b, self.c, 60, 60, 60)

    def test_init(self):
        print("test_init")
        self.assertEqual(self.test_triangle.a, float(self.a))
        self.assertEqual(self.test_triangle.b, float(self.b))
        self.assertEqual(self.test_triangle.c, float(self.c))

    def test_S(self):
        p = (float(self.a) + float(self.b) + float(self.c)) /2
        S = (p*(p-float(self.a))*(p-float(self.b))*(p-float(self.c)))**0.5
        test_triangle = Triangle.Triangle(float(self.a), float(self.b), float(self.c), 60, 60, 60)
        test_triangle.s() # считаем площадь
        print(int(test_triangle.S))
        self.assertEqual(int(test_triangle.S), int(S))
    # def test_s_negative(self)