"""Exact outward boundary-aware pilot cover in the (q,z=qy) chart."""
from fractions import Fraction as F
from pathlib import Path
import json
from theta_dominant_fraction_interval_core import (Dual,Interval,PI,cosh_sqrt_dual,
 negative_log1m_dual,one_minus_exp_negative_dual,exp_negative_dual)
def evaluate(qa,qb,za,zb):
 q=Dual(Interval(qa,qb),dq=1);z=Dual(Interval(za,zb),dy=1);y=z/q
 def m_qz(q,z):
  A=Dual(2*PI)/q;h=cosh_sqrt_dual(z)-1
  return A*h+negative_log1m_dual(6*A*h/((A-3)*(A-3)))
 m=m_qz(q,z);m4=m_qz(q,4*z);eta=m4-4*m
 if eta.value.hi<0:raise AssertionError("eta convexity contradicted")
 eta=Dual(Interval(max(F(0),eta.value.lo),eta.value.hi),eta.dq,eta.dy)
 u=one_minus_exp_negative_dual(2*m)
 R=u*u-exp_negative_dual(4*m)*one_minus_exp_negative_dual(eta)
 # D=q^2*R/z^2. Positive prefactors reduce the requested signs exactly to
 # H=z*R_z-2R<0 and J=q*R_q+z*R_z>0, avoiding quotient differentiation.
 H=z.value*R.dy-2*R.value
 J=q.value*R.dq+z.value*R.dy
 return H,J
q0,q1=F(7,16),F(1,2);Q=8;Z=8;accepted=[];unresolved=[]
for i in range(Q):
 qa=q0+(q1-q0)*i/Q;qb=q0+(q1-q0)*(i+1)/Q
 # This rectangle starts at qa/1000, hence is an explicit superset of the
 # slanted domain on the q cell and overlaps only outside the target domain.
 zl=qa/1000;zu=F(1,64)
 for j in range(Z):
  za=zl+(zu-zl)*j/Z;zb=zl+(zu-zl)*(j+1)/Z
  a,b=evaluate(qa,qb,za,zb);rec={"q":[str(qa),str(qb)],"z":[str(za),str(zb)],
   "H_hi":float(a.hi),"J_lo":float(b.lo)}
  (accepted if a.hi<0 and b.lo>0 else unresolved).append(rec)
point_failures=[];point_min_combo=None;point_max_qDz=None
for i in range(3):
 q=q0+(q1-q0)*i/2
 for j in range(3):
  z=q/1000+(F(1,64)-q/1000)*j/2;a,b=evaluate(q,q,z,z)
  point_max_qDz=a.hi if point_max_qDz is None else max(point_max_qDz,a.hi)
  point_min_combo=b.lo if point_min_combo is None else min(point_min_combo,b.lo)
  if not (a.hi<0 and b.lo>0):point_failures.append({"q":str(q),"z":str(z)})
result={"scope":"8x8 exact rectangular-superset pilot cover plus 3x3 exact point scan","q_cells":Q,"z_cells_per_q":Z,
 "evaluated":Q*Z,"accepted":len(accepted),"unresolved":len(unresolved),
 "point_scan_count":9,"point_failures":point_failures,"point_max_H":float(point_max_qDz),
 "point_min_J":float(point_min_combo),"accepted_boxes":accepted,"unresolved_boxes":unresolved}
out=json.dumps(result,indent=2)+"\n"
Path("research/grothendieck/results/theta-dominant-chart2-signs.json").write_text(out)
print(json.dumps({k:result[k] for k in ("scope","evaluated","accepted","unresolved","point_scan_count","point_failures","point_max_H","point_min_J")},indent=2))
