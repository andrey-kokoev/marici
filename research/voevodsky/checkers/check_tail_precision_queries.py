"""Exact set-valued threshold answers for two free tail coordinates.

Measurement uncertainty is a coordinate box, not an L1 ball. Pins are exact.
"""
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
def vertices(rows):
 out=set()
 for (a,b,c),(d,e,f) in combinations(rows,2):
  det=a*e-b*d
  if not det:continue
  x,y=(c*e-b*f)/det,(a*f-c*d)/det
  if all(a*x+b*y<=c for a,b,c in rows):out.add((x,y))
 return sorted(out)
def feasible(m,u,v,eu,ev):
 r=Q(1,128**(m-2));s=Q(1,128**(m-1));cp=Q(100+2*(m-2));cq=Q(100+2*(m-1))
 rows=[(Q(-1),Q(0),Q(0)),(Q(1),Q(0),cp),(Q(0),Q(-1),Q(0)),(Q(0),Q(1),cq),
       (Q(1),Q(1),u+eu),(Q(-1),Q(-1),-u+eu),(r,s,v+ev),(-r,-s,-v+ev)]
 return vertices(rows)
def answer(vs,h):
 if not vs:return 'INCONSISTENT'
 lo=min(x for x,y in vs);hi=max(x for x,y in vs)
 if hi<=h:return 'FORCED_TRUE'
 if lo>h:return 'FORCED_FALSE'
 return 'UNRESOLVED'
records=[]
for m in (3,4,8,16,64):
 r,s=Q(1,128**(m-2)),Q(1,128**(m-1));gap=r-s
 xp=Q(100+2*(m-2),2);xq=Q(100+2*(m-1),2)
 u=xp+xq;v=r*xp+s*xq;h=xp+1
 controls=[]
 for label,eu,ev,expected in [('exact',Q(0),Q(0),'FORCED_TRUE'),
   ('below_margin',Q(0),gap/2,'FORCED_TRUE'),('at_margin',Q(0),gap,'FORCED_TRUE'),
   ('above_margin',Q(0),2*gap,'UNRESOLVED'),('both_errors',Q(1),gap/2,'FORCED_TRUE')]:
  vs=feasible(m,u,v,eu,ev);radius=(ev+s*eu)/gap
  assert min(x for x,y in vs)==xp-radius and max(x for x,y in vs)==xp+radius
  assert answer(vs,h)==expected
  controls.append({'case':label,'epsilon_U':str(eu),'epsilon_V':str(ev),'x_interval':[str(xp-radius),str(xp+radius)],'answer':expected})
 # Explicit same-observation-box indistinguishability; both points are admitted.
 low=(xp-2,xq+2);high=(xp+2,xq-2)
 assert low[0]<=h<high[0]
 assert all(abs(r*a+s*b-v)<=2*gap and a+b==u for a,b in (low,high))
 assert answer(feasible(m,u,v,Q(0),gap/2),xp-1)=='FORCED_FALSE'
 assert answer(feasible(m,Q(-2),Q(0),Q(1),Q(1)),h)=='INCONSISTENT'
 records.append({'m':m,'slope_gap':str(gap),'threshold':str(h),'controls':controls,
                 'opposite_truth_witnesses':[list(map(str,low)),list(map(str,high))]})
report={'passed':True,'measurement_contract':'Residual moment box |U-Uhat|<=epsilon_U, |V-Vhat|<=epsilon_V; all pins fixed exactly.',
 'records':records,'sharp_interior_radius':'(epsilon_V+r_q*epsilon_U)/(r_p-r_q)',
 'scope':'Thresholds of the first of two free coordinates; caps enforced by exact bounded-polytope enumeration. No claim about actual-source authentication or a general noisy-audit optimizer.'}
(OUT/'tail-precision-queries.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'m_values':[r['m'] for r in records],'controls_per_m':8,'sharp_radius':report['sharp_interior_radius']},indent=2))
