"""Exact shift-vector preflight for the first two-translate spline Gram hostile."""
from fractions import Fraction as F
import json
base={2:F(1),1:F(-5),0:F(33,4),-1:F(-5),-2:F(1)}
# Symmetric physical translation delta=2a shifts the spline index by one.
cross={m:(base.get(m-1,F(0))+base.get(m+1,F(0)))/2 for m in range(-3,4)}
expected={3:F(1,2),2:F(-5,2),1:F(37,8),0:F(-5),-1:F(37,8),-2:F(-5,2),-3:F(1,2)}
assert cross==expected
assert all(cross[m]==cross[-m] for m in cross)
assert list(base.values())==[F(1),F(-5),F(33,4),F(-5),F(1)]
# Deliberate failure: one-sided translation is not Hermitian-symmetric.
one_sided={m:base.get(m-1,F(0)) for m in range(-3,4)}
assert any(one_sided[m]!=one_sided[-m] for m in one_sided)
print(json.dumps({'schema':'marici.nima.first-two-translate-spline-shift-vector.v1','status':'passed','base_by_descending_shift':[[m,str(base[m])] for m in range(2,-3,-1)],'cross_by_descending_shift':[[m,str(cross[m])] for m in range(3,-4,-1)],'symmetric':True,'baseline_regression_preserved':True,'deliberate_failure':'one-sided translation violates Hermitian shift symmetry','next_test':'interval-evaluate L on arbitrary symmetric shift lists and test L(f)^2-L(f_delta)^2'},sort_keys=True))
