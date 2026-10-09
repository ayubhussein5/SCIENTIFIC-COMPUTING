import numpy as np
from scipy.integrate import simpson

# New case: distance travelled by a bus from speed readings every 10 s.
t = np.arange(0, 130, 10, dtype=float)                 # 0 to 120 s
v = np.array([0, 5, 9, 12, 14, 15, 15, 14, 12, 9, 6, 3, 0], dtype=float)  # m/s

d_trap = np.trapezoid(v, t)
d_simp = simpson(v, x=t)
print(f"Distance (trapezoidal): {d_trap:.1f} m")
print(f"Distance (Simpson):     {d_simp:.1f} m")
print(f"Difference: {abs(d_simp - d_trap):.1f} m")
print(f"Average speed: {d_simp/120*3.6:.1f} km/h")
