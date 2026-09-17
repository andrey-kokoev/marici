#!/usr/bin/env python3
"""Arb-certified principal-minor audit for nested Clark packet rungs 1..6."""
import itertools,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_flint'))
from flint import arb,acb,acb_series,ctx
ctx.prec=512;I=acb(0,1);HALF=arb(1)/2;PI=arb.pi()
def xi_jet(s):
 x=acb_series([s,1],2);y=(x*(x-1)/2)* (-(x/2)*PI.log()).exp()*(x/2).gamma()*x.zeta();return y[0],y[1]
def E(z):
 x,xp=xi_jet(HALF-I*z);return x+xp
def theta(z):return E(z.conjugate()).conjugate()/E(z)
def K(z,w):return (1-theta(z)*theta(w).conjugate())/(-I*(z-w.conjugate()))
def parity(p):return -1 if sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2 else 1
def det(A):
 out=acb(0)
 for p in itertools.permutations(range(len(A))):
  x=acb(parity(p))
  for i,j in enumerate(p):x*=A[i][j]
  out+=x
 return out
spec=[('0','.4'),('3','.5'),('7','.75'),('12','1'),('18','1.25'),('24','1.5')]
pts=[acb(x,y) for x,y in spec];G=[[K(z,w) for w in pts] for z in pts]
minors=[];passed=True;order_counts={}
for n in range(1,7):
 order_counts[str(n)]=0
 for idx in itertools.combinations(range(6),n):
  d=det([[G[i][j] for j in idx] for i in idx]);ok=d.imag.contains(0) and float(d.real.lower())>0
  passed &= ok;order_counts[str(n)]+=int(ok);minors.append({'indices':list(idx),'order':n,'determinant':str(d),'strictly_positive':ok})
out={'schema':'marici.voevodsky.xi-clark-nested-six-point-rung.v1','precision_bits':ctx.prec,
 'points':[[float(x),float(y)] for x,y in spec],'principal_minors':minors,'principal_minor_count':len(minors),
 'positive_count_by_order':order_counts,'all_63_principal_minors_strictly_positive':passed,
 'nested_rung_consequence':'Every leading packet on the first N points, N=1..6, is rigorously positive definite.',
 'scope':'One nested finite family only; no uniform all-rung, continuum, Schur, or RH claim.','passed':passed,'rh_proved':False}
p=ROOT/'research/voevodsky/results/xi_clark_nested_six_point_rung.json';p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='principal_minors'},indent=2));raise SystemExit(0 if passed else 1)
