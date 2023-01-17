# num1, num2, num3 = map(int, input().split())

# if (num1 == num2 == num3) :
#   num = num1
#   prize = 10000 + (num *1000)
#   print(prize)
# elif (num1 == num2) :
#   num = num1
#   prize = 1000 + (num*100)
#   print(prize)
# elif (num1 == num3) :
#   num = num1
#   prize = 1000 + (num*100)
#   print(prize)
# elif (num2 == num3) :
#   num = num2
#   prize = 1000 + (num*100)
#   print(prize)
# else :
#   if (num1 > num2) & (num1 > num3) :
#     num = num1
#     prize = num*100
#     print(prize)
#   elif (num2 > num1) & (num2 > num3) :
#     num = num2
#     prize = num*100
#     print(prize)
#   else :
#     num = num3
#     prize = num*100
#     print(prize)


dice1, dice2, dice3 = map(int, input().split())

if (dice1 == dice2 == dice3) :
  print(10000 + (dice1)*1000)
elif (dice1 == dice2) | (dice1 == dice3) :
  print(1000 + dice1 * 100)
elif (dice2 == dice3) :
  print(1000 + dice2 * 100)
else :
  print(max(dice1,dice2,dice3)*100)