#!/usr/bin/env python3
"""High-precision Sylvester certification of nested Clark towers through rung sixteen."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_flint'))
from flint import arb,acb,acb_series,acb_mat,ctx
ctx.prec=1024; I=acb(0,1); HALF=arb(1)/2; PI=arb.pi()
def xi_jet(s):
 x=acb_series([s,1],2); y=(x*(x-1)/2)* (-(x/2)*PI.log()).exp()*(x/2).gamma()*x.zeta(); return y[0],y[1]
def E(z):
 x,xp=xi_jet(HALF-I*z); return x+xp
def theta(z): return E(z.conjugate()).conjugate()/E(z)
def K(z,w): return (1-theta(z)*theta(w).conjugate())/(-I*(z-w.conjugate()))
families={
 'moderate16':[(str(x),str(y)) for x,y in [(0,.4),(3,.5),(7,.75),(12,1),(18,1.25),(24,1.5),(31,1.8),(39,2.1),(48,2.4),(58,2.7),(69,3),(81,3.3),(94,3.6),(108,3.9),(123,4.2),(139,4.5)]],
 'high16':[(str(x),str(y)) for x,y in [(2,2),(8,3),(14,2),(20,4),(27,3),(35,5),(44,4),(54,6),(65,5),(77,7),(90,6),(104,8),(119,7),(135,9),(152,8),(170,10)]],
 'bilateral16':[(str(x),str(y)) for x,y in [(-48,3),(-39,2.5),(-31,2.1),(-24,1.7),(-18,1.3),(-12,1),(-6,.8),(-1,.6),(5,.7),(12,1),(20,1.2),(29,1.5),(39,1.8),(50,2.1),(62,2.5),(75,3)]]
}
reports=[]; passed=True
for name,spec in families.items():
 pts=[acb(x,y) for x,y in spec]; G=[[K(z,w) for w in pts] for z in pts]; leading=[]; okall=True
 for n in range(1,17):
  d=acb_mat([[G[i][j] for j in range(n)] for i in range(n)]).det()
  ok=d.imag.contains(0) and float(d.real.lower())>0; okall &= ok
  leading.append({'order':n,'lower_bound':float(d.real.lower()),'strictly_positive':ok})
 passed &= okall
 reports.append({'id':name,'points':[[float(x),float(y)] for x,y in spec],
  'leading_principal_minors':leading,'sylvester_positive_definite':okall})
out={'schema':'marici.voevodsky.xi-clark-sixteen-point-towers.v1','precision_bits':ctx.prec,
 'families':reports,'family_count':len(reports),'all_towers_certified':passed,
 'consequence':'Every ordered prefix through rung sixteen has a positive Clark Gram and canonical compatible finite Douglas contraction.',
 'scope':'Three explicit ordered sixteen-point families only; no arbitrary-packet inference.',
 'passed':passed,'rh_proved':False}
p=ROOT/'research/voevodsky/results/xi_clark_sixteen_point_towers.json';p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2));raise SystemExit(0 if passed else 1)
