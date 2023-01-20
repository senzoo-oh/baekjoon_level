num_array = []

for i in range(10) :
  num_array.append(int(input())%42)
print(len(set(num_array)))