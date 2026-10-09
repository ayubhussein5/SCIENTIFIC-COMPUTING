import numpy as np
import matplotlib.pyplot as plt

# New case: steady temperature along a 10-node metal rod in a factory oven wall.
# Left end held at 150 C, right end at 30 C.
n = 10
A = 2*np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1)
b = np.zeros(n); b[0] = 150.0; b[-1] = 30.0

def jacobi(A, b, tol=1e-8, max_iter=5000):
    D = np.diag(A); R = A - np.diagflat(D); x = np.zeros_like(b); errs = []
    for _ in range(max_iter):
        x_new = (b - R @ x) / D
        errs.append(np.linalg.norm(x_new - x, np.inf))
        x = x_new
        if errs[-1] < tol: break
    return x, errs

def gauss_seidel(A, b, tol=1e-8, max_iter=5000):
    x = np.zeros_like(b); errs = []
    for _ in range(max_iter):
        old = x.copy()
        for i in range(len(b)):
            x[i] = (b[i] - A[i, :i] @ x[:i] - A[i, i+1:] @ old[i+1:]) / A[i, i]
        errs.append(np.linalg.norm(x - old, np.inf))
        if errs[-1] < tol: break
    return x, errs

xj, ej = jacobi(A, b); xg, eg = gauss_seidel(A, b)
print("Gauss-Seidel temperatures (C):", np.round(xg, 2))
print("Jacobi iterations:", len(ej), "  Gauss-Seidel iterations:", len(eg))
print("Max difference from direct solve:", np.abs(xg - np.linalg.solve(A, b)).max())

plt.semilogy(ej, label="Jacobi"); plt.semilogy(eg, label="Gauss-Seidel")
plt.xlabel("Iteration"); plt.ylabel("Maximum change")
plt.title("Convergence for 10-node rod"); plt.legend(); plt.grid(True); plt.show()
