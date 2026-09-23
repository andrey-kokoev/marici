"""Two comparison edges can have zero net delta without becoming identity."""
from pathlib import Path
import json
P={'id':'fictional-P','weights':(0,1,0,0),'surplus':1,'target':((1,0),2)}
Q={'id':'fictional-Q','weights':(1,2,0,0),'surplus':0,'target':((1,0),2)}
rows=(((-1,0),0),((1,0),1),((0,-1),0),((0,1),1))
def valid(p):
 w=p['weights'];c=p['surplus']
 return min((*w,c))>=0 and tuple(sum(w[i]*rows[i][0][j] for i in range(4)) for j in (0,1))==p['target'][0] and sum(w[i]*rows[i][1] for i in range(4))+c==p['target'][1]
assert valid(P) and valid(Q)
d1=tuple(a-b for a,b in zip(Q['weights'],P['weights']));d2=tuple(a-b for a,b in zip(P['weights'],Q['weights']))
assert tuple(a+b for a,b in zip(d1,d2))==(0,0,0,0)
cycle=(('fictional-P','fictional-Q','comparison@1'),('fictional-Q','fictional-P','comparison@1'))
identity=()
assert cycle!=identity and len(cycle)==2 and cycle[0][0]==cycle[-1][1]
report={'passed':True,'both_endpoint_packets':'valid x<=2','cycle_signed_delta_sum':'zero','cycle_edge_count':2,'identity_edge_count':0,'finding':'equal endpoints and zero net math do not erase edge occurrences','scope':'Synthetic comparison edges, not observed events, issuer authority or analytic mapping.'}
out=Path(__file__).resolve().parents[1]/'results/nonempty-comparison-cycle.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
