"""Zero signed difference cannot repair invalid endpoint certificates."""
from pathlib import Path
import json
rows=(((-1,0),0),((1,0),1),((0,-1),0),((0,1),1))
def valid(p):
 m=p['weights'];c=p['surplus'];target=p['target']
 normal=tuple(sum(m[i]*rows[i][0][j] for i in range(4)) for j in (0,1))
 bound=sum(m[i]*rows[i][1] for i in range(4))+c
 return min((*m,c))>=0 and (normal,bound)==target
bad={'weights':(0,1,0,0),'surplus':-1,'target':((1,0),0)}
good={'weights':(0,1,0,0),'surplus':1,'target':((1,0),2)}
def compare(left,right):
 delta=tuple(x-y for x,y in zip(left['weights'],right['weights']))
 surplus_delta=left['surplus']-right['surplus']
 if not valid(left) or not valid(right):return 'REJECT_INVALID_ENDPOINT',delta,surplus_delta
 if left['target']!=right['target']:return 'REJECT_TARGET_MISMATCH',delta,surplus_delta
 return 'VALID_SIGNED_COMPARISON',delta,surplus_delta
assert not valid(bad) and compare(bad,bad)==('REJECT_INVALID_ENDPOINT',(0,0,0,0),0)
assert compare(good,good)==('VALID_SIGNED_COMPARISON',(0,0,0,0),0)
assert compare(good,bad)[0]=='REJECT_INVALID_ENDPOINT'
report={'passed':True,'identical_invalid_endpoints':'delta zero and surplus delta zero, rejected','identical_valid_endpoints':'zero signed comparison accepted as local math only','gate_order':'validate each endpoint then common target then signed difference','scope':'In-memory packet test, no source issuer, observed history or analytic role mapping.'}
out=Path(__file__).resolve().parents[1]/'results/invalid-endpoint-zero-delta.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
