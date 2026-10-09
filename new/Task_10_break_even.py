import numpy as np
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt

# New case: break-even point for a small juice business.
# Price falls as more is sold: revenue R(q) = q(200 - 0.05q) KSh
# Cost: fixed KSh 20,000 + KSh 60 per bottle
def profit(q):
    return q*(200 - 0.05*q) - (20000 + 60*q)

sol = root_scalar(profit, bracket=[0, 1000], method="bisect", xtol=1e-8)

# Fixed-point form of the same equation: q = (20000 + 0.05 q^2) / 140
def g(q): return (20000 + 0.05*q**2) / 140
q = 100.0
for it in range(1, 200):
    q_new = g(q)
    if abs(q_new - q) < 1e-8: break
    q = q_new

print(f"Break-even (bisection): {sol.root:.2f} bottles, iterations {sol.iterations}")
print(f"Break-even (fixed point): {q_new:.2f} bottles, iterations {it}")
print(f"Profit at 400 bottles: KSh {profit(400):,.0f}")

qs = np.linspace(0, 2000, 400)
plt.plot(qs, profit(qs)); plt.axhline(0, linewidth=0.8)
plt.axvline(sol.root, linestyle="--")
plt.xlabel("Bottles sold per month"); plt.ylabel("Profit (KSh)")
plt.title("Break-even for juice business"); plt.grid(True); plt.show()
