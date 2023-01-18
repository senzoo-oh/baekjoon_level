import sys
the_number_of_test = int(input())

for i in range(the_number_of_test) :
  A, B = map(int,sys.stdin.readline().split())
  print(A + B)

# a, b = map(int,input().split())
# print(type(a))

# c, d = input().split()
# print(type(c))