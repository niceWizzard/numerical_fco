from typing import Callable
from typing import Optional, Tuple

def fixed_point_iteration(
    f: Callable[[float], float], 
    g: Callable[[float], float], 
    p0: float, 
    tol: float=1e-5, 
    n0: int=100,
) -> Optional[Tuple[float, int]]:
    # Initialize with the user-provided starting guess.
    i: int = 1
    current_p = p0

    # Apply p_{n+1} = g(p_n) until the update is smaller than tolerance.
    while i <= n0:
        next_p = g(current_p)
        error = abs(next_p - current_p)
        
        # Converged when successive approximations are sufficiently close.
        if error < tol:
            return (next_p, i)
        
        # Continue iterating from the newest approximation.
        current_p = next_p
        i += 1
    print("Fixed point failed to converge.")
    return None
    