print('hello world')
user = {
    'username': 'tagila',
    'password': '1939',
    'rub': '500000',
    'age': '27',
    'gender': 'муржской'
}
print()
print()

print()
# user.clear
# print('после clear' ,user)


# print(user.get())
# print(user.ite)
# print(user.)
# print(user.)
# print(user)
# print(user.)

class CHVK:
    def __init__(self, newName, newBreed, newWeight, newEvil):
        self.name = newName
        self.breed = newBreed
        self.weight = newWeight
        self.evil = newEvil

    def Info(self):
        print('название', self.name)
        print('сторона', self.breed)
        print('вес со снарягой', self.weight)
        print('процент поснания на хубобубу', self.evil)


    def Run(self):
        print(self.name,'убегает от tagila')

CHVK1 = CHVK('ЧВК', 'BEAR', '58', 95)
CHVK1.Run()
CHVK1.Info()









































