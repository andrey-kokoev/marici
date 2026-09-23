"""One-row proof support does not shrink full-manifest publication scope."""
from hashlib import sha256
from fractions import Fraction as Q
from pathlib import Path
import json
r=json.loads((Path(__file__).resolve().parents[1]/'results/row-attestation-request.json').read_text())
full=r['manifest'];subset=dict(full,ordered_primitive_rows=[full['ordered_primitive_rows'][1]])
def H(x):return sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
assert H(full)==r['manifest_sha256'] and H(subset)!=H(full)
row=subset['ordered_primitive_rows'][0]
assert tuple(Q(x) for x in row['normal'])==(Q(1),Q(0)) and Q(row['upper'])+Q(1)==Q(2)
fictional_grant={'source_manifest':H(full),'action':'authorize-future-source-rooted-proof-use'}
def scope(m,grant):
 if H(m)!=grant['source_manifest']:raise ValueError('FULL_SOURCE_SCOPE_MISMATCH')
 return 'TEST_ONLY_FULL_MANIFEST_MATCH_NOT_AUTHORIZED'
try:scope(subset,fictional_grant)
except ValueError as err:assert str(err)=='FULL_SOURCE_SCOPE_MISMATCH'
else:raise AssertionError('subset substituted')
assert scope(full,fictional_grant)=='TEST_ONLY_FULL_MANIFEST_MATCH_NOT_AUTHORIZED'
report={'passed':True,'proof_support':'x-upper single row with surplus1 proves x<=2','full_manifest_sha256':H(full),'support_subset_sha256':H(subset),'subset_against_full_grant':'FULL_SOURCE_SCOPE_MISMATCH','actual_grant':'NONE; fictional full grant not signed/issued','scope':'Minimal selected proof support vs exact full source manifest, no universal proof minimum or analytic map.'}
out=Path(__file__).resolve().parents[1]/'results/support-vs-source-scope.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
