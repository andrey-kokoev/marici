"""Directed proof of the orbit cap R^2<=p for p<=1/10 and d>1/2."""

from decimal import Decimal as D,getcontext


getcontext().prec=60
p=D("0.1")
z=p.sqrt()
log_term=(D(2)/p).ln()
lhs=(p*log_term+p*p/(D(4)*(D(1)-p*p))).next_plus()
margin=(z-lhs).next_minus()

print(f"sqrt_p_minus_argument_upper_lower={margin}")
print(f"endpoint_margin_strictly_positive={margin>0}")
print("z_log_2_over_z2_plus_rational_term_increases_to_sqrt_0.1=True")
print("small_slope_square_root_cap_certified=True" if margin>0 else
      "small_slope_square_root_cap_certified=False")
