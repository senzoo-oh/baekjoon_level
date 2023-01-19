first_num = int(input())
temporary_num = first_num
sum = 0
count = 0

while True :
  sum = (temporary_num//10) + (temporary_num%10)
  count += 1
  new_number = (((temporary_num%10)*10) + (sum%10))
  if (new_number == first_num) :
    break
  temporary_num = new_number
print(count)