my_numbers = [1, 2, 3, 4, 5, 8]
real_numbers = [1, 2, 3, 4, 5, 6]
bonus = 7

count = 0 # 카운트를  제로부터 시작  ex) n=0
for my_number in my_numbers:
    for real_number in real_numbers:
        if my_number == real_number:
            count +=1

print (count)

if count == 6:
    print(1)
elif count == 5 and bonus in my_numbers:
    print(2)
elif count == 5:
    print(3)


# list = [1, 2, 3]
# tuple = (1, 2, 3)

# set = {1, 2, 3}