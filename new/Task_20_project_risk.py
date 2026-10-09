import numpy as np
import matplotlib.pyplot as plt

# New case: risk that a 3-stage IT project misses a 30-day deadline.
# Each stage duration is uncertain (triangular: min, most likely, max days).
rng = np.random.default_rng(1)
N = 100_000
design = rng.triangular(5, 7, 12, N)
build  = rng.triangular(10, 14, 22, N)
test   = rng.triangular(3, 5, 9, N)
total = design + build + test

DEADLINE = 30
p_late = (total > DEADLINE).mean()
print(f"Mean project duration: {total.mean():.1f} days")
print(f"Probability of missing {DEADLINE}-day deadline: {p_late:.2%}")
print(f"Duration with 90% confidence: {np.percentile(total, 90):.1f} days")

plt.hist(total, bins=60)
plt.axvline(DEADLINE, linestyle="--", label="Deadline")
plt.xlabel("Total project duration (days)"); plt.ylabel("Number of simulations")
plt.title("Monte Carlo project-duration risk"); plt.legend(); plt.grid(True); plt.show()
