import re

input = open("2024/day3/input.txt", 'r')
str =  input.read()
# str = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
# Part 1
matches = re.findall(r'mul[(](\d{1,3})[,](\d{1,3})[)]', str)
sum = 0
for match in matches:
    sum += int(match[0])*int(match[1])
print(sum)

# Part 2
sum = 0
matches = re.findall(r"(?>mul[(](\d{1,3})[,](\d{1,3})[)])|(?>(do(?:n't)?)[(][)])", str)
do = True
for match in matches:
    if match[2] == 'do':
        do = True
        continue
    if match[2] == "don't":
        do = False
        continue
    if do:
        sum += int(match[0])*int(match[1])
print(sum)