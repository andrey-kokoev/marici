"""Exact point-enclosure falsification scan for compensated Nq dominance."""
import json
from fractions import Fraction as F
from theta_fixedpoint_interval import FixedDual,scaled_derivative_numerators
Q0,Q1,Y0,Y1=F(3,10),F(7,16),F(1,1000),F(1,28);N=40
worst=None
for i in range(N+1):
 q=Q0+(Q1-Q0)*F(i,N)
 for j in range(N+1):
  y=Y0+(Y1-Y0)*F(j,N)
  nq,ny=scaled_derivative_numerators(FixedDual(q,dq=1),FixedDual(y,dy=1))
  row=(nq.lo,nq.hi,ny.lo,ny.hi,q,y)
  if worst is None or row[0]<worst[0]:worst=row
result={"points":(N+1)**2,"minimum_nq_lower_scaled":str(worst[0]),
"corresponding_nq_upper_scaled":str(worst[1]),"ny_lower_scaled":str(worst[2]),
"ny_upper_scaled":str(worst[3]),"q":str(worst[4]),"y":str(worst[5]),
"point_scan_survives":worst[0]>0 and worst[3]<0}
print(json.dumps(result,indent=2));assert result["point_scan_survives"]
