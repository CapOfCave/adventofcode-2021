with open('input.txt') as input:
    count = 0
    for entry in input.readlines():
        signalpatterns, output = [e.split() for e in entry.split(" | ")]
        count += len([out for out in output if len(out) in [2, 3, 4, 7]])
    print(count) # 237