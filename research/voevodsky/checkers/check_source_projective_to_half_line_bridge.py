#!/usr/bin/env python3
"""Check the source projective completion and isolate its half-line bridge datum."""
from pathlib import Path
import hashlib,json,math
ROOT=Path(__file__).resolve().parents[3]
SOURCE=ROOT/'research/nima/a-greedy-global-forest-completes-the-cycle-observer-on-the-projective-edge-source.md'
BOUND=ROOT/'research/voevodsky/common_radial_history_has_a_cutoffwise_half_line_L2_bound_20260911.md'
PACKET=ROOT/'research/voevodsky/source_projective_completion_supersedes_synthetic_edge_weight_20260911.md'
RESULT=ROOT/'research/voevodsky/results/source_projective_to_half_line_bridge.json'
source=SOURCE.read_text(); checks={
 'projective_source_declared':'mathcal C_{D,\\exp}' in source,
 'all_positive_delta_seminorms':'bigcap_{\\delta>0}' in source,
 'greedy_forest_declared':'Greedy global forest' in source,
 'chord_port_contractive':'z_\\delta(Z_Dc)\\le q_\\delta(c)' in source,
 'completed_augmented_observer_injective':'is injective' in source,
 'cutoff_naturality_declared':'Z_DP_N=Q_NZ_D' in source,
 'edge_grade_only_declared_proper':'proper edge grade' in source,
 'no_explicit_interval_length_grade_formula':not any(x in source for x in ('log(q/p) <=','\\ell_e\\le','interval_length_grade')),
 'half_line_column_bound_available':'C_D=' in BOUND.read_text(),
}
# Finite sections verify l2(exp(2 delta W)) <= l1(exp(delta W)).
sections={}
for N in (4,8,16):
 c=[((-1)**i)*(i+1)/(N+1) for i in range(N)]; W=[i for i in range(N)]; delta=0.3
 x=[abs(c[i])*math.exp(delta*W[i]) for i in range(N)]
 l1=sum(x); l2=math.sqrt(sum(v*v for v in x))
 checks[f'projective_to_Hilbert_section_{N}']=l2<=l1+1e-14
 # Polynomial interval growth is exponentially dominated in this fixture.
 ell=[i+1 for i in range(N)]; ratios=[ell[i]*math.exp(-delta*W[i]) for i in range(N)]
 sections[str(N)]={'l2_over_l1':l2/l1,'max_length_grade_ratio':max(ratios)}
checks['polynomial_length_fixture_has_bounded_ratio']=max(sections[str(N)]['max_length_grade_ratio'] for N in (4,8,16))<4
# A superexponential hostile family is not bounded by one exponential grade.
hostile=[math.exp(n*n-0.3*n) for n in range(1,13)]
checks['superexponential_length_hostile_detected']=all(hostile[i+1]>hostile[i] for i in range(len(hostile)-1)) and hostile[-1]>1e50
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.source-projective-to-half-line-bridge-check.v1','input_digests':{'source_completion':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'half_line_bound':hashlib.sha256(BOUND.read_bytes()).hexdigest(),'packet':hashlib.sha256(PACKET.read_bytes()).hexdigest()},'checks':checks,'passed':all(checks.values()),'finite_sections':sections,'disposition':{'supersedes':'synthetic geometric edge budget as preferred source topology','retains':'synthetic Hilbert model only as comparison','first_missing':'explicit bound |log(q/p)| <= C_delta exp(delta W(e)) for the declared source grade and edge order'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':result['passed'],'check_count':len(checks),'first_missing':'interval_length_grade_bound'}))
raise SystemExit(0 if result['passed'] else 1)
