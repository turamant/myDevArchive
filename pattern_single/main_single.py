from pattern_single import config


class Singleton(object):
    def __new__(cls, *args):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

    def __init__(self, x):
        self.x = x


class SinglePat:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, x):
        self.x = x


if __name__ == '__main__':
    set1 = config.setting.Name
    set2 = config.setting.Name
    print(set1, id(set1))
    print(set2, id(set2))
    if set1 is set2:
        print("single")
    else:
        print('This is not одиночка')

    sing1 = SinglePat(1)
    singl2 = SinglePat(1)
    print(id(sing1), ':', id(singl2))
    print(sing1.x, singl2.x)

    print('#' * 28)
    s = Singleton(1)
    s2 = Singleton(2)
    if not id(s) is id(s2):
        print("singleton!", id(s),':', id(s2))
