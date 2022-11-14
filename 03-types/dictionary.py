'''
Slovníky (dictionaries) podobně jako seznamy v sobě obsahují další hodnoty.
Na rozdíl od seznamů, ve kterých jsou všechny prvky uspořádané do jedné sekvence, ve slovnících máme dva druhy prvků:
klíč (angl. key) a hodnotu (angl. value).
Každému klíči je přiřazena jedna hodnota.
'''

# Collection which is unordered, changeable and indexed.
# In Python dictionaries are written with curly brackets, and they have keys and values.
car = {
  'brand': 'Ford',
  'model': 'Mustang',
  'year': 1964
}

point = {'x': 1, 'y': 10}

# Vytvoření slovníku pomocí konstruktoru dict()
point = dict(x=1, y=10)

# Změna hodnoty jednoho prvku slovníku
point['x'] = 2

# Vložení nového prvku do slovníku
point['z'] = 20

# Přístup k položkám slovníku
print(f'point["x"]: {point["x"]}')
print(f'point.get("x"): {point.get("x")}')

# Zjištění, zda existuje hodnota
if 'z' in point:
    print(f'point.get("z"): {point.get("z")}')

# Když hodnota neexistuje, vrací 0    
print(f'point.get("v", 0): {point.get("v", 0)}')

# Odstranění prvku ze slovníku  
del point['x']
print(f'point: {point}')

print(f'car.pop(): {car.pop("model")}')

# Odstraní poslední prvek ze slovníku
print(f'car.popitem(): {car.popitem()}')

# Procházení slovníkem - vypíše vždy pár klíč - hodnota
for key, value in point.items():
    print(f'{key} - {value}')

# Dictionary comprehension - zkráceně vytvoří slovník, jehož klíče tvoří čísla od 0 do 9 a hodnoty druhé mocniny 
values = {x: x ** 2 for x in range(10)}
print(f'values: {values}')

# Unpacking operator - pro slovníky se používají **
first = {'x': 1, 'y': 2}
second = {'x': 10, 'z': 5}
common = {**first, 'a': 15, **second}
print(f'common: {common}')

# Nested dictionary - vnořené slovníky
myfamily = {
  'child1' : {
    'name' : 'Emil',
    'year' : 2004
  },
  'child2' : {
    'name' : 'Tobias',
    'year' : 2007
  },
  'child3' : {
    'name' : 'Linus',
    'year' : 2011
  }
}
print(f'Nested dictionary myfamily: {myfamily}')

# ??? 4. cvičení ???
# a) Navrhněte vlastní vnořený slovník tvořený 3 reálnými objekty s aspoň 6 klíči tak, abyste kromě jednoduchých
# datových typů (čísla, řetězce, boolean) ve slovníku vhodně využili i všechny v tomto bloku probrané strukturované
# typy - tedy set, tuple a list.
# Volte příklad vycházející z reality - např. slovník aut, slovník filmů, slovník historických postav atd.
# b) Pomocí vhodných metod přidejte do slovníku nový prvek a nějaký starý naopak odstraňte
# c) Proveďte výpis obsahu slovníku tak, aby i v konzoli vytvořil hezky naformátovanou tabulku i s mezerami
# viz níže uvedený vzor.
'''
Slovník myfamily
---------------------------------------------
child           name                year
---------------------------------------------
child1          Emil                2004
child2          Tobias              2007
child3          Linus               2011
---------------------------------------------
Počet záznamů: 3
'''

groups = {
  'group1': {
    'name': 'BTS',
    'debut-year': 2013,
    'favourite': True,
    'genre': ('K-pop','EDM', 'R&B', 'Rock'),
    'members': {'RM', 'Jin', 'Suga', 'J-hope', 'Jimin', 'V', 'Jungkook'},
    'new songs': ['Yet To Come', 'Run BTS']
  },
  'group2': {
    'name': 'Stray Kids',
    'debut-year': 2018,
    'favourite': True,
    'genre': ('K-pop','Hip hop', 'Electronic'),
    'members': {'Bang Chan','Lee Know','Changbin', 'Hyunjin', 'Han', 'Felix', 'Seungmin', 'I.N'},
    'new songs': ['CASE 143', 'CHILL']
  },
  'group3': {
    'name': 'Coldplay',
    'debut-year': 1996,
    'favourite': False,
    'genre': ('Alternative rock', 'Electronic'),
    'members': {'Ch. Martin', 'J. Buckland', 'G. Berryman', 'W. Champion', 'P. Harvey'},
    'new songs': ['Biutyful', 'Let Somebody Go']
  }
}

groups['group3']['members'].add('Timmy')
del groups['group2']['debut-year']

print("\nslovnik groups")
print("-" * 184)
print ("{:<10} {:<12} {:<12} {:<10} {:<30} {:<70} {:<10}".format('groups','name','debut-year','favourite','genre','members','new songs'))
print("-" * 184)
for k, info in groups.items():
  print("{:<10} {:<12} {:<12} {:<10} {:<30} {:<70} {:<10}".format(k,str(info['name']),str(info['debut-year']) if 'debut-year' in info else '----',str(info['favourite']),
  ','.join(str(x) for x in info['genre']),','.join(str(x) for x in info['members']),','.join(str(x) for x in info['new songs'])))
print("-" * 184)
print("Počet záznamů:", len(groups))