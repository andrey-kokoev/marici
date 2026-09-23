"""Fail-closed typing audit of polyhedral selector certificates against NNMHV artifacts."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
N=ROOT/'research/nima'
def load(name):return json.loads((N/'results'/name).read_text())
def main():
 seed=load('nnmhv-positroid-seed.json');match=load('seven-point-history-parity-cell-matching.json');tail=load('nnmhv-long-exponent-two-limit.json');approx=load('selector-approximation-contract.json');compiled=load('seven-point-positroid-compiler.json');chart=load('seven-point-positive-chart.json');overlap=load('seven-point-chart-overlap.json');collapse=load('seven-point-triple-fibre-obstruction.json');repair=load('seven-point-zero-column-repair.json');wall=load('seven-point-repair-shared-wall.json');residue=load('seven-point-repair-wall-residue.json');third=load('seven-point-third-wall-residue.json');census=load('seven-point-repaired-fibre-census.json');polygon=load('seven-point-fibre-polygon-stress.json');multichamber=load('seven-point-multichamber-stress.json');fourfive=load('seven-point-four-five-wall.json');cycle=load('seven-point-local-six-cycle.json');facets=load('seven-point-fibre-facet-census.json');cyclic=load('seven-point-cyclic-fibre-reduction-probe.json');bounded=load('seven-point-cyclic-polygon-boundedness.json');extreme=load('seven-point-cyclic-extreme-stress.json');farkas=load('seven-point-cyclic-farkas-verification.json');chambers=load('seven-point-farkas-support-chambers-verification.json');decision=load('seven-point-cyclic-decision.json');curvature=load('eight-point-fibre-curvature.json');n9=load('nine-point-determinantal-fibre.json');support=load('nine-point-no-seven-support-packet-verification.json');padded=load('nine-point-seven-support-cell.json');exact_support=load('nine-point-minimum-eight-support-verification.json');paired_n9=load('nine-point-paired-cell-verification.json');form_n9=load('nine-point-paired-source-form.json');normal_n9=load('nine-point-zero-column-residue.json');push_n9=load('nine-point-paired-pushforward-samples-verification.json');algebraic_n9=load('nine-point-algebraic-target-local-pushforward-verification.json');branch_n9=load('nine-point-single-sheet-rationality-obstruction-verification.json');four_mass=load('nine-point-four-mass-source-match.json');auxiliary=load('nine-point-four-mass-auxiliary-match.json');psi_jac=load('nine-point-four-mass-psi-jacobian.json');psi_partition=load('four-mass-psi-universal-partition.json')
 assert seed['six_point_seed']['dimension']==8
 requests=seed['seven_point_cell_requests'];matches=match['matches'];assert len(requests)==len(matches)==6
 assert {x['history_index'] for x in requests}=={x['history_index'] for x in matches}==set(range(6))
 assert all(x['full_canonical_form_ratio']=='1' for x in matches)
 assert compiled['passed'] and len(compiled['cells'])==6 and chart['history_index']==0
 assert len(overlap['samples'])==2 and all(all(x['status']=='OUTSIDE_POSITIVE_CELL' for x in sample['candidate_fibres'][1:]) for sample in overlap['samples'])
 assert [x['history_index'] for x in collapse['rows']]==[1,3,5]
 assert [x['history_index'] for x in repair['rows']]==[1,3,5]
 assert all(not x['inverse_of_history_zero_sample_is_positive'] for x in repair['rows'])
 assert wall['inward_side']=='OPPOSITE' and residue['source_residue_ratio']=='1'
 assert third['source_residue_ratio']=='1' and [x['positive_image_count'] for x in census['cell_seed_rows']]==[1]*6
 assert polygon['membership_count_histogram']=={'1':160} and [r['members'] for r in polygon['sector_lifts']]==[[i] for i in range(6)]
 assert multichamber['membership_count_histogram']=={'open=1,closed=1':717,'open=0,closed=2':3} and len(multichamber['shared_wall_witnesses'])==3
 assert fourfive['inward_side']=='OPPOSITE' and fourfive['source_residue_ratio']=='1'
 assert cycle['passed'] and len(cycle['edges'])==6
 assert facets['tested']==245 and len(facets['never_edge_in_samples'])==14
 assert cyclic['passed_samples']==350 and cyclic['nonadmitted_target_negative_control']['full_positive_fibre_empty']
 assert bounded['passed'] and bounded['single-weight-deletion_rejections']==7
 assert extreme['tested']==14000 and extreme['first_admitted_target_counterexample'] is None
 assert farkas['passed'] and farkas['whole_fibre_noncyclic_implications']==98
 assert chambers['passed'] and len(chambers['cases'])==2
 assert decision['passed'] and len(decision['admitted_cases'])==7 and decision['unadmitted_control']['verdict']=='CYCLIC_INSUFFICIENT'
 assert curvature['passed'] and curvature['ordered_minor_12']=='7a+b+ab' and curvature['boundary_midpoint_minor_12']!='0'
 assert n9['passed'] and n9['symbolic_affine_minor_identities']==36 and n9['spurious_relaxed_lift']['violates_realizability']
 assert padded['passed'] and padded['source_dimension']==8 and support['passed'] and support['seven_support_subsets_excluded']==36
 assert exact_support['passed'] and exact_support['minimum_label_support']==8 and exact_support['upper_retained_minors_checked']==28
 assert paired_n9['passed'] and paired_n9['full_image_rank']==8 and paired_n9['matched_pair_constraints']==4
 assert form_n9['passed'] and normal_n9['passed'] and normal_n9['oriented_residue_ratio_to_eight_column_top_form']=='1'
 assert push_n9['passed'] and push_n9['exact_local_pushforward_samples']==2
 assert algebraic_n9['passed'] and algebraic_n9['independent_pluecker_differential_stress']
 assert branch_n9['passed'] and branch_n9['nonsquare_discriminant_specialization'] and branch_n9['unequal_rational_sheet_specializations']==2
 assert four_mass['passed'] and auxiliary['passed'] and auxiliary['alpha_and_beta_source_equations_vanish_mod_graph_quadratic']
 assert psi_jac['passed'] and psi_jac['jacobian_and_psi_denominators_coprime_to_graph_quadratic']
 assert psi_partition['passed'] and psi_partition['two_simple_solution_prefactors_sum_to_one']
 assert tail['model']=='S_n=L+c2/n^2+c3/n^3' and len(tail['families'])>=2
 ref=approx['reference'];assert len(approx['scope'])==6 and len(ref['source_lifts'][0])==3
 gates={
  'common_fixed_projection':{'status':'MISSING','reason':'Six-point top G_+(2,6) and seven-point history/canonical-form matches do not provide a single affine source-to-public projection shared across n.'},
  'positive_cell_compiler':{'status':'THREE_OF_SIX_COLLAPSE','reason':'Three original triple-parallel carriers collapse under CZ. Their adjacent-minor equations also admit a zero-middle-column branch with full image dimension, but matching that branch to the corresponding physical history form has not been established.'},
  'common_refinement_overlap':{'status':'LOCAL_FIBRE_SEPARATION_ONLY','reason':'For one positive moment-curve Z, two exact points in the history-zero chart have no positive lift in the other five compiled charts. This is local separation, not global coverage or n-to-n+1 refinement.'},
  'uniform_norm_and_rate':{'status':'MISSING','reason':'The n^-2 record is a fitted scalar full-history component on selected kinematic families, not a uniform-in-n bound in a norm of canonical forms on a fixed domain.'},
  'existing_selector_certificate':{'status':'PRESENT_BUT_DIFFERENT_TYPE','reason':'A rational three-atom polygon section has whole-domain infinity error, but is not a map into G(2,6) and is not a rational differential canonical form.'}}
 assert all(x['status']=='MISSING' for k,x in gates.items() if k not in ('existing_selector_certificate','positive_cell_compiler','common_refinement_overlap'))
 report={'schema':'marici.nima.nnmhv-selector-transfer-gate.v1','passed':True,'n6_dimension':8,'n7_matched_histories':len(matches),'n7_ratios_one':True,'selector_scope_vertices':len(approx['scope']),'selector_source_atoms':3,'fitted_tail_families':sorted(tail['families']),'gates':gates,'conclusion':'The fixed-target positive source fibre is an exact 21-halfspace polygon. Zero-column repairs pass image rank; three local walls pass orientation and source-residue checks; 160 top-source tests plus strict positive lifts for all six sectors have unique repaired membership. All six proposed local adjacency edges have opposite target inward directions and equal symbolic source residues. A separate 720-target six-gauge multichamber test finds three shared-wall targets with zero open but two closed memberships. A universal positive telescoping relation proves the seven-cyclic-halfspace fibre is compact whenever cyclic source minors are strictly positive. A 14,000-target adversarial probe finds no admitted counterexample to cyclic sufficiency, but an explicit unadmitted target refutes unrestricted sufficiency. Seven admitted targets have 98 independently replayed whole-fibre sparse Farkas identities. Two exact positive sources falsify previously stable fixed two-edge supports, while alternative supports still certify their noncyclic inequalities. A complete exact per-target primal/dual cyclic-fibre decision procedure now certifies seven admitted targets and rejects an unadmitted one. At n=8 an admitted positive target has a curved, nonpolyhedral source fibre, so the seven-point halfspace method does not extend verbatim. At n=9 all 36 source minors admit an exact affine determinantal lift, but ignoring its quadratic realizability equations produces fictitious positive witnesses. A fixed strictly positive nine-point target has exact MINIMUM source support eight: 36 Farkas exclusions below eight and one independently verified eight-label source witness. A minimum-eight-support four-pair candidate has an exact algebraic positive image point of full rank eight. The nine-point four-pair source form and zero-column normalization are exact; two rational CZ pushforwards AND a certified local algebraic pushforward at the minimum-eight target are exact, but the ONE-SHEET density is provably nonrational, so only the FULL TWO-SHEET TRACE or a cell sum could match a rational history; the EIGHT-POINT cell is source-identified as starred four-mass psi with BOTH kinematic branches matched and its psi prefactor equals the normalized inverse auxiliary Jacobian and its TWO sourced solution weights universally sum to one; its NINE-POINT generalized-R history, complete superform equality, global positive-cell compilation and uniform completion remain open.'}
 p=N/'results/nnmhv-selector-transfer-gate.json';p.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
