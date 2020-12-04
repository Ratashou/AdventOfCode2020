file = open(r"C:\Users\hoodm_000\Documents\Python Projects\AdventOfCode2020\Day2.txt", "r")

answer = 0
for line in file:
    entry = []
    #remove new line gubbins
    line = line.strip('\n')
    
    #this creates a list where each important segment of line is its own entry
    entry = line.split()
    #split up numbers at the start to account for potential double digits
    temp = entry[0].split("-")

    #Now to check if password is valid
    lowerValue = int(temp[0])
    upperValue = int(temp[1])
    reqChar = entry[1][0]
    times = 0
    for chars in entry[2]:
        if chars == reqChar:
            times += 1
    if times >= lowerValue and times <= upperValue:
        answer += 1

print(answer)

file.close()

