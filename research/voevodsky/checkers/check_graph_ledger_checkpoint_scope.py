"""Read-only graph-ledger audit: linkage and identity fields, no source grant."""
import json,glob
from pathlib import Path
root=Path(__file__).resolve().parents[3]
ledger=root/'.narada/epistemic/ledger'
current=json.loads(Path(glob.glob(str(ledger/'ev-000000015066-*.json'))[0]).read_text())
prev=json.loads(Path(glob.glob(str(ledger/'ev-000000015065-*.json'))[0]).read_text())
assert current['previous_hash']==prev['event_hash']
assert current['event_kind']=='proposal_admitted' and current['certifies_truth'] is False
assert current['identity_state']['authentication']['status']=='missing'
assert current['identity_state']['authority']['granted'] is False
assert any(op.get('entity_id','').endswith(':publication-checkpoint-audit:v1') for op in current['operations'])
assert not any(op.get('kind')=='farkas_row_attestation' for op in current['operations'])
report={'passed':True,'event_id':current['event_id'],'previous_hash_matches_stored_predecessor':True,'event_kind':'proposal_admitted','certifies_truth':False,'actor_authentication':current['identity_state']['authentication']['status'],'actor_authority_granted':current['identity_state']['authority']['granted'],'farkas_row_source_grant_in_event':False,'scope':'Read-only two-file header/reference audit, not independent recomputation of ledger event hashes, signature verification, global anti-fork consistency or source-owner attestation.'}
out=Path(__file__).resolve().parents[1]/'results/graph-ledger-checkpoint-scope.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
