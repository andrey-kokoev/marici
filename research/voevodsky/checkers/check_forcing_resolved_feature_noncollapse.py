"""Exact normalization and tensor-separation fixtures, not sampled spectra."""
from pathlib import Path
import json
import sympy as s
A=(s.I*s.Matrix([[-1,1,1,1],[-1,1,-1,-1]])/2)*s.diag(s.I,-s.I,s.I,-s.I)
J=s.diag(1,-1)
assert s.ones(1,2)*A==s.Matrix([[1,1,0,0]])
assert A.rank()==2 and (A.H*J*A).rank()==2

# An injective compact diagonal model shows why no uniform lower bound is
# required for tensor separation and why such a lower bound cannot be inferred.
fixtures=[]
for n in (2,3,5):
    L=s.diag(*(s.Rational(1,k) for k in range(1,n+1)))
    for d in (1,2,3):
        T=L
        for _ in range(d-1):T=s.kronecker_product(T,L)
        assert all(T[i,i]!=0 for i in range(T.rows))
        fixtures.append({'dimension':n,'tensor_degree':d,'injective':True,
                         'smallest_diagonal':str(s.Rational(1,n)**d)})
# Finite coordinate projections separate a tensor even if one low truncation
# misses it; full projection family, not a fixed finite rank test, is needed.
v=s.zeros(9,1);v[8]=1
P=s.diag(1,1,0)
assert s.kronecker_product(P,P)*v==s.zeros(9,1)
assert s.kronecker_product(s.eye(3),s.eye(3))*v==v
result={'passed':True,'checks':{'normalized_sheet_sum_is_even_zeroth_trace':True,
 'singular_raw_coefficient_not_used_as_signature':True,
 'one_fixed_projection_can_miss_a_nonzero_tensor':True},
 'tensor_fixtures':fixtures,
 'scope':'Normalization and abstract finite tensor fixtures. Infinite forcing and projective tensor injectivity use strip Fourier uniqueness, dense adjoint range, and finite-rank approximation in the companion proof.'}
ROOT=Path(__file__).resolve().parents[3]
out=ROOT/'research/voevodsky/results/forcing-resolved-feature-noncollapse.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
