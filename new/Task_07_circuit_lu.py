import numpy as np
from scipy.linalg import lu_factor, lu_solve

# New case: 3-loop electrical circuit (mesh analysis). Resistances fixed,
# source voltages change every hour, so we factor once and reuse.
R = np.array([
    [15.0, -5.0,  0.0],
    [-5.0, 20.0, -10.0],
    [ 0.0, -10.0, 25.0]
])   # ohms

hourly_voltages = {
    "08:00": np.array([12.0, 0.0, 6.0]),
    "09:00": np.array([10.0, 2.0, 6.0]),
    "10:00": np.array([12.0, 4.0, 3.0]),
}

lu, piv = lu_factor(R)
for hour, V in hourly_voltages.items():
    I = lu_solve((lu, piv), V)
    residual = np.linalg.norm(V - R @ I)
    print(f"{hour}  loop currents (A): {np.round(I, 4)}  residual: {residual:.1e}")
