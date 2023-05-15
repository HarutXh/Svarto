class MyDictionary:
    def __init__(self, dct):
        self.__dct = dct

    def clear(self):
        for key in list(self.__dct.keys()):
            del self.__dct[key]
        return self.__dct

    def copy(self):
        new_dict = {}
        for key, value in self.__dct.items():
            new_dict[key] = value
        return new_dict

    def fromkeys(self, keys, value=None):
        new_dict = {}
        for key in keys:
            new_dict[key] = value
        return new_dict

    def get(self, key, default=None):
        if key in self.__dct:
            return self.__dct[key]
        else:
            return default

    def items(self):
        items_list = []
        for key in self.__dct:
            items_list.append((key, self.__dct[key]))
        return items_list

    def keys(self):
        keys_list = []
        for key in self.__dct:
            keys_list.append(key)
        return keys_list

    def pop(self, key, default=None):
        if key in self.__dct:
            value = self.__dct[key]
            del self.__dct[key]
            return value
        else:
            return default

    def pop(self, key, default=None):
        if key in self.__dct:
            value = self.__dct[key]
            del self.__dct[key]
            return (key, value)
        else:
            return (key, default)

    def popitem(self):
        if len(self.__dct) == 0:
            raise KeyError("popitem(): dictionary is empty")
        key, value = self.__dct.popitem()
        return key, value

    def setdefault(self, key, default=None):
        if key not in self.__dct:
            self.__dct[key] = default
        return self.__dct[key]

    def update(self, other):
        for key, value in other.items():
            self.__dct[key] = value
        return self.__dct

    def values(self):
        return [value for key, value in self.__dct.items()]


if __name__ == "__main__":
    dct = MyDictionary({"key1": "value1", "key2": "value2", "key3": "value3"})
    keys = {"key1", "key2", "key3"}
    default_value = "default"
    print(dct.copy())
    print(dct.fromkeys(keys, default_value))
    print(dct.get("key1"))
    print(dct.items())
    print(dct.keys())
    print(dct.values())
    print(dct.update({"key4": "value4", "key5": "value5"}))
    print(dct.setdefault("key1", "value1"))
    print(dct.pop("key1"))
    print(dct._MyDictionary__dct)
    print(dct.popitem())
    print(dct._MyDictionary__dct)
    print(dct.clear())
