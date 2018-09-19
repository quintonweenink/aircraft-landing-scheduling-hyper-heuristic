

def acceptAll(prevSolution, nextSolution):
    return True


def acceptIfImproving(prevSolution, nextSolution):
    return nextSolution.getFitness() < prevSolution.getFitness()


def acceptIfEqualOrImproving(prevSolution, nextSolution):
    return nextSolution.getFitness() <= prevSolution.getFitness()