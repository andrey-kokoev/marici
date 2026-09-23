"""Equal exact proof packets can occur at distinct synthetic events."""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json
packet={'manifest':'local-square-rows-v1','multipliers':['0','1','0','0'],'surplus':'1','target_normal':['1','0'],'target_bound':'2'}
def H(x):return sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
a={'occurrence':'fictional-proof-001','packet_digest':H(packet),'predecessor':'fictional-source'}
b={'occurrence':'fictional-proof-002','packet_digest':H(dict(packet)),'predecessor':'fictional-source'}
assert a['packet_digest']==b['packet_digest'] and a['occurrence']!=b['occurrence']
edge={'from_occurrence':a['occurrence'],'to_occurrence':'fictional-checkpoint','packet_digest':a['packet_digest']}
def replay(link,observed):
 if link['packet_digest']!=observed['packet_digest']:raise ValueError('PACKET_MISMATCH')
 if link['from_occurrence']!=observed['occurrence']:raise ValueError('OCCURRENCE_ID_MISMATCH')
 return 'TEST_ONLY_OCCURRENCE_FIELDS_MATCH_NOT_OBSERVED'
assert replay(edge,a)=='TEST_ONLY_OCCURRENCE_FIELDS_MATCH_NOT_OBSERVED'
try:replay(edge,b)
except ValueError as err:assert str(err)=='OCCURRENCE_ID_MISMATCH'
else:raise AssertionError('same packet conflated events')
report={'passed':True,'math_packet_digest_same':True,'two_synthetic_occurrence_ids_distinct':True,'edge_replay_with_other_occurrence':'OCCURRENCE_ID_MISMATCH','status':'TEST_ONLY_NOT_OBSERVED','scope':'Local packet equivalence versus hypothetical occurrence identity; no actual event observation, owner attestation or analytic map.'}
out=Path(__file__).resolve().parents[1]/'results/packet-vs-occurrence-id.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
