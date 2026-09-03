import json,runpy
from fractions import Fraction as F
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name('rh_quarter_order_four_interpolated_hurwitz_minors.py')));D=g['D']
def audit(p):
 a=list(reversed(p));n=len(a)-1;m=(n+2)//2;R=[[F(0)]*m for _ in range(n+1)];R[0][:len(a[0::2])]=a[0::2];R[1][:len(a[1::2])]=a[1::2]
 for i in range(2,n+1):
  if not R[i-1][0]:return False
  for j in range(m-1):R[i][j]=(R[i-1][0]*R[i-2][j+1]-R[i-2][0]*R[i-1][j+1])/R[i-1][0]
 return all(x[0]>0 for x in R)
records=[{'n':n,'shift':s,'degree':len(D(n,s))-1,'stable':audit(D(n,s))} for n in range(2,9) for s in range(3)];checks={'twenty_one':len(records)==21,'all_stable':all(x['stable'] for x in records),'control':not audit([F(-1),F(0),F(1)])};r={'schema':'marici.strominger.rh_quarter_D_routh_interlacing_ladder.v2','status':'passed' if all(checks.values()) else 'failed','verdict':'Finite exact Hermite-Biehler/Routh backend regenerated without uniform promotion.','records':records,'checks':checks};(base/'results'/'rh_quarter_D_routh_interlacing_ladder.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({'status':r['status'],'max_degree':max(x['degree'] for x in records)}))
