#!/usr/bin/env python3
"""Replay the sourced physical Cut pair in the primitive e6 Betti basis."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[3]
comp=json.loads((R/'research/benincasa/results/rank12-e6-parity-occurrence-composition.json').read_text())
bet=json.loads((R/'research/benincasa/results/rank12-e6-local-betti-lattice.json').read_text())
sat=json.loads((R/'research/benincasa/results/rank12-e6-global-integral-saturation.json').read_text())
loc=json.loads((R/'research/benincasa/et-cut-nearby-normal-form.json').read_text())
F=comp['occurrence_forgetting_matrix'];S=comp['sheet_parity_matrix']
def mv(A,v):return [sum(A[i][j]*v[j] for j in range(len(v))) for i in range(len(A))]
# q_G12 physical residue has the two lower occurrences (12|23),(12|31).
q12_pair=[1,1,0,0,0,0]
sheet=mv(S,q12_pair);forgot=mv(F,sheet)
# Each target rational generator g_j is rho_e6; eta_j=4*g_j is primitive Betti.
eta_coords=[v//4 for v in forgot]
checks={'two_lower_occurrences_per_cut':q12_pair[:2]==[1,1] and sum(q12_pair)==2,'sheet_difference_factor_two':sheet==[-2,-2,0,0,0,0],'occurrence_pair_factor_four':forgot==[-4,0,0],'local_Betti_index_four':bet['comparison']=='rho_e6=(1/4)*eta','global_source_index_four':sat['source_line_in_saturated_frame']=='4*Z*g','integral_eta_coordinate_unit':eta_coords==[-1,0,0],'physical_interval_primitive':loc['canonical_boundary_vector']==[-1,1],'v_alg_tail_zero':loc['exceptional_period_functional_e1_to_e9'][6:]==[0,0,0]}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.C1-integral-e6-replay.v1','source_cut':'q_G12','occurrence_basis':comp['occurrence_order'],'physical_occurrence_pair':q12_pair,'stage_one_sheet_parity':sheet,'stage_two_occurrence_forgetting':forgot,'primitive_Betti_basis_relation':'eta_j=4*g_j=4*rho_e6,j','primitive_Betti_output':eta_coords,'mod_two_output':[abs(eta_coords[0])%2,0],'result':'The sourced two-occurrence q_G12 physical current maps to minus one primitive e6 Betti generator and zero v_alg coordinate.','C1_original_four_mark_statement':'remains rejected; its four-mark Cech support is a different global coefficient-side object.','C1_replacement':'confirmed: the physical single-Cut occurrence pair has multiplicity one in the primitive e6 Betti lattice.','physical_parity':[1,0],'checks':checks,'passed':True}
(R/'research/voevodsky/results/C1_integral_e6_replay.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'pair':q12_pair,'sheet':sheet,'forgotten':forgot,'Betti':eta_coords,'replacement_C1':out['C1_replacement'],'parity':out['physical_parity']}))
