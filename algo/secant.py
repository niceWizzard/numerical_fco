from typing import Callable
from typing import Optional, Tuple



def secant_method(
    f: Callable[[float], float], 
    p0: float, 
    p1: float, 
    tol: float=1e-5, 
    n0: int=100,
) -> Optional[Tuple[float, int]]:
    i: int = 1
    q0 = f(p0)
    q1 = f(p1)
    
    while i <= n0:
        if q1 - q0 == 0:
            print("Failure: Division by zero in Secant Method.")
            return None
            
        p: float = p1 - q1 * (p1 - p0) / (q1 - q0)
        abs_error = abs(p - p1)
        
        if abs_error < tol:
            return (p,i )
        
        i += 1
        p0 = p1
        q0 = q1
        p1 = p
        q1 = f(p)
            
    return None
