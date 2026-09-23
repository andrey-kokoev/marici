"""Two redundant-row eliminations commute; weaker bound needs surplus."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
base=(((-1,0),0),((1,0),1),((0,-1),0),((0,1),1))
def rows(bound):return base+(((1,1),2),((2,1),bound))
def image(rs,m,c=Q(0)):
 return tuple(sum(Q(rs[i][0][j])*m[i] for i in range(len(m))) for j in (0,1)),sum(Q(rs[i][1])*m[i] for i in range(len(m)))+c
def staged(v,c,weak):
 a,x,b,y,z,w=map(Q,v)
 # 2x+y<=3 from (x+y<=2)+(x<=1); <=4 costs extra unit.
 x+=w;z+=w;c+=w if weak else 0
 x+=z;y+=z
 return (a,x,b,y),c
def direct(v,c,weak):
 a,x,b,y,z,w=map(Q,v)
 return (a,x+z+2*w,b,y+z+w),c+(w if weak else 0)
checks=0
for weak,z,w in product((False,True),(Q(0),Q(1,2),Q(1)),(Q(0),Q(1,2),Q(1))):
 r=rows(4 if weak else 3);v=(Q(0),Q(0),Q(0),Q(0),z,w);c=Q(0)
 st=staged(v,c,weak);di=direct(v,c,weak)
 assert st==di and image(r,v,c)==image(base,*st)
 assert min((*st[0],st[1]))>=0
 checks+=1
assert checks==18
v=(Q(0),)*5+(Q(1),)
assert image(rows(4),v)==((2,1),Q(4))
assert image(base,(0,2,0,1),Q(0))==((2,1),Q(3))
assert image(base,(0,2,0,1),Q(1))==((2,1),Q(4))
report={'passed':True,'staged_direct_elimination_checks':checks,'exact_second_row':'2x+y<=3; two routes same old multipliers without surplus','weaker_second_row':'2x+y<=4; both routes add old second-row multiplier to surplus','naive_grade_preservation_refused':True,'scope':'Nonnegative exact finite square row presentations and Farkas packets. Equality of output packets is not proof-history 2/3-cell equality or source-owner migration.'}
out=Path(__file__).resolve().parents[1]/'results/two-redundant-square-rows.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
