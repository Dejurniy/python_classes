import json
import yaml

# Ex. 1

with open("sample.json", "r") as js_file:
    text = json.load(js_file)


with open("user_js.txt", "w") as user_js:
    json.dump(text, user_js, indent=4)


# Ex. 2

with open("sample.json", "r") as js_file:
    text = json.load(js_file)

with open("user.yaml", "w") as user_yaml:
    yaml.safe_dump(text, user_yaml)

# Ex. 3

with open("user.yaml") as y_file:
    text = yaml.safe_load(y_file)

with open("user_2.json", "w") as js_file2:
    json.dump(text, js_file2, indent=4)

# Ex. 4

with open("user.yaml") as y_file:
    text = yaml.safe_load(y_file)

with open("user_yaml.txt", "w") as yml_txt:
    yaml.dump(text, yml_txt)








