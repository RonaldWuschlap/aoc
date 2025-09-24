input = open("2024/day5/input.txt")

class rule:
    def __init__(self, value: int):
        self.value = int
        self.after = []

    def addAfter(self, value: int):
        self.after.append(value)
        return self

rules: dict[int, rule] = {}
updates = []

while True:
    ruleTxt = input.readline()
    if ruleTxt == "\n":
        break
    arr = (list(map(int, ruleTxt.rstrip("\n").split("|"))))
    rule1 = rules.get(arr[0])
    if rule1 == None:
        rules[arr[0]] = rule(arr[0]).addAfter(arr[1])
    else:
        rule1.addAfter(arr[1])

updates = [list(map(int, line.split(','))) for line in input.readlines()]
sum_correct = 0
sum_fixed = 0

#Part 1 check update for validity
def checkUpdate(update: list) -> bool:
    for idx, page in enumerate(update):
        list_before = update[:idx]
        rule_local = rules.get(page)
        if rule_local == None:
            continue
        if any(v in rule_local.after for v in list_before):
            return False
    return True

#Part 2 Bubble sort to fix broken updates
def fixUpdate(update: list) -> list:
    n = len(update)
    for i in range(n):
        for j in range(0, n-i-1):
            rule_local = rules.get(update[j])
            if rule_local == None:
                continue
            if update[j+1] not in rule_local.after:
                update[j], update[j+1] = update[j+1], update[j]
                swapped = True
        if not swapped:
            break
    return update
          

for update in updates:
    if not checkUpdate(update):
        fix_updated = fixUpdate(update)
        sum_fixed += fix_updated[len(fix_updated) // 2]
        continue
    sum_correct += update[len(update) // 2]

print(sum_correct)
print(sum_fixed)