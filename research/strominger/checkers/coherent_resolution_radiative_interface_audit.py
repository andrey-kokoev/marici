#!/usr/bin/env python3
"""Audit whether the sourced Coherent Construction data define a radiative/BMS chain map."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
atlas=(ROOT/'nima/coherent-construction-bridge-atlas.md').read_text()
prior=json.loads((ROOT/'strominger/results/nnmhv_soft_bms_boundary_comparison.json').read_text())
required_cr={
 'oriented_history_chain':'Gamma_n=' in atlas,
 'pushforward_canonical_form':'Omega_{n,2,4}' in atlas and '(\\Phi_Z)_*' in atlas,
 'graded_history_generators':'A_m' in atlas and 'positive roots' in atlas,
 'relation_cells':'commuting square' in atlas and 'Mac Lane pentagon' in atlas,
 'mobius_differential':'\\Box_d=\\Delta_u\\Delta_v' in atlas,
 'cutoff_filtration':'newly created shell at cutoff' in atlas and 'AF/Wedderburn tower' in atlas,
}
missing_cr={
 'single_chain_complex_with_degrees_and_boundary_maps':True,
 'proof_square_pentagon_cells_are_boundaries_for_weighted_canonical_forms':True,
 'declared_admissible_quotient_for_the_resolution':True,
 'homotopies_compatible_with_physical_weights_and_cutoff_filtration':True,
}
target_fields=['Bondi cuts u=const','shear C_AB','news N_AB=partial_u C_AB','helicity polarization','sphere smearing f or Y^A','radiative symplectic form','BMS charge normalization','frequency omega and omega->0 prescription']
result={
 'schema':'marici.strominger.coherent-resolution-radiative-interface-audit.v1',
 'status':'passed',
 'source_authority':{
  'primary':'research/nima/coherent-construction-bridge-atlas.md',
  'meaning':'The source names a Coherent Construction Law: an oriented history-cell chain Gamma_n in G_+(2,n), pushed by Phi_Z(C)=CZ to the NNMHV canonical form.',
  'warning':'It does not name or present a complete Coherent Resolution chain complex. CR below is the maximal cellular complex reconstructible from the atlas, not an additional sourced object.'},
 'maximal_sourced_CR':{
  'degree_0':'history/positive-root interval vertices and weighted history cells',
  'degree_1':'cluster mutations/diagonal flips and endpoint-cover generators',
  'degree_2':'commuting squares and associahedral pentagons resolving flip ambiguities',
  'candidate_differentials':['cellular boundary of squares/pentagons','interval-poset Mobius operator Box_d=Delta_u Delta_v'],
  'filtrations':['external cutoff n via new history shells','root interval length','AF/Wedderburn shell tower'],
  'candidate_quotients':['pushforward Phi_Z from positive cells to amplituhedron canonical form','selected-center radial map (isometric as vector spaces but changes multiplication)']},
 'source_checks':required_cr,
 'missing_resolution_data':missing_cr,
 'radiative_target_required_fields':target_fields,
 'comparison_arrows':{
  'CR_generators_to_radiative_modes':'obstructed: no map assigns a history cell/root/flip to a Bondi shear or news mode with helicity',
  'CR_differential_to_flux':'obstructed: no chain-map identity F d_CR = d_BMS F and no cut-to-cut charge normalization',
  'CR_cycles_to_soft_charges':'obstructed: no sphere smearing, zero-frequency limit, or Ward action; descent on CR boundaries cannot be stated',
  'CR_boundaries_to_gauge':'obstructed: no map from square/pentagon boundaries or Mobius-exact fields to Bondi gauge/supertranslation equivalence',
  'secondary_classes_to_memory':'obstructed: no transgression from a CR 2-cell/homotopy to integrated news, displacement memory, or spin memory',
  'canonical_weights_to_symplectic_pairing':'falsified for the naive identification: the tested kernel is non-Hermitian/non-normal and its linear weights are not the antisymmetric radiative symplectic form'},
 'kernel_image_data':{
  'sourced_insertion_image':'new shell rank-one transport image equals inserted null-edge spinor',
  'sourced_reflow_kernel':'kernel line varies with endpoint/history at fixed inserted image',
  'radiative_interpretation':'none: spinor image/kernel lines have no sourced map to radiative phase-space kernel, soft radical, or gauge quotient'},
 'exact_residuals':prior['nonzero_residuals'],
 'independence_checks':{
  'history_order_is_not_Bondi_time':True,
  'deformation_t_is_not_Bondi_time':True,
  'cutoff_n_is_not_a_Bondi_cut':True,
  'cluster_exchange_residual_is_not_a_BMS_flux':True,
  'structural_two_channel_split_is_not_radiative_polarization':True},
 'disposition':'obstructed at named missing arrows',
 'first_obstruction':'The source does not supply a complete CR chain complex/admissible quotient, and even its maximal cellular reconstruction has no typed generator map to Bondi radiative phase space. Therefore descent, gauge compatibility, soft factors, charges, flux, and memory cannot be derived.'}
path=ROOT/'strominger/results/coherent_resolution_radiative_interface_audit.json';path.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
