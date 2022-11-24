string = "Это ставит эту штуку в зону досягаемости России. Мы намеренно пытаемся быть провыкационными без того, чтобы эскалировать. Мы пытаемся сдержать российскую агрессию, экспансивное поведение, показывая расширенные возможности союзников», — приводит издание Stars and Stripes заявление подполковника европейского командования специальных операций Лоуренса Мельникова"

list_word =list()


for char in string:
    if char not in list_word:
        list_word.append(char)

print(list_word)
print("#" * 28)

string1 = string.split(' ')
print(string1)
my_set = set()
for i in string1:
    my_set.add(i)
print(my_set.difference())

