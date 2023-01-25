count = 0
for i in range(int(input())) :
    word = input()
    if len(word) == len(set(word)) :
        count += 1
        continue
    num = word[0]
    alphabet = []
    alphabet.append(num)
    for j in word[1:] :
        if (j in alphabet) & (num == j) :
            num = j
            continue
        elif (j not in alphabet) & (num != j) :
            num = j
            alphabet.append(j)
        else :
            break
    if (j in alphabet) & (num != j) :
        continue
    count += 1

print(count)