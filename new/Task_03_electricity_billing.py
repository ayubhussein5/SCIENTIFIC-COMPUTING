import numpy as np
import timeit

# New case: billing one million smart-meter customers (illustrative data).
rng = np.random.default_rng(7)
usage_kwh = rng.uniform(10, 400, 1_000_000)   # monthly kWh per customer
TARIFF = 25.0                                  # KSh per kWh (assumed flat rate)
VAT = 0.16                                     # 16% VAT

def loop_version():
    bills = []
    for kwh in usage_kwh:
        bills.append(kwh * TARIFF * (1 + VAT))
    return bills

def vectorized_version():
    return usage_kwh * TARIFF * (1 + VAT)

loop_time = timeit.timeit(loop_version, number=1)
vector_time = timeit.timeit(vectorized_version, number=3) / 3
bills = vectorized_version()

print("First five bills (KSh):", np.round(bills[:5], 2))
print(f"Total billed: KSh {bills.sum():,.0f}")
print(f"Loop time: {loop_time:.4f} s")
print(f"Vectorized time: {vector_time:.4f} s")
print(f"Approximate speed-up: {loop_time/vector_time:.1f}x")
