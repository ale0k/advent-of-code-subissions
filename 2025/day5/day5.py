import heapq

def partOne():
    with open("input.txt", 'r') as f: 
        lines = f.readlines()
        ranges = []
        ids = []
        res = 0
        for line in lines:
            code = line.strip()
            if code == '':
                continue
            elif '-' in code:
                lower, upper = code.split('-')
                ranges.append((int(lower), int(upper)))
            else:
                ids.append(int(code))
        
        for id in ids:
            for range in ranges:
                lower, upper = range
                if id >= lower and id <= upper:
                    res += 1
                    break

        print("Part One:", res)

def partTwo():
    with open("input.txt", 'r') as f: 
        lines = f.readlines()
        ranges = []
        res = 0
        for line in lines:
            code = line.strip()
            if '-' in code:
                lower, upper = code.split('-')
                l, u = int(lower), int(upper)
                ranges.append((l, u))
        ranges.sort()
        for i in range(len(ranges)):
            lower, upper = ranges[i]
            range_diff = upper - lower + 1
            if i == 0:
                res += range_diff
            else:
                prev_lower, prev_upper = ranges[i - 1]
                if lower > prev_lower and lower > prev_upper:
                    res += range_diff
                elif lower == prev_lower and lower < prev_upper:
                    res += upper - prev_upper
                elif lower < prev_upper and upper > prev_upper:
                    res += range_diff - (prev_upper - lower + 1)
                elif lower == prev_upper:
                    res += upper - prev_upper
                elif lower > prev_lower and upper <= prev_upper:
                    # overlapping
                    continue
                else:
                    print('Missing Case', (prev_lower, prev_upper), (lower, upper))
                
            
        print("Part Two:", res)

if __name__ == "__main__":
    partOne()
    partTwo()