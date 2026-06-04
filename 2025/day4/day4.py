def partOne():
    with open("input.txt", 'r') as f:
        lines = f.readlines()
        rows = []
        res = 0
        for line in lines:
            row = line.strip()
            rows.append(row)

        for i in range(len(rows)):
            for j in range(len(rows[0])):
                cell = rows[i][j]
                count = 0
                if cell == '@':
                    # top
                    if i > 0:
                        if rows[i - 1][j] == '@':
                            count += 1
                    # bot
                    if i < len(rows) - 1:
                        if rows[i + 1][j] == '@':
                            count += 1
                    # left
                    if j > 0:
                        if rows[i][j - 1] == '@':
                            count += 1
                    # right
                    if j < len(rows[0]) - 1:
                        if rows[i][j + 1] == '@':
                            count += 1
                    
                    # top left
                    if i > 0 and j > 0:
                        if rows[i - 1][j - 1] == '@':
                            count += 1
                    
                    # top right
                    if i > 0 and j < len(rows[0]) - 1:
                        if rows[i - 1][j + 1] == '@':
                            count += 1
                    
                    # bot left
                    if i < len(rows) - 1 and j > 0:
                        if rows[i + 1][j - 1] == '@':
                            count += 1

                    # bot right
                    if i < len(rows) - 1 and j < len(rows[0]) - 1:
                        if rows[i + 1][j + 1] == '@':
                            count += 1

                    if count < 4:
                        res += 1 

        print("Part One:", res) 


def partTwo():
    with open("input.txt", 'r') as f:
        lines = f.readlines()
        rows = []
        res = 0
        remove_check = '@X'
        last_removed_rolls = 0
        for line in lines:
            row = line.strip()
            rows.append(row)

        while last_removed_rolls > 0 or res == 0:
            for i in range(len(rows)):
                rows[i] = rows[i].replace('X', '.')
                
            last_removed_rolls = 0
            for i in range(len(rows)):
                for j in range(len(rows[0])):
                    cell = rows[i][j]
                    count = 0
                    if cell == '@':
                        # top
                        if i > 0:
                            if rows[i - 1][j] in remove_check:
                                count += 1
                        # bot
                        if i < len(rows) - 1:
                            if rows[i + 1][j] in remove_check:
                                count += 1
                        # left
                        if j > 0:
                            if rows[i][j - 1] in remove_check:
                                count += 1
                        # right
                        if j < len(rows[0]) - 1:
                            if rows[i][j + 1] in remove_check:
                                count += 1
                        
                        # top left
                        if i > 0 and j > 0:
                            if rows[i - 1][j - 1] in remove_check:
                                count += 1
                        
                        # top right
                        if i > 0 and j < len(rows[0]) - 1:
                            if rows[i - 1][j + 1] in remove_check:
                                count += 1
                        
                        # bot left
                        if i < len(rows) - 1 and j > 0:
                            if rows[i + 1][j - 1] in remove_check:
                                count += 1

                        # bot right
                        if i < len(rows) - 1 and j < len(rows[0]) - 1:
                            if rows[i + 1][j + 1] in remove_check:
                                count += 1

                        if count < 4:
                            string_list = list(rows[i])
                            string_list[j] = 'X'
                            rows[i] = "".join(string_list)
                            res += 1 
                            last_removed_rolls += 1
            
        print("Part Two:", res) 

if __name__ == "__main__":
    partOne()
    partTwo()