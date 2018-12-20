my_numbers = set([1, 2, 3, 4, 5, 8])
real_numbers = set([1, 2, 3, 4, 5, 6])
bonus = 7

match_count = len(my_numbers & real_numbers)
print(match_count)

if match_count == 6: # same meaning of if diff == 0:
    print('1등')
elif match_count == 5 and bonus in my_numbers:
    print('2등')
elif match_count == 5:
    print('3등')
elif match_count == 4:
    print('4등')
elif match_count == 3:
    print('5등')
else:
    print('6등')

    # {1, 2, 3} 클래스는 set으로 된다.
    # {1, 2, 3} - {2, 3, 4} = {1}