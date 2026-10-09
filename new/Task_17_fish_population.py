import numpy as np
import matplotlib.pyplot as plt

# New case: logistic growth of tilapia in a fish pond (Euler method).
# dP/dt = r P (1 - P/K)
r = 0.3        # growth rate per month (assumed)
K = 2000.0     # pond carrying capacity (fish)
P0 = 100.0
h = 1.0        # months
months = 24

def rate(P): return r * P * (1 - P / K)

t = np.arange(0, months + h, h)
P = np.zeros_like(t); P[0] = P0
for i in range(len(t) - 1):
    P[i + 1] = P[i] + h * rate(P[i])

exact = K / (1 + (K - P0) / P0 * np.exp(-r * t))
print(f"Euler population after {months} months: {P[-1]:.0f} fish")
print(f"Exact population after {months} months: {exact[-1]:.0f} fish")
print(f"Maximum absolute error: {np.max(np.abs(P - exact)):.1f} fish")

plt.plot(t, P, marker="o", label="Euler"); plt.plot(t, exact, label="Exact")
plt.xlabel("Months"); plt.ylabel("Fish population")
plt.title("Logistic growth in a fish pond"); plt.legend(); plt.grid(True); plt.show()
