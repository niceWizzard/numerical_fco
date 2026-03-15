import pandas as pd
import numpy as np
import timeit
from typing import Dict, Callable, Tuple
from algo.bisection import bisection_method
from algo.newton import newtons_method
from algo.fixed_point import fixed_point_iteration
from algo.secant import secant_method
from algo.haley import solve_halley

class KeplerBenchmarker:
    def __init__(self, M: float, e: float, E0: float):
        self.M = M
        self.e = e
        self.E0 = E0
        
        # Define the physics functions based on current parameters
        self.f = lambda E: E - self.e * np.sin(E) - self.M
        self.df = lambda E: 1 - self.e * np.cos(E)
        self.ddf = lambda E: self.e * np.sin(E)
        self.g = lambda E: self.e * np.sin(E) + self.M


    def __do_bisection(self):
        return bisection_method(self.f, self.M, self.M+self.e)

    def __do_newton(self):
        return newtons_method(self.f, self.df, self.E0)

    def __do_fixed_point(self):
        return fixed_point_iteration(self.f, self.g, self.E0)

    def __do_secant(self):
        return secant_method(self.f, self.M, self.M+self.e)

    def __do_halley(self):
        return solve_halley(self.f, self.df,self.ddf, self.E0)

    def run_benchmark(self) -> pd.DataFrame:
        """
        Executes and benchmarks the solver functions, returning a DataFrame 
        with results in both Radians and Degrees.
        """
        methods = {
            ("Bisection", self.__do_bisection),
            ("Newton", self.__do_newton),
            ("Fixed Point", self.__do_fixed_point),
            ("Secant", self.__do_secant),
            ("Halley", self.__do_halley),
        }

        results = []
        
        for name, method in methods:
            start_time = timeit.default_timer()
            root_rad, iterations = method()
            end_time = timeit.default_timer()
            
            duration = (end_time - start_time) * 1_000_000 # microseconds
            residual = abs(self.f(root_rad))
            
            results.append({
                "Method": name,
                "Root (Rad)": root_rad,
                "Root (Deg)": np.rad2deg(root_rad), # Conversion added here
                "Iterations": iterations,
                "Residual Error": residual,
                "Runtime (μs)": round(duration, 3)
            })
            
        return pd.DataFrame(results).sort_values(by="Iterations")