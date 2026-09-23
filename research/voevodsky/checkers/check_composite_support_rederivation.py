"""Nonnegative composition unions supports; normalization can introduce roots."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
names=('x-low','x-high','y-low','y-high')
base=(((-1,0),0),((1,0),1),((0,-1),0),((0,1),1))
def support(m):return frozenset(names[i] for i,z in enumerate(m) if z>0)
def cert(m,c,v,T,rows=base):
 return min((*m,c))>=0 and tuple(sum(rows[i][0][j]*m[i] for i in range(4)) for j in (0,1))==v and sum(rows[i][1]*m[i] for i in range(4))+c==T
x=(Q(0),Q(1),Q(0),Q(0));y=(Q(0),Q(0),Q(0),Q(1))
assert cert(x,0,(1,0),1) and cert(y,0,(0,1),1)
checks=0
for k,l in product((Q(0),Q(1,2),Q(1),Q(2)),repeat=2):
 m=tuple(k*x[i]+l*y[i] for i in range(4))
 expected=(support(x) if k>0 else frozenset())|(support(y) if l>0 else frozenset())
 assert support(m)==expected and cert(m,0,(k,l),k+l)
 checks+=1
assert checks==16
# Surplus x<=2 can be consumed by y-cycle, creating new primitive-row
# support even though the unchanged x proof did not depend on those rows.
p=x;c=Q(1);dy=(Q(0),Q(0),Q(1),Q(1));q=tuple(p[i]+dy[i] for i in range(4))
assert cert(p,c,(1,0),2) and cert(q,0,(1,0),2)
assert support(p)=={'x-high'} and support(q)=={'x-high','y-low','y-high'}
changed=list(base);changed[3]=(changed[3][0],Q(2))
assert cert(p,c,(1,0),2,changed) and not cert(q,0,(1,0),2,changed)
# The source-generation tag is still old for both records; only arithmetic
# of p survives the changed-row scenario.
report={'passed':True,'nonnegative_composition_support_cases':checks,'composition_support_law':'support(kp+lq)=support(p) for k>0 union support(q) for l>0','normalizer_introduced_roots':['y-low','y-high'],'y_high_edit_old_slack_proof_valid':True,'y_high_edit_normalized_proof_invalid':True,'boundary':'Every OUTPUT proof must derive support from its own multiplier vector; inherited input support and generation authority are insufficient.'}
out=Path(__file__).resolve().parents[1]/'results/composite-support-rederivation.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
