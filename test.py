from algo.bisection import bisection_method
from algo.newton import newtons_method
from algo.fixed_point import fixed_point_iteration
from algo.secant import secant_method
from typing import Callable
import numpy as np

f : Callable[[float], float] = lambda x : x**3 - 7*x**2 + 14*x - 6
df : Callable[[float], float] = lambda x : 3*x**2 - 14*x + 14
g : Callable[[float], float] = lambda x : (-x**3 + 7*x**2 + 6) / 14

p0 = 0
p1 = 1

bm = bisection_method(f, p0, p1, 1e-5, 100)
fp = fixed_point_iteration = fixed_point_iteration(f, g, p0, 1e-5, 100)
newton = newtons_method(f, df, p0, 1e-5, 100)
secant = secant_method(f, p0, p1, 1e-5, 100)




print(f"""
    Actual roots: {np.roots([1, -7, 14, -6])}
    Bisection method: {bm} <{f(bm if bm else 0)}>
    Fixed point iteration: {fp} <{f(fp if fp else 0 )}>
    Newton's method: {newton} <{f(newton if newton else 0)}>
    Secant method: {secant} <{f(secant if secant else 0)}>
    
""")


print(f(10.798673629760742))