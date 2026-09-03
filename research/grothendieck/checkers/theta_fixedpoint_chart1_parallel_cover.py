"""Parallel breadth-first symbolic Chart-1 cover audit."""
import argparse,json,time
from concurrent.futures import ProcessPoolExecutor
from fractions import Fraction as F
from theta_fixedpoint_chart1_adaptive import evaluate,children,Q0,Q1,Y0,Y1

def area(b):
 q0,q1,y0,y1,_=b;return (q1-q0)*(y1-y0)/((Q1-Q0)*(Y1-Y0))

def run(depth,workers):
 pending=[(Q0,Q1,Y0,Y1,0)];rows=[];evaluations=accepted_total=0;start=time.perf_counter()
 with ProcessPoolExecutor(max_workers=workers) as pool:
  for level in range(depth+1):
   signs=list(pool.map(evaluate,pending,chunksize=max(1,len(pending)//(workers*8))))
   failed=[];accepted=0
   for b,s in zip(pending,signs):
    if s is not None and s[0]>0 and s[1]<0:accepted+=1
    else:failed.append(b)
   evaluations+=len(pending);accepted_total+=accepted
   rows.append({"depth":level,"tested":len(pending),"accepted":accepted,"failed":len(failed),
                "unresolved_area":str(sum((area(b) for b in failed),F(0)))})
   if not failed:pending=[];break
   pending=[c for b in failed for c in children(b)]
 elapsed=time.perf_counter()-start
 return {"status":"complete" if not pending else "depth_exhausted","workers":workers,"evaluations":evaluations,
 "accepted_cells":accepted_total,"next_pending_cells":len(pending),"elapsed_seconds":elapsed,
 "evaluations_per_second":evaluations/elapsed,"levels":rows}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("--depth",type=int,default=16);p.add_argument("--workers",type=int,default=8);a=p.parse_args()
 print(json.dumps(run(a.depth,a.workers),indent=2))
