my_info = {
    'name':'neo', 
    'job':'hacker',
    'mobile': '01053596596',
    'email': 'excelsior@gmail.com'
}

my_info[email]

hphk = [
    {
    'name': 'john',
    'email': 'john@hphk.io'
},

{
    'name': 'neo',
    'email': 'neo@hphk.io'
},

{
    'name': 'tak',
    'email': 'tak@hphk.io',
    'married': False
}
]

type(hphk) # list
hphk[]


p = hphk[2]
print(type(p)) # dic

print(p['name'])

# p['name'] = hphk[2]['name']