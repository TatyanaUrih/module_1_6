# DZ
# 2
my_dict = {'Ivan': 1995, 'Petya': 1990, 'Oleg': 2000}
print("Dict:", my_dict)
print("Existing value:", my_dict['Oleg'])
print("Not existing value:", my_dict.get('Nikita'))
my_dict.update({'Nikita': 2005, 'Sasha': 2010})
del_value = my_dict.pop('Sasha')
print("Deleted value:", del_value)
print("Modified dictionary:", my_dict)

print("")
# 3
my_set = {5,4,3,3,5,2,1,2,4, 'Oleg', 'Oleg2', 'Oleg', (8,7,6), (8,7,6), 1.5, 2.0, 3.7, 2.0}
print("Set:", my_set)
my_set.add(100)
my_set.add('Ivan')
my_set.discard('Oleg2')
print("Modified set:", my_set)
