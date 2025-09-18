input = open("2024/day2/input.txt", 'r')
sum = 0
sum_with_dampener = 0

def isDiffSafe(diff: int, prev_diff: int) -> bool:
    if abs(diff) == 0 or abs(diff) > 3:
        return False
    if prev_diff*diff < 0:
        return False
    return True

def isLvlSafe(lvl: list) -> bool:
    index = 0
    prev_diff = 0
    while index+1 < len(lvl):
        diff = int(lvl[index]) - int(lvl[index+1])
        if not isDiffSafe(diff, prev_diff):
            return False
        prev_diff=diff
        index+=1
    return True

while True:
    line = input.readline()
    if line == '':
        break
    values = line.split() 
    dampened = False
    if not isLvlSafe(values):
        for idx, x in enumerate(values):
            new_values = values.copy()
            new_values.pop(idx)
            if isLvlSafe(new_values):
                dampened = True
                break
        if dampened:
            sum_with_dampener+=1
            continue
        continue
    sum+=1
    sum_with_dampener+=1

print(sum)
print(sum_with_dampener)