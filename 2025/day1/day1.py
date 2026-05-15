def partOne():
    dial = 50
    zeros = 0
    with open("input.txt", 'r') as f:
        for line in f.readlines():
            code = line.strip()
            direction = code[0]
            magnitude = int(code[1:])

            if direction == 'R':
                dial += magnitude
            else:
                dial -= magnitude

            while dial > 99:
                dial -= 100
            while dial < 0:
                dial += 100
            
            if dial == 0:
                zeros += 1
    print("Part One:", zeros)

def partTwo():
    dial = 50
    zeros = 0
    with open("input.txt", 'r') as f:
        for line in f.readlines():
            code = line.strip()
            direction = code[0]
            magnitude = int(code[1:])

            while magnitude > 0:
                if direction == 'R':
                    dial += 1
                else:
                    dial -= 1

                if dial == 0:
                    zeros += 1
                elif dial > 99:
                    dial -= 100
                    zeros += 1
                elif dial < 0:
                    dial += 100

                magnitude -= 1

    print("Part Two:", zeros)

if __name__ == "__main__":
    partOne()
    partTwo()