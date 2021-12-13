textfile = open("advent2.txt", "r")

data = []
for line in textfile:
    data.append(line)


forward = 0
height = 0
aim = 0

for i in data:
    command = i.split(" ")
    if (command[0] == "forward"):
        forward = forward + int(command[1])
        height = height + (aim*int(command[1]))
    elif (command[0] == "up"):
        aim = aim - int(command[1])
    elif (command[0] == "down"):
        aim = aim + int(command[1])
print(int(forward * height))
