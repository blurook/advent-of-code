# Import data from input file
with open("2021\day_3\input.txt") as file:
    data = [line.strip() for line in file]

# Part 1

gamma = ''
epsilon = ''

for c in range(len(data[0])):
    num0 = 0
    num1 = 0
    for i in range(len(data)):
        if int(data[i][c]) == 1:
            num1 += 1
        else:
            num0 += 1
    if num0 > num1:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

print('Submarine power consumption: ', int(gamma,2)*int(epsilon,2))

# I'd like to revisit this part in the near future to get a better understanding of what happened here. I'm out of practice, clearly. Credit to Reddit user ithar14 for the code base.

print("----------") # Divider for part one and part 2 solutions in the console.

# Part 2

o2=data
for j in range(len(o2[0])):
    num0 = 0
    num1 = 0
    for i in range(len(o2)):
        if int(o2[i][j]) == 1 :
            num1 += 1
        else:
            num0 += 1  
    if num0>0 and num1>0:
        if num1 >= num0:
            o2 = list(filter(lambda a: int(a[j]) == 1, o2))
        
        if num0 > num1:
            o2 = list(filter(lambda a: int(a[j]) == 0, o2)) 

co2 = data
for j in range(len(co2[0])):
    num0 = 0
    num1 = 0
    for i in range(len(co2)):
        if int(co2[i][j]) == 1:
            num1 += 1
        else:
            num0 += 1 
    if num0>0 and num1>0:
        if num1 >= num0:
            co2 = list(filter(lambda a: int(a[j]) == 0, co2))
        if num0 > num1:
            co2 = list(filter(lambda a: int(a[j]) == 1, co2))
print('Sumbarine life support rating: ', int(o2[0], 2) * int(co2[0], 2))