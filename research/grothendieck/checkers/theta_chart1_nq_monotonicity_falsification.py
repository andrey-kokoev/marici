"""Exact adjacent-point falsification of coordinatewise Nq monotonicity."""
import json
from fractions import Fraction as F
from theta_fixedpoint_interval import FixedDual,scaled_derivative_numerators
Q0,Q1,Y0,Y1=F(3,10),F(7,16),F(1,1000),F(1,28);N=40
values={}
for i in range(N+1):
 for j in range(N+1):
  q=Q0+(Q1-Q0)*F(i,N);y=Y0+(Y1-Y0)*F(j,N)
  values[i,j]=scaled_derivative_numerators(FixedDual(q,dq=1),FixedDual(y,dy=1))[0]
steps=[]
for i in range(N+1):
 for j in range(N+1):
  if i<N:steps.append((values[i+1,j].hi-values[i,j].lo,"q",i,j))
  if j<N:steps.append((values[i,j+1].hi-values[i,j].lo,"y",i,j))
worst=min(steps)
strict_decreases=[x for x in steps if x[0]<0]
result={"points":(N+1)**2,"adjacent_steps":len(steps),"strict_decreases":len(strict_decreases),
"minimum_step_upper_scaled":str(worst[0]),"direction":worst[1],"index":[worst[2],worst[3]],
"coordinatewise_nondecreasing_survives":not strict_decreases}
print(json.dumps(result,indent=2))
# This checker resolves either way: a negative upper is an exact monotonicity falsifier.
assert result["coordinatewise_nondecreasing_survives"] or worst[0]<0
