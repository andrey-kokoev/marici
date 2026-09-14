#!/usr/bin/env python3
"""Test the formal endpoint/soft identity against the sourced coordinate t=xi+1."""
import json
from fractions import Fraction
from pathlib import Path
R=Path(__file__).resolve().parents[3];B=R/'research/benincasa'
formal=json.loads((R/'research/voevodsky/results/endpoint_to_base_soft_formal_comparison.json').read_text())
cycle=json.loads((B/'soft-endpoint-full-a-cycle-compatibility.json').read_text())
grade=json.loads((B/'soft-endpoint-relative-cone-grade.json').read_text())
stokes=json.loads((B/'soft-endpoint-stokes-cospan.json').read_text())
# Domain order (+1,-1), codomain order (t=0,t=2). t=xi+1 induces swap.
S=[[0,1],[1,0]];gamma=stokes['boundary_map']['column']
def mv(A,v):return [sum(A[i][j]*v[j] for j in range(2)) for i in range(2)]
push=mv(S,gamma)
checks={'formal_candidate_identity':formal['unique_integral_solution']==[[1,0],[0,1]],'sourced_coordinate_is_t_xi_plus_one':all(Fraction(row['t'])==Fraction(row['xi'])+1 for row in cycle['exact_cycle_packets']),'sourced_label_map_is_swap':S==[[0,1],[1,0]],'sourced_push_reverses_target_generator':push==[-1,1],'identity_assignment_conflicts_with_coordinate_map':formal['unique_integral_solution']!=S,'ports_need_weight_three_transition':grade['p_homogeneous_degrees']['difference']==3,'transition_unconstructed':'unconstructed' in grade['required_transition']}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.endpoint-to-base-soft-label-falsifier.v1','sourced_coordinate':'t=xi+1','domain_order':['xi=+1','xi=-1'],'codomain_order':['t=0','t=2'],'induced_matrix':S,'stokes_boundary':gamma,'induced_boundary':push,'target_generator':[1,-1],'formal_identity_assignment_status':'rejected','orientation_note':'The induced boundary is the negative generator, which alone is harmless under global orientation reversal. The decisive conflict is that the sourced map is the swap rather than the formally assumed identity; moreover the two ports differ by p-weight three, so a label permutation is not the required Gysin comparison.','result':'The proposed identity comparison is not source-derived. The explicit base coordinate reverses its label assignment and does not supply the missing degree-three off-diagonal transition.','remaining_route':'Compute a genuine weight-three Gysin transition from the moving a-cycle pushforward. Without it, the Stokes cone cannot define the logarithmic physical readout.','checks':checks,'passed':True}
d=R/'research/voevodsky/results/endpoint_to_base_soft_label_falsifier.json';d.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'formal':'rejected','sourced_matrix':S,'boundary':push,'weight_gap':3}))
