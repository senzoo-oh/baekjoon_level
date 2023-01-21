num_from_1_10001 = set(range(1,10001))
num_to_remove = set()

for i in num_from_1_10001 :
    for j in str(i) :
        i += int(j)
    num_to_remove.add(i)

magic_number = num_from_1_10001 - num_to_remove
for i in sorted(magic_number) :
    print(i)