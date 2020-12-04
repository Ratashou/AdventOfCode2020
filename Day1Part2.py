file = open(r"C:\Users\hoodm_000\Documents\Python Projects\AdventOfCode2020\Day1.txt", "r")

expenseList = []
for line in file:
    line = int(line)
    expenseList.append(line)

answer = 0
for number in expenseList:
    for number2 in expenseList:
        for number3 in expenseList:
            #compare position against every other number twice to find 3 that sum to 2020
            if number != number2 and number != number3 and number2 != number3 and number + number2 + number3 == 2020:
                answer = number * number2 * number3
                break
    if answer != 0:
        break
    #don't need to compare this number against another one again
    del expenseList[0]

print(answer)
file.close()
