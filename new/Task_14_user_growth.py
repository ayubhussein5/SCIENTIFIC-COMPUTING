import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# New case: forecast monthly active users of a new student app
# using an exponential growth model y = a*exp(b*t). (Illustrative data.)
month = np.arange(1, 9, dtype=float)
users = np.array([520, 610, 740, 860, 1030, 1210, 1440, 1700], dtype=float)

def model(t, a, b):
    return a * np.exp(b * t)

(a, b), _ = curve_fit(model, month, users, p0=[400, 0.1])
rmse = np.sqrt(np.mean((users - model(month, a, b))**2))

print(f"Fitted model: users = {a:.1f} * exp({b:.4f} t)")
print(f"Monthly growth rate: {np.exp(b) - 1:.2%}")
print(f"RMSE: {rmse:.1f} users")
print(f"Forecast for month 12: {model(12, a, b):.0f} users")

t = np.linspace(1, 12, 200)
plt.scatter(month, users, label="Observed")
plt.plot(t, model(t, a, b), label="Exponential fit")
plt.xlabel("Month"); plt.ylabel("Active users")
plt.title("Student app user growth"); plt.legend(); plt.grid(True); plt.show()
