import string
import random
import requests


# Ex. 1

def password_generator(generator):
    lenght = 12
    gen = string.ascii_letters + string.digits

    for item in range(lenght):
        generator += random.choice(gen)
    yield generator


password = ""
g_1 = password_generator(password)
print(g_1)
print(next(g_1))


# Ex. 2

def quotes_generator(url):
    while True:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            yield data


g_2 = quotes_generator("https://zenquotes.io/api/random")
print(next(g_2))
print(next(g_2))
