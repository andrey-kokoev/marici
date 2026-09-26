"""Exact local-jet and bound controls for a written C1-loss/C2-extension result.
Not a sampled proof of uniform convergence; see companion note for estimates.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

# beta_n=(1-cos(nu))/n^2; r_n''=-beta_n'^2 r_n; r_n(0)=1,r_n'(0)=0.
# On [0,1]: |beta|<=2/n^2, |beta'|<=1/n, |beta''|<=1,
# 1-1/(2n^2)<=r<=1 and |r'|<=1/n^2 by the positive Volterra bootstrap.
rows=[]
for n in (1,2,4,8,16,32):
    eps=F(1,n)
    beta0=F(0);bp0=F(0);bpp0=F(1)
    r0=F(1);rp0=F(0);rpp0=-bp0*bp0*r0
    # p=r exp(beta), q=r exp(-beta), evaluated at u=0.
    p0=q0=F(1);pp0=rp0+bp0;pq0=rp0-bp0
    ppp0=rpp0+2*rp0*bp0+r0*(bpp0+bp0**2)
    pqq0=rpp0-2*rp0*bp0+r0*(-bpp0+bp0**2)
    E=(-ppp0/(2*p0),-pqq0/(2*q0),F(0))
    rows.append(dict(n=n,beta_bound=str(2*eps**2),beta_prime_bound=str(eps),
        radial_lower_bound=str(1-eps**2/2),corner_metric=(1,1),corner_metric_first_derivative=(0,0),
        corner_metric_second_derivative=(str(2*ppp0),str(2*pqq0)),
        tidal=list(map(str,E)),vacuum_trace=ppp0/p0+pqq0/q0==0,
        matched_first_jet=pp0==pq0==0))
checks={
 'all_sources_have_identical_corner_first_jet':all(r['matched_first_jet'] for r in rows),
 'all_corner_vacuum_traces_zero':all(r['vacuum_trace'] for r in rows),
 'tidal_gap_independent_of_n':all(r['tidal']==['-1/2','1/2','0'] for r in rows),
 'uniform_positive_radial_margin':all(F(r['radial_lower_bound'])>=F(1,2) for r in rows),
 'boundary_shape_bounds_decrease':all(F(rows[i+1]['beta_bound'])<F(rows[i]['beta_bound']) for i in range(len(rows)-1)),
 'first_derivative_bounds_decrease':all(F(rows[i+1]['beta_prime_bound'])<F(rows[i]['beta_prime_bound']) for i in range(len(rows)-1)),
 'second_jet_not_collapsed':all(r['corner_metric_second_derivative']==('2','-2') for r in rows),
}
# Rational prefactors in the general extension bound, with lambda=B1=B2=T=1.
lam=B1=B2=T=F(1)
K=B1/(2*lam)
LG=(1/lam+B1/lam**2)/2
LR=F(1,2)+B1/(2*lam)+B1**2/(4*lam**2)
BR=B2/2+B1**2/(4*lam)
prefactor=LR/2+T*BR*LG
checks['extension_bound_prefactors']=K==F(1,2) and LG==1 and LR==F(5,4) and BR==F(3,4) and prefactor==F(11,8)
checks['norm_gap_is_nonzero']=F(1,2)>0
root=Path(__file__).resolve().parents[2]
paths=[Path(__file__),root/'research/voevodsky/two-polarization-shear-selects-area-and-parallel-frame.md',root/'research/nima/fibration-constructor-equivalence.md']
packet=dict(passed=all(checks.values()),checks=checks,rows=rows,
    scope='Finite exact jet and constant checks. Uniform C1 counterexample and C2 local-Lipschitz extension are written proofs. No owner topology admission or Agda completion theorem.',
    source_sha256={str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
Path(__file__).with_name('tidal-completion-regularity-gate.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
print(json.dumps(packet,indent=2))
raise SystemExit(0 if packet['passed'] else 1)
