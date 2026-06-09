import math 

def partOne():
    points = []
    distance_pairs = []
    circuits = []
    points_in_circuits = {}
    with open("input.txt", 'r') as f:
        for line in f.readlines():
            x, y, z = line.strip().split(',')
            points.append((int(x), int(y), int(z)))
    
    for point_1 in points:
        for point_2 in points:
            if point_1 != point_2:
                x1, y1, z1 = point_1
                x2, y2, z2 = point_2
                distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2) + math.pow(z2 - z1, 2))
                distance_pairs.append((distance, (point_1, point_2)))

    distance_pairs.sort()
    connections = 0
    used_pairs = set()
    for distance, pair in distance_pairs:
        point_1, point_2 = pair

        if connections == 1000:
            break

        if pair in used_pairs:
            continue
    
        used_pairs.add(pair)
        used_pairs.add((point_2, point_1))

        if point_1 in points_in_circuits and point_2 in points_in_circuits:
            if points_in_circuits[point_1] != points_in_circuits[point_2]:
                circuit_index_1 = points_in_circuits[point_1]
                circuit_index_2 = points_in_circuits[point_2]
                for point in circuits[circuit_index_2].copy():
                    circuits[circuit_index_1].add(point)
                    circuits[circuit_index_2].remove(point)
                    points_in_circuits[point] = circuit_index_1
        elif point_2 in points_in_circuits:
            circuit_index = points_in_circuits[point_2]
            circuits[circuit_index].add(point_1)
            points_in_circuits[point_1] = circuit_index
        elif point_1 in points_in_circuits:
            circuit_index = points_in_circuits[point_1]
            circuits[circuit_index].add(point_2)
            points_in_circuits[point_2] = circuit_index
        else:
            circuits.append(set())
            circuits[-1].add(point_1)
            circuits[-1].add(point_2)
            points_in_circuits[point_1] = len(circuits) - 1
            points_in_circuits[point_2] = len(circuits) - 1
        connections += 1 
    
    len_of_circuits = []
    for circuit in circuits:
        len_of_circuits.append(len(circuit))
    len_of_circuits.sort(reverse=True)

    res = 1
    for i in range(3):
        res *= len_of_circuits[i]
    print("Part One:", res)


def partTwo():
    points = []
    distance_pairs = []
    circuits = []
    points_in_circuits = {}
    with open("input.txt", 'r') as f:
        for line in f.readlines():
            x, y, z = line.strip().split(',')
            points.append((int(x), int(y), int(z)))
    
    for point_1 in points:
        for point_2 in points:
            if point_1 != point_2:
                x1, y1, z1 = point_1
                x2, y2, z2 = point_2
                distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2) + math.pow(z2 - z1, 2))
                distance_pairs.append((distance, (point_1, point_2)))

    distance_pairs.sort()
    res = 0
    used_pairs = set()
    for distance, pair in distance_pairs:
        point_1, point_2 = pair

        if pair in used_pairs:
            continue
    
        used_pairs.add(pair)
        used_pairs.add((point_2, point_1))

        if point_1 in points_in_circuits and point_2 in points_in_circuits:
            if points_in_circuits[point_1] != points_in_circuits[point_2]:
                circuit_index_1 = points_in_circuits[point_1]
                circuit_index_2 = points_in_circuits[point_2]
                for point in circuits[circuit_index_2].copy():
                    circuits[circuit_index_1].add(point)
                    circuits[circuit_index_2].remove(point)
                    points_in_circuits[point] = circuit_index_1
                if len(circuits[circuit_index_1]) == 1000:
                    res = point_1[0] * point_2[0]
                    break
        elif point_2 in points_in_circuits:
            circuit_index = points_in_circuits[point_2]
            circuits[circuit_index].add(point_1)
            points_in_circuits[point_1] = circuit_index
        elif point_1 in points_in_circuits:
            circuit_index = points_in_circuits[point_1]
            circuits[circuit_index].add(point_2)
            points_in_circuits[point_2] = circuit_index
        else:
            circuits.append(set())
            circuits[-1].add(point_1)
            circuits[-1].add(point_2)
            points_in_circuits[point_1] = len(circuits) - 1
            points_in_circuits[point_2] = len(circuits) - 1
        
    print("Part Two:", res)
        

if __name__ == "__main__":
    partOne()
    partTwo()