"""Tiered verification failures for bounded square proof provenance record."""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json
rows=(((-1,0),0),((1,0),1),((0,-1),0),((0,1),1))
def H(x):return sha256(repr(x).encode()).hexdigest()
manifest=H(rows);ctx=(manifest,'W','slot-1');event='w#local';nonce='private-local-salt'
def commitment():return H(('occurrence-v1',ctx,event,nonce))
record={'row_manifest':manifest,'multipliers':(Q(0),Q(1),Q(0),Q(1)),'surplus':Q(1),'target':((Q(1),Q(1)),Q(3)),'prefix_digest':H(('Z',manifest)),'left_commit':commitment(),'right_commit':commitment(),'event_opening':(event,nonce),'issuer_attestation':None}
def check_math(r):
 if r.get('row_manifest')!=manifest or 'multipliers' not in r:raise ValueError('MATH_PACKET_INCOMPLETE')
 m=r['multipliers'];c=r.get('surplus')
 if c is None or len(m)!=4 or min(m)<0 or c<0:raise ValueError('MATH_PACKET_INCOMPLETE')
 if (tuple(sum(rows[i][0][j]*m[i] for i in range(4)) for j in (0,1)),m[1]+m[3]+c)!=r['target']:raise ValueError('MATH_PACKET_INVALID')
 return True
def check_link(r):
 check_math(r)
 if not r.get('prefix_digest') or r.get('left_commit')!=r.get('right_commit'):raise ValueError('LINK_EVIDENCE_INCOMPLETE')
 return True
def check_replay(r):
 check_link(r)
 opening=r.get('event_opening')
 if opening is None:raise ValueError('UNVERIFIABLE_TRACE')
 if H(('occurrence-v1',ctx,*opening))!=r['left_commit']:raise ValueError('WRONG_OPENING')
 if r.get('issuer_attestation') is None:raise ValueError('ISSUER_ATTESTATION_MISSING')
 raise ValueError('EXTERNAL_ATTESTATION_VERIFIER_NOT_AVAILABLE')
assert check_math(record) and check_link(record)
for checker,field,error in ((check_math,'multipliers','MATH_PACKET_INCOMPLETE'),(check_link,'prefix_digest','LINK_EVIDENCE_INCOMPLETE'),(check_replay,'event_opening','UNVERIFIABLE_TRACE'),(check_replay,'issuer_attestation','ISSUER_ATTESTATION_MISSING')):
 r=dict(record);r.pop(field,None)
 try:checker(r)
 except ValueError as err:assert str(err)==error
 else:raise AssertionError('missing required field accepted')
try:check_replay(record)
except ValueError as err:assert str(err)=='ISSUER_ATTESTATION_MISSING'
else:raise AssertionError('issuer invented')
report={'passed':True,'math_tier':'exact packet check with manifest, multipliers, surplus, target','link_tier':'math plus prefix and equal adjacent commitments; does not prove occurrence','replay_tier':'requires opening and separately authenticated issuer attestation; unavailable in inspected evidence','missing_multiplier':'MATH_PACKET_INCOMPLETE','missing_prefix':'LINK_EVIDENCE_INCOMPLETE','missing_opening':'UNVERIFIABLE_TRACE','missing_attestation':'ISSUER_ATTESTATION_MISSING','scope':'Necessary fields for THESE concrete verifiers only, not globally minimal sufficient statistic or external owner grant.'}
out=Path(__file__).resolve().parents[1]/'results/provenance-retention-tiers.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
