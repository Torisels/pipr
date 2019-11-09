import math


# Stwórz klasę modelującą wektor w ℝ2. Zaproponuj atrybuty/zmienne takiej klasy. Klasa powinna posiadać następujące metody:
#
# Dodawanie dwóch wektorów
# Iloczyn skalarny wektorów
# Znajdowanie wektora odwrotnego
# Obliczenie kąta pomiędzy dwoma wektorami w stopniach
# Obrót wektora o kąt podany w stopniach
# Podpowiedź: moduł math biblioteki standardowej posiada funkcje sin, cos, acos, oraz stałą pi.


class Vector:
    def __init__(self, coord_a=0, coord_b=0):
        self.coord_a = coord_a
        self.coord_b = coord_b
        self.length = self.__len__()

    def __len__(self):
        sq_a = self.coord_a ** 2
        sq_b = self.coord_b ** 2
        return math.sqrt(sq_a + sq_b)

    def __add__(self, other):
        """

        :type other: Vector
        """
        v = self
        v.add(other)
        return v

    def add(self, vector):
        if type(vector) != Vector:
            return False
        self.coord_a += vector.coord_a
        self.coord_b += vector.coord_b

    def dot_product(self, vector):
        """
        :type vector: Vector
        :rtype: number
        """
        if type(vector) != Vector:
            return False
        return self.coord_a * vector.coord_a + self.coord_b * vector.coord_b

    def rotate(self, angle):
        """
        This function rotates vector by given angle in degrees

        :type angle: float or int in degrees
        """
        radians = math.radians(angle)
        sin_a = math.sin(radians)
        cos_a = math.cos(radians)
        self.coord_a = self.coord_a * cos_a - self.coord_b * sin_a
        self.coord_b = self.coord_a * sin_a + self.coord_b * cos_a

    def opposite_vector(self):
        return Vector(-self.coord_a, -self.coord_b)

    def angle_between_vectors(self, vector):
        cosine = self.dot_product(vector) / (self.length * vector.length)
        return math.degrees(math.acos(cosine))

    @staticmethod
    def add_two_vectors(vector_1, vector_2):
        if vector_1.add(vector_2) is not False:
            return vector_1
        return False

    @staticmethod
    def rotate_vector(vector, angle):
        return vector.rotate(angle)


