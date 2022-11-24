group = ['ZZ Top', 'ACDC', 'Accept', 'Led Zeppelin']
score = [155, 201, 99, 201]

muzik = {'ZZ Top': 155,
         'ACDC': 201,
         'Accept': 99,
         'Led Zeppelin': 201
         }


new_list = list()

for i in zip(group, score):
    new_list.append(i)

print("Новый список: ", new_list)
print(sorted(new_list, key=lambda x: x[1]))

print("...", sorted(muzik.items(), key=lambda x: x[1]))

