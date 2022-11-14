'''
Tuples - neměnitelné n-tice hodnot (seřazený seznam prvků)
V Pythonu se tuples píší do kulatých závorkách.
'''

# Vytvoření tuples
numbers = (1, 2, 3)
print('numbers: ', numbers)
print('Type(numbers): ',type(numbers))

chars = tuple('Hello world')
print('chars: ', chars)
print('Type(chars): ',type(chars))

# To create a tuple with only one item, you have add a comma after the item, unless Python will not recognize the variable as a tuple.
# Pro vytvoření tuple jenom s jednou hodnotou, musíte zadat čárku za hodnotou, pokud Python nerozezná proměnou jako tuple.
colors = ('red',)
print('colors: ', colors)

# Součet tuples
print(f'chars + numbers: {chars + numbers}')

# Výpis hodnot 
# You can specify a range of indexes by specifying where to start and where to end the range.
# Můžete zadat délku indexů pomocí zadání kde začít a kde ukončit délku.
# When specifying a range, the return value will be a new tuple with the specified items.
# Když zadáte délku, vrácená hodnota bude nový tuple se zadanými hodnotami.
print(f'chars[2:5]: {chars[2:5]}')

# Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.
# Záporné indexování znamená začátek od konce, -1 označuje poslední hodnotu, -2 označuje předposlední hodnotu atd.
# Specify negative indexes if you want to start the search from the end of the tuple:
# Pokud chcete záčit od konce tuple, zadejte záporný index.
# This example returns the items from index -4 (included) to index -1 (excluded)
# Tenhle příklad vrací hodnotu od indexu -4 (zahrnuto) do indexu -1 (vyloučeno)
print(f'chars[-4:-1]: {chars[-4:-1]}')

# To determine how many items a tuple has, use the len() method:
# Pro určení kolik tuple má hodnot, použijte len() metodu:
print(f'len(chars): {len(chars)}')

# Zjištění prvního výskytu a počtu výskytu prvku
if 'l' in chars:
    print(f'chars.index("l"): {chars.index("l")}')
    print(f'chars.count("l"): {chars.count("l")}')

# Záměna hodnot proměnných
x = 10
y = 2
x, y = y, x
print(f'x: {x}, y: {y}')
