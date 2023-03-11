i = int

DAY = "03"
EXPECTED = 0

def pre_process(n):
    return n

def load(pre):
    with open(f"{pre}{DAY}.txt") as f:
        return map(pre_process, f.read().splitlines())

def solve(d):
    PIECES = "XO"
    win_counts = {"X":0, "O":0, "D":0}
    for game in d:
        win = False

        board = ["" ] * 9
        for i, m in enumerate(map(int, game.split())):
            board[m-1] = PIECES[i%2]

            check = "".join(board)
            for i in range(0, 9, 3):
                if board[i] != "" and (board[i] == board[i+1] == board[i+2]):
                    win_counts[board[i]] += 1
                    win = True
                    break


            if not win:
                if board[4] != '' and (board[0] == board[4] == board[8] or board[2] == board[4] == board[6]):
                    win_counts[board[4]] += 1
                    win = True
                else:                   
                    for i in range(3):
                        if board[i] != "" and (board[i] == board[3+i] == board[6+i]):
                            win_counts[board[i]] += 1
                            win = True       
                            break


            if not win and len(check) == 9:
                win_counts["D"] += 1
                win = True


            if win:
                break
        
    return win_counts["X"] * win_counts["O"] * win_counts["D"]

result = solve(load("test"))
if result == EXPECTED:
    print("TEST PASSED. FINAL RESULT:")
    print(solve(load("day")))
else:
    print(f"EXPECTED {EXPECTED} but got {result}.")
