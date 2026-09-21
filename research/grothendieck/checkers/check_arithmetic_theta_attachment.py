"""High-precision checks of explicit first-theta-atom attachment matrices.

Analytic proof is in the companion note. Numerical checks are regression tests,
not interval certificates or proofs of conditioning.
"""
from pathlib import Path
import json
import mpmath as mp
mp.mp.dps=100
pi=mp.pi
labels=(1,2,3,6)

def column(n,u):
    return (2*pi**2*n**4*mp.exp(mp.mpf(9)*u/2)
            -3*pi*n**2*mp.exp(mp.mpf(5)*u/2))*mp.exp(-pi*n*n*mp.exp(2*u))

def moment(r,c,a,b):
    lo=c*mp.exp(2*a)
    hi=mp.inf if b==mp.inf else c*mp.exp(2*b)
    return mp.gammainc(r,lo,hi)/c**r

def kernel(m,n,a,b):
    c=pi*(m*m+n*n)
    return (2*pi**4*m**4*n**4*moment(mp.mpf(9)/2,c,a,b)
            -3*pi**3*(m**4*n**2+m**2*n**4)*moment(mp.mpf(7)/2,c,a,b)
            +mp.mpf(9)/2*pi**2*m**2*n**2*moment(mp.mpf(5)/2,c,a,b))

def close(x,y):
    return abs(x-y)<mp.mpf('1e-75')*max(abs(x),abs(y),mp.mpf('1e-2000'))

cuts=(mp.mpf(0),mp.log(2),mp.log(3),mp.log(6),mp.inf)
checks={}
for m in labels:
    for n in labels:
        pieces=[kernel(m,n,a,b) for a,b in zip(cuts,cuts[1:])]
        assert close(sum(pieces),kernel(m,n,0,mp.inf))
        for p in (2,3):
            # A_p=sqrt(p) S_p, with S_p e_n=e_(pn).
            assert close(p*kernel(p*m,p*n,0,mp.inf),kernel(m,n,mp.log(p),mp.inf))
            assert close(kernel(m,n,0,mp.inf)-p*kernel(p*m,p*n,0,mp.inf),
                         kernel(m,n,0,mp.log(p)))
checks['all_mixed_entries_stein_and_common_refinement']=True
# Independent direct integration on a substantial first window.
for m,n in ((1,1),(1,2),(2,3)):
    direct=mp.quad(lambda u:column(m,u)*column(n,u),[0,mp.log(2)/2,mp.log(2)])
    assert close(direct,kernel(m,n,0,mp.log(2)))
checks['incomplete_gamma_formula_matches_quadrature']=True
for m in labels:
    for n in labels:
        lhs=kernel(m,n,0,mp.log(2))+2*kernel(2*m,2*n,0,mp.log(3))
        rhs=kernel(m,n,0,mp.log(3))+3*kernel(3*m,3*n,0,mp.log(2))
        assert close(lhs,rhs) and close(lhs,kernel(m,n,0,mp.log(6)))
checks['two_prime_polarized_attachment_square']=True
# Delta is genuinely present on a nonzero basis state.
assert kernel(1,1,mp.log(2),mp.log(3))>0
checks['ratio_window_has_positive_energy']=True
result={'schema':'marici.grothendieck.arithmetic-theta-attachment.v1',
        'passed':True,'precision_decimal_digits':100,'labels':labels,'checks':checks,
        'scope':'First theta atom numerical regression. General forcing identities proved analytically; Xi-to-Haar comparison remains uninstantiated.'}
p=Path(__file__).resolve().parents[1]/'results/arithmetic-theta-attachment.json'
p.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
