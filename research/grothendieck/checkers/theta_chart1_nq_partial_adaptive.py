"""Adaptive exact box audit of both Nq partial derivatives."""
import json,time
from fractions import Fraction as F
from theta_fixedpoint_interval import FixedInterval
from theta_fixedpoint_jet import FixedJet,scaled_nq_jet
Q0,Q1,Y0,Y1=F(3,10),F(7,16),F(1,1000),F(1,28)
def evaluate(b):
 q0,q1,y0,y1,d=b
 try:r=scaled_nq_jet(FixedJet(FixedInterval.enclosing(q0,q1),dq=1),FixedJet(FixedInterval.enclosing(y0,y1),dy=1))
 except ValueError:return None
 return r.dq.lo,r.dy.lo
def split(b):
 q0,q1,y0,y1,d=b
 if (q1-q0)/(Q1-Q0)>=(y1-y0)/(Y1-Y0):
  m=(q0+q1)/2;return [(q0,m,y0,y1,d+1),(m,q1,y0,y1,d+1)]
 m=(y0+y1)/2;return [(q0,q1,y0,m,d+1),(q0,q1,m,y1,d+1)]
def run(limit=5000):
 stack=[(Q0,Q1,Y0,Y1,0)];accepted=[];n=0;start=time.perf_counter();maxd=0
 while stack and n<limit:
  b=stack.pop();maxd=max(maxd,b[4]);s=evaluate(b);n+=1
  if s is not None and s[0]>=0 and s[1]>=0:accepted.append((b,*s))
  else:stack.extend(split(b))
 elapsed=time.perf_counter()-start
 return {"status":"complete" if not stack else "budget_exhausted","evaluations":n,"accepted_cells":len(accepted),
 "pending_cells":len(stack),"max_depth_seen":maxd,"evaluations_per_second":n/elapsed,
 "minimum_partial_q_lower_scaled":str(min((x[1] for x in accepted),default=0)),
 "minimum_partial_y_lower_scaled":str(min((x[2] for x in accepted),default=0))}
if __name__=="__main__":print(json.dumps(run(),indent=2))
