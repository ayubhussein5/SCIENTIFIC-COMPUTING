from scipy.optimize import root_scalar

# New case: what monthly interest rate does a lender charge?
# Loan KSh 50,000 repaid in 12 monthly instalments of KSh 4,800.
P, pay, n = 50000.0, 4800.0, 12

def f(r):    # present value of payments minus loan
    return pay * (1 - (1 + r)**-n) / r - P

def df(r):
    return pay * (n*r*(1 + r)**(-n - 1) - (1 - (1 + r)**-n)) / r**2

newton = root_scalar(f, fprime=df, x0=0.02, method="newton", xtol=1e-12)
secant = root_scalar(f, x0=0.01, x1=0.03, method="secant", xtol=1e-12)
r = newton.root
print(f"Monthly rate (Newton): {r:.6%}  in {newton.iterations} iterations")
print(f"Monthly rate (Secant): {secant.root:.6%}  in {secant.iterations} iterations")
print(f"Effective annual rate: {(1 + r)**12 - 1:.2%}")
print(f"Total repaid: KSh {pay*n:,.0f}  (interest KSh {pay*n - P:,.0f})")
