from darksky import forecast

multicampus = forecast('2b50570745d80a1cc39c7ee163c23cbc', 37.501588, 127.039681)

print(multicampus ['currently']['summary'])
print(multicampus ['currently']['temperature'])

# import requests

# url = ''

# res = requests.get(url)
# data = res.json())

# print(data['currently'][])