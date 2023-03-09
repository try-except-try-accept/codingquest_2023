from collections import defaultdict

i = int

DAY = "04"
EXPECTED = "This is a test. This is a test. Thankyou."
NO_TEST = True

def pre_process(n):
    return n

def load(pre):
    with open(f"{pre}{DAY}.txt") as f:
        return map(pre_process, f.read().splitlines())

def get_bytes(msg, char_mode=False):
    x = int
    if char_mode:
        x = chr
    
    return [x(int(msg[i:i+2], 16)) for i in range(0, len(msg), 2)]

def solve(d):

    messages = []
    for line in d:        
        if line.startswith("5555"):
            line = line[4:]
            sender = line[:8]
            line = line[8:]
            seq = int(line[:2], 16)
            line = line[2:]
            checksum = int(line[:2], 16)
            line = line[2:]
            msg = line          
            payload_check = sum(get_bytes(msg)) % 256            

            if payload_check != checksum:
                continue

            messages.insert(seq, msg)
            
    msg = "".join(messages)
    #msg = msg.replace("20202020202020", "")

    return "".join(get_bytes(msg, True))

result = solve(load("test"))
if NO_TEST or result == EXPECTED:
    print("TEST PASSED. FINAL RESULT:")
    print(solve(load("day")))
else:
    print(f"EXPECTED\n{EXPECTED} \nbut got\n{result}.")
