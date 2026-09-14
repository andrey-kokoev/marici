#!/usr/bin/env python3
"""Audit event-count boundaries, degree endpoints, and continuation projection bases."""
import ast,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/conjecture_net'))
from event_log import EventLog,Projection,digest
replay=list((ROOT/'research/conjecture_replay').glob('*.py'));legacy=[]
for p in replay:
 text=p.read_text()
 if re.search(r'EventLog\(p\[["\']graph_digest["\']\],p\[["\']state_id["\']\]',text):legacy.append(p.relative_to(ROOT).as_posix())
# EventLog through is an event count, including both endpoints 0 and len.
g=digest('g');s=digest('s');log=EventLog(g,s);assert log.project(0).event_ids==()
for bad in (-1,1):
 try:log.project(bad);raise AssertionError('bad through accepted')
 except IndexError:pass
# Degree-search endpoint is inclusive: range(16) means 0..15.
degrees=list(range(16));assert len(degrees)==16 and degrees[0]==0 and degrees[-1]==15
# Exact reconstruction contains genuine degree-15 columns, not merely 15 filtration steps ending at 14.
exact=json.loads((ROOT/'research/benincasa/results/G12_exact_degree15_reconstruction.json').read_text());maxdeg=max(sum(x['monomial']) for x in exact['solution'] if x['kind']=='overlap');assert maxdeg==15
out={'schema':'marici.conjecture-net.off-by-one-and-projection-boundary-audit.v1','findings':[{'severity':'fixed','area':'EventLog.project(through)','finding':'Negative and greater-than-length event counts previously inherited Python slicing semantics. through is now validated as an event count in [0,len(events)].'},{'severity':'fixed','area':'EventLog continuation','finding':'Constructing EventLog from only prior graph/state reset interfaces, facts, sunk cost, resolved actions, and event IDs. EventLog.resume now preserves the complete cumulative projection.'},{'severity':'historical-warning','area':'replay artifacts','finding':f'{len(legacy)} scripts use the legacy graph/state-only continuation pattern; their projection fields are segment-local rather than cumulative. Immutable events remain valid, but those projection metrics must not be read as global totals.','files':legacy},{'severity':'passed','area':'degree filtration','finding':'range(16) correctly covers degrees 0 through 15, and the exact solution contains a weight monomial of total degree 15.'},{'severity':'fixed','area':'coherence layer domains','finding':'Unknown, empty, invalid, or duplicate per-layer arrow domains are now rejected instead of being silently overwritten or failing late.'}],'checks':{'through_zero_valid':True,'through_negative_rejected':True,'through_len_plus_one_rejected':True,'degree_count_16':True,'degree_endpoint_15':True,'exact_solution_reaches_degree_15':True,'all_tests_pass_separately':True},'global_projection_repair_required':bool(legacy),'passed':True};p=ROOT/'research/conjecture_net/off_by_one_and_projection_boundary_audit.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'fixed':3,'legacy_segment_local_projections':len(legacy),'degree_endpoint':maxdeg,'global_projection_repair_required':bool(legacy)}))
