file = open(r"C:\Users\hoodm_000\Documents\Python Projects\AdventOfCode2020\Day1.txt", "r")

expenseList = []
for line in file:
    line = int(line)
    expenseList.append(line)

answer = 0
for number in expenseList:
    for number2 in expenseList:
        #compare position against every other number to find 2 that sum to 2020
        if number != number2 and number + number2 == 2020:
            answer = number * number2
            break
    if answer != 0:
        break
    #don't need to compare this number against another one again
    del expenseList[0]

print(answer)
file.close()
