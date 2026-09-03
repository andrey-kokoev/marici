"""Exact point-enclosure falsification scan for partial derivatives of Nq."""
import json
from fractions import Fraction as F
from theta_fixedpoint_jet import FixedJet,scaled_nq_jet
Q0,Q1,Y0,Y1=F(3,10),F(7,16),F(1,1000),F(1,28);N=20
worst_q=worst_y=None
for i in range(N+1):
 q=Q0+(Q1-Q0)*F(i,N)
 for j in range(N+1):
  y=Y0+(Y1-Y0)*F(j,N)
  r=scaled_nq_jet(FixedJet(q,dq=1),FixedJet(y,dy=1))
  rq=(r.dq.lo,r.dq.hi,q,y);ry=(r.dy.lo,r.dy.hi,q,y)
  if worst_q is None or rq[0]<worst_q[0]:worst_q=rq
  if worst_y is None or ry[0]<worst_y[0]:worst_y=ry
result={"points":(N+1)**2,"minimum_partial_q_lower_scaled":str(worst_q[0]),
"partial_q_upper_scaled":str(worst_q[1]),"partial_q_point":[str(worst_q[2]),str(worst_q[3])],
"minimum_partial_y_lower_scaled":str(worst_y[0]),"partial_y_upper_scaled":str(worst_y[1]),
"partial_y_point":[str(worst_y[2]),str(worst_y[3])],
"point_derivative_scan_survives":worst_q[0]>=0 and worst_y[0]>=0}
print(json.dumps(result,indent=2))
assert result["point_derivative_scan_survives"] or worst_q[1]<0 or worst_y[1]<0
