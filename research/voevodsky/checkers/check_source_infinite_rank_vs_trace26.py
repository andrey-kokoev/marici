#!/usr/bin/env python3
"""Rank-nullity audit of the source infinite-rank family against trace26."""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
SOURCE=ROOT/'research/nima/the-diagonal-shell-wronskian-family-is-infinite-rank-and-cannot-factor-through-the-scalar-wall-incidence-plane.md'
JETS=ROOT/'research/nima/laplace-transform-of-the-gaussian-pair-green-identity-gives-an-exact-spectral-jet-recurrence.md'
TRACE=ROOT/'research/voevodsky/contracts/radial-jointly-faithful-sampled-four-trace.v1.json'
PACKET=ROOT/'research/voevodsky/source_infinite_rank_forces_radial_trace_carrier_enlargement_20260911.md'
t=json.loads(TRACE.read_text()); source=SOURCE.read_text(); jets=JETS.read_text()
# Universal hostile finite restriction: projection of 27 independent coordinates to 26.
P=s.zeros(26,27)
for i in range(26): P[i,i]=1
w=s.zeros(27,1); w[26]=1
checks={
 'source_packet_declares_infinite_dimension':'infinite dimensional' in source,
 'source_packet_declares_every_finite_set_independent':'every finite set at distinct shell locations is linearly independent' in source,
 'jet_packet_declares_all_jets':'all of its jets' in jets,
 'jet_packet_withholds_frozen_port_identification':'does not yet identify' in jets,
 'synthetic_trace_dimension_26':t['comparison']['rank']==26 and t['comparison']['kernel_dimension']==0,
 'projection_rank_at_most_26':P.rank()==26,
 '27_source_directions_force_kernel':27-P.rank()==1 and P*w==s.zeros(26,1) and w!=s.zeros(27,1),
 'finite_internal_faithfulness_does_not_resolve_source_rank':t['comparison']['jointly_faithful'] and P.rank()<27,
}
# For every tested larger source rank, nullity grows exactly by N-26 for coordinate projection.
nullities={}
for n in (27,28,32,52):
 Q=s.zeros(26,n)
 for i in range(26): Q[i,i]=1
 nullities[str(n)]=n-Q.rank()
checks['tested_nullity_growth']=all(v==int(n)-26 for n,v in nullities.items())
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.source-infinite-rank-vs-trace26.v1','input_digests':{'source_rank_packet':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'jet_packet':hashlib.sha256(JETS.read_bytes()).hexdigest(),'trace_contract':hashlib.sha256(TRACE.read_bytes()).hexdigest(),'packet':hashlib.sha256(PACKET.read_bytes()).hexdigest()},'checks':checks,'passed':all(checks.values()),'tested_source_rank_to_minimum_nullity':nullities,'disposition':{'retained':'trace26 as finite observation functor','rejected':'faithful identification with source infinite-rank shell/all-jet family','next':'indexed finite trace tower with transition maps; completion remains separate'}}
RESULT=ROOT/'research/voevodsky/results/source_infinite_rank_vs_trace26.json'; RESULT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':result['passed'],'check_count':len(checks),'rank_27_minimum_nullity':nullities['27']}))
raise SystemExit(0 if result['passed'] else 1)
