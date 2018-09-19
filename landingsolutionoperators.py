import numpy as np


def mutate(solution):
    clone = solution.clone()
    randomPlane = clone.landingSolution[np.random.randint(clone.p)]
    randomPlane.x = np.random.randint(low=randomPlane.e, high=randomPlane.l + 1)
    while not clone.valid():
        clone = solution.clone()
        randomPlane = clone.landingSolution[np.random.randint(clone.p)]
        randomPlane.x = np.random.randint(low=randomPlane.e, high=randomPlane.l + 1)
    return clone


def swap(solution):
    clone = solution.clone()
    randomPlane1 = clone.landingSolution[np.random.randint(clone.p)]
    randomPlane2 = clone.landingSolution[np.random.randint(clone.p)]
    randomPlane1.x = randomPlane2.x
    randomPlane2.x = randomPlane1.x
    while not clone.valid():
        clone = solution.clone()
        randomPlane1 = clone.landingSolution[np.random.randint(clone.p)]
        randomPlane2 = clone.landingSolution[np.random.randint(clone.p)]
        randomPlane1.x = randomPlane2.x
        randomPlane2.x = randomPlane1.x
    return clone


def swapCrossover(parent1, parent2):
    clone1 = parent1.clone()
    clone2 = parent2.clone()

    randomPlane1 = clone1.landingSolution[np.random.randint(clone1.p)]
    randomPlane2 = clone2.landingSolution[np.random.randint(clone2.p)]

    randomPlane1.x = randomPlane2.x
    randomPlane2.x = randomPlane1.x

    while not clone1.valid() and clone2.valid():
        clone1 = parent1.clone()
        clone2 = parent2.clone()

        randomPlane1 = clone1.landingSolution[np.random.randint(clone1.p)]
        randomPlane2 = clone2.landingSolution[np.random.randint(clone2.p)]

        randomPlane1.x = randomPlane2.x
        randomPlane2.x = randomPlane1.x

    return clone1, clone2