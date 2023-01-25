word = input()
time = 0

for i in word :
    match i :
        case "A"|"B"|"C" :
            time += 3
        case "D"|"E"|"F" :
            time += 4
        case "G"|"H"|"I" :
            time += 5
        case "J"|"K"|"L" :
            time += 6
        case "M"|"N"|"O" :
            time += 7
        case "P"|"Q"|"R"|"S" :
            time += 8
        case "T"|"U"|"V" :
            time += 9
        case "W"|"X"|"Y"|"Z" :
            time += 10
print(time)