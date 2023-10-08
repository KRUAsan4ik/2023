# cats = [('Мартин', 5, 'Вова', 'Чак-чак')
# #         ('Яшкот', 4, 'Алекс', 'Чуприк')
# #         ('НеЯшкот', 3, 'Окрошка', 'С квасом')
# #         ('Никола', 2, 'Олег', 'Абортов')
# #         ('Кола', 1, 'Олег', 'Абортов')]
# # dict = {}
# # for cat in cats:
# #         nameage = cat[0] + ', ' + str(cat[1])
# #         result.setdefault(cat[2:],[]).append(nameage)
# #
# # for i in result.items():
# #         print(i)
# my_dict = {}
# def funs(**kwards):
#         my_dict.update(**kwards)
#
# funs(a=5, b=10, c=10)
#
# print(my_dict)
#
import random
class Voin:
    def __init__(self, name, health, damage):
        self.health = health
        self.damage = damage
        self.name = name

    def hit(self, voin):
        voin.health -= self.damage
        print(f'{self.name} Ударил {voin.name}, и у него осталось {voin.health}')


Igor = Voin('Igor', 100, random.randint(5, 10))
Ahiles = Voin('Ahiles', 100, random.randint(5, 10))

while Igor.health > 0 and Ahiles.health > 0:
        if random.randint(1,2) == 2:
                Igor.hit(Ahiles)
        else:
                Ahiles.hit(Igor)
        if Igor.health <= 0:
                print('game over for Игорь')
                break
        if Ahiles.health <= 0:
                print('game over for Ахилес')
                break