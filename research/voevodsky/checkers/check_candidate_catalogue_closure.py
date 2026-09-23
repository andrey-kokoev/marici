"""A source candidate requires packet validity and edge referential closure atomically."""
from pathlib import Path
import json
rows=(((-1,0),0),((1,0),2),((0,-1),0),((0,1),2))
source='synthetic-row-manifest-v2';generation=2
def packet(id,weights,surplus,bound):return {'id':id,'source':source,'generation':generation,'weights':weights,'surplus':surplus,'target':((1,0),bound)}
p=packet('P-new',(0,1,0,0),0,2);q=packet('Q-new',(0,1,0,0),1,3)
edge={'id':'weakening-new','from':'P-new','to':'Q-new','rule':'bound-weakening','source':source,'generation':generation}
def valid(p):
 w=p['weights'];c=p['surplus']
 return p['source']==source and p['generation']==generation and min((*w,c))>=0 and tuple(sum(w[i]*rows[i][0][j] for i in range(4)) for j in (0,1))==p['target'][0] and sum(w[i]*rows[i][1] for i in range(4))+c==p['target'][1]
def closure(packets,edges):
 if not all(valid(p) for p in packets.values()):return 'PACKET_INVALID'
 for e in edges:
  if e['from'] not in packets or e['to'] not in packets:return 'MISSING_ENDPOINT'
  a,b=packets[e['from']],packets[e['to']]
  if e['source']!=source or e['generation']!=generation:return 'STALE_EDGE_SOURCE'
  if e['rule']!='bound-weakening' or a['target'][0]!=b['target'][0] or a['target'][1]>b['target'][1] or a['weights']!=b['weights'] or b['surplus']-a['surplus']!=b['target'][1]-a['target'][1]:return 'EDGE_RULE_INVALID'
 return 'LOCAL_CLOSED_CANDIDATE_NOT_AUTHORIZED'
assert closure({p['id']:p,q['id']:q},[edge])=='LOCAL_CLOSED_CANDIDATE_NOT_AUTHORIZED'
assert closure({p['id']:p},[edge])=='MISSING_ENDPOINT'
assert closure({p['id']:p,q['id']:dict(q,surplus=0)},[edge])=='PACKET_INVALID'
assert closure({p['id']:p,q['id']:q},[dict(edge,generation=1)])=='STALE_EDGE_SOURCE'
report={'passed':True,'complete':'closed local packet+edge candidate, not authorized source migration','missing_endpoint':'rejected','invalid_packet':'rejected','stale_edge_generation':'rejected','scope':'In-memory synthetic catalogue, not persistent row change, grant or analytic mapping.'}
out=Path(__file__).resolve().parents[1]/'results/candidate-catalogue-closure.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
