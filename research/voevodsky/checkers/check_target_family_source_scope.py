"""Hypothetical rational target interval remains manifest/generation scoped."""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json
req=json.loads((Path(__file__).resolve().parents[1]/'results/row-attestation-request.json').read_text())
manifest=req['manifest'];digest=req['manifest_sha256']
def H(x):return sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
assert H(manifest)==digest
family={'normal':(Q(1),Q(0)),'lo':Q(1),'hi':Q(2),'manifest':digest,'generation':7}
def check(m,generation,bound,multiplier,surplus):
 if H(m)!=family['manifest']:raise ValueError('SOURCE_MANIFEST_MISMATCH')
 if generation!=family['generation']:raise ValueError('GENERATION_SCOPE_MISMATCH')
 b=Q(bound)
 if not family['lo']<=b<=family['hi']:raise ValueError('TARGET_OUTSIDE_INTERVAL')
 if Q(multiplier)!=1 or Q(surplus)!=b-1:raise ValueError('INVALID_FARKAS_PACKET')
 return 'TEST_ONLY_INTERVAL_MATCH_NOT_AUTHORIZED'
for b in (Q(1),Q(3,2),Q(2)):
 assert check(manifest,7,b,1,b-1)=='TEST_ONLY_INTERVAL_MATCH_NOT_AUTHORIZED'
def refuse(m,g,b,mult,surplus,expected):
 try:check(m,g,b,mult,surplus)
 except ValueError as err:assert str(err)==expected
 else:raise AssertionError('out-of-scope interval use accepted')
refuse(manifest,7,Q(1,2),1,Q(-1,2),'TARGET_OUTSIDE_INTERVAL')
refuse(manifest,7,Q(5,2),1,Q(3,2),'TARGET_OUTSIDE_INTERVAL')
refuse(manifest,8,Q(3,2),1,Q(1,2),'GENERATION_SCOPE_MISMATCH')
changed=json.loads(json.dumps(manifest));changed['ordered_primitive_rows'][0]['normal'][0]='-2'
refuse(changed,7,Q(3,2),1,Q(1,2),'SOURCE_MANIFEST_MISMATCH')
refuse(manifest,7,Q(3,2),1,Q(0),'INVALID_FARKAS_PACKET')
report={'passed':True,'interval':'x<=b for rational b in [1,2]','inside_samples':['1','3/2','2'],'outside_samples':['1/2','5/2'],'same_math_changed_unused_row':'SOURCE_MANIFEST_MISMATCH','same_manifest_new_generation':'GENERATION_SCOPE_MISMATCH','bad_surplus':'INVALID_FARKAS_PACKET','scope':'Fictional generation 7; no signed family grant or issuer. Interval match is NOT_AUTHORIZED; analytic role mapping deferred.'}
out=Path(__file__).resolve().parents[1]/'results/target-family-source-scope.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
