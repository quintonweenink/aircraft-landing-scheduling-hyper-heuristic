import numpy as np


def shiftUp(solution):
    newSolution = solution.clone()
    sortedPlanes = [i[0] for i in sorted(enumerate(newSolution.landingSolution), key=lambda x: x[1].x, reverse=False)]
    prev = None
    for i in sortedPlanes:
        if prev == None:
            prev = newSolution.landingSolution[i]
            continue
        if prev.x + prev.s[newSolution.landingSolution[i].i] + 1 <= newSolution.landingSolution[i].x:
            newSolution.landingSolution[i].x = prev.x + prev.s[newSolution.landingSolution[i].i] + 1
            if newSolution.valid():
                return newSolution
            else:
                newSolution = solution.clone()
        else:
            prev = newSolution.landingSolution[i]

    return solution


def shiftUpReversed(solution):
    newSolution = solution.clone()
    sortedPlanes = [i[0] for i in sorted(enumerate(newSolution.landingSolution), key=lambda x: x[1].x, reverse=True)]
    prev = None
    for i in sortedPlanes:
        if prev == None:
            prev = newSolution.landingSolution[i]
            continue
        if prev.x + prev.s[newSolution.landingSolution[i].i] + 1 <= newSolution.landingSolution[i].x:
            newSolution.landingSolution[i].x = prev.x + prev.s[newSolution.landingSolution[i].i] + 1
            if newSolution.valid():
                return newSolution
            else:
                newSolution = solution.clone()
        else:
            prev = newSolution.landingSolution[i]

    return solution


def shiftDown(solution):
    newSolution = solution.clone()
    sortedPlanes = [i[0] for i in sorted(enumerate(newSolution.landingSolution), key=lambda x: x[1].x, reverse=False)]
    prev = None
    for i in sortedPlanes:
        if prev == None:
            prev = i
            continue
        if newSolution.landingSolution[prev].x + newSolution.landingSolution[prev].s[i] + 1 <= \
                newSolution.landingSolution[i].x:
            newSolution.landingSolution[prev].x = newSolution.landingSolution[prev].x + \
                                                  newSolution.landingSolution[prev].s[i] + 1
            if newSolution.valid():
                return newSolution
            else:
                newSolution = solution.clone()
        else:
            prev = i

    return solution


def shiftDownReversed(solution):
    newSolution = solution.clone()
    sortedPlanes = [i[0] for i in sorted(enumerate(newSolution.landingSolution), key=lambda x: x[1].x, reverse=True)]
    prev = None
    for i in sortedPlanes:
        if prev == None:
            prev = i
            continue
        if newSolution.landingSolution[prev].x + newSolution.landingSolution[prev].s[i] + 1 <= \
                newSolution.landingSolution[i].x:
            newSolution.landingSolution[prev].x = newSolution.landingSolution[prev].x + \
                                                  newSolution.landingSolution[prev].s[i] + 1
            if newSolution.valid():
                return newSolution
            else:
                newSolution = solution.clone()
        else:
            prev = i

    return solution


def tryMoveHighestCloseToTarget(solution):
    newSolution = solution.clone()
    sortedPlanes = [i[0] for i in
                    sorted(enumerate(newSolution.landingSolution), key=lambda x: x[1].getFitness(), reverse=True)]
    for i in sortedPlanes:
        newSolution.landingSolution[i].x = newSolution.landingSolution[i].t
        if newSolution.valid():
            return newSolution
        else:
            newSolution = solution.clone()
    return solution


def tryMoveHighestCloseToTargetReversed(solution):
    newSolution = solution.clone()
    sortedPlanes = [i[0] for i in
                    sorted(enumerate(newSolution.landingSolution), key=lambda x: x[1].getFitness(), reverse=False)]
    for i in sortedPlanes:
        newSolution.landingSolution[i].x = newSolution.landingSolution[i].t
        if newSolution.valid():
            return newSolution
        else:
            newSolution = solution.clone()
    return solution


def trySwap(solution):
    newSolution = solution.clone()
    sortedPlanes = [i[0] for i in
                    sorted(enumerate(newSolution.landingSolution), key=lambda x: x[1].getFitness(), reverse=True)]
    for x in sortedPlanes:
        for i in sortedPlanes:
            if x == i:
                continue
            tempX = newSolution.landingSolution[i].x
            newSolution.landingSolution[i].x = newSolution.landingSolution[x].x
            newSolution.landingSolution[x].x = tempX
            if newSolution.valid():
                return newSolution
            else:
                newSolution = solution.clone()
    return solution


def trySwapReversed(solution):
    newSolution = solution.clone()
    sortedPlanes = [i[0] for i in
                    sorted(enumerate(newSolution.landingSolution), key=lambda x: x[1].getFitness(), reverse=False)]
    for x in sortedPlanes:
        for i in sortedPlanes:
            if x == i:
                continue
            tempX = newSolution.landingSolution[i].x
            newSolution.landingSolution[i].x = newSolution.landingSolution[x].x
            newSolution.landingSolution[x].x = tempX
            if newSolution.valid():
                return newSolution
            else:
                newSolution = solution.clone()
    return solution


def randomMove(solution):
    newSolution = solution.clone()
    sortedPlanes = [i[0] for i in
                    sorted(enumerate(newSolution.landingSolution), key=lambda x: x[1].getFitness(), reverse=True)]
    for x in sortedPlanes:
        newSolution.landingSolution[x].x = np.random.randint(low=newSolution.landingSolution[x].e,
                                                             high=newSolution.landingSolution[x].l + 1)
        if newSolution.valid():
            return newSolution
        else:
            newSolution = solution.clone()
    return solution


def doNothing(solution):
    return solution