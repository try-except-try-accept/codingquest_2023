i = int

DAY = "07"
EXPECTED = 320



def pre_process(n):
    return n

def load(pre):
    with open(f"{pre}{DAY}.txt") as f:
        return f.read().splitlines()


def draw_game(snake, fruit):
    out = ""
    for y in range(H):

        for x in range(W):
            
            if [x, y] in snake:
                out += 'S'
            elif [x, y] == fruit:
                out += 'F'
            else:
                out += "."
        out += "\n"
    print(out)
    input()
    
def solve(d):
    
    fruits = [list(map(int, fruit.split(','))) for fruit in d[1].split()]
    fruit = fruits.pop(0)
    moves = d[3]
    score = 0

    snake = [[0, 0]]

    for move in moves:

        new_x, new_y = snake[0]

        #print(move)

        if move == "D":
            new_y = snake[0][1] + 1
        elif move == "U":
            new_y = snake[0][1] - 1
        elif move == "L":
            new_x = snake[0][0] - 1
        else:
            new_x = snake[0][0] + 1

        
        snake.insert(0, [new_x, new_y])
        snake.pop(-1)

        for bit in snake:
            if bit[0] < 0 or bit[0] >= W or bit[1] < 0 or bit[1] >= H or len(set(tuple(bit) for bit in snake)) != len(snake):                
                return score

        if snake[0] == fruit:
            score += 100
            snake.append(snake[0])
            fruit = fruits.pop(0)

        score += 1

        #draw_game(snake, fruit)
        last_head = list(snake[0])
    
W, H = 8, 8

result = solve(load("test"))
if result == EXPECTED:
    W, H = 20, 20
    print("TEST PASSED. FINAL RESULT:")
    print(solve(load("day")))
else:
    print(f"EXPECTED {EXPECTED} but got {result}.")
