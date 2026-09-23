"""Target-only hypothetical scope is exact (source,normal,bound), not implication closure."""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json
req=json.loads((Path(__file__).resolve().parents[1]/'results/row-attestation-request.json').read_text())
rows=req['manifest']['ordered_primitive_rows'];mhash=req['manifest_sha256']
def H(m):return sha256(json.dumps(m,sort_keys=True,separators=(',',':')).encode()).hexdigest()
scope={'manifest':mhash,'normal':(Q(1),Q(0)),'bound':Q(2),'action':'authorize-future-source-rooted-proof-use','quantifier':'ANY_VALID_PACKET_FOR_EXACT_TARGET'}
def check(manifest,normal,bound,multipliers,surplus):
 if H(manifest)!=scope['manifest']:raise ValueError('SOURCE_SCOPE_MISMATCH')
 if tuple(normal)!=scope['normal'] or Q(bound)!=scope['bound']:raise ValueError('EXACT_TARGET_MISMATCH')
 m=tuple(map(Q,multipliers));c=Q(surplus)
 if min((*m,c))<0 or tuple(sum(Q(rows[i]['normal'][j])*m[i] for i in range(4)) for j in (0,1))!=tuple(normal) or sum(Q(rows[i]['upper'])*m[i] for i in range(4))+c!=Q(bound):raise ValueError('INVALID_PACKET')
 return 'TEST_ONLY_TARGET_SCOPE_MATCH_NOT_AUTHORIZED'
assert check(req['manifest'],(1,0),2,(0,1,0,0),1)=='TEST_ONLY_TARGET_SCOPE_MATCH_NOT_AUTHORIZED'
assert check(req['manifest'],(1,0),2,(1,2,0,0),0)=='TEST_ONLY_TARGET_SCOPE_MATCH_NOT_AUTHORIZED'
def refuse(manifest,normal,bound,m,c,code):
 try:check(manifest,normal,bound,m,c)
 except ValueError as err:assert str(err)==code
 else:raise AssertionError('scope escaped')
refuse(req['manifest'],(1,0),1,(0,1,0,0),0,'EXACT_TARGET_MISMATCH')
refuse(req['manifest'],(1,0),3,(0,1,0,0),2,'EXACT_TARGET_MISMATCH')
refuse(req['manifest'],(0,1),2,(0,0,0,1),1,'EXACT_TARGET_MISMATCH')
altered=json.loads(json.dumps(req['manifest']));altered['ordered_primitive_rows'][0]['normal'][0]='-2'
refuse(altered,(1,0),2,(0,1,0,0),1,'SOURCE_SCOPE_MISMATCH')
report={'passed':True,'exact_x_le_2_two_packets':'TEST_ONLY_TARGET_SCOPE_MATCH_NOT_AUTHORIZED','stronger_x_le_1':'EXACT_TARGET_MISMATCH','weaker_x_le_3':'EXACT_TARGET_MISMATCH','changed_normal':'EXACT_TARGET_MISMATCH','changed_unused_source_row':'SOURCE_SCOPE_MISMATCH','scope':'Hypothetical exact-target quantifier and packet validity; no real owner grant, generation, signature or analytic role map.'}
out=Path(__file__).resolve().parents[1]/'results/exact-target-grant-scope.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
