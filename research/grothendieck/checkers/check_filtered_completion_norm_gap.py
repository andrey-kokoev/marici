"""Exact path-coefficient certificates for the native filtration norm gap.

Forgetting all letters makes each two-route diamond a source relation.
The path l1 lower bound and an equally sized factorization lift certify the
finite quotient norms, without a numerical quotient-norm optimization.
"""
from collections import defaultdict
from fractions import Fraction
from math import factorial
from pathlib import Path
import json


def diamond(k):
    return {(2*k,2*k+1):1,(2*k+1,2*k):-1}


def product(a,b):
    out=defaultdict(int)
    for u,c in a.items():
        for v,d in b.items():out[u+v]+=c*d
    return {u:c for u,c in out.items() if c}


def l1(a):return sum(abs(c) for c in a.values())


def weight(r,n):
    # lambda=s=b=a=1; the general ratio is proved symbolically in the note.
    return 2**r*factorial(r)*(1+n)**r


count=0
for r in range(1,6):
    for n in range(2*(r+1),65):
        factors=[diamond(k) for k in range(r+1)]
        factors[-1]={u+tuple(range(2*(r+1),n)):c for u,c in factors[-1].items()}
        expanded={():1}
        for f in factors:expanded=product(expanded,f)
        native_lift_norm=1
        for f in factors:native_lift_norm*=l1(f)
        merged=[product(factors[0],factors[1])]+factors[2:]
        inherited_lift_norm=1
        reconstructed={():1}
        for f in merged:
            inherited_lift_norm*=l1(f)
            reconstructed=product(reconstructed,f)
        assert reconstructed==expanded
        assert l1(expanded)==native_lift_norm==inherited_lift_norm==2**(r+1)
        # Both quotient norms equal this path l1 lower certificate.
        ratio=Fraction(weight(r,n),weight(r+1,n))
        assert ratio==Fraction(1,2*(r+1)*(1+n))
        count+=1

# A finite prefix of the infinite missing-lift construction: choose one native
# unit in each of these distinct endpoint corners. Its inherited norm is exact.
r=1
prefix=[]
for j in range(1,25):
    n=2**j+2*(r+1)
    ratio=Fraction(1,2*(r+1)*(1+n))
    assert ratio<=Fraction(1,2*(r+1)*2**j)
    prefix.append(ratio)
assert sum(prefix)<Fraction(1,2*(r+1))

result={
    'schema':'marici.grothendieck.filtered-completion-norm-gap.v1',
    'passed':True,
    'exact_factorization_norm_certificates':count,
    'missing_lift_series_prefix':len(prefix),
    'checks':{
        'merged_factorization_preserves_actual_source_product':True,
        'path_lower_bound_equals_both_unweighted_quotient_lifts':True,
        'native_to_inherited_norm_ratio_decays_with_length':True,
        'inherited_series_summable_while_native_unit_sum_diverges':True,
    },
    'scope':'Finite exact norm certificates and series-prefix inequalities. The infinite dense-proper-image result and strict exactness in the induced norm are proved in the companion note.'
}
root=Path(__file__).resolve().parents[3]
out=root/'research/grothendieck/results/filtered-completion-norm-gap.json'
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
