# class Car:
#     def __init__(self, name, year, color):
#         self.car_name = name
#         self.car_year = year
#         self.car_color = color
#
#
#     def present(self):
#         print(f"This {self.car_color} {self.car_name} produced in {self.car_year}")
#
#
#     def get_age(self, current_year):
#
#         return current_year - self.car_year
# #
# #
# #
# #
# #
# #
# car_1 = Car(name="Jaguar", year="2022", color="Black")
# car_2 = Car(name="Mercedes", year="2022", color="White")
# car_3 = Car(name="BMW", year="2022", color="Violet")
# #
#
# print(car_1.car_name, car_1.car_year, car_1.car_color)
# print(car_2.car_name, car_2.car_year, car_2.car_color)
#
# Car.present(car_1)
# print(car_1.get_age(current_year=2022))


# class CV:
#     description = "This is a car class"
#
#     def __init__(self, name, surname, email, age):
#         self.name = name
#         self.surname = surname
#         self.email = email
#         self.age = age
#
#     # def present(self):
#     #     print(f"This is {self.}")
#
#
# user1 = CV(name="Arthur,", surname="Demirchyan,", email="gamesrandom68@gmail.com,", age="18")
#
# print(user1.name, user1.surname, user1.email, user1.age)

# class Rectangle:
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def perimeter(self):
#         return (self.a * 2) + (self.b * 2)
#
#     def area(self):
#         return self.a * self.b
#
#
# per = Rectangle(a=4, b=5)
# print(per.perimeter())
# print(per.area())

# class Actor:
#
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age
#
#     def best_one(self):
#         print(f"The best actor is {self.name} {self.surname}, who is {self.age} years old!")
#
#
# actor1 = Actor("Ryan", "Gosling", 40)
# actor2 = Actor("Patrick", "Bateman", 45)
#
# Actor.best_one(actor1)


# string_ = "python"
# dic = {}
#
# for cr in string_:
#
#     if cr not in dic:
#         dic[cr] = 1
#
#     else:
#         dic[cr] += 1
#
# print(dic)

# class Circle:
#     def __init__(self):

# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def present(self):
#         return f"Hello there! My name is {self.name} and im {self.age} years old!"
#
#
# class Employee(Human):
#     def __init__(self, profession, company_name, *args, **kwargs):
#         self.profession = profession
#         self.company_name = company_name
#         super().__init__(*args, **kwargs)
#
#     def present(self):
#         return f"{super().present()}" \
#                f"My profession is {self.profession} and I'm working at {self.company_name}"
#
#
# class Student(Human):
#     def __init__(self, university, *args, **kwargs):
#         self.university = university
#         self.marks = []
#         super().__init__(*args, **kwargs)
#
#     def add_marks(self, grade):
#         self.marks.append(grade)
#
# class StudentEmployee(Student, Employee):
#
#
#
#
# human_ = Human("Arthur", 18)
# print(Human.present(human_))

# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def to_sorted_tuple(self):
#         return sorted((self.a, self.b, self.c))
#
#     def __eq__(self, other):
#         first = self.to_sorted_tuple()
#         second = other.to_sorted_tuple()
#
#         for i in range(3):
#             if first[i] != second[i]:
#                 return False
#         return True


# class A:
#     def __new__(cls):
#         print('Creation of A')
#         instance = super().__new__(cls)
#         return instance
#
#     def __init__(self):
#         print('Initialization')
#
#     def __del__(self):
#         print('Delete')
#
#
# a = A()
# del a


import json
import random

# users = []
#
# while True:
#     input_ = input("Name. Surname: ")
#     name = input_.split()[0]
#     surname = input_.split()[1]
#     dict_ = dict(
#         name=name,
#         surname=surname
#     )
#     users.append(dict_)
#
#     check = input("Enough? Type yes for exit. ")
#     if check == "yes":
#         break
#
# with open("user_list.txt", "w") as file:
#     for item in range(len(users)):
#         file.write(f"{item + 1}: {users[item]}\n")
#
# users = []
#
# with open("user_list.txt") as list_user:
#     for line in list_user:
#         print(line.strip())
#         # 1: {'name': 'John', 'surname': 'Don'} =>
#         # => 1: {name: John, surname: Don} => name: John, surname: Don} => name: John, surname: Don
#         str_dict = line.replace("'", "").split("{")[1].split("}")[0]
#         print(str_dict)
#
#         list_strings = str_dict.split(", ")  # name: John, surname: Don => ["name: John", "surname: Don"]
#         print(list_strings)
#
#         user_list = []
#         for item in list_strings:
#             user_list.append(item.split(": ")[1]) # in first circle item = "name: John"  in second circle "surname: Don"
#
#         print(user_list)  # ['John', 'Don']
#
#         dict_ = dict(
#             name=user_list[0],  # 'John'
#             surname=user_list[1]  # 'Don'
#         )
#         users.append(dict_)
# print(users)
#
# with open("user.json", "w") as json_:
#     json.dump(users, json_, indent=3)


# from datetime import datetime
#
# this_year = datetime.now().year
# this_month = datetime.now().month
# print(this_year)
#
#
# year_dict = dict(
#     year=this_year,
#     month=this_month
#
# )
#
# with open("data.json", "w") as data_json:
#     json.dump(year_dict, data_json, indent=4)

# import json
import requests
# import pprint


# def download_image(image):
#     response = requests.get(image)
#
#     with open("image.png", "wb") as img:
#         img.write(response.content)
#
#
# download_image(image=)


# response = requests.get('https://xkcd.com/')
# print(response.url)

# url_path = "https://api.isevenapi.xyz/api/iseven"
# response = requests.get(f"{url_path}/{7}/")
# r = response.json()
# pprint.pprint(r)

# params = {"name": "python", "school": "BITC"}
# path = "https://www.youtube.com/watch"
# response_ = requests.get("https://www.youtube.com/watch/", params=params)
# n = response_.json()
# print(n)
# print(response_.url)
# print(response_.text)
# response = requests.get("https://www.pinterest.com")
# print(response)
#
# print(response.json())


# def download_image(url, name):
#     try:
#         response_ = requests.get(url)
#     except Exception as err:
#         print(f"smth happened {err}")
#         return

import threading
import json
import requests
import datetime
import time


# def func_1():
#     for item in range(11):
#         time.sleep(0.1)
#         print(item)


# if __name__ == "__main__":
#     print(__name__, "threading")
# starting_time = datetime.datetime.today()
# print(starting_time)

# for i in range(4):
#     func_1()
#
# t = (datetime.today() - starting_time).seconds
#
# print(f"it took {t} seconds.")

# Using threads

# for i in range(4):
#     x = threading.Thread(target=func_1())
#     x.start()
#
# t = (datetime.datetime.today() - starting_time).seconds
#
# print(f"it took {t} seconds.")


# thread_list = []
# for i in range(3):
#     x = threading.Thread(target=func_1)
#     thread_list.append(x)
#     x.start()
#
# for thread in thread_list:
#     thread.join()
# t = (datetime.datetime.today() - starting_time).seconds
# print(f"it took {t} seconds.")

# def countdown(word):
#     for char in word:
#         yield char.upper()
#
#
# g_1 = countdown("hello")
# # print(next(g_1))
# # print(next(g_1))
# # print(next(g_1))
# for item in g_1:
#     print(item)

# def even_digits(num):
#     check = True
#     while check:
#         even_num = random.randint(0, num)
#         if even_num % 2 != 0:
#             even_num += 1
#         yield even_num
#
#
# g_2 = even_digits(1000)
# print(next(g_2))
# print(next(g_2))
# print(next(g_2))

# for num in g_2:
#     print(num)


# import json
# import requests
# import threading
#
#
# class ImgDownloader:
#     def __init__(self, path):
#         with open(path) as file:
#             self.image = json.load(file)
#
#     def download(self, url, name):
#         response = requests.get(url)
#         with open(f"{name}.png", "wb") as img:
#             img.write(response.content)
#             print(f"Image {name} is downloaded")
#
#     def with_threads(self):
#         thread_list = []
#         for image in self.image:
#             x = threading.Thread(target=self.download, args=(image["image_url"], image["url_name"]))
#             thread_list.append(x)
#             x.start()
#
#         for td in thread_list:
#             td.join()
#
#
# a = ImgDownloader(path="images.json")
# a.with_threads()


def decorator(func: callable) -> callable:
    print("Decorated!")

    def decor():
        print("----------")

        func()

        print("---finished---")

    return decor


@decorator
def text():
    print("Hello world!!!")


text()

