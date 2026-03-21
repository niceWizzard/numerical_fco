from typing import Callable, Optional, Tuple

def bisection_method(
    f: Callable[[float], float], 
    a: float, 
    b: float, 
    tol: float=1e-5, 
    n0: int = 100,
) -> Optional[Tuple[float, int]]:
    # Start the iteration counter and cache f(a) to avoid recomputing it.
    i: int = 1
    fa: float = f(a)

    # Repeatedly halve the interval [a, b] until convergence or max iterations.
    while i <= n0:
        # Midpoint of the current interval.
        p: float = a + (b - a) / 2
        fp: float = f(p)
        
        # Stop if we found an exact root or the interval is smaller than tolerance.
        if fp == 0 or (b - a) / 2 < tol:
            return (p, i)
        i += 1

        # Keep the subinterval where the sign change occurs.
        if fa * fp > 0:
            a = p
            fa = fp
        else:
            b = p
    print("Bisection did not converge after", n0, "iterations.")
    return None