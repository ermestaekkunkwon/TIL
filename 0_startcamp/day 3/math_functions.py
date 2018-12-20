def average(numbers): # 함수안에서 함수 갖다쓸 수 있다.
    return sum(numbers) / len(numbers) # result = sum(nubers) / len(numbers)
                                       # return result 이래도 된다

def cube(x):
    return x * x * x


# 1. 평균값을 구하시오
my_score = [79, 84, 66, 93]
print(my_score)
print(average(my_score))
print(cube(3))