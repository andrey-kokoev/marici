"""Centered Hessian transport with adaptive subdivision of the former weak cell."""
import json
from fractions import Fraction as F
from theta_fixedpoint_interval import FixedInterval, fixed
from theta_fixedpoint_jet import FixedJet, cancellation_free_residual_jet, magnitude

ROOT=(F(819,2048),F(8201,20480),F(59869,1792000),F(3757,112000),0)

def certify(b):
 q0,q1,y0,y1,d=b; qc,yc=(q0+q1)/2,(y0+y1)/2
 center=cancellation_free_residual_jet(FixedJet(qc,dq=1),FixedJet(yc,dy=1))
 box=cancellation_free_residual_jet(FixedJet(FixedInterval.enclosing(q0,q1),dq=1),FixedJet(FixedInterval.enclosing(y0,y1),dy=1))
 rq,ry=fixed((q1-q0)/2),fixed((y1-y0)/2)
 qcost=fixed(magnitude(box.dqq))*rq+fixed(magnitude(box.dqy))*ry
 ycost=fixed(magnitude(box.dqy))*rq+fixed(magnitude(box.dyy))*ry
 return center.dq.lo-qcost.hi,center.dy.hi+ycost.hi

def split(b):
 q0,q1,y0,y1,d=b
 if q1-q0>=y1-y0:
  m=(q0+q1)/2;return [(q0,m,y0,y1,d+1),(m,q1,y0,y1,d+1)]
 m=(y0+y1)/2;return [(q0,q1,y0,m,d+1),(q0,q1,m,y1,d+1)]

def run(limit=100):
 stack=[ROOT];accepted=[];evaluations=0;max_seen=0
 while stack and evaluations<limit:
  b=stack.pop();max_seen=max(max_seen,b[4]);lo,hi=certify(b);evaluations+=1
  if lo>0 and hi<0:accepted.append((b,lo,hi))
  else:stack.extend(split(b))
 return {"status":"complete" if not stack else "budget_exhausted","evaluations":evaluations,
 "accepted_cells":len(accepted),"pending_cells":len(stack),
 "max_depth_seen":max_seen,
 "worst_dq_lower_scaled":str(min((x[1] for x in accepted),default=0)),
 "worst_dy_upper_scaled":str(max((x[2] for x in accepted),default=0))}

if __name__=="__main__":
 result=run();print(json.dumps(result,indent=2))
 # Deliberate witness: propagated Hessians remain unusable under subdivision.
 assert result["status"]=="budget_exhausted" and result["accepted_cells"]==0
