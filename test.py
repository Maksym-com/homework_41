# Розробіть свої класи з використанням усіх 4 принципів ООП та з 3 типами інкапсуляції(public, private, protected)
# 4 принципи - Поліморфізм, Наслідування, Інкапсуляція, Універсальність (Abstraction)
# Додайте в коді коментарі де ви якраз таки бачите оті принципи, щоб це було зрозуміло для вас та викладача


# Принцип Універсальності (Abstraction): Визначення абстрактного класу Games з методом genre()
class Games:
    def genre(self):
        pass

# Принцип Наслідування: Створення підкласу, який успадковує властивості та методи від базового класу
class Minecraft(Games):
    def genre(self):
        return """Minecraft — відеогра від незалежної студії Mojang 2011 року жанру «пісочниця»
у відкритому світі з виглядом від першої/третьої особи.
Гра започаткувала однойменну серію, для всіх творів якої характерний мінімалістичний кубічний дизайн.
Ця гра передусім дає змогу виразити свою креативність."""

class Dota_2(Games):
    def genre(self):
        return """Dota 2, Defense of the Ancients — багатокористувацька відеогра в піджанрі MOBA,
автономне продовження ідей карти DotA для гри Warcraft III: Reign of Chaos і її модифікації Warcraft III:
The Frozen Throne. Dota 2 випущена компанією Valve Corporation для платформи Microsoft Windows в публічній бета-версії у 2011 році."""

# Принцип Поліморфізм: Використання поліморфізму для виклику методу game() на різних об'єктах
def what_about(game):
    return game.genre()

# Принцип Інкапсуляції:
class Examples:
    def __init__(self):
        # Приватна змінна
        self.__private_think = 13
        # "Захищена" змінна
        self._protected_think = 100
        # Звичайна(публічна) змінна
        self.public_think = 60

    def get_private_think(self):
        return self.__private_think

    def set_private_think(self, somethink):
        self.__private_think = somethink

# Створення об'єктів
mine = Minecraft()
dota = Dota_2()
examle = Examples()

# Виклик методів інкапсуляції
print(examle.get_private_think())  # Виведе 13
examle.set_private_think(50)
print(examle.get_private_think())  # Виведе 50

# Виклик методів поліморфізму
print(what_about(mine))  # Виведе опис гри Minecraft
print(what_about(dota))  # Виведе опис гри Dota 2





