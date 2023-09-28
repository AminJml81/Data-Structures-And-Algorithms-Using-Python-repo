from hashmap import HashMap

a = HashMap()
names = [['amin', 'jamali'], ['ali', 'moghimi'], ['akram', 'khorasany'], ['rojan', 'ashrafi'],
         ['mohammadamin', 'hashemi'], ['koorosh', 'zamani'], ['dorsa', 'alifekr'], ['soheil', 'jafari'],
         ['arian', 'farzaneh'], ['kiana', 'alimadadi'], ['mobina', 'alimohammdi']]

for first_name, last_name in names:
    a.add(first_name, last_name)

a['rojan'] = 'karimi'
a['dorsa'] = 'bifekr'
a['ali'] = 'karimi'
a.remove('dorsa')
for key, value in a:
    print(key, value)
