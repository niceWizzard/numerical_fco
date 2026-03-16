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
        return secant_method(self.f, self.E0, self.E0+self.e)

    def __do_halley(self):
        return solve_halley(self.f, self.df,self.ddf, self.E0)

    def run_benchmark(self, num_runs: int = 10_000, repeats: int = 10) -> pd.DataFrame:
        """
        Executes and benchmarks solver functions with statistical sampling.
        'num_runs' is the number of loops inside each sample.
        'repeats' is the number of samples collected to calculate Std Dev.
        """
        methods = {
            "Newton": self.__do_newton,
            "Halley": self.__do_halley,
        }

        results = []
        
        for name, method in methods.items():
            # Get the root and iterations once (assuming they are deterministic)
            root_rad, iterations = method()
            residual = abs(self.f(root_rad))

            # Collect multiple samples (each sample is 'num_runs' executions)
            # returns a list of total times per sample
            raw_sample_times = timeit.repeat(method, repeat=repeats, number=num_runs)
            
            # Convert each total sample time into microseconds per single execution
            durations_us = [(t / num_runs) * 1_000_000 for t in raw_sample_times]
            
            # Statistical calculations
            avg_duration = np.mean(durations_us)
            std_dev = np.std(durations_us)
            best_time = np.min(durations_us)
            
            results.append({
                "Method": name,
                "Root (Rad)": round(root_rad, 8),
                "Iterations": iterations,
                "Avg (μs)": round(avg_duration, 4),
                "Std Dev (μs)": round(std_dev, 4),
                "Best (μs)": round(best_time, 4),
                "Residual Error": f"{residual:.2e}"
            })
            
        return pd.DataFrame(results).sort_values(by="Iterations")
