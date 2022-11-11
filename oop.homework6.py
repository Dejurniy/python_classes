import json

# Ex. 1

with open("sample.json", "r") as js_file:
    text = js_file.read()


with open("user_js.txt", "w") as user_js:
    data = user_js.write(text)


# Ex. 2

with open("sample.json", "r") as js_file:
    text = js_file.read()

with open("user.yaml", "w") as user_yaml:
    user_yaml.write(text)

# Ex. 3

with open("user.yaml") as y_file:
    text = y_file.read()

with open("user_2.json", "w") as js_file2:
    js_file2.write(text)

# Ex. 4

with open("user.yaml") as y_file:
    text = y_file.read()

with open("user_yaml.txt", "w") as yml_txt:
    yml_txt.write(text)









