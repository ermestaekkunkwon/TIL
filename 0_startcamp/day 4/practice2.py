from random import choice

row = ['a','b','d','e','g','h']
col = list(range(2, 7))

coord = [choice(row), choice(col)]
print(coord)