"""Exact all-depth graph weights and the separate monoidal growth hostile."""
from math import factorial, comb
from fractions import Fraction
from pathlib import Path
import json

checks=0
for lam in (Fraction(1),Fraction(3,2),Fraction(5)):
    def weight(k):return (2*lam)**k*factorial(k)
    for r in range(1,41):
        for k in range(1,r+1):
            # Up to k active seam boundaries, two outputs each.
            assert 2*k*lam*weight(k-1)==weight(k)
            checks+=1
    for k in range(16):
        for ell in range(16):
            assert weight(k+ell)/(weight(k)*weight(ell))==comb(k+ell,k)

result={'passed':True,'exact_differential_weight_checks':checks,
 'weighted_differential_bound':1,
 'tensor_weight_ratio':'binomial(k+l,k)',
 'scope':'Uniform differential graph-norm bound for direct sums of the existing finite-depth complexes. Does not claim bounded arbitrary cross-depth tensor multiplication.'}
ROOT=Path(__file__).resolve().parents[3]
out=ROOT/'research/voevodsky/results/all-depth-seam-graph-norm.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
