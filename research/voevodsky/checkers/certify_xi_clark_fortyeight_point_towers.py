#!/usr/bin/env python3
"""High-precision Sylvester certification of nested Clark towers through rung 48."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_flint'))
from flint import arb,acb,acb_series,acb_mat,ctx
ctx.prec=3072; I=acb(0,1); HALF=arb(1)/2; PI=arb.pi()
def xi_jet(s):
 x=acb_series([s,1],2); y=(x*(x-1)/2)* (-(x/2)*PI.log()).exp()*(x/2).gamma()*x.zeta(); return y[0],y[1]
def E(z):
 x,xp=xi_jet(HALF-I*z); return x+xp
def theta(z): return E(z.conjugate()).conjugate()/E(z)
def K(z,w): return (1-theta(z)*theta(w).conjugate())/(-I*(z-w.conjugate()))
# Deterministic, well-separated families; all coordinates are exact decimal strings.
moderate=[]; x=0
for j in range(48):
 if j: x += j+2
 moderate.append((str(x),str(.4+.27*j)))
high=[]; x=2
for j in range(48):
 if j: x += j+5
 high.append((str(x),str(2+.42*j+(1 if j%2 else 0))))
# Ordered bilateral family traverses negative to positive real coordinates.
bilateral=[]
for j in range(48):
 x=(j-24)*(j+8)/2
 y=.7+.16*abs(j-24)
 bilateral.append((str(x),str(y)))
families={'moderate48':moderate,'high48':high,'bilateral48':bilateral}
reports=[]; passed=True
for name,spec in families.items():
 pts=[acb(x,y) for x,y in spec]
 vals=[theta(z) for z in pts]
 G=[[(1-vals[i]*vals[j].conjugate())/(-I*(pts[i]-pts[j].conjugate())) for j in range(48)] for i in range(48)]
 leading=[]; okall=True
 for n in range(1,49):
  d=acb_mat([[G[i][j] for j in range(n)] for i in range(n)]).det()
  ok=d.imag.contains(0) and d.real.lower()>0; okall &= ok
  leading.append({'order':n,'lower_bound':str(d.real.lower()),'strictly_positive':ok})
 passed &= okall
 reports.append({'id':name,'points':[[float(x),float(y)] for x,y in spec],
  'leading_principal_minors':leading,'sylvester_positive_definite':okall})
out={'schema':'marici.voevodsky.xi-clark-fortyeight-point-towers.v1','precision_bits':ctx.prec,
 'families':reports,'family_count':len(reports),'all_towers_certified':passed,
 'consequence':'Every ordered prefix through rung 48 has a positive Clark Gram and canonical compatible finite Douglas contraction.',
 'scope':'Three explicit ordered 48-point families only; no arbitrary-packet inference.',
 'passed':passed,'rh_proved':False}
p=ROOT/'research/voevodsky/results/xi_clark_fortyeight_point_towers.json';p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'passed':passed,'precision_bits':ctx.prec,'families':[{'id':r['id'],'order48':r['leading_principal_minors'][-1]} for r in reports]},indent=2));raise SystemExit(0 if passed else 1)
