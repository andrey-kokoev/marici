#!/usr/bin/env python3
"""Arb-certify Clark-kernel positivity for several independent nested point families."""
import itertools,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_flint'))
from flint import arb,acb,acb_series,ctx
ctx.prec=512; I=acb(0,1); HALF=arb(1)/2; PI=arb.pi()

def xi_jet(s):
    x=acb_series([s,1],2)
    y=(x*(x-1)/2)* (-(x/2)*PI.log()).exp()*(x/2).gamma()*x.zeta()
    return y[0],y[1]
def E(z):
    x,xp=xi_jet(HALF-I*z); return x+xp
def theta(z): return E(z.conjugate()).conjugate()/E(z)
def K(z,w): return (1-theta(z)*theta(w).conjugate())/(-I*(z-w.conjugate()))
def parity(p): return -1 if sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2 else 1
def det(A):
    out=acb(0)
    for p in itertools.permutations(range(len(A))):
        x=acb(parity(p))
        for i,j in enumerate(p): x*=A[i][j]
        out+=x
    return out

families={
 'baseline': [('0','.4'),('3','.5'),('7','.75'),('12','1'),('18','1.25'),('24','1.5')],
 'high_imaginary': [('2','2'),('8','3'),('14','2'),('20','4'),('27','3'),('35','5')],
 'translated_moderate': [('5','.6'),('9','.8'),('14','1.1'),('20','1.4'),('27','1.7'),('35','2')],
 'mixed_spacing': [('-6','.7'),('-1','1.3'),('4','.9'),('11','1.8'),('19','1.1'),('30','2.4')],
}
reports=[]; all_pass=True
for name,spec in families.items():
    pts=[acb(x,y) for x,y in spec]; G=[[K(z,w) for w in pts] for z in pts]
    counts={}; lower_by_order={}; family_pass=True
    for n in range(1,7):
        good=0; lower=None
        for idx in itertools.combinations(range(6),n):
            d=det([[G[i][j] for j in idx] for i in idx])
            ok=d.imag.contains(0) and float(d.real.lower())>0
            family_pass &= ok; good+=int(ok)
            lo=float(d.real.lower()); lower=lo if lower is None else min(lower,lo)
        counts[str(n)]=good; lower_by_order[str(n)]=lower
    all_pass &= family_pass
    reports.append({'id':name,'points':[[float(x),float(y)] for x,y in spec],
      'positive_count_by_order':counts,'minimum_lower_bound_by_order':lower_by_order,
      'all_63_principal_minors_strictly_positive':family_pass})
out={'schema':'marici.voevodsky.xi-clark-multiple-point-families.v1','precision_bits':ctx.prec,
 'families':reports,'family_count':len(reports),'all_families_certified':all_pass,
 'consequence':'Each listed ordering gives a compatible strict finite Douglas contraction tower through rung six.',
 'scope':'Four explicit nested families only; no arbitrary-packet or continuum inference.',
 'passed':all_pass,'rh_proved':False}
p=ROOT/'research/voevodsky/results/xi_clark_multiple_point_families.json'
p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2)); raise SystemExit(0 if all_pass else 1)
