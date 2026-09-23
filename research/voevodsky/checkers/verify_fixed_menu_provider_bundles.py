"""Independent finite cover proof from separate receipt artifacts and frozen typed menu."""
from pathlib import Path
from itertools import combinations
import json,copy
ROOT=Path(__file__).resolve().parents[3];V=ROOT/'research/voevodsky'
load=lambda name:json.loads((V/'results'/name).read_text())
packet=load('fixed-menu-provider-bundles.json');ledger=load('scoped-cost-ledger.json');delta=load('archive-cost-delta.json')
assert packet['passed'] and packet['migration_binding']==ledger['migration_binding']==delta['migration_binding']
cost={'restricted_archive':ledger['accounts']['live_provider_receipt_encodings']['per_provider'][0],
      'full_archive':ledger['accounts']['live_provider_receipt_encodings']['per_provider'][1],
      'full_lift':sum(delta['without_archive'].values())}
assert cost==packet['provider_receipt_bytes'] and cost=={'restricted_archive':1921,'full_archive':1917,'full_lift':1737}
assert delta['archive_free_reexposure_refused'] and delta['same_lift_and_coverage']
# Frozen declared task semantics: answer and re-exposure require this PUBLISHED
# refined owner state; full-domain lifting requires a CURRENT full-scope head.
tasks={'public_answer_restricted':{'restricted_archive'},'whole_domain_lift':{'full_archive','full_lift'},'restricted_fine_reexposure':{'restricted_archive'}}
assert set(tasks)==set(packet['service_menu'])
valid=[]
for length in range(1,len(cost)+1):
 for subset in combinations(cost,length):
  if all(set(subset)&eligible for eligible in tasks.values()):
   valid.append((sum(cost[n] for n in subset),set(subset)))
minimum=min(x for x,_ in valid)
assert minimum==3658 and {frozenset(group) for value,group in valid if value==minimum}=={frozenset({'restricted_archive','full_lift'})}
assert len(valid)==len(packet['admissible_bundles'])
for item in packet['admissible_bundles']:
 group=set(item['providers']);assert (item['receipt_bytes'],group) in valid
 assert item['covering']=={task:[n for n in item['providers'] if n in eligible] for task,eligible in tasks.items()}
assert packet['minimum_receipt_bundle']['receipt_bytes']==minimum
assert packet['stale_full_lift_forces_archive_enabled_replacement']
post_stale=[(v,g) for v,g in valid if 'full_lift' not in g]
assert min(v for v,g in post_stale)==3838
assert not any('restricted_archive' not in g for _,g in valid)
# False optimization from unauthorized archive escalation is rejected by the
# independently frozen eligibility table.
assert not all({'full_lift'}&eligible for eligible in tasks.values())
report={'passed':True,'valid_bundles':len(valid),'minimum_receipt_bytes':minimum,'after_full_lift_stale_minimum_bytes':3838,'restricted_archive_indispensable':True,'archive_free_provider_cannot_reexpose':True,'scope':'Independent arithmetic and frozen typed eligibility replay from distinct receipt artifacts; runtime liveness and owner approval tested in producer, not recreated from serialized packet.'}
(V/'results/fixed-menu-provider-bundles-verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
