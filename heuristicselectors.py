import numpy as np


def randomHeuristicSelection(heuristics):
    randomIndex = np.random.randint(len(heuristics))
    return heuristics[randomIndex]