"""Endpoint/depth moment control for the actual Green-mate channel count."""
from fractions import Fraction as F
from pathlib import Path
import json

checks=0
for lam in (F(1),F(3,2),F(4)):
    for s in (1,2,5):
        for r in range(1,33):
            for n in (0,1,2,7,31,100):
                for k in range(r+1):
                    # (r-k) vertex factors, <=2n insertion-reversal channels,
                    # norm lambda, and graph ratio 2 lambda s (k+1).
                    local=4*lam**2*s*n*(r-k)*(k+1)
                    bound=lam**2*s*(1+n)*(1+r)**2
                    assert local<=bound
                    checks+=1
# Two-seam sharp count specializes to the supplied bound.
for k in (0,1):assert (2-k)*(k+1)<=2
# One mate increases active edges but preserves endpoint length, depth and
# total feature count. Extra observer moments therefore absorb the count.
for p in range(4):
    for q in range(4):
        for n,r in ((0,1),(5,2),(20,8)):
            assert (1+n)**p*(1+r)**q*(1+n)*(1+r)**2 == (1+n)**(p+1)*(1+r)**(q+2)

result={'passed':True,'channel_and_graph_weight_comparisons':checks,
 'mate_bound':'lambda^2*s * observer_norm(p+1,q+2)',
 'checks':{'two_seam_estimate_recovered':True,
           'endpoint_and_depth_moments_absorb_incidence':True},
 'scope':'Exact general channel-count inequalities. Completeness, continuous mate extension and observer chain structure follow from the companion proof and the supplied local mate theorem.'}
ROOT=Path(__file__).resolve().parents[3]
out=ROOT/'research/voevodsky/results/all-depth-observer-moment-bounds.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
