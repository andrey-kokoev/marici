"""Exact outward certificate for the dominant Chart-1 upper-y/lower-q corner."""
from fractions import Fraction as F
from pathlib import Path
import json
from theta_dominant_fraction_interval_core import Dual, Interval, cancellation_free_residual_quotient
q=Dual(Interval(F(3,10)))
y=Dual(Interval(F(1,28)))
D=cancellation_free_residual_quotient(q,y).value
assert D.lo>32
# Tightened-threshold witness: the same outward box lies strictly below 33,
# so replacing the theorem threshold 32 by 33 must fail.
assert D.hi<33
result={"q":"3/10","y":"1/28",
 "D_lower_numerator_hex":hex(D.lo.numerator),"D_lower_denominator_hex":hex(D.lo.denominator),
 "D_upper_numerator_hex":hex(D.hi.numerator),"D_upper_denominator_hex":hex(D.hi.denominator),
 "D_lower_float":float(D.lo),"D_upper_float":float(D.hi),
 "strictly_above_32":D.lo>32,"strictly_below_33":D.hi<33,
 "tightened_threshold_33_certified":D.lo>33}
out=json.dumps(result,indent=2)+"\n"
Path("research/grothendieck/results/theta-dominant-corner-exact.json").write_text(out)
print(out,end="")
