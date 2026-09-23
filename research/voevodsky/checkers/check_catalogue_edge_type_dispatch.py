"""A catalogue must dispatch same-target comparison and bound-weakening separately."""
from pathlib import Path
import json
rows=(((-1,0),0),((1,0),2),((0,-1),0),((0,1),2))
def packet(id,w,c,b):return {'id':id,'weights':w,'surplus':c,'target':((1,0),b)}
p=packet('P',(0,1,0,0),0,2);q=packet('Q',(0,1,0,0),1,3);r=packet('R',(1,2,0,0),0,4);s=packet('S',(0,1,0,0),2,4)
def valid(p):
 w=p['weights'];c=p['surplus'];n,b=p['target']
 return min((*w,c))>=0 and tuple(sum(w[i]*rows[i][0][j] for i in range(4)) for j in (0,1))==n and sum(w[i]*rows[i][1] for i in range(4))+c==b
assert all(map(valid,(p,q,r,s)))
def edge(a,b,kind):
 if not valid(a) or not valid(b):return 'INVALID_ENDPOINT'
 if kind=='comparison':return 'VALID_COMPARISON' if a['target']==b['target'] else 'COMPARISON_TARGET_MISMATCH'
 if kind=='bound-weakening':return 'VALID_WEAKENING' if a['target'][0]==b['target'][0] and a['target'][1]<=b['target'][1] and a['weights']==b['weights'] and b['surplus']-a['surplus']==b['target'][1]-a['target'][1] else 'WEAKENING_RULE_MISMATCH'
 return 'UNKNOWN_EDGE_TYPE'
assert edge(p,q,'comparison')=='COMPARISON_TARGET_MISMATCH'
assert edge(p,q,'bound-weakening')=='VALID_WEAKENING'
assert edge(s,r,'comparison')=='VALID_COMPARISON'
assert edge(s,r,'bound-weakening')=='WEAKENING_RULE_MISMATCH'
report={'passed':True,'P_x2_to_Q_x3':'comparison rejected; weakening valid','S_x4_to_R_x4':'comparison valid; weakening rule rejects distinct weights','scope':'Local packet/edge type checks only, not observed history, source authority or analytic map.'}
out=Path(__file__).resolve().parents[1]/'results/catalogue-edge-type-dispatch.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
