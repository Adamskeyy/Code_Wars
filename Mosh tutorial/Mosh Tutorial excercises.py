# command = ""
# started = False
#
# while True:
#     command = input('> ').lower()
#     if command == 'help':
#         print("""
# start - to start the car
# stop - to stop the car
# quit - to quit
#         """)
#     elif command == 'start':
#         if started:
#             print('Car is already started!')
#         else:
#             started = True
#             print('Car started...Ready to go!')
#     elif command == 'stop':
#         if started:
#             print('Car stopped')
#             started = False
#         else:
#             print('Car is already stopped!')
#     elif command == 'quit':
#         break
#     else:
#         print("I don't understand that")


# for item in 'Python':
#     print(item)


# for item in [1, 2, 3]:
#     print(item)


# for item in range(1, 11, 2):
#     print(item)


# prices = [10, 20, 30]
# cost = 0
# for price in prices:
#     cost += price
# print(f'Total: {cost}')

# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y})')

# numbers = [5, 2, 5, 2, 2]
# for num in numbers:
#     print(num * 'x')

# numbers = [5, 2, 5, 2, 2]
# for x_count in numbers:
#     output = ''
#     for count in range(x_count):
#         output += 'x'
#     print(output)

# names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
# names[0] = 'Jon'
# print(names)
# print(names[2:4])

# numbers = [32, 43534, 6544, 23, 5674784, 321]
# max = numbers[0]
# for num in numbers:
#     if num > max:
#         max = num
# print(max)


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 7, 8]
# ]
#
# print(matrix[1][2])


# numbers = [1, 1, 4, 7, 8, 4, 6, 9, 13, 7]
# uniques = []
#
# for i in numbers:
#     if i not in uniques:
#         uniques.append(i)
#
# print(uniques)


#rozpakowywanie list

# coordinates = (1, 2, 3)
# x, y, z = coordinates
# print(y)


# customer = {
#     "name": "John Smith",
#     "age": 30,
#     "is_verified": True
# }
# customer["birthdate"] = "January 1 1980"
# print(customer["birthdate"])


# phone_number = input("Phone: ")
# digits = {"1": "One", "2": "Two", "3": "Three",
#           "4": "Four", "5": "Five", "6": "Six",
#           "7": "Seven", "8": "Eight", "9": "Nine"}
# translate = []
# for i in phone_number:
#     translate.append(digits.get(i))
# print(" ".join(translate))


# class Person:
#     def __init__(self, name):
#         self.name = name
#
#
#     def talk(self):
#         print(f"Hi, I'm {self.name}")
#
#
# john = Person("John Smith")
# john.talk()
#
# bob = Person("Bob Smith")
# bob.talk()


# class Mammal:
#     def walk(self):
#         print("walk")
#
#
# class Dog(Mammal):
#     def bark(self):
#         print("bark")
#
# class Cat(Mammal):
#     def be_annoying(self):
#         print("annoying")
#
#
# dog = Dog()
# dog.walk()
# dog.bark()
#
# cat = Cat()
# cat.be_annoying()

# import converters
# from converters import kg_to_lbs
#
# print(kg_to_lbs(70))


# from utils import find_max
#
# numbers = [32, 43534, 6544, 23, 5674784, 321]
#
# find_max(numbers)


# from ecommerce import shipping
# shipping.calc_shipping()


# import random

# for i in range(3):
#     print(random.randint(10, 20))

# members = ['John', 'Mary', 'Bob', 'Mosh']
# leader = random.choice(members)
# print(leader)


# class Dice:
#     def roll(self):
#         first = random.randint(1, 6)
#         second = random.randint(1, 6)
#         return first, second #tuple
#
#
# dice = Dice()
# print(dice.roll())


from pathlib import Path

# path = Path("ecommerce")
# print(path.exists())

# path = Path("email")
# print(path.mkdir())

# path = Path("email")
# print(path.rmdir())

path = Path()
for file in path.glob('*.py'):
    print(file)