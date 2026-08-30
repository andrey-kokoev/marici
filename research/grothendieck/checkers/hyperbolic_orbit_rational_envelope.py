"""Exact ODE supersolution proof for a rational hyperbolic orbit envelope."""

import sympy as sp

p, t = sp.symbols("p T", positive=True)
denominator = 1-(1-p)*t**2
upper = p*t/denominator

# The exact orbit solves R_T=p(1-R^2)/(1-T^2).  A nonnegative
# supersolution with the same initial value bounds it from above.
reserve = sp.factor(
    sp.diff(upper,t)-p*(1-upper**2)/(1-t**2)
)
print("upper=", upper)
print("ode_supersolution_reserve=", reserve)
print("cleared_reserve=", sp.factor(reserve*(1-t**2)*denominator**2/p))
print("endpoint_at_T_0=", upper.subs(t,0))
print("endpoint_at_T_1=", sp.factor(upper.subs(t,1)))

a = (1-p**2)/3
b = (1-p)*(2-p)/3
denominator2 = 1-a*t**2-b*t**4
upper2 = p*t/denominator2
reserve2 = sp.factor(sp.diff(upper2,t)-p*(1-upper2**2)/(1-t**2))
print("matched_upper=", sp.factor(upper2))
print("matched_reserve_factor=", reserve2)
print("matched_cleared_reserve=", sp.factor(
    reserve2*(1-t**2)*denominator2**2/p
))
print("matched_endpoint_at_T_1=", sp.factor(upper2.subs(t,1)))
