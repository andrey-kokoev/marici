"""An edge labelled same-target must refuse distinct valid target packets."""
from pathlib import Path
import json
rows=(((-1,0),0),((1,0),1),((0,-1),0),((0,1),1))
def check(p):
 m,c,n,b=p
 return all(v>=0 for v in (*m,c)) and tuple(sum(rows[i][0][j]*m[i] for i in range(4)) for j in (0,1))==n and sum(rows[i][1]*m[i] for i in range(4))+c==b
a=((0,1,0,0),1,(1,0),2)
b=((1,1,0,0),0,(0,0),1)
c=((0,1,0,0),0,(1,0),1)
assert all(check(p) for p in (a,b,c))
def edge(p,q):
 delta=tuple(x-y for x,y in zip(p[0],q[0]))
 if not check(p) or not check(q):return 'INVALID_ENDPOINT',delta
 if p[2:]!=q[2:]:return 'TARGET_SCOPE_MISMATCH',delta
 return 'SAME_TARGET_COMPARISON',delta
assert edge(a,b)==('TARGET_SCOPE_MISMATCH',(-1,0,0,0))
assert edge(a,c)==('TARGET_SCOPE_MISMATCH',(0,0,0,0))
assert edge(a,a)==('SAME_TARGET_COMPARISON',(0,0,0,0))
report={'passed':True,'nonzero_signed_delta':'valid x<=2 vs valid 0<=1: rejected target scope','zero_multiplier_delta':'valid x<=2 vs valid x<=1: rejected target bound scope','same_target':'local comparison accepted','scope':'Only same-target signed comparison label tested; no general cross-target transformation, owner authority or analytic map.'}
out=Path(__file__).resolve().parents[1]/'results/comparison-target-scope.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
