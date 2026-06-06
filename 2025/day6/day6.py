def partOne():
    with open("input.txt", 'r') as f:
        rows = []
        res = 0
        for line in f.readlines():
            data = line.strip()
            rows.append(data.split())

        for col in range(len(rows[0])):
            nums = [] 
            total = 0
            for row in range(len(rows)):
                nums.append(rows[row][col])
            operator = nums.pop()
            if operator == '+':
                for num in nums:
                    total += int(num)
            elif operator == '*':
                total = 1
                for num in nums:
                    total *= int(num)
            res += total

        print("Part One:", res)


def partTwo():
    with open("input.txt", 'r') as f:
        rows = []
        res = 0
        for line in f.readlines():
            data = line.strip('\n')
            rows.append(data)
        col = 0
        total = 1
        last_operator = ''
        while col < len(rows[0]):
            chars = [] 
            for row in range(len(rows)):
                chars.append(rows[row][col])
            operator = chars.pop()
            num = ''
            for char in chars:
                if char == ' ':
                    continue
                num += char
            if num == '':
                if last_operator == '+':
                    res += total - 1
                else:
                    res += total
                total = 1
                col += 1 
                continue

            if operator == ' ':
                operator = last_operator

            if operator == '+':
                last_operator = operator
                total += int(num)
            elif operator == '*':
                last_operator = operator
                total *= int(num)
                
            col += 1 
            
        if last_operator == '+':
            res += total - 1
        else:
            res += total

        print("Part Two:", res)
        

if __name__ == "__main__":
    partOne()
    partTwo()