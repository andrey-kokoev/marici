"""Bounded diagnostic for the first failed undilated moment row: baseline n=0."""
from fractions import Fraction as F
from math import comb,factorial
from decimal import Decimal
import json
import preconditioned_spline_weil as w
A=w.scale(F(2),w.log_q(F(2)));CS=[F(1),F(-5),F(33,4),F(-5),F(1)];MS=[2,1,0,-1,-2]
def exp_iv(x):
 lo=w.exp_q(x[0]);hi=w.exp_q(x[1]);return (lo[0],hi[1])
def J(b,s):
 y=w.max0(s);e=exp_iv(w.scale(b,w.sub(s,y)));poly=w.Z;by=w.scale(b,y)
 for r in range(8):poly=w.add(poly,w.scale(F(1,factorial(r)),w.pow_pos(by,r)))
 return w.scale(F(1,b**8),w.mul(e,poly))
b=F(1,4);out=w.Z
for c,m in zip(CS,MS):
 for j in range(9):
  s=w.add(w.scale(F(m),A),(F(4-j),F(4-j)))
  out=w.add(out,w.scale(c*F((-1)**j*comb(8,j)),J(b,s)))
center=F(Decimal('0.46230108744927819962243646708542235'))
residual=(center-out[1] if center>out[1] else out[0]-center if center<out[0] else F(0))
print(json.dumps({'schema':'marici.nima.undilated-baseline-n0-diagnostic.v1','interval':[float(out[0]),float(out[1])],'center':float(center),'enclosed':out[0]<=center<=out[1],'distance_outside':float(residual),'width':float(out[1]-out[0])},sort_keys=True))
