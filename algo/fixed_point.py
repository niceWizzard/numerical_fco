from typing import Callable
from typing import Optional, Tuple



def fixed_point_iteration(
    f: Callable[[float], float], 
    g: Callable[[float], float], 
    p0: float, 
    tol: float=1e-5, 
    n0: int=100,
) -> Optional[Tuple[float, int]]:
    i: int = 1
    current_p = p0
    while i <= n0:
        next_p = g(current_p)
        error = abs(next_p - current_p)
        
        if error < tol:
            return (next_p, i)
        
        current_p = next_p
        i += 1
    print("Fixed point failed to converge.")
    return None
    