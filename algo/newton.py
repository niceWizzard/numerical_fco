from typing import Callable
from typing import Optional, Tuple

def newtons_method(
    f: Callable[[float], float], 
    df: Callable[[float], float], 
    p0: float, 
    tol: float=1e-5, 
    n0: int=100,
) -> Optional[Tuple[float, int]]:
    i: int = 1
    while i <= n0:
        p: float = p0 - f(p0) / df(p0)
        abs_error = abs(p - p0)
        
        if abs_error < tol:
            return (p, i)
        
        i += 1
        p0 = p
    print("Newton did not converge after", n0, "iterations.")
    return None