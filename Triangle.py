class Triangle:

    def __init__(self, a, b, c, A, B, C): #инициализатор - момент создания объекта
        self.a = float (a)  # self - свойства, параметры, атрибуты, характеристика
        self.b = float (b)
        self.c = float (c)
        self.A = A
        self.B = B
        self.C = C
        self.S = 0

    def s(self):    # фукнцмия внутри класса, это и есть метод
        a = self.a
        b = self.b
        c = self.c
        p = (a + b + c)/2
        #return (p*(p-a)*(p-b)*(p-c))**0.5 # вернет подсчет площади
        self.S = (p*(p-a)*(p-b)*(p-c))**0.5
a = "3"
print(float(a))
triangle = Triangle(3, 3, 3, 60, 60, 60)
triangle.s()
print(triangle.a, triangle.b, triangle.c, triangle.S)

