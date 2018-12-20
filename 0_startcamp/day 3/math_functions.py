print(__name__)

def average(numbers): # 함수안에서 함수 갖다쓸 수 있다.
    return sum(numbers) / len(numbers) # result = sum(nubers) / len(numbers)
                                       # return result 이래도 된다

def cube(x):
    return x * x * x


# 1. 평균값을 구하시오

def main(): # 이걸 해야 math_functions를 import한 곳에서 굳이 또 값 안나옴!
    my_score = [79, 84, 66, 93]
    print(average(my_score))
    print(cube(3))


if __name__ == '__main__':
    main() #위의 거랑 같은 말.