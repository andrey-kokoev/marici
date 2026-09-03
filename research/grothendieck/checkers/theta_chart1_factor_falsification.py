"""Strongest coarse exact falsification of the termwise-positive Nq conjecture."""
import json
from fractions import Fraction as F
from theta_fixedpoint_interval import (FixedDual,FixedInterval,dominant_log_magnitude,
 exp_negative,scaled_derivative_numerators)
Q0,Q1,Y0,Y1=F(3,10),F(7,16),F(1,1000),F(1,28)
rows=[]
for i in range(4):
 for j in range(4):
  q0=Q0+(Q1-Q0)*F(i,4);q1=Q0+(Q1-Q0)*F(i+1,4)
  y0=Y0+(Y1-Y0)*F(j,4);y1=Y0+(Y1-Y0)*F(j+1,4)
  q=FixedDual(FixedInterval.enclosing(q0,q1),dq=1);y=FixedDual(FixedInterval.enclosing(y0,y1),dy=1)
  try:
   m=dominant_log_magnitude(q,y);m4=dominant_log_magnitude(q,4*y);eta=m4-4*m
   ev=FixedInterval(max(0,eta.value.lo),eta.value.hi)
   e2,ee=exp_negative(2*m.value),exp_negative(ev);u,c=1-e2,1-ee
   positive=4*u*e2*m.dq;bracket=4*m.dq*c-ee*eta.dq
   nq,ny=scaled_derivative_numerators(q,y)
   rows.append((bracket.lo,positive.lo,nq.lo,ny.hi,i,j))
  except ValueError:
   continue
worst=min(rows)
i,j=worst[4],worst[5]
qc=(Q0+(Q1-Q0)*F(2*i+1,8));yc=(Y0+(Y1-Y0)*F(2*j+1,8))
qp,yp=FixedDual(qc,dq=1),FixedDual(yc,dy=1)
mp=dominant_log_magnitude(qp,yp);m4p=dominant_log_magnitude(qp,4*yp);etap=m4p-4*mp
eep=exp_negative(FixedInterval(max(0,etap.value.lo),etap.value.hi))
cp=1-eep
point_bracket=4*mp.dq*cp-eep*etap.dq
result={"tested_boxes":len(rows),"grid_boxes":16,"minimum_bracket_lower_scaled":str(worst[0]),
"corresponding_positive_lower_scaled":str(worst[1]),"corresponding_nq_lower_scaled":str(worst[2]),
"corresponding_ny_upper_scaled":str(worst[3]),"cell":[worst[4],worst[5]],
"point_q":str(qc),"point_y":str(yc),"point_bracket_upper_scaled":str(point_bracket.hi),
"termwise_positive_conjecture_survives":point_bracket.hi>=0}
print(json.dumps(result,indent=2))
assert len(rows)>0
# A strictly negative point upper enclosure rejects termwise positivity itself.
assert point_bracket.hi<0
