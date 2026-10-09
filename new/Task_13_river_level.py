import numpy as np
from scipy.interpolate import interp1d, CubicSpline
import matplotlib.pyplot as plt

# New case: a river gauge recorded the water level every 3 hours,
# but a flood-warning app needs hourly values. (Illustrative readings.)
hours = np.array([0, 3, 6, 9, 12, 15, 18, 21, 24], dtype=float)
level_m = np.array([1.20, 1.25, 1.40, 1.85, 2.30, 2.45, 2.20, 1.80, 1.50])

lin = interp1d(hours, level_m)
cub = CubicSpline(hours, level_m)
hourly = np.arange(0, 25, 1.0)
WARNING = 2.0   # warning level in metres (assumed)

print(f"Level at 10:00  linear: {float(lin(10)):.3f} m   cubic: {float(cub(10)):.3f} m")
above = hourly[cub(hourly) > WARNING]
print(f"Cubic spline: above {WARNING} m from {above.min():.0f}:00 to {above.max():.0f}:00")

plt.scatter(hours, level_m, label="3-hourly gauge readings", zorder=3)
plt.plot(hourly, lin(hourly), label="Linear")
plt.plot(np.linspace(0, 24, 300), cub(np.linspace(0, 24, 300)), label="Cubic spline")
plt.axhline(WARNING, linestyle="--", label="Warning level")
plt.xlabel("Hour"); plt.ylabel("Water level (m)")
plt.title("River level interpolation"); plt.legend(); plt.grid(True); plt.show()
