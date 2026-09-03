import json,runpy
from fractions import Fraction as F
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name('rh_quarter_order_four_interpolated_hurwitz_minors.py')));D=g['D']
def ev(p,x):return sum(c*x**i for i,c in enumerate(p))
def divlin(p,c):
 q=[F(0)]*(len(p)-1);q[-1]=p[-1]
 for i in range(len(q)-2,-1,-1):q[i]=p[i+1]-c*q[i+1]
 return q
records=[]
for n in range(2,7):
 for s in range(3):
  p=D(n,s)[:];roots=[]
  while len(p)>1:
   c=next((F(q,4) for q in range(1,2001) if ev(p,-F(q,4))==0),None)
   if c is None:break
   roots.append(str(-c));p=divlin(p,c)
  records.append({'n':n,'shift':s,'degree':len(D(n,s))-1,'fully_split':len(p)==1,'unfactored_degree':len(p)-1,'roots':roots})
checks={'fifteen':len(records)==15,'route_decided':any(not x['fully_split'] for x in records)};r={'schema':'marici.strominger.rh_quarter_D_recurrence_factor_audit.v2','status':'passed' if all(checks.values()) else 'failed','verdict':'Quarter-lattice linear-factor route classified and rejected at first nontrivial D polynomial.','records':records,'first_unfactored':next(x for x in records if not x['fully_split']),'checks':checks};(base/'results'/'rh_quarter_D_recurrence_factor_audit.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({'status':r['status'],'first':r['first_unfactored']}))
