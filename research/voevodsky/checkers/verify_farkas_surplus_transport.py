"""Independent exact replay of reported Farkas residuals and proof-choice hostile."""
from fractions import Fraction as Q
from pathlib import Path
import json
V=Path(__file__).resolve().parents[1]/'results'
p=json.loads((V/'farkas-surplus-transport.json').read_text());choice=json.loads((V/'farkas-proof-choice.json').read_text())
assert p['passed'] and choice['passed']
# Recompute without importing either producer; source r=(0,1), A=(-1,1).
d=Q(1,4);e=-Q(1,8)
B=(-Q(1),Q(1),Q(0));Mr=(Q(0),Q(1),Q(1));c=(Q(0),Q(1,2),Q(1,3))
u=tuple(x-n*d+s for x,n,s in zip(Mr,B,c))
assert tuple(map(Q,p['intermediate_residuals']))==u
C=(-Q(1),Q(1));Nu=(u[0],u[1]+u[2]);k=(Q(1,5),Q(2,5))
v=tuple(x-n*e+s for x,n,s in zip(Nu,C,k))
assert tuple(map(Q,p['final_residuals']))==v
margin=(c[0]+k[0],c[1]+c[2]+k[1]);assert tuple(map(Q,p['composite_surplus']))==margin
assert Q(p['combined_reference_shift'])==d+e
# Independently recheck both target x<=2 certificates at the shifted base.
for row in choice['certificates']:
 a,b=map(Q,row['multiplier']);surplus=Q(row['surplus'])
 assert a>=0 and b>=0 and surplus>=0
 assert -a+b==1 and b-d+surplus==Q(7,4)
assert {x['surplus'] for x in choice['certificates']}=={'0','1'}
report={'passed':True,'verified_composite_surplus':list(map(str,margin)),'two_proof_surpluses':['0','1'],'conclusion':'covariant under chosen proof composition; not invariant under changing proof','scope':'Independent arithmetic on frozen rational example; no generic owner authority or analytic functor.'}
(V/'farkas-surplus-transport-verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
