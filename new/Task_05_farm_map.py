import numpy as np

# New case: converting a farm plot from a sketch grid to a north-aligned map.
# Corners of the plot on the sketch (grid units).
plot = np.array([
    [0.0, 0.0],
    [4.0, 0.0],
    [4.0, 2.0],
    [0.0, 2.0]
])

angle = np.deg2rad(30)          # sketch is rotated 30 degrees from north
rotation = np.array([[np.cos(angle), -np.sin(angle)],
                     [np.sin(angle),  np.cos(angle)]])
scale = np.array([[25.0, 0.0],  # 1 grid unit = 25 m (assumed)
                  [0.0, 25.0]])

T = rotation @ scale
map_points = plot @ T.T

area_grid = 4.0 * 2.0
area_m2 = area_grid * abs(np.linalg.det(T))

print("Map coordinates (m):\n", np.round(map_points, 2))
print(f"Determinant (area scale factor): {np.linalg.det(T):.2f}")
print(f"Plot area: {area_m2:.0f} m^2 = {area_m2/10000:.2f} hectares")
