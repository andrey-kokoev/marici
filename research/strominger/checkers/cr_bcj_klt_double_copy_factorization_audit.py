#!/usr/bin/env python3
"""Audit locally sourced BCJ/KLT data against the CR-to-Bondi factorization contract."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
load=lambda p:json.loads((ROOT/p).read_text())
cr=load('nima/results/arbitrary-m-coherent-resolution.json')
bcj=load('nima/results/six-point-nmhv-bcj-chain-relation.json')
color=load('nima/results/six-point-chy-full-color-dressing.json')
proj=load('nima/results/little_group_graviton_projector.json')
orient=load('nima/results/helicity_double_copy_orientation_gate.json')
soft=load('nima/results/arbitrary-n-exact-soft-family.json')
carrier=load('nima/results/carrier_gravitational_soft_double_copy_gate.json')
checks={
 'finite_CR_exact':cr.get('passed',False),
 'soft_family_exact':soft['passed'],
 'six_point_BCJ_forms_vanish':bcj['assertions']['all_24_bcj_component_forms_zero'],
 'six_point_BCJ_raw_CR_chains_do_not_vanish':not bcj['assertions']['any_raw_chain_relation'],
 'six_point_BCJ_PT_dressed_CR_chains_do_not_vanish':not bcj['assertions']['any_parke_taylor_dressed_chain_relation'],
 'full_color_DDM_dressing_exists':color['status']=='passed',
 'abstract_graviton_projector_exists':proj['status']=='PASS' and proj['idempotent'] and proj['rank']==2,
 'projector_requires_typed_sector_projection':orient['remaining_gate'].startswith('derive the graviton projector/state pairing'),
 'CR_compatible_Jacobi_numerators_exist':False,
 'second_gauge_copy_on_CR_exists':False,
 'typed_two_copy_state_pairing_on_CR_exists':False,
 'Bondi_chain_map_exists':False,
}
out={
 'schema':'marici.strominger.cr-bcj-klt-double-copy-factorization-audit.v1',
 'status':'passed',
 'disposition':'partial factorization only; first missing arrow retained',
 'factorization':[
  {'arrow':'CR_SYM -> BCJ/Jacobi-enriched CR','status':'obstructed','evidence':'BCJ identities vanish after canonical-form/worldsheet evaluation, but all 24 raw and Parke-Taylor-dressed six-point CR chains remain nonzero. No cubic-graph Jacobi numerator n_i with n_i+n_j+n_k=0 is assigned functorially to CR generators.'},
  {'arrow':'BCJ copy x BCJ copy -> gravity states','status':'not constructed','evidence':'Full-color DDM/CHY dressing supplies color structure, not a second kinematic numerator copy or KLT bilinear on CR chains.'},
  {'arrow':'two-copy states -> graviton sector','status':'constructed only abstractly','evidence':'Pi_grav=(h1+h2)^2/4=diag(1,0,0,1) is an exact rank-two parity-natural little-group projector, but no sourced CR state pairing feeds it.'},
  {'arrow':'gravity amplitudes -> Bondi radiative complex','status':'not constructed','evidence':'Current soft family supplies momentum kinematics only; no normalization to C_AB/N_AB, radiative symplectic form, or Bondi differential is intertwined with CR.'}],
 'what_current_sources_do_construct':{
  'BCJ':'six-point amplitude/worldsheet quotient identities and full-color DDM basis independence',
  'KLT':'local citations and inverse/pairing structures, but no sourced gravitational KLT image of the NNMHV CR',
  'state_projector':'abstract helicity-square graviton projector on basis (++,+-,-+,--)',
  'soft_kinematics':'exact momentum-conserving epsilon-soft family with nonzero hard limit'},
 'first_missing_arrow':'CR_SYM -> CR_BCJ: a CR-compatible cubic-graph numerator assignment satisfying kinematic Jacobi and commuting with the CR differential.',
 'why_not_bypass':'Amplitude-level BCJ vanishing is downstream of the CR chain obstruction; squaring evaluated planar weights would import a comparison-side prescription and would not prove differential compatibility.',
 'required_next_witness':{
  'minimum':'At six points, assign a Jacobi numerator vector to every relevant CR generator and exhibit matrices F_k with d_BCJ F_k = F_(k-1) d_CR.',
  'hostile_test':'All 24 fundamental BCJ combinations must vanish as enriched chains, not only after canonical-form evaluation.',
  'then':'Construct a second copy, pair states, apply Pi_grav, and verify that the resulting soft mode maps to Bondi news with the frozen BMS normalization.'},
 'checks':checks,
 'claim_boundary':'This audit does not deny standard amplitude-level double copy. It shows that current local sources do not construct the requested CR-compatible double-copy chain map.'}
(ROOT/'strominger/results/cr_bcj_klt_double_copy_factorization_audit.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
