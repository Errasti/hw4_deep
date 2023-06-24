def dictionaizer(**kwargs):
    res = {}
    for key, value in kwargs.items():
        new_key = value
        if not isinstance(value, (int, float, str, tuple, frozenset)):
            new_key = str(value)
        res[new_key] = key
    return res


result = dictionaizer(number=123, txt="test", lst=[22, 66, 234])
print(result)
