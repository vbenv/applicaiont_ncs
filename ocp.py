import time

def one_to_n_loop(n):           # O(n)
    s = time.time()
    result = 0
    for i in range(1, n+1):
        result += i
    e = time.time()
    print(e-s)
    return result

def one_to_n_math(n):           # O(1)
    s = time.time()
    r = n * (n + 1) // 2
    e = time.time()
    print(e-s)
    return r

# 함수 실행
number = int(input("정수 입력 : "))
print(one_to_n_loop(number))


number = int(input("정수 입력 : "))
print(one_to_n_math(number))