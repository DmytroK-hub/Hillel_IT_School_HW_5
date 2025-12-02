import string
import keyword

name = input("Введіть ім'я змінної: ")

def is_valid(name):
    if not name or name in keyword.kwlist:
        return False
    if name[0].isdigit():
        return False
    if name.count("_") > 1:
        return False
    allowed = string.ascii_lowercase + string.digits + "_"
    for ch in name:
        if ch not in allowed:
            return False
    return True

print(is_valid(name))
