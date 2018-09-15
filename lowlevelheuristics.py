import numpy as np

def firstFit(result, item, capacity, prev):
    allocated = False
    for i, bin in enumerate(result):
        if bin + item <= capacity:
            result[i] += item
            allocated = True
            break

    if not allocated:
        result.append(item)

    return result, prev

def lastFit(result, item, capacity, prev):
    allocated = False
    for i in range(len(result) - 1, -1, -1):
        if result[i] + item <= capacity:
            result[i] += item
            allocated = True
            break

    if not allocated:
        result.append(item)

    return result, prev

def randomFit(result, item, capacity, prev):
    allocated = False
    randomList = np.arange(len(result))
    np.random.shuffle(randomList)
    for i in randomList:
        if result[i] + item <= capacity:
            result[i] += item
            allocated = True
            break

    if not allocated:
        result.append(item)

    return result, prev

def nextFit(result, item, capacity, prev):
    allocated = False

    for i in range(prev, len(result)):
        bin = result[i]
        prev = i
        if bin + item <= capacity:
            result[i] += item
            allocated = True

    if not allocated:
        result.append(item)
        prev = 0

    return result, prev


def bestFit(result, item, capacity, prev):
    best = float('inf')
    pos = None
    for i, bin in enumerate(result):
        if bin + item <= capacity:
            space = capacity - (bin + item)
            if space < best:
                best = space
                pos = i
                break

    if pos == None:
        result.append(item)
    else:
        result[pos] += item

    return result, prev


def worstFit(result, item, capacity, prev):
    worst = -1
    pos = None
    for i, bin in enumerate(result):
        if bin + item <= capacity:
            space = capacity - (bin + item)
            if space > worst:
                worst = space
                pos = i
                break

    if pos == None:
        result.append(item)
    else:
        result[pos] += item

    return result, prev