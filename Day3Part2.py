file = open(r"C:\Users\hoodm_000\Documents\Python Projects\AdventOfCode2020\Day3.txt", "r")

course = file.read()

file.close()

#create 2D array of course
course = course.split("\n")

def slope(theRight, theDown):
    xpos = 0
    ypos = 0
    answer = 0

    #ypos max will be 1 less than the length
    while ypos < len(course):
        if course[ypos][xpos] == "#":
            answer += 1
        xpos += theRight
        ypos += theDown
        if xpos > (len(course[0]) -1):
            xpos = xpos - len(course[0])
    return answer

finalAnswer = 1

while True:
    print("Enter movement to the right or 'done' if done")
    right = input()
    if right == "done":
        break
    else:
        right = int(right)

    print("Enter movement down")
    down = int(input())

    finalAnswer = finalAnswer * slope(right,down)    

print(finalAnswer)
