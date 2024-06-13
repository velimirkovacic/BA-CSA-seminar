import numpy as np
from mealpy import FloatVar, BA
from numpy import pi as PI

n = 10


def objective_function(solution):
    return np.sum(solution**2) + 25*np.sum(np.sin(solution)**2)


problem = {
    "obj_func": objective_function,
    "bounds": FloatVar(lb=(-2*PI,)*n, ub=(2*PI,)*n),
    "minmax": "min",
}


model = BA.AdaptiveBA(epoch=1000, pop_size=50, 
                      loudness_min = 1.0, loudness_max = 2.0,
                      pf_min = -10., pf_max = 10.)

g_best = model.solve(problem)

print("Solution:", g_best.solution)
print("Fitness:", g_best.target.fitness)