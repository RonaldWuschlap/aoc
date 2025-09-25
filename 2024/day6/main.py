import copy

input = open("2024/day6/input.txt")
start_y: int
start_x: int

class Guard:
    def __init__(self, x: int, y: int, dir: str):
        self.x, self.y, self.dir = x, y, dir

class Step:
    def __init__(self, x: int, y: int, dir: str):
        self.x, self.y, self.dir = x, y, dir
    
    def __str__(self):
        return f"{self.x}, {self.y}, {self.dir}"
    
    def __eq__(self, other):
        return isinstance(other, Step) and self.x == other.x and self.y == other.y and self.dir == other.dir

    def __hash__(self):
        return hash(str(self))

dirs = ["UP", "RIGHT", "DOWN", "LEFT"]
map = []
path = []
visited = set()
found_obstacles = set()

for idx, line in enumerate(input):
    temp_y = line.find('^')
    if temp_y != -1:
        start_x = idx
        start_y = temp_y
    map.append(list(line.strip()))

guard = Guard(start_x, start_y, "UP")

def walk(guard: Guard, map: list, path: list, visited: set):
    prev_x, prev_y, prev_dir = guard.x, guard.y, guard.dir
    prev_step = Step(prev_x, prev_y, prev_dir)
    if guard.dir == "UP":
        x, y = guard.x-1, guard.y
    elif guard.dir == "DOWN":
        x, y = guard.x+1, guard.y
    elif guard.dir == "LEFT":
        x, y = guard.x, guard.y-1
    elif guard.dir == "RIGHT":
        x, y = guard.x, guard.y+1
    if x < 0 or x >= len(map) or y < 0 or y >= len(map[0]):
       map[prev_x][prev_y] = "X"
       path.append(prev_step)
       visited.add((prev_x, prev_y, prev_dir))
       return True
    if map[x][y] == "#":
        next_dir = (dirs.index(guard.dir)+1) % 4
        guard.dir = dirs[next_dir]
        return False
    map[prev_x][prev_y] = "X"
    guard.x, guard.y = x,y
    path.append(prev_step)
    visited.add((prev_x, prev_y, prev_dir))
    return False

def evaluate(obstacle: Step, map):
    path = []
    visited = set()
    guard = Guard(start_x, start_y, "UP")
    map[obstacle.x][obstacle.y]="#"
    if (obstacle.x, obstacle.y) in found_obstacles:
        #print("Obstacle already found")
        return False
    while True:
        is_exit = walk(guard, map, path, visited)
        if is_exit:
            return False
        if (guard.x, guard.y, guard.dir) in visited:
            #print("Loop found at", (guard.x, guard.y, guard.dir))
            found_obstacles.add((obstacle.x, obstacle.y))
            return True

clean_map = copy.deepcopy(map)
is_exit = False
while not is_exit:
    is_exit = walk(guard, map, path, visited)

# Part 1
sum = 0
sum_obstacles = 0
for line in map:
    sum+=line.count("X")
print(sum)

# Part 2
skibidi = range (1, len(path))
original_path = path
for i in skibidi:
    map = copy.deepcopy(clean_map)
    if evaluate(original_path[i], map):
        sum_obstacles+=1
print(sum_obstacles)