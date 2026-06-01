# Task 1

def add_to_dict(dictionary: dict, element: dict) -> dict:
    if not isinstance(dictionary, dict):
        print(f"Error: dictionary must be dict, got {type(dictionary).__name__}")
        return {}
    if not isinstance(element, dict):
        print(f"Error: element must be dict, got {type(element).__name__}")
        return {}
    for key, value in element.items():
        dictionary[key] = value
    return dictionary


students1 = {"Anna": 99, "Vadim": 98, "Alex": 100}
new_dict = {"Nikita": 88}

print(add_to_dict(students1, new_dict))


# Task 2
def char_freq(s: str) -> dict:
    if not isinstance(s, str):
        print(f"Error: s must be str, got {type(s).__name__}")
        return {}
    if s == "":
        print("Error: s cant be empty")
        return {}
    dct = {}
    for i in s.lower():
        if i == " ":
            continue
        if i in dct:
            dct[i] += 1
        else:
            dct[i] = 1
    return dct


print(char_freq("HellooO World"))


# Task 3
def invert_dict(dire: dict) -> dict:
    if not isinstance(dire, dict):
        print(f"Error: dire must be dict, got {type(dire).__name__}")
        return {}
    if dire == {}:
        print("Error: dire cant be empty")
        return {}
    dct1 = {}
    for key, value in dire.items():
        dct1[value] = key
    return dct1


print(invert_dict(students1))


# Task 4:
def invert_dict_not_uniq(dirc: dict) -> dict:
    if not isinstance(dirc, dict):
        print(f"Error: dirc must be dict, got {type(dirc).__name__}")
        return {}
    if dirc == {}:
        print("Error: dire cant be empty")
        return {}
    dct2 = {}
    for key, value in dirc.items():
        if value in dct2:
            dct2[value].append(key)
        else:
            dct2[value] = [key]
    return dct2


directory3 = {'Anna': 99, 'Vadim': 99, 'Alex': 100, 'Nikita': 88}
print(invert_dict_not_uniq(directory3))
