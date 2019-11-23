# Stwórz klasę Enemy. Wymagania:
#
#   posiada atrybuty takie jak nazwa, punkty zdrowia i liczba żyć.
#   metoda zwracająca opis obiektu
#   metoda take_damage ktora bedzie odejmować punkty od zdrowia obiektu, a po osiągnięciu zera zmniejszy liczbę żyć
#   metoda is_alive ktora na podstawie liczby żyć określa czy obiekt jest żywy czy nie.
#


class Enemy:
    def __init__(self, name, max_health, lives):
        self.name = name
        self.health = max_health
        self.lives = lives
        self.base_health = max_health

    def __repr__(self):
        return f"Enemy({self.name}, {self.base_health}, {self.lives})"

    def __str__(self):
        return self.description()

    def description(self):
        return f"I'm Enemy, my name is {self.name}, I have {self.health} health and {self.lives} lives"

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.lives -= 1
            self.health = self.base_health

    def is_alive(self):
        return self.lives > 0

