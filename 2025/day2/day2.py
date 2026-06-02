def partOne():
    with open("input.txt", 'r') as f:
        line = f.readline()
        ids = line.split(',') 
        sum = 0
        for id in ids:
            lower, upper = id.split('-')
            for i in range(int(lower), int(upper) + 1): 
                string = str(i)
                if (len(string) % 2 == 0) and string[:len(string) // 2] == string[len(string) // 2:]:
                   sum += i 
        print("Part One:", sum)


def partTwo():
    with open("input.txt", 'r') as f:
        line = f.readline()
        ids = line.split(',') 
        sum = 0
        for id in ids:
            lower, upper = id.split('-')
            for i in range(int(lower), int(upper) + 1): 
                string = str(i)
                for j in range(1, len(string)):
                    split_string = string.split(string[:j])
                    for split in split_string:
                        if split != "":
                            break
                    if split == "":
                        sum += i
                        break
                    
        print("Part Two:", sum)


if __name__ == "__main__":
    partOne()
    partTwo()