import numpy as np
from benchmarker import KeplerBenchmarker
import os
import pandas as pd
import matplotlib.pyplot as plt



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

test1 = KeplerBenchmarker(M, e, E01).run_benchmark()
test2 = KeplerBenchmarker(M, e, E02).run_benchmark()
test3 = KeplerBenchmarker(M, e, E03).run_benchmark()
test4 = KeplerBenchmarker(M, e, E04).run_benchmark()


print("===== E01 =====")
print(test1)
print("\n===== E02 =====")
print(test2)
print("\n===== E03 =====")
print(test3)
print("\n===== E04 =====")
print(test4)


output_dir = "results"
os.makedirs(output_dir, exist_ok=True)


all_results = pd.concat([test1, test2, test3, test4])
all_results.to_csv('results/results.csv', index=False)

# Setup Plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot Average Duration (Bars)
color_time = '#2c3e50' 
bars = ax.bar(all_results['Method'], all_results['Avg (μs)'], color=color_time, alpha=0.8)

# Add Iteration Labels on top of bars
for bar, iter_val in zip(bars, all_results['Iterations']):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + (height * 0.02),
            f'Iter: {int(iter_val)}',
            ha='center', va='bottom', fontweight='bold', color='crimson')

# Formatting
ax.set_xlabel('Initial Guess Method', fontsize=12)
ax.set_ylabel('Avg Duration (μs)', fontsize=12)
ax.set_title(f"Kepler Equation Performance ($e={e}$, $M=7deg$)", fontsize=14, pad=20)
ax.grid(axis='y', linestyle='--', alpha=0.3)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Save and Show
plot_path = os.path.join(output_dir, "benchmark_clean.png")
plt.savefig(plot_path, dpi=300, bbox_inches='tight')
print(f"Cleaned plot saved to {plot_path}")
plt.show()