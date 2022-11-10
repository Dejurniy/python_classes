import os

# name = "dir_1"
# os.mkdir(f"{os.getcwd()}/{name}")
# print(os.getcwd())
# os.chdir("dir_1")
# print(os.getcwd())
# print(os.name)

file_path = os.path.join(os.getcwd(), "dir_1", "file.txt")
file2_path = os.path.join(os.getcwd(), "dir_1", "file2.txt")

# Ex. 1

num1 = 0
num2 = 0
dict_ = {}
with open(file_path, "r") as file:
    for line in file:
        num1 += 1
        for digit in line:
            if digit.isdigit():
                num2 += 1
        dict_[num1] = num2
        num2 = 0


print(dict_)

# Ex. 2

user_num = input("Write a number: ")
num_ = 0

with open(file_path, "r") as file:
    for line in file:
        for digit in line:
            if user_num == digit:
                num_ += 1

print(f"There are {num_} of specific number in text.")

# Ex. 3

list_ = []

with open(file_path, "r") as file:
    text = file.read().split()
    for letter in text:
        if letter.startswith("<<") and letter.endswith(">>"):
            list_.append(letter)

print("Special words are:", list_)


# Ex. 4
string = ""

with open(file_path, "r") as file:
    for line in file:
        for letter in line:
            if letter.isalpha():
                string += letter

with open(file2_path, "a") as file2:
    file2.write(string)















