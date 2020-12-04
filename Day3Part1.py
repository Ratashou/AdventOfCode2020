file = open(r"C:\Users\hoodm_000\Documents\Python Projects\AdventOfCode2020\Day3.txt", "r")

course = file.read()

file.close()

#create 2D array of course
course = course.split("\n")

xpos = 0
ypos = 0
answer = 0

#ypos max will be 1 less than the length
while ypos < len(course):
    if course[ypos][xpos] == "#":
        answer += 1
    xpos += 3
    ypos += 1
    if xpos > (len(course[0]) -1):
        xpos = xpos - len(course[0])

print(answer)
