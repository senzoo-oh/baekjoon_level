array = []

for i in range(9) :
  array.append(int(input()))
print(max(array))
print(array.index(max(array))+1)


# while 1:
#   try:
#     num = int(sys.stdin.readline())
#     array.append(num)
#   except:
#     break