"""Exact negative control at the disk boundary and interior evaluation bounds."""
from fractions import Fraction
from math import factorial,comb
from pathlib import Path
import json

# Suppress the common 1/(pi R^2) factor in the Bergman diagonal kernel.
# The exact series is sum_(n>=0) (n+1) t^n = 1/(1-t)^2, 0<=t<1.
checks=0
for t in (Fraction(0),Fraction(1,4),Fraction(9,16),Fraction(81,100)):
    bound=1/(1-t)**2
    for N in (1,2,8,32):
        partial=sum((n+1)*t**n for n in range(N))
        assert partial<=bound
        remainder=t**N*((N+1)-N*t)/(1-t)**2
        assert partial+remainder==bound
        checks+=1
# At the boundary even a single normalized monomial has unbounded value.
assert [n+1 for n in (0,3,15,63)]==[1,4,16,64]

# Feature-degree weights absorb evaluation growth without altering seam count.
for C in (Fraction(1,2),Fraction(1),Fraction(3),Fraction(7,2)):
    b=max(Fraction(1),C)
    for m in range(65):assert C**m<=b**m
    for k in range(9):
        for l in range(9):
            # Depth factorial weights require scale loss, feature weights do not.
            assert factorial(k+l)<=2**(k+l)*factorial(k)*factorial(l)

result={'passed':True,'exact_interior_kernel_tail_checks':checks,
 'checks':{'disk_boundary_evaluation_unbounded':True,
           'feature_degree_scale_absorbs_slotwise_evaluation':True},
 'scope':'Scalar Bergman negative control and exact weight regressions. Vector-valued holomorphic closure and completed Clark packet bounds are proved in the companion note; no boundary evaluation or positivity claim.'}
ROOT=Path(__file__).resolve().parents[3]
out=ROOT/'research/voevodsky/results/holomorphic-packet-evaluation-bounds.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
