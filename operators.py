import numpy as np

def swap(chromosome, heuristics, times=1):
    clone = chromosome[:]

    for _ in range(times):
        pos1 = np.random.randint(len(clone))
        pos2 = np.random.randint(len(clone))
        tmp = clone[pos1]
        clone[pos1] = clone[pos2]
        clone[pos2] = tmp

    return clone


def crossover(chromosome1, chromosome2, points=1):
    clone1 = chromosome1[:]
    clone2 = chromosome2[:]

    poss1 = np.sort(np.random.randint(len(clone1), size=points))
    poss2 = np.sort(np.random.randint(len(clone2), size=points))

    result1 = []
    result2 = []
    old1 = 0
    old2 = 0
    for idx, _ in enumerate(poss1):
        if idx % 2 == 0:
            result1.extend(clone2[old2:poss2[idx]])
            result2.extend(clone1[old1:poss1[idx]])
        else:
            result1.extend(clone1[old1:poss1[idx]])
            result2.extend(clone2[old2:poss2[idx]])
        old1 = poss1[idx]
        old2 = poss2[idx]

    if points % 2 == 0:
        result1.extend(clone2[old2:len(clone2)])
        result2.extend(clone1[old1:len(clone1)])
    else:
        result1.extend(clone1[old1:len(clone1)])
        result2.extend(clone2[old2:len(clone2)])

    return result1, result2


def add(chromosome, heuristics, points=1):
    clone = chromosome[:]

    for _ in range(points):
        pos = np.random.randint(len(clone))

        heuristic = heuristics[np.random.randint(len(heuristics))]

        clone.insert(pos, heuristic)

    return clone


def change(chromosome, heuristics, points=1):
    clone = chromosome[:]

    for _ in range(points):
        pos = np.random.randint(len(clone))

        heuristic = heuristics[np.random.randint(len(heuristics))]

        clone[pos] = heuristic

    return clone


def remove(chromosome, heuristics, points=1):
    clone = chromosome[:]

    for _ in range(points):
        pos = np.random.randint(len(clone))

        clone.pop(pos)

    return clone