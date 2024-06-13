import numpy as np
from mealpy import FloatVar, CSA
from numpy import pi as PI

n = 10


def objective_function(solution):
    x = solution[0]
    y = solution[1]
    return np.sum(solution**2) + 25*np.sum(np.sin(solution)**2)


problem = {
    "obj_func": objective_function,
    "bounds": FloatVar(lb=(-2*PI,)*n, ub=(2*PI,)*n),
    "minmax": "min",
}


model = CSA.OriginalCSA(epoch=1000, pop_size=50, p_a = 0.3)

g_best = model.solve(problem)

print("Solution:", g_best.solution)
print("Fitness:", g_best.target.fitness)