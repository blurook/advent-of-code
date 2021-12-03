#Import data from input file
with open("2021\day_1\input.txt") as file:
    data = [int(line.strip()) for line in file]

# Part 1

N = len(data)

count = 0

for i in range(1, N):
    if data[i] > data[i - 1]:
        count += 1

print(count)

# Part 2

count = 0

for i in range(1, N):
    if data[i] > data[i - 3]:
        count += 1

print(count)