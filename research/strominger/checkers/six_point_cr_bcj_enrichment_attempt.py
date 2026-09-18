#!/usr/bin/env python3
"""Exact six-point CR_BCJ enrichment attempt from existing sourced results."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
load=lambda p:json.loads((ROOT/p).read_text())
chains=load('nima/results/six-point-nmhv-bcj-chain-relation.json')
repair=load('nima/results/six-point-minimal-bcj-chain-repair.json')
quot=load('nima/results/six-point-bcj-quotient-rank.json')
world=load('nima/results/six-point-worldsheet-universal-quotient.json')
first=chains['relations'][0]
raw=first['raw_nonzero_cell_coefficients']; dressed=first['dressed_nonzero_cell_coefficients']
out={
 'schema':'marici.strominger.six-point-cr-bcj-enrichment-attempt.v1',
 'status':'obstructed',
 'scope':'six points at the existing exact rational fixture',
 'candidate_target':{
  'name':'ordering-level BCJ quotient Q6',
  'definition':'Q6 = V_DDM / B6, with dim(V_DDM)=24 and rank(B6)=18',
  'dimension':quot['quotient_dimension'],
  'degree_zero_map':'canonical quotient q: V_DDM -> Q6',
  'higher_chain_map':'not induced on the existing CR: the BCJ-weighted top chains have nonzero simplicial residue boundaries'},
 'numerator_attempt':{
  'available':'worldsheet quotient and inverse-pairing data can select amplitude-level BCJ-basis/master coefficient representatives',
  'failure':'no source labels these representatives by cubic graphs on each CR generator, fixes generalized gauge, or proves kinematic Jacobi generatorwise',
  'consequence':'they are evaluated amplitude coordinates, not Jacobi-satisfying numerator vectors defining F_k'},
 'exact_ranks':{
  'DDM_ordering_dimension':24,
  'BCJ_relation_rank':quot['rank'],
  'BCJ_quotient_dimension':quot['quotient_dimension'],
  'fundamental_BCJ_CR_top_chain_span':repair['ranks']['original_bcj_top_chain_span'],
  'residue_defect_span':repair['ranks']['residue_defect_span'],
  'corrected_cycle_span':repair['ranks']['corrected_bcj_cycle_span'],
  'repaired_H4_dimension':repair['ranks']['repaired_H4_dimension']},
 'first_nonzero_chain_residual':{
  'fundamental_permutation':first['permutation'],
  'evaluated_form_zero':first['canonical_form_component_residual_zero'],
  'raw_cell_coefficients':raw,
  'parke_taylor_dressed_cell_coefficients':dressed},
 'all_24_tests':{
  'evaluated_forms_zero':chains['assertions']['all_24_bcj_component_forms_zero'],
  'raw_enriched_chains_zero':chains['assertions']['any_raw_chain_relation'],
  'PT_dressed_enriched_chains_zero':chains['assertions']['any_parke_taylor_dressed_chain_relation']},
 'minimal_mapping_cone_repair':repair['minimal_extension'],
 'repair_provenance':{
  'source_forced_generators':0,
  'freely_adjoined_degree4_defect_lifts':repair['minimal_extension']['new_degree4_defect_lifts'],
  'freely_adjoined_degree5_null_homotopies':repair['minimal_extension']['new_degree5_null_homotopies'],
  'bridge_established':False,
  'reason':'The new generators are chosen as linear-algebraic defect bases; no cubic-graph, Jacobi, CHY cocycle, or CR relation-cell source identifies them.'},
 'chain_map_test':{
  'equation':'d_BCJ F_k = F_(k-1) d_CR',
  'degree0_ordering_quotient':'passes as a quotient of evaluated ordering data',
  'top_CR_degree':'fails before a sourced F_k exists; residue defect rank is 4',
  'all_24_vanish_before_evaluation':False},
 'downstream':'Second copy, state pairing, Pi_grav, epsilon-soft/Bondi tests are not activated because the first arrow fails.',
 'first_missing_datum':'A source-derived assignment of cubic-graph Jacobi numerators to CR generators, including generalized-gauge choice and boundary-compatible differential images for the rank-4 defect basis.'}
(ROOT/'strominger/results/six_point_cr_bcj_enrichment_attempt.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
