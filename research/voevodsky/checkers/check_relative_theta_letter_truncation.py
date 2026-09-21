"""Uniform relative theta tails: exact algebra and high-precision regressions."""
from pathlib import Path
import json
import sympy as s
import mpmath as mp
mp.mp.dps=80
# t=pi*exp(2x)>=12, n>=1. Bound the polynomial atom ratio by (8/7)n^4.
t,n=s.symbols('t n',positive=True)
ratio=n**2*(2*n**2*t-3)/(2*t-3)
assert s.simplify(n**4*(2*t)/(2*t-3)-ratio)==3*n**2/(2*t-3)
# 2t/(2t-3)<=8/7 iff t>=12.
assert s.simplify(s.Rational(8,7)-2*t/(2*t-3)-2*(t-12)/(7*(2*t-3)))==0

def bound(K):
    m=K+1
    r=16*mp.exp(-12*(2*K+3))
    return mp.mpf(8)/7*m**4*mp.exp(-12*(m*m-1))/(1-r)

def atom_ratio(n,y):
    return n*n*(2*mp.pi*n*n*y-3)/(2*mp.pi*y-3)*mp.exp(-mp.pi*(n*n-1)*y)

fixtures=[]
for K in (1,2,3,5):
    eta=bound(K)
    assert 0<eta<1
    for y in (mp.mpf(4),mp.mpf(16),mp.mpf(100)):
        # Normalize by atom 1 to avoid underflow. A finite relative tail is
        # a regression only; the infinite sum is bounded analytically.
        ratios=[atom_ratio(n,y) for n in range(1,K+21)]
        partial_relative=sum(ratios[K:])/sum(ratios)
        assert 0<=partial_relative<=eta
    fixtures.append({'cutoff':K,'uniform_relative_majorant':mp.nstr(eta,22)})

# Tensor substitution: contractions with relative error eps telescope.
eps=s.Rational(1,100)
for d in range(1,65):
    assert 1-(1-eps)**d<=d*eps
    assert d<=2**d
result={'passed':True,'relative_tail_fixtures':fixtures,
 'checks':{'positive_atom_polynomial_majorant':True,
 'relative_tensor_error_and_radius_two_bound':True},
 'scope':'Exact polynomial and tensor inequalities; numerical atom ratios are regressions, not interval certificates. Uniform infinite relative tails follow from the geometric majorant in the companion proof.'}
ROOT=Path(__file__).resolve().parents[3]
out=ROOT/'research/voevodsky/results/relative-theta-letter-truncation.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
