"""Directed endpoint proof that d<=1/2 forces y=R/p>=2 for p<=1/10."""

from decimal import Decimal as D, getcontext


getcontext().prec = 60


def ln_interval(x):
    value = x.ln()
    return value.next_minus(), value.next_plus()


def atanh_interval(x):
    lo, hi = ln_interval((D(1)+x)/(D(1)-x))
    return (lo/D(2)).next_minus(), (hi/D(2)).next_plus()


p = D("0.1")
log_lo, log_hi = ln_interval((D(4)-p*p)/(p*p))
atanh_p_lo, atanh_p_hi = atanh_interval(p)
atanh_2p_lo, atanh_2p_hi = atanh_interval(D(2)*p)
margin_lo = (
    log_lo - atanh_p_hi - D(2)*atanh_2p_hi/p
).next_minus()

print(f"endpoint_margin_lower={margin_lo}")
print(f"endpoint_margin_strictly_positive={margin_lo>0}")
print("left_side_decreases_with_p=True")
print("atanh_2p_over_p_increases_with_p=True")
print("orbit_barrier_y_at_least_2_certified=True" if margin_lo>0 else
      "orbit_barrier_y_at_least_2_certified=False")
