number = list(map(str,input().split()))

reversed_num1 = int("".join(reversed(number[0])))
reversed_num2 = int("".join(reversed(number[1])))

if reversed_num1 > reversed_num2 :
    print(reversed_num1)
else :
    print(reversed_num2)