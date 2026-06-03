def partOne():
    with open("input.txt", 'r') as f:
        lines = f.readlines()
        res = 0 
        for line in lines:
            bank = line.strip()
            first = None
            second = None
            for i, char in enumerate(bank):
                digit = int(char)
                if (first is None or digit > first) and i < len(bank) - 1:
                    first = digit
                    second = None
                elif second is None or digit > second:
                    second = digit
            res += int(str(first) + str(second))

        print("Part One:", res) 

def partTwo():
    with open("input.txt", 'r') as f:
        lines = f.readlines()
        res = 0 
        for line in lines:
            bank = line.strip()
            batteries = []
            removes = len(bank) - 12
            for i, char in enumerate(bank):
                if removes == 0:
                    break
                elif batteries:
                    while batteries and batteries[-1] < char:
                        batteries.pop()
                        removes -= 1
                        if removes == 0:
                            break
                batteries.append(char)
            batteries = batteries + list(bank[i:])
            batteries = batteries[:12]
            res += int("".join(batteries))
        print("Part Two:", res) 
    

if __name__ == "__main__":
    partOne()
    partTwo()