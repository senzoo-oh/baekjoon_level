total_of_amount_X= int(input())
the_number_of_product_N = int(input())
sum = 0

for i in range(the_number_of_product_N) :
  price, quantity = map(int,input().split())
  sum += (price * quantity)

if total_of_amount_X == sum :
  print ("Yes")
else:
  print ("No")