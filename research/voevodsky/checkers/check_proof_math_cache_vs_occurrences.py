"""Reuse exact math computation, not occurrence or source-generation identity."""
from hashlib import sha256
from pathlib import Path
import json
rows1=(((-1,0),0),((1,0),1),((0,-1),0),((0,1),1))
rows2=rows1[:1]+(((1,0),2),)+rows1[2:]
packet=(0,1,0,0)
def H(x):return sha256(repr(x).encode()).hexdigest()
def calculate(rows,m):return tuple(sum(rows[i][0][j]*m[i] for i in range(4)) for j in (0,1)),sum(rows[i][1]*m[i] for i in range(4))
cache={};events=[]
def check(rows,generation,m,occurrence,parent):
 key=(H(rows),generation,H(m))
 hit=key in cache
 if not hit:cache[key]=calculate(rows,m)
 events.append({'id':occurrence,'parent':parent,'key':key,'math':cache[key]})
 return cache[key],hit
first,hit=check(rows1,1,packet,'fictional-occ-1','source-event-A');assert not hit and first==((1,0),1)
second,hit=check(rows1,1,packet,'fictional-occ-2','source-event-B');assert hit and second==first
assert len(cache)==1 and len(events)==2 and events[0]['id']!=events[1]['id'] and events[0]['parent']!=events[1]['parent']
third,hit=check(rows2,2,packet,'fictional-occ-3','source-event-C');assert not hit and third==((1,0),2)
fourth,hit=check(rows1,2,packet,'fictional-occ-4','source-event-D');assert not hit and fourth==first
assert len(cache)==3 and len(events)==4
report={'passed':True,'same_rows_generation_packet':'cache hit but two distinct synthetic occurrence records','changed_rows_generation':'cache miss, bound1 -> bound2','same_rows_new_generation':'cache miss despite same math target','cache_entries':len(cache),'occurrence_records':len(events),'scope':'In-memory local arithmetic cache, not actual audit events, issuer grant or analytic role mapping.'}
out=Path(__file__).resolve().parents[1]/'results/proof-math-cache-vs-occurrences.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
