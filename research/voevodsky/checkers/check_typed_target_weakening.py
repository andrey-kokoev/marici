"""A target-bound weakening is a typed new certificate, not a relabelled event."""
from fractions import Fraction as Q
from pathlib import Path
import json
rows=(((-1,0),Q(0)),((1,0),Q(1)),((0,-1),Q(0)),((0,1),Q(1)))
parent={'id':'synthetic-proof-x1','normal':(1,0),'bound':Q(1),'weights':(Q(0),Q(1),Q(0),Q(0)),'surplus':Q(0)}
def valid(p):
 m=p['weights'];c=p['surplus']
 return min((*m,c))>=0 and tuple(sum(rows[i][0][j]*m[i] for i in range(4)) for j in (0,1))==p['normal'] and sum(rows[i][1]*m[i] for i in range(4))+c==p['bound']
def weaken(child):
 if not valid(parent):return 'INVALID_PARENT'
 if child['id']==parent['id']:return 'OCCURRENCE_RELABELLING'
 if child['normal']!=parent['normal']:return 'NORMAL_MISMATCH'
 if child['bound']<parent['bound']:return 'NOT_WEAKENING'
 if child['weights']!=parent['weights'] or child['surplus']!=parent['surplus']+child['bound']-parent['bound']:return 'TRANSFORM_INCONSISTENT'
 return 'LOCAL_TYPED_WEAKENING' if valid(child) else 'INVALID_CHILD'
child=dict(parent,id='synthetic-proof-x2',bound=Q(2),surplus=Q(1))
assert valid(parent) and weaken(child)=='LOCAL_TYPED_WEAKENING'
assert weaken(dict(child,id=parent['id']))=='OCCURRENCE_RELABELLING'
assert weaken(dict(child,normal=(0,1)))=='NORMAL_MISMATCH'
assert weaken(dict(child,bound=Q(0)))=='NOT_WEAKENING'
assert weaken(dict(child,surplus=Q(0)))=='TRANSFORM_INCONSISTENT'
report={'passed':True,'parent':'x<=1, surplus0','child':'x<=2, same weights surplus1, new fictional occurrence','edge':'typed bound-weakening, not same-target comparison','rejected':'same occurrence ID; changed normal; strengthening; stale surplus','scope':'Local rational implication only, neither observed source event nor publication authority nor analytic map.'}
out=Path(__file__).resolve().parents[1]/'results/typed-target-weakening.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
