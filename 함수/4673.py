number = list(map(str,range(1,10001)))
nums_by_num = []

for num in number :
    next_number = int(num)
    for j in range (len(num)) :
        next_number += int(num[j])
    next_number = str(next_number)
    nums_by_num.append(next_number)

number = list(set(number) - set(nums_by_num))
number = [int(x) for x in number]
number.sort()
for i in range(len(number)) :
    print(number[i])