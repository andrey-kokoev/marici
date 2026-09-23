"""Frozen payload/cost ledger, with explicit unknown accounts; not heap or optimum."""
from pathlib import Path
import json,gzip,hashlib
ROOT=Path(__file__).resolve().parents[3];V=ROOT/'research/voevodsky';G=ROOT/'research/grothendieck/results'
load=lambda p:json.loads(p.read_text())
a=load(V/'results/integrated-local-continuation.json');b=load(V/'results/same-base-live-archive-services.json')
assert a['passed'] and b['passed'] and a['root']==b['migration_binding']
assert a['resource_receipts']==b['bytes'] and len(b['bytes'])==2
expected={'live_descriptor','lift_context','archive','cached_point_witnesses','section_encodings','full_segment_encodings'}
assert all(set(row)==expected and all(type(x)==int and x>=0 for x in row.values()) for row in b['bytes'])
raw=gzip.decompress((G/'audit-elimination.json.gz').read_bytes());case=json.loads(raw)['compactions'][0]
canonical=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
proof_bytes=len(canonical(case))
source_files=[V/'checkers/checked_retirement_interface.py',V/'checkers/migration_checkpoint.py',V/'checkers/full_segment_checkpoint.py',V/'checkers/check_same_base_live_archive_services.py',V/'checkers/check_integrated_local_continuation.py']
code=[{'path':p.relative_to(ROOT).as_posix(),'source_bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in source_files]
receipts=b['bytes'];payloads=[sum(row.values()) for row in receipts]
assert payloads==[1921,1917]
# The separate snapshots may duplicate an archive, and do not count process
# objects or prior heads. Summing their fields is an encoding subtotal ONLY.
accounts={'live_provider_receipt_encodings':{'status':'measured_snapshot_bytes','units':'canonical payload bytes','per_provider':payloads,'sum':sum(payloads),'retention':'two reported live generations; prior head not included'},'owner_migration_case':{'status':'measured_separate_artifact','units':'canonical JSON bytes','bytes':proof_bytes,'retention':'owning proof packet; not included in receipt sum'},'shared_source_files':{'status':'measured_file_bytes_not_heap','files':code},'live_handles':{'status':'observed_not_sized','generations':'two independent bootstraps plus one verified advance; process-local token overhead unavailable'},'verification_work':{'status':'partially_observed','full_domain_lift_comparisons':b['full_domain_lift_comparisons'],'owner_projection_checks':'import verifier reports five projection/compaction certificates; work allocation to this workload unavailable','time_and_memory':'unavailable'},'owner_grant_records':{'status':'not_applicable_to_this_public_only_session','note':'owning migration is verified; no external fine-rebase grant was consumed'},'redundant_refinement_history':{'status':'not_exercised','note':'one public refinement; no asymptotic history bound follows'},'complete_heap_and_archives':{'status':'unavailable','note':'shared code, old heads, dependency processes, proof retention and Python overhead not included'}}
assert {'measured_snapshot_bytes','measured_separate_artifact','measured_file_bytes_not_heap','observed_not_sized','partially_observed','not_applicable_to_this_public_only_session','not_exercised','unavailable'}=={v['status'] for v in accounts.values()}
report={'passed':True,'migration_binding':a['root'],'frozen_workload':'two owner-verified providers; one public u<=3/4 advance, five lift comparisons, stale refusal and fresh archive','accounts':accounts,'nonadditivity':'Receipt subtotals, owning proof packet and shared source bytes overlap or differ in retention horizon; never add them as total resource cost.','scope':'Encoding snapshot and explicit unknowns, not minimum information, heap use, total work or universal cost bound.'}
(V/'results/scoped-cost-ledger.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'receipt_payloads':payloads,'receipt_encoding_subtotal':sum(payloads),'owning_case_bytes':proof_bytes,'unknown_accounts':[k for k,v in accounts.items() if v['status'] in ('unavailable','partially_observed','observed_not_sized')]},indent=2))
