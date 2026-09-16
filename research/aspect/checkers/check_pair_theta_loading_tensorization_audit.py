#!/usr/bin/env python3
import json
from pathlib import Path
R=Path(__file__).resolve().parents[3]
x=json.loads((R/'research/aspect/results/pair_theta_loading_tensorization_audit.v1.json').read_text())
riesz=(R/'research/conjecture_replay/contracts/CR1-weighted-Riesz-U-theta-rad.candidate.v1.json').read_text()
pair=(R/'research/aspect/contracts/pair-theta-carrier.candidate.v1.json').read_text()
crossing=(R/'research/aspect/contracts/polarized-pair-to-bordered-radial-crossing.v1.json').read_text()
checks={
 'prime_power_domain_source':'e_(p,k), p prime, k>=1' in riesz,
 'pair_integer_labels_source':'(n,m)=(kb,ka)' in pair,
 'pair_realization_source':'Phi_(kb) tensor Phi_(ka)' in pair,
 'composite_scope_recognized':x['pair_data']['not_restricted_to_prime_powers'] is True,
 'conditional_unique':x['conditional_tensor_extension']['unique_after_premise'] is True,
 'embedding_missing':x['missing_premise']['status']=='not_constructed',
 'no_riesz_tensor_literal':'m_t tensor' not in riesz.lower(),
 'Ttheta_occurs_in_comparison':'T_theta tensor T_theta' in crossing,
 'four_inequivalent_choices':len(x['inequivalent_possible_extensions'])==4,
 'none_authorized':x['none_authorized_by_current_Riesz_packet'] is True,
 'pp_subcarrier_typeable':x['maximal_current_domain']['tensorization_typeable'] is True,
 'pp_not_exhaustive':x['maximal_current_domain']['global_ThetaPair_exhaustive'] is False,
 'pp_not_sufficient':x['maximal_current_domain']['sufficient_for_actual_shell_catalogue'] is False,
 'pair_map_open':x['claim_boundary']['pair_level_U_G4_constructed'] is False,
 'comparison_not_used':x['claim_boundary']['comparison_used_in_construction'] is False,
 'rh_not_promoted':x['claim_boundary']['rh_implication'] is False}
o={'schema':'marici.aspect.pair-theta-loading-tensorization-audit-check.v1','passed':all(checks.values()),'checks':checks,'verdict':'tensorization is canonical only after an owner-selected integer-to-prime-grade one-leg embedding; current prime-power subcarrier is nonexhaustive'}
(R/'research/aspect/results/pair_theta_loading_tensorization_audit.check.v1.json').write_text(json.dumps(o,indent=2)+'\n');print(json.dumps(o,indent=2));raise SystemExit(0 if o['passed'] else 1)
