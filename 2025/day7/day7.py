def partOne():
    rows = []
    res = 0

    with open("input.txt", 'r') as f:
        for line in f.readlines():
            rows.append(line.strip()) 

    previous_beams = set()
    previous_beams.add(rows[0].find('S'))

    for row in range(len(rows)):
        previous_beams
        for col in previous_beams.copy():
            if rows[row][col] == '^':
                previous_beams.remove(col)
                previous_beams.add(col - 1)
                previous_beams.add(col + 1)
                res += 1

    print("Part One:", res)


memo = {}
def partTwo():
    rows = []

    with open("input.txt", 'r') as f:
        for line in f.readlines():
            rows.append(line.strip()) 

    staring_beam = rows[0].find('S')
    res = dfs(rows, 0, staring_beam)

    print("Part Two:", res)

def dfs(rows, row, beam):
    if (row, beam) in memo:
        return memo[(row,beam)]
    elif row == len(rows) - 1:
        return 1
    elif rows[row][beam] == '^':
        res = dfs(rows, row + 1, beam - 1) + dfs(rows, row + 1, beam + 1)
        memo[(row, beam)] = res
    else:
        res = dfs(rows, row + 1, beam)
        memo[(row, beam)] = res

    return res


if __name__ == "__main__":
    partOne()
    partTwo()