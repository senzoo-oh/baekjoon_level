# 10000 이하의 소수를 구하는 함수
def find_prime_number() :
    numbers = [True] * 10001
    for i in range(2, 101) :
        if numbers [i] == True :
            for j in range(i + i, 10000, i) :
                numbers[j] = False
    prime = [i for i in range(2, 10001) if numbers[i] == True]
    return prime

T = int(input())
prime = find_prime_number()

for i in range(T) :
    n = int(input())
    num1 = n // 2
    num2 = n - num1
    while True :
        if (num1 not in prime) | (num2 not in prime):
            num1 -= 1
            num2 = n - num1
        else :
            break
    print(num1, num2)