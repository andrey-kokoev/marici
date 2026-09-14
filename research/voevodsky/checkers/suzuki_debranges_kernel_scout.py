#!/usr/bin/env python3
"""Certified pointwise/2x2 scout for Suzuki's candidate second-stage kernel."""
import json, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_flint'))
from flint import arb, acb, acb_series, ctx
ctx.prec=192

I=acb(0,1); HALF=arb(1)/2; PI=arb.pi()

def xi_jet(s):
    """Return xi(s), xi'(s), rigorously via a degree-one power series."""
    x=acb_series([s,1],2)
    y=(x*(x-1)/2) * (-(x/2)*PI.log()).exp() * (x/2).gamma() * x.zeta()
    return y[0],y[1]

def E(z):
    s=HALF-I*z
    x,xp=xi_jet(s)
    return x+xp

def theta(z):
    return E(z.conjugate()).conjugate()/E(z)

def kernel(z,w):
    return (1-theta(z)*theta(w).conjugate())/(-I*(z-w.conjugate()))

def lower(x): return float(x.lower())
def upper(x): return float(x.upper())

# Interior points avoid all boundary-limit and derivative issues.
points=[acb('0','0.4'),acb('3','0.5'),acb('7','0.75'),acb('12','1')]
diag=[]; pairs=[]; passed=True
for i,z in enumerate(points):
    q=kernel(z,z)
    ok=q.imag.contains(0) and lower(q.real)>0
    passed &= ok
    diag.append({'i':i,'z':str(z),'kernel':str(q),'positive':ok})
for i in range(len(points)):
 for j in range(i+1,len(points)):
    a=kernel(points[i],points[i]).real
    d=kernel(points[j],points[j]).real
    b=kernel(points[i],points[j])
    det=a*d-b.real*b.real-b.imag*b.imag
    ok=lower(a)>0 and lower(d)>0 and lower(det)>0
    passed &= ok
    pairs.append({'ij':[i,j],'determinant':str(det),'positive_definite':ok})
out={'schema':'marici.suzuki-debranges-kernel-scout.v1','status':'passed' if passed else 'not_certified','precision_bits':ctx.prec,'kernel':'(1-Theta(z)conj(Theta(w)))/(-i(z-conj(w)))','points':diag,'two_by_two_minors':pairs,'scope':'Certified only at the listed points and pairs; no continuum or RH claim.'}
p=ROOT/'research/voevodsky/results/suzuki-debranges-kernel-scout.json';p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
raise SystemExit(0 if passed else 1)
