def solve_halley(f, df, ddf,E_n, tol=1e-5, iter=100):
    cycles = 0
    print(f"{'Cycle':<10} | {'E (degrees)':<20} | {'Correction'}")
    print("-" * 50)
    
    for i in range(iter):
        cycles += 1
        f_val = f(E_n)
        df_val = df(E_n)
        ddf_val = ddf(E_n)
        
        # Halley's Step Formula
        numerator = 2 * f_val * df_val
        denominator = 2 * (df_val**2) - f_val * ddf_val
        correction = numerator / denominator
        
        E_next = E_n - correction
        
        if abs(E_next - E_n) < tol:
            return E_next, cycles
        E_n = E_next
    return None