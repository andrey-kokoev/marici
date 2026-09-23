"""Independent ledger arithmetic/fingerprint replay and deleted-premise hostiles."""
from pathlib import Path
import json,gzip,hashlib,copy
ROOT=Path(__file__).resolve().parents[3];V=ROOT/'research/voevodsky';G=ROOT/'research/grothendieck/results'
load=lambda p:json.loads(p.read_text())
ledger=load(V/'results/scoped-cost-ledger.json');work=load(V/'results/integrated-local-continuation.json')
assert ledger['passed'] and work['passed'] and ledger['migration_binding']==work['root']
a=ledger['accounts'];expected={'live_provider_receipt_encodings','owner_migration_case','shared_source_files','live_handles','verification_work','owner_grant_records','redundant_refinement_history','complete_heap_and_archives'}
assert set(a)==expected
rows=work['resource_receipts'];sums=[sum(row.values()) for row in rows]
assert a['live_provider_receipt_encodings']['per_provider']==sums and a['live_provider_receipt_encodings']['sum']==sum(sums)
assert len(rows)==2 and sums==[1921,1917]
case=json.loads(gzip.decompress((G/'audit-elimination.json.gz').read_bytes()))['compactions'][0]
canonical=json.dumps(case,sort_keys=True,separators=(',',':')).encode()
assert a['owner_migration_case']['bytes']==len(canonical)
for record in a['shared_source_files']['files']:
 p=ROOT/record['path'];raw=p.read_bytes()
 assert len(raw)==record['source_bytes'] and hashlib.sha256(raw).hexdigest()==record['sha256']
assert a['complete_heap_and_archives']['status']=='unavailable' and a['verification_work']['time_and_memory']=='unavailable'
assert 'not' in ledger['nonadditivity'].lower() or 'never' in ledger['nonadditivity'].lower()
refused=[]
def reject(name,mutate):
 trial=copy.deepcopy(ledger);mutate(trial);v=trial['accounts']
 valid=set(v)==expected and v['live_provider_receipt_encodings']['per_provider']==sums and v['live_provider_receipt_encodings']['sum']==sum(sums) and v['owner_migration_case']['bytes']==len(canonical) and v['complete_heap_and_archives']['status']=='unavailable' and v['verification_work']['time_and_memory']=='unavailable' and trial['migration_binding']==work['root']
 if valid:raise AssertionError('false ledger admitted: '+name)
 refused.append(name)
reject('altered-receipt-sum',lambda r:r['accounts']['live_provider_receipt_encodings'].update(sum=3837))
reject('omitted-heap-unknown',lambda r:r['accounts'].pop('complete_heap_and_archives'))
reject('false-total-memory-measured',lambda r:r['accounts']['complete_heap_and_archives'].update(status='measured'))
reject('wrong-source-binding',lambda r:r.update(migration_binding='foreign'))
# Deleting provider zero removes THAT scoped lift bundle; the other remains
# a live replacement. This counterfactual reuses snapshot bytes only, not
# a measured heap delta or archive entitlement transfer.
remaining=sums[1];assert remaining==1917 and work['replacement_lift_live']
report={'passed':True,'receipt_subtotal_bytes':sum(sums),'remaining_provider_receipt_bytes':remaining,'owning_case_bytes':len(canonical),'fingerprints_checked':len(a['shared_source_files']['files']),'refusals':refused,'scope':'Independent arithmetic and file-fingerprint replay; provider deletion is a snapshot/account counterfactual, not heap freeing, proof of security, or independent runtime handle check.'}
(V/'results/scoped-cost-ledger-verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
