"""Breadth-first complexity audit for the symbolic Chart-1 cover."""
import json,time
from fractions import Fraction as F
from theta_fixedpoint_chart1_adaptive import evaluate, children, Q0,Q1,Y0,Y1

def area_ratio(b):
 q0,q1,y0,y1,_=b
 return (q1-q0)*(y1-y0)/((Q1-Q0)*(Y1-Y0))

def run(max_depth=12):
 pending=[(Q0,Q1,Y0,Y1,0)];rows=[];accepted_total=0;evaluations=0;start=time.perf_counter()
 for depth in range(max_depth+1):
  failed=[];accepted=0
  for b in pending:
   result=evaluate(b);evaluations+=1
   if result is not None and result[0]>0 and result[1]<0:accepted+=1
   else:failed.append(b)
  accepted_total+=accepted
  unresolved=sum((area_ratio(b) for b in failed),F(0))
  rows.append({"depth":depth,"tested":len(pending),"accepted":accepted,"failed":len(failed),"unresolved_area":str(unresolved)})
  if not failed:break
  pending=[child for b in failed for child in children(b)]
 elapsed=time.perf_counter()-start
 return {"status":"complete" if not pending else "depth_exhausted","evaluations":evaluations,
 "accepted_cells":accepted_total,"next_pending_cells":0 if not pending else len(pending),
 "elapsed_seconds":elapsed,"evaluations_per_second":evaluations/elapsed,"levels":rows}

if __name__=="__main__":print(json.dumps(run(),indent=2))
