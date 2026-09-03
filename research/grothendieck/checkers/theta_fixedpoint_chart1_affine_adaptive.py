"""Adaptive exact outward Chart-1 cover using correlated affine-dual cells."""
import argparse, json, time
from fractions import Fraction as F
from theta_fixedpoint_affine import Affine
from theta_fixedpoint_affine_dual import AffineDual, cancellation_free_residual_affine_dual

Q0,Q1=F(3,10),F(7,16)
Y0,Y1=F(1,1000),F(1,28)

def evaluate(box):
 q0,q1,y0,y1,d=box
 q=AffineDual(Affine((q0+q1)/2,aq=(q1-q0)/2),dq=1)
 y=AffineDual(Affine((y0+y1)/2,ay=(y1-y0)/2),dy=1)
 try: r=cancellation_free_residual_affine_dual(q,y)
 except (ValueError,ZeroDivisionError): return None
 return r.dq.range().lo,r.dy.range().hi

def children(b):
 q0,q1,y0,y1,d=b
 if (q1-q0)/(Q1-Q0)>=(y1-y0)/(Y1-Y0):
  m=(q0+q1)/2; return [(q0,m,y0,y1,d+1),(m,q1,y0,y1,d+1)]
 m=(y0+y1)/2; return [(q0,q1,y0,m,d+1),(q0,q1,m,y1,d+1)]

def run(limit):
 stack=[(Q0,Q1,Y0,Y1,0)]; accepted=[]; n=0; start=time.perf_counter()
 while stack and n<limit:
  b=stack.pop(); signs=evaluate(b); n+=1
  if signs is not None and signs[0]>0 and signs[1]<0: accepted.append((b,*signs))
  else: stack.extend(children(b))
 elapsed=time.perf_counter()-start
 return {"status":"complete" if not stack else "budget_exhausted","evaluations":n,
 "accepted_cells":len(accepted),"pending_cells":len(stack),"max_depth":max((x[0][4] for x in accepted),default=0),
 "elapsed_seconds":elapsed,"evaluations_per_second":n/elapsed,
 "worst_dq_lower_scaled":str(min((x[1] for x in accepted),default=0)),
 "worst_dy_upper_scaled":str(max((x[2] for x in accepted),default=0))}

if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("--limit",type=int,default=5000);a=p.parse_args()
 print(json.dumps(run(a.limit),indent=2))
