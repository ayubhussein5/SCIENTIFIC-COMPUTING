import numpy as np

# New case: a bakery makes three products. How many batches of each were made?
# Columns: bread, cakes, mandazi (per batch)
# Rows: flour (kg), sugar (kg), oven hours
A = np.array([
    [10.0, 6.0, 4.0],
    [ 1.0, 4.0, 2.0],
    [ 2.0, 3.0, 1.0]
])
b = np.array([128.0, 48.0, 41.0])   # totals used today (illustrative)

x = np.linalg.solve(A, b)
residual = b - A @ x

for name, val in zip(["Bread", "Cakes", "Mandazi"], x):
    print(f"{name} batches: {val:.2f}")
print("Check A @ x:", A @ x)
print("Residual norm:", np.linalg.norm(residual))
