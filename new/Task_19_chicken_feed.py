from scipy.optimize import minimize

# New case: cheapest chicken-feed mix from maize and soybean meal.
# Per kg: maize KSh 45, 9% protein; soybean KSh 90, 44% protein.
# Need 100 kg of feed with at least 18% protein (18 kg protein).
def cost(z):
    m, s = z
    return 45*m + 90*s

cons = [
    {"type": "eq",   "fun": lambda z: z[0] + z[1] - 100},           # 100 kg total
    {"type": "ineq", "fun": lambda z: 0.09*z[0] + 0.44*z[1] - 18},  # protein
]
sol = minimize(cost, x0=[50, 50], method="SLSQP", bounds=[(0, None)]*2, constraints=cons)
m, s = sol.x
print("Optimization success:", sol.success)
print(f"Maize: {m:.2f} kg   Soybean meal: {s:.2f} kg")
print(f"Protein: {(0.09*m + 0.44*s):.2f} kg ({(0.09*m + 0.44*s)/100:.1%})")
print(f"Minimum cost: KSh {sol.fun:,.2f} per 100 kg")
