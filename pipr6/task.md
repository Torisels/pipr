Zadania lab 6
Zadanie 0
Zmodyfikuj klasę Game tak aby realizowała następującą logikę:

W każdej rundzie gracz atakuje jakiegoś przeciwnika
Gra jest wygrana jeśli graczowi udało się zabić wszystkie potwory
Gra jest przegrana jeśli gracz straci całą moc, lub jeśli jakikolwiek potwór pozostaje żywy po MAX_ROUNDS
Weź pod uwagę możliwość regeneracji specyficznych przeciwników
Pamiętaj o dobrym podziale problemu na metody.

Zadanie 1
Wprowadź do gry nową klasę: SuperHero, która będzie szczególnym rodzajem gracza. Jego ataki bedą zawsze dotykały wszystkich przeciwników, a jego moc nie będzie spadać. Przetestuj rozgrywkę dla gracza, który jest SuperHero.
Zmień klasy Player i Enemy tak, aby wyciągnąć wspólną klasę bazową. Sprawdź działanie calosci.
Popraw działanie gry: jeśli uda się wyzerować health konkretnego wroga usuń go z listy potencjalnych wrogów do ataku.
Napisz metody w klasie Game, które będą dodawać/usuwac wrogów z listy wrogów.
Zadanie 2
Rozszerz klasy z poprzedniego zadania domowego. Album powinien posiadać piosenki oraz metodę odtworzenia albumu (przyjmującą opcjonalny argument numer piosenki, od której zacząć). Powinien też mieć atrybut/metodę zwracającą czas trwania całości albumu.

Dla chętnych
zapoznaj się z koncepcją dekoratora @property