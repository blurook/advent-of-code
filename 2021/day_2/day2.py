#Import data from input file
with open("2021\day_2\input.txt") as file:
    data = [line.strip() for line in file]

# Part 1

hp = 0
vp = 0

for d in data:
    k,v = d.split()

    if k == "forward":
        hp += int(v)
    
    if k == "down":
        vp += int(v)
    
    if k == "up":
        vp -= int(v)

result = (hp*vp)

print("Horizontal: ", hp)
print("Vertical: ", vp)

print("Site input:", result)

# Part 2

aim = 0
hp = 0
vp = 0

for d in data:
    k,v = d.split()

    if k == "forward":
        hp += int(v)
        vp += aim * int(v)
    
    if k == "down":
        aim += int(v)
    
    if k == "up":
        aim -= int(v)

print("----------------") # Divider for the part one and two results

print("Aim: ", aim)
print("Depth: ", vp)
print("Horizontal: ", hp)

print("Site input: ", hp*vp)