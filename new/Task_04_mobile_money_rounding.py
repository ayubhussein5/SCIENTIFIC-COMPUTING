import numpy as np
from decimal import Decimal

# New case: a mobile-money system adds a KSh 0.10 fee one million times.
N = 1_000_000
fee = 0.10

total_float = 0.0
for _ in range(N):
    total_float += fee                       # binary floating point

total_cents = N * 10                         # store money as whole cents
total_decimal = sum([Decimal("0.10")] * N)   # exact decimal arithmetic

expected = 100_000.00
abs_err = abs(total_float - expected)

print(f"Float total:   {total_float:.10f}")
print(f"Cents total:   {total_cents/100:.2f}")
print(f"Decimal total: {total_decimal}")
print(f"Absolute error of float total: {abs_err:.3e}")
print(f"Relative error of float total: {abs_err/expected:.3e}")
print("Float equals expected?", total_float == expected)
print("np.isclose?", np.isclose(total_float, expected))
