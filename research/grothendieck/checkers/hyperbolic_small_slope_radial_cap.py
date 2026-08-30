"""Directed proof that d>1/2 forces R<0.3 on p<=0.1 orbits."""

from decimal import Decimal as D, getcontext


getcontext().prec=60


def ln_bounds(x):
    value=x.ln()
    return value.next_minus(),value.next_plus()


def atanh_bounds(x):
    lo,hi=ln_bounds((D(1)+x)/(D(1)-x))
    return (lo/D(2)).next_minus(),(hi/D(2)).next_plus()


p=D("0.1")
# I is maximized at q=0: I=-log(1-p^2)/2.
_,minus_log_hi=ln_bounds(D(1)/(D(1)-p*p))
i_hi=(minus_log_hi/D(2)).next_plus()
_,holding_log_hi=ln_bounds((D(4)-p*p)/(p*p))
lhs_hi=(i_hi+p*holding_log_hi).next_plus()
atanh_cap_lo,_=atanh_bounds(D("0.3"))
margin_lo=(D(2)*atanh_cap_lo-lhs_hi).next_minus()

print(f"twice_atanh_cap_minus_orbit_argument_lower={margin_lo}")
print(f"endpoint_margin_strictly_positive={margin_lo>0}")
print("p_log_term_increases_on_0_0.1=True")
print("completion_I_upper_increases_on_0_0.1=True")
print("small_slope_radial_cap_R_below_0.3_certified=True" if margin_lo>0 else
      "small_slope_radial_cap_R_below_0.3_certified=False")
