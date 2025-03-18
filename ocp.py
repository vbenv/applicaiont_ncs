import time

def time_measure_decorator(f):
    def wrapper(*args):
        s = time.time()         # start
        r = f(*args)            # function
        e = time.time()         # end
        print(e-s)
        return r
    return wrapper


@time_measure_decorator
def one_to_n_loop(n):           # O(n)
    result = 0
    for i in range(1, n+1):
        result += i
    return result

@time_measure_decorator
def one_to_n_math(n):           # O(1)
    r = n * (n + 1) // 2
    return r

# 함수 실행
number = int(input("정수 입력 : "))
print(one_to_n_loop(number))


number = int(input("정수 입력 : "))
print(one_to_n_math(number))