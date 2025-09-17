input = open("2024/day1/input.txt", 'r')
stop: bool = 0
left = []
right = []

# Part 1
while True :
    line = input.readline()
    if line == '':
        break
    digits = line.split()
    left.append(digits[0])
    right.append(digits[1])
left.sort()
right.sort()
sum = 0
for x,y in zip(left, right):
    sum += abs(int(x)-int(y))
print('Part 1 ', sum)   

# Part 2

## build count dic
index = 0
count_dict = {}
while index < len(right):
    count = 1
    pointer = index
    if pointer+1 >= len(right):
        count_dict[right[index]] = count
        break
    while right[pointer+1] == right[pointer]:
        count+=1
        pointer+=1
    count_dict[right[index]] = count
    index=pointer+1

## lookup counts
sum = 0
for x in left:
    sum += int(x) * count_dict.get(x, 0)
print('Part 2 ', sum)   