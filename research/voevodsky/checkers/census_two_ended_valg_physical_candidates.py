#!/usr/bin/env python3
"""Census two-ended physical candidates after rejecting cyclic soft endpoints."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[3];B=R/'research/benincasa'
soft_no=json.loads((R/'research/voevodsky/results/soft_endpoint_GM_valg_torsor_no_go.json').read_text())
inf=json.loads((B/'results/infinity-physical-leray-covector.json').read_text())
infrel=json.loads((B/'results/infinity-gysin-physical-relative-gate.json').read_text())
top=json.loads((B/'top-sector-residue-boundary.json').read_text())
checks={'soft_family_rejected':soft_no['passed'],'infinity_path_is_relative':infrel['physical_projective_path']['boundary_vector']==[-1,1],'infinity_annihilates_valg':'v_alg' in inf['kernel_annihilated'],'top_has_odd_mixed_residue':top['mixed_to_q_second_residues']==[1,-1],'top_boundary_is_oriented':top['oriented_geometric_boundary']==[1,-1,1],'top_denominators_horizontal':top['all_denominators_horizontal'] is True,'top_is_existing_relative_class':'relative coefficient class' in top['classification']}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.two-ended-v-alg-physical-candidate-census.v1','candidates':[{'family':'cyclic soft endpoint','residue_support':['marked endpoint only'],'disposition':'rejected: vector (L,0)'},{'family':'physical infinity relative path','boundary':[-1,1],'disposition':'rejected: canonical Leray covector annihilates v_alg'},{'family':'top-sector triple logarithmic residue','denominators':top['denominator_order'],'geometric_boundary':top['oriented_geometric_boundary'],'mixed_second_residues':top['mixed_to_q_second_residues'],'horizontal_lifts':top['horizontal_fiber_lifts'],'disposition':'survives algebraic/de Rham and orientation gates'}],'survivor':'top-sector triple logarithmic residue','why_nonredundant':'Unlike the soft endpoint and infinity candidates, it simultaneously has a source-oriented geometric boundary, the exact odd mixed vector (1,-1), and horizontal denominator lifts.','not_yet_claimed':'physical Betti pairing and integral normalization onto v_alg','next_action':'Construct the Leray tube of the oriented top-sector triple section and evaluate its induced mixed covector before marked-extension projection.','checks':checks,'passed':True}
d=R/'research/voevodsky/results/two_ended_valg_physical_candidate_census.json';d.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'survivor':out['survivor'],'mixed':top['mixed_to_q_second_residues']}))
