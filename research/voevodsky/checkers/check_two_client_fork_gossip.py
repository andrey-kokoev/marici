"""Two-client same-slot head exchange detects witnessed, not unseen, forks."""
from itertools import product
from pathlib import Path
import json
A=('issuer-A','unit-square','event-A',1,2,'head-A')
B=('issuer-A','unit-square','event-A',1,2,'head-B')
COMMON=('issuer-A','unit-square','event-A',1,1,'common-head')
def compare(x,y,delivered=True,authenticated=False):
 if not delivered:return 'NO_SHARED_OBSERVATION'
 if not authenticated:return 'UNAUTHENTICATED_GOSSIP_INPUT'
 if x[:5]==y[:5] and x[5]!=y[5]:return 'OBSERVED_SAME_SLOT_FORK'
 if x[:5]==y[:5] and x[5]==y[5]:return 'SAME_OBSERVED_HEAD_NOT_GLOBAL_UNIQUENESS'
 return 'DIFFERENT_SEQUENCE_NEEDS_CONSISTENCY_WITNESS'
assert compare(A,B,authenticated=True)=='OBSERVED_SAME_SLOT_FORK'
assert compare(A,A,authenticated=True)=='SAME_OBSERVED_HEAD_NOT_GLOBAL_UNIQUENESS'
assert compare(A,COMMON,authenticated=True)=='DIFFERENT_SEQUENCE_NEEDS_CONSISTENCY_WITNESS'
assert compare(A,B,delivered=False,authenticated=True)=='NO_SHARED_OBSERVATION'
assert compare(A,B,authenticated=False)=='UNAUTHENTICATED_GOSSIP_INPUT'
checks=0
for x,y in product((A,B,COMMON),repeat=2):
 assert isinstance(compare(x,y,authenticated=True),str);checks+=1
assert checks==9
report={'passed':True,'pairings_checked':checks,'conflicting_authenticated_heads':'OBSERVED_SAME_SLOT_FORK','same_head':'SAME_OBSERVED_HEAD_NOT_GLOBAL_UNIQUENESS','undelivered':'NO_SHARED_OBSERVATION','untrusted_channel':'UNAUTHENTICATED_GOSSIP_INPUT','scope':'Conditional trust in both head provenance and delivered exchange; no actual authenticated gossip network or proof that all log forks are observed.'}
out=Path(__file__).resolve().parents[1]/'results/two-client-fork-gossip.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
