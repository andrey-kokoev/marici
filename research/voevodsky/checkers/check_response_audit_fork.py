"""Pinned hypothetical branch heads retain a policy fork, not its resolution."""
from hashlib import sha256
from pathlib import Path
import json
p=json.loads((Path(__file__).resolve().parents[1]/'results/unsent-owner-handoff-payload.json').read_text())
def H(v):return sha256(json.dumps(v,sort_keys=True,separators=(',',':')).encode()).hexdigest()
parent={'id':'fictional-denial','decision':'deny','request':p['request_sha256']}
parent_hash=H(parent)
a={'id':'fictional-child-allow','parent':parent_hash,'decision':'allow','request':parent['request']}
b={'id':'fictional-child-deny','parent':parent_hash,'decision':'deny','request':parent['request']}
heads={H({'parent':parent_hash,'event':a}),H({'parent':parent_hash,'event':b})}
assert len(heads)==2 and a['parent']==b['parent']==parent_hash
def decide(children,merge=None):
 if len({c['parent'] for c in children})!=1:raise ValueError('DIFFERENT_PARENT')
 if len({c['decision'] for c in children})>1:
  if merge is None:return 'PINNED_FORK_UNRESOLVED'
  if set(merge.get('parents',()))!={c['id'] for c in children}:raise ValueError('INCOMPLETE_MERGE')
  return 'TEST_ONLY_MERGE_BYTES_NOT_AUTHORIZED'
 return 'TEST_ONLY_UNCONTESTED_BYTES_NOT_AUTHORIZED'
assert decide((a,b))==decide((b,a))=='PINNED_FORK_UNRESOLVED'
assert decide((a,b),{'parents':(a['id'],b['id'])})=='TEST_ONLY_MERGE_BYTES_NOT_AUTHORIZED'
try:decide((a,b),{'parents':(b['id'],)})
except ValueError as err:assert str(err)=='INCOMPLETE_MERGE'
else:raise AssertionError('partial merge accepted')
report={'passed':True,'distinct_pinned_branch_heads':2,'same_parent_denial':True,'result':'PINNED_FORK_UNRESOLVED independent of order','merge_shape':'TEST_ONLY_MERGE_BYTES_NOT_AUTHORIZED','actual_issuer':'NONE; no real handoff/audit signature','scope':'Local hash records show fork integrity, not trusted source owner or policy priority.'}
out=Path(__file__).resolve().parents[1]/'results/response-audit-fork.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
