import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# New case: flu outbreak in a school of 1,000 students (SIR model).
N = 1000.0
beta = 0.5     # contacts that transmit per day (assumed)
gamma = 0.2    # recovery rate per day (about 5 days ill)

def sir(t, y):
    S, I, R = y
    return [-beta*S*I/N, beta*S*I/N - gamma*I, gamma*I]

sol = solve_ivp(sir, (0, 60), [999, 1, 0], t_eval=np.linspace(0, 60, 601), rtol=1e-8)
S, I, R = sol.y
peak = I.argmax()
print("Solver success:", sol.success)
print(f"R0 = beta/gamma = {beta/gamma:.1f}")
print(f"Peak infections: {I[peak]:.0f} students on day {sol.t[peak]:.1f}")
print(f"Total ever infected after 60 days: {R[-1] + I[-1]:.0f}")

plt.plot(sol.t, S, label="Susceptible"); plt.plot(sol.t, I, label="Infected")
plt.plot(sol.t, R, label="Recovered")
plt.xlabel("Day"); plt.ylabel("Students"); plt.title("School flu outbreak (SIR)")
plt.legend(); plt.grid(True); plt.show()
