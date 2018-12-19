dict = {
    'a': [1,2,3],
    'b': [3,2,1]
}

for key, value in dict.items():
    print(key, max(value))