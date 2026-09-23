"""Original tight x<=1 packet is unique; relaxed target admits substitution."""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
original=json.loads((root/'results/proof-use-request-envelope.json').read_text())['packet']
assert original=={'multipliers':['0','1','0','0'],'surplus':'0','target_normal':['1','0'],'target_bound':'1'}
def verify(m,c,b):
 a,x,d,y=map(Q,m);c=Q(c)
 return x-a==1 and y-d==0 and x+y+c==b and min((a,x,d,y,c))>=0
assert verify((0,1,0,0),0,1)
# Tight bound 1 forces x=1+a, y=d and a+d+c=0 -> a=d=c=0.
assert all(not verify((a,1+a,d,d),c,Q(1)) for a,d,c in ((Q(1),Q(0),Q(0)),(Q(0),Q(1),Q(0)),(Q(0),Q(0),Q(1))))
p={'multipliers':['0','1','0','0'],'surplus':'1','target_normal':['1','0'],'target_bound':'2'}
q={'multipliers':['1','2','0','0'],'surplus':'0','target_normal':['1','0'],'target_bound':'2'}
assert verify(p['multipliers'],p['surplus'],Q(2)) and verify(q['multipliers'],q['surplus'],Q(2))
def H(v):return sha256(json.dumps(v,sort_keys=True,separators=(',',':')).encode()).hexdigest()
assert H(p)!=H(q)
request={'target_bound':'2','packet_digest':H(p),'scope':'EXACT_PACKET','authorization':'NONE'}
def check(packet,scope):
 if packet['target_bound']!=request['target_bound'] or packet['target_normal']!=p['target_normal']:raise ValueError('TARGET_MISMATCH')
 if scope=='EXACT_PACKET' and H(packet)!=request['packet_digest']:raise ValueError('EQUIVALENT_PACKET_NOT_COVERED')
 return 'TEST_ONLY_TARGET_MATCH_NOT_AUTHORIZED'
try:check(q,'EXACT_PACKET')
except ValueError as err:assert str(err)=='EQUIVALENT_PACKET_NOT_COVERED'
else:raise AssertionError('equivalent packet promoted')
assert check(q,'EXPLICIT_TARGET_ONLY')=='TEST_ONLY_TARGET_MATCH_NOT_AUTHORIZED'
report={'passed':True,'original_x_le_1':'tight source packet unique under nonnegative exact Farkas bound','new_relaxed_target':'x<=2','packet_P':p,'packet_Q':q,'different_hash_same_target':True,'exact_request_substitution':'EQUIVALENT_PACKET_NOT_COVERED','hypothetical_explicit_target_scope':'TEST_ONLY_TARGET_MATCH_NOT_AUTHORIZED','scope':'No owner grant or target-level authorization; original request not changed.'}
(root/'results/equivalent-packet-request-scope.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'passed':True,'tight_original_unique':True,'relaxed_equivalent_packets':2,'exact_request':'EQUIVALENT_PACKET_NOT_COVERED'}))
