"""Two contrary hypothetical revisions of one denial need explicit merge."""
from pathlib import Path
import json
p=json.loads((Path(__file__).resolve().parents[1]/'results/unsent-owner-handoff-payload.json').read_text())
prior={'id':'fictional-deny-0','decision':'deny','action':'authorize-future-source-rooted-proof-use','request':p['request_sha256'],'manifest':p['ordered_manifest_sha256']}
a={'id':'fictional-allow-1','parent':prior['id'],'decision':'allow','action':prior['action'],'request':prior['request'],'manifest':prior['manifest'],'graph_order':10}
b=dict(a,id='fictional-deny-2',decision='deny',graph_order=11)
def assess(children,merge=None):
 if any(c['parent']!=prior['id'] or c['request']!=prior['request'] or c['manifest']!=prior['manifest'] or c['action']!=prior['action'] for c in children):raise ValueError('FORK_SCOPE_MISMATCH')
 if len(children)>1 and len({c['decision'] for c in children})>1:
  if merge is None:return 'CONFLICTING_REVISIONS'
  if set(merge.get('parents',()))!={c['id'] for c in children}:raise ValueError('MERGE_PARENTS_MISMATCH')
  if merge.get('source_owned') is not True:raise ValueError('SOURCE_OWNED_RESOLUTION_MISSING')
  return 'TEST_ONLY_MERGE_SHAPE_NOT_AUTHORIZED'
 return 'TEST_ONLY_UNCONTESTED_FIXTURE_NOT_AUTHORIZED'
assert assess((a,b))==assess((b,a))=='CONFLICTING_REVISIONS'
assert assess((a,b),{'parents':(a['id'],b['id']),'source_owned':True})=='TEST_ONLY_MERGE_SHAPE_NOT_AUTHORIZED'
for merge,code in (({'parents':(a['id'],),'source_owned':True},'MERGE_PARENTS_MISMATCH'),({'parents':(a['id'],b['id']),'source_owned':False},'SOURCE_OWNED_RESOLUTION_MISSING')):
 try:assess((a,b),merge)
 except ValueError as err:assert str(err)==code
 else:raise AssertionError('unresolved fork accepted')
assert prior['decision']=='deny'
report={'passed':True,'fork_status':'CONFLICTING_REVISIONS independent of graph order','prior_denial_preserved':True,'merge_requires':'both parent IDs and independent source-owned verification; fictional shape only','actual_state':'no owner, denial, response, merge or grant','scope':'Synthetic conflict model; cannot authenticate source-owned flag or promote graph chronology to issuer policy.'}
out=Path(__file__).resolve().parents[1]/'results/forked-owner-revisions.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
