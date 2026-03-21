# Numerical FCO

A robust collection of numerical root-finding algorithms and benchmarking tools.

## Structure

* **`algo/`**: implementations of various root-finding algorithms:
  * `bisection.py` - Bisection Method
  * `fixed_point.py` - Fixed-Point Iteration Method
  * `haley.py` - Halley's Method
  * `newton.py` - Newton-Raphson Method
  * `secant.py` - Secant Method
* **`tex/`**: LaTeX source files for documentation and reporting.
* **`benchmarker.py` & `compare.py`**: Scripts to benchmark, evaluate, and compare the performance and convergence rates of the different algorithms.
* **Notebooks**: Interactive comparisons (`compare.ipynb`, `try.ipynb`).

## Instructions on Running the Program

To run the benchmarking and comparison tools, follow these steps:

1. **Prerequisites**
   Ensure you have Python installed. You may also need to install standard numerical libraries (like `numpy`, `matplotlib`, or `jupyter` for the notebooks) if required by the scripts:
   ```bash
   pip install numpy matplotlib jupyter
   ```

2. **Running the Benchmarker**
   Execute the `benchmarker.py` script from your terminal to evaluate the root-finding algorithms:
   ```bash
   python benchmarker.py
   ```

3. **Running the Comparison Script**
   Execute `compare.py` to compare different algorithms side-by-side:
   ```bash
   python compare.py
   ```

4. **Running Interactive Notebooks**
   Start Jupyter Notebook to open the interactive `.ipynb` files (`compare.ipynb` and `try.ipynb`):
   ```bash
   jupyter notebook
   ```
   Then open the notebooks from your browser to run the cells and visualize the data.
