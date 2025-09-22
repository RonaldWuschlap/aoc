import re

input = open("2024/day4/input.txt", 'r')
txt_array = [line.strip() for line in open("2024/day4/input.txt", 'r').readlines()]

x_mas_count = 0
count = 0

def back(row: int, column: int): 
    if column < 3:
        return 0
    if "XMAS" != "".join(txt_array[row][column-k] for k in range(4)):
        return 0
    return 1
    
def back_up(row: int, column: int):
    if column < 3 or row < 3:
        return 0
    if "XMAS" != "".join(txt_array[row - k][column- k] for k in range(4)):
        return 0
    return 1

def back_down(row: int, column: int):
    if row+3 >= len(txt_array) or column < 3:
        return 0
    if "XMAS" != "".join(txt_array[row + k][column - k] for k in range(4)):
        return 0
    return 1

def up(row: int, column: int):
    if row < 3:
        return 0
    if "XMAS" != "".join(txt_array[row-k][column] for k in range(4)):
        return 0
    return 1

def up_right(row: int, column: int):
    if row < 3 or column+3 >= len(txt_array[row]):
        return 0
    if "XMAS" != "".join(txt_array[row-k][column+k] for k in range(4)):
        return 0
    return 1

def right(row: int, column: int):
    if column+3 >= len(txt_array[row]):
        return 0
    if "XMAS" != "".join(txt_array[row][column+k] for k in range(4)):
        return 0
    return 1

def down_right(row: int, column: int):
    if row+3 >= len(txt_array) or column+3 >= len(txt_array[row]):
        return 0
    if "XMAS" != "".join(txt_array[row+k][column+k] for k in range(4)):
        return 0
    return 1

def down(row: int, column: int):
    if row+3 >= len(txt_array):
        return 0
    if "XMAS" != "".join(txt_array[row+k][column] for k in range(4)):
        return 0
    return 1

def find_xmas(row: int, column: int):
    if row < 1 or column < 1 or row+1 >= len(txt_array) or column+1 >= len(txt_array[row]):
        return 0
    down_diag = [txt_array[row-1+k][column-1+k] for k in range(3)]
    up_diag = [txt_array[row+1-k][column-1+k] for k in range(3)]
    sum = len(re.findall('MAS',"".join(down_diag))) + len(re.findall('MAS',"".join(down_diag[::-1]))) + len(re.findall('MAS',"".join(up_diag))) + len(re.findall('MAS',"".join(up_diag[::-1])))
    if sum == 2:
        return 1
    return 0


# Part 1
for row, line in enumerate(txt_array):
    for column, letter in enumerate(line):
        if letter == "X":
            count += back(row, column)
            count += back_up(row, column)
            count += up(row,column)
            count += up_right(row,column)
            count += right(row,column)
            count += down_right(row,column)
            count += down(row,column)
            count += back_down(row, column)

# Part 2
for row, line in enumerate(txt_array):
    for column, letter in enumerate(line):
        if letter == "A":
            x_mas_count += find_xmas(row, column)

print(count)
print(x_mas_count)