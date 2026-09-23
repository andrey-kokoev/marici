"""Positive row isomorphism transports proofs, never exact-manifest grants."""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json
source=json.loads((Path(__file__).resolve().parents[1]/'results/row-attestation-request.json').read_text())
old=source['manifest'];new=json.loads(json.dumps(old))
new['ordered_primitive_rows'][1]={'normal':['2','0'],'upper':'2'}
def H(m):return sha256(json.dumps(m,sort_keys=True,separators=(',',':')).encode()).hexdigest()
assert H(old)==source['manifest_sha256'] and H(new)!=H(old)
def image(manifest,weights):
 r=manifest['ordered_primitive_rows']
 return tuple(sum(Q(r[i]['normal'][j])*weights[i] for i in range(4)) for j in (0,1)),sum(Q(r[i]['upper'])*weights[i] for i in range(4))
p=(Q(0),Q(1),Q(0),Q(0));q=(Q(0),Q(1,2),Q(0),Q(0))
assert image(old,p)==image(new,q)==((Q(1),Q(0)),Q(1))
exact_grant={'manifest':H(old),'action':'authorize-future-source-rooted-proof-use'}
def check(m,grant,rebind=None):
 h=H(m)
 if h!=grant['manifest']:
  if rebind is None:raise ValueError('PRESENTATION_REBIND_REQUIRED')
  if rebind.get('old')!=grant['manifest'] or rebind.get('new')!=h:raise ValueError('REBIND_SCOPE_MISMATCH')
  return 'TEST_ONLY_REBIND_FIELDS_MATCH_NOT_AUTHORIZED'
 return 'TEST_ONLY_ORIGINAL_SCOPE_MATCH_NOT_AUTHORIZED'
assert check(old,exact_grant)=='TEST_ONLY_ORIGINAL_SCOPE_MATCH_NOT_AUTHORIZED'
try:check(new,exact_grant)
except ValueError as err:assert str(err)=='PRESENTATION_REBIND_REQUIRED'
else:raise AssertionError('math carried grant')
try:check(new,exact_grant,{'old':H(old),'new':'wrong'})
except ValueError as err:assert str(err)=='REBIND_SCOPE_MISMATCH'
else:raise AssertionError('wrong rebind accepted')
assert check(new,exact_grant,{'old':H(old),'new':H(new)})=='TEST_ONLY_REBIND_FIELDS_MATCH_NOT_AUTHORIZED'
report={'passed':True,'old_new_proof_image':'same x<=1 exact normal and bound','old_manifest':H(old),'new_manifest':H(new),'unrebound_grant':'PRESENTATION_REBIND_REQUIRED','fictional_rebind':'TEST_ONLY_REBIND_FIELDS_MATCH_NOT_AUTHORIZED','actual_issuer':'unassigned; no approved rebind','scope':'Math row transport only, fictional grant fields never cryptographic authorization or analytic mapping.'}
out=Path(__file__).resolve().parents[1]/'results/presentation-grant-rebind.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
