"""Two weakening paths may share final certificate bytes without sharing events."""
from hashlib import sha256
from pathlib import Path
import json
source={'weights':(0,1,0,0),'normal':(1,0),'bound':1,'surplus':0}
def next_packet(packet,bound):
 assert bound>=packet['bound']
 return dict(packet,bound=bound,surplus=packet['surplus']+bound-packet['bound'])
def H(obj):return sha256(repr(obj).encode()).hexdigest()
mid=next_packet(source,2);via=next_packet(mid,3);direct=next_packet(source,3)
assert via==direct and via['surplus']==2 and H(via)==H(direct)
paths={'via':('synthetic-x1','synthetic-x2','synthetic-x3-via'),'direct':('synthetic-x1','synthetic-x3-direct')}
assert paths['via']!=paths['direct'] and paths['via'][-1]!=paths['direct'][-1]
assert H(paths['via'])!=H(paths['direct'])
assert next_packet(source,3)==next_packet(next_packet(source,2),3)
report={'passed':True,'endpoint_packet_digest_equal':True,'final_math':'x<=3 with x-upper multiplier1 surplus2','path_events':'two edges with middle occurrence versus one direct edge, distinct final occurrence IDs','composition':'arithmetic additive, audit paths not equal','scope':'Synthetic histories only; neither observed source events nor issuer authority nor analytic map.'}
out=Path(__file__).resolve().parents[1]/'results/weakening-path-vs-endpoint.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
