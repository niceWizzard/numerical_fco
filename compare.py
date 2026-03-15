import numpy as np
from benchmarker import KeplerBenchmarker



M = np.deg2rad(7)
e = 0.999

E01 = M
E02 = M + (e * np.sin(M)) / (1 - np.sin(M + e) + np.sin(M))
E03 = M + e * np.sin(M + e* np.sin(M + e))

# E0 = np.deg2rad(38.52700657)
B= 1.173439404
A = -0.584013113
C = 0.809460441
D = 0.077357763

a = (B * np.sin(M) + D * np.cos(M)) / ( (1 / e) - A * np.sin(M) - C * np.cos(M) )
E04 = M  + e * (np.sin( M + e * np.sin(M + a)))

print("===== E01 =====")
print(KeplerBenchmarker(M, e, E01).run_benchmark())
print("\n===== E02 =====")
print(KeplerBenchmarker(M, e, E02).run_benchmark())
print("\n===== E03 =====")
print(KeplerBenchmarker(M, e, E03).run_benchmark())
print("\n===== E04 =====")
print(KeplerBenchmarker(M, e, E04).run_benchmark())



