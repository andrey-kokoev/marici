"""Mixed trace: opened join, opaque join, only partial occurrence replay."""
from hashlib import sha256
from fractions import Fraction as Q
from pathlib import Path
import json
ctx='square-synthetic-v1'
def commit(role,id_value,nonce):return sha256(repr((ctx,role,id_value,nonce)).encode()).hexdigest()
b=('B','b#01','nonce-b-01');c=('C','c#01','nonce-c-01')
cb=commit(*b);cc=commit(*c)
edges=({'source':'A','target_commit':cb,'target_role':'B'}, {'source_commit':cb,'source_role':'B','target_commit':cc,'target_role':'C'}, {'source_commit':cc,'source_role':'C','target':'D'})
assert edges[0]['target_commit']==edges[1]['source_commit'] and edges[1]['target_commit']==edges[2]['source_commit']
def join(i,opening):
 left,right=edges[i:i+2]
 if left['target_commit']!=right['source_commit'] or left['target_role']!=right['source_role']:raise ValueError('BROKEN_LINK')
 if opening is None:return 'COMMITMENT_LINK_ONLY'
 role,id_value,nonce=opening
 if role!=left['target_role'] or commit(role,id_value,nonce)!=left['target_commit']:raise ValueError('OPENING_MISMATCH')
 return 'LOCAL_OCCURRENCE_CHECKED'
assert join(0,b)=='LOCAL_OCCURRENCE_CHECKED' and join(1,None)=='COMMITMENT_LINK_ONLY'
assert (join(0,b),join(1,None))!=('LOCAL_OCCURRENCE_CHECKED',)*2
try:join(1,b)
except ValueError as err:assert str(err)=='OPENING_MISMATCH'
else:raise AssertionError('wrong opening accepted')
A=((Q(0),Q(1),Q(0),Q(1)),Q(1));B=((Q(1),Q(2),Q(0),Q(1)),Q(0));C=((Q(0),Q(1),Q(1),Q(2)),Q(0));D=A
def delta(x,y):return tuple(y[0][k]-x[0][k] for k in range(4))+(y[1]-x[1],)
parts=(delta(A,B),delta(B,C),delta(C,D))
assert tuple(sum(p[k] for p in parts) for k in range(5))==delta(A,D)==(Q(0),)*5
report={'passed':True,'first_join':'LOCAL_OCCURRENCE_CHECKED','second_join':'COMMITMENT_LINK_ONLY','full_occurrence_replay':'UNVERIFIABLE_TRACE','mathematical_packet_delta_telescope':True,'wrong_opening_refused':True,'scope':'Synthetic digest chain. Local opening is not proof of historical execution or source/effect issuer authority; mathematical telescope does not repair missing C occurrence.'}
out=Path(__file__).resolve().parents[1]/'results/mixed-opened-trace-chain.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
