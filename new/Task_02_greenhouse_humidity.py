import numpy as np

# New case: greenhouse humidity monitoring (illustrative sensor data).
# 24 hourly relative-humidity readings (%) from a tomato greenhouse.
humidity = np.array([
    88, 90, 91, 92, 92, 90,
    85, 78, 70, 63, 58, 55,
    53, 54, 57, 61, 66, 72,
    77, 81, 84, 86, 87, 88
], dtype=float)

THRESHOLD = 85.0   # above this, fungal disease risk rises (assumed threshold)

print(f"Mean humidity: {humidity.mean():.2f} %")
print(f"Minimum humidity: {humidity.min():.0f} %")
print(f"Maximum humidity: {humidity.max():.0f} %")

risky = humidity > THRESHOLD                 # vectorized comparison
print(f"Hours above {THRESHOLD:.0f}%: {risky.sum()} of 24")
print("Risky hours (0 = midnight):", np.where(risky)[0])

# Vectorized conversion of % to a 0-1 fraction for a control model
fraction = humidity / 100
print("First six readings as fractions:", fraction[:6])
