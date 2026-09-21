"""Regression for analytic weighted theta-tail and path-derivative bounds.

Numerical fixtures illustrate proved inequalities, not interval certificates.
"""
from pathlib import Path
from math import comb
import json
import mpmath as mp
mp.mp.dps=60
beta=mp.mpf(3);y0=mp.mpf(4)
p=beta+mp.mpf(13)/2
c=mp.pi*y0/2
C=5*mp.pi**2/mp.sqrt(2)*mp.sqrt(mp.gammainc(p,mp.pi*y0,mp.inf)/mp.pi**p)

def tail_bound(K):
    n=K+1
    ratio=16*mp.exp(-c*(2*n+1))
    assert ratio<1
    return C*n**4*mp.exp(-c*n*n)/(1-ratio)

fixtures=[]
for K in (0,1,2,4,8):
    bound=tail_bound(K)
    # L2 norm of the polynomial atom MAJORANT, via incomplete gamma.
    exact_majorants=mp.mpf(0)
    for n in range(K+1,K+21):
        rate=2*mp.pi*n*n
        exact_majorants+=5*mp.pi**2*n**4/mp.sqrt(2)*mp.sqrt(mp.gammainc(p,rate*y0,mp.inf)/rate**p)
    assert exact_majorants<=bound
    fixtures.append({'cutoff':K,'analytic_bound':mp.nstr(bound,18),
                     'twenty_atom_majorant_sum':mp.nstr(exact_majorants,18)})

# Marking r distinct events costs at most binomial(n,r), with a fixed
# seam/memory norm ratio lambda per marked site.
counts=[]
for r in (1,2,3):
    for n in (r,r+1,7,20):
        count=comb(n,r)
        assert count<= (1+n)**r
        counts.append({'path_length':n,'seams':r,'terms':count})
result={'passed':True,'beta':3,'lower_log_coordinate':'log(2)',
 'theta_tail_regressions':fixtures,'ordered_distinct_seam_counts':counts,
 'scope':'Analytic inequalities proved in companion note; mpmath values are non-certified regressions. Does not establish completed source injectivity.'}
ROOT=Path(__file__).resolve().parents[3]
out=ROOT/'research/voevodsky/results/weighted-theta-tail-and-path-bounds.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
