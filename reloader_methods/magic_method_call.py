class Person:
    title = "Person"
    lis = {}
    pis = []
    def __init__(self, name, age):
        self.name = name
        self.age = age



    def __repr__(self):
        return f" Person: {self.name}, {self.age}"

    def __call__(self, *args, **kwargs):
        return Person(name=self.name, age=self.age)

    def __getitem__(self, item):
        return self.pis[item]

    def __setitem__(self, key, value):
        pass
        #self.lis[key] = value
        #self.pis.append(value)



person = Person("Tupak", 33)
print(person)
p1 = person()
print(p1)
print(person[10])
person.lis['asdf'] = 3
print(person.lis['asdf'])
for i in range(7):
    person.pis.append(i)

print(*person.pis)

