from typing import Callable, Optional, Tuple


def bisection_method(
    f: Callable[[float], float], 
    a: float, 
    b: float, 
    tol: float=1e-5, 
    n0: int = 100,
) -> Optional[Tuple[float, int]]:
    i: int = 1
    fa: float = f(a)
    while i <= n0:
        p: float = a + (b - a) / 2
        fp: float = f(p)
        
        if fp == 0 or (b - a) / 2 < tol:
            return (p, i)
        i += 1
        if fa * fp > 0:
            a = p
            fa = fp
        else:
            b = p
    print("Bisection did not converge after", n0, "iterations.")
    return None