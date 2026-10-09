import numpy as np
from scipy.optimize import root

# New case: locate a phone from distances to two cell towers (trilateration).
# Tower 1 at (0, 0) km, measured distance 5 km
# Tower 2 at (6, 0) km, measured distance 4 km
def equations(z):
    x, y = z
    return [x**2 + y**2 - 25,
            (x - 6)**2 + y**2 - 16]

for guess in ([3.0, 3.0], [3.0, -3.0]):
    s = root(equations, guess)
    print(f"Guess {guess} -> location {np.round(s.x, 4)} km, converged: {s.success}")
