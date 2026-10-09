import numpy as np
import matplotlib.pyplot as plt

# New case: estimate acceleration of a motorbike from speedometer data
# recorded every 0.5 s. (Illustrative readings.)
t = np.arange(0, 5.5, 0.5)
v = np.array([0.0, 1.6, 3.4, 5.0, 6.8, 8.1, 9.2, 10.0, 10.6, 11.0, 11.2])  # m/s

acc = np.gradient(v, t)   # central differences inside, one-sided at ends

for ti, vi, ai in zip(t, v, acc):
    print(f"t={ti:.1f}s  v={vi:5.1f} m/s  a={ai:5.2f} m/s^2")
print(f"Peak acceleration: {acc.max():.2f} m/s^2 at t={t[acc.argmax()]:.1f}s")

plt.plot(t, acc, marker="o")
plt.xlabel("Time (s)"); plt.ylabel("Acceleration (m/s^2)")
plt.title("Acceleration from speed data"); plt.grid(True); plt.show()
