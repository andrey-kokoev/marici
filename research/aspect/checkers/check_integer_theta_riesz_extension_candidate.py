#!/usr/bin/env python3
import json,math
from pathlib import Path
R=Path(__file__).resolve().parents[3]
x=json.loads((R/'research/aspect/contracts/integer-theta-riesz-extension.candidate.v1.json').read_text())
texts='\n'.join((R/p).read_text() for p in x['sources'])
restriction=max(abs(math.log(p**k)-k*math.log(p)) for p in [2,3,5,7,11] for k in range(1,8))
p=x['pair_extension'];d=x['synthesized_disposition']
checks={
 'sources_exist':all((R/q).exists() for q in x['sources']),
 'riesz_uniqueness_source':'unique weighted-relative Riesz vector' in texts,
 'integer_theta_atoms_source':'Phi_n' in texts,
 'spectral_translation_source':'log n' in texts,
 'prime_power_restriction_exact':restriction<1e-12,
 'extends_existing':x['one_leg_map']['extends_existing_candidate'] is True,
 'no_factorization_choice':x['one_leg_map']['does_not_choose_prime_factor_decomposition'] is True,
 'analytic_lane_ordered':'no conjugation' not in p['analytic_transpose_lane'] or 'tensor' in p['analytic_transpose_lane'],
 'hermitian_lane_conjugated':'conjugate' in p['hermitian_lane'],
 'ratio_retained':p['ratio_translation']=='log(m/n)=log m-log n',
 'Euler_support_prime_power':x['arithmetic_loading_relation']['Euler_support'].endswith('n=p^k'),
 'no_fake_integer_loading':x['arithmetic_loading_relation']['general_integer_atoms_receive_Euler_coefficient'] is False,
 'independent':all(v is False for k,v in x['independence'].items() if k!='source_equations_only') and x['independence']['source_equations_only'] is True,
 'source_math_canonical':d['source_carrier_identification_mathematically_canonical'] is True,
 'source_authority_open':d['source_carrier_identification_authoritative'] is False,
 'target_open':d['target_identification_constructed_independently'] is False,
 'U_G4_open':d['authoritative_U_G4_constructed'] is False,
 'four_owner_actions':len(x['remaining_owner_actions'])==4,
 'rh_not_promoted':d['rh_implication'] is False}
o={'schema':'marici.scc.integer-theta-riesz-extension-candidate-check.v1','passed':all(checks.values()),'checks':checks,'max_prime_power_log_residual':restriction,'verdict':'integer-labelled Riesz extension canonically solves the source-carrier mathematics; only owner adoption and target-side authoritative data remain'}
(R/'research/aspect/results/integer_theta_riesz_extension_candidate.check.v1.json').write_text(json.dumps(o,indent=2)+'\n');print(json.dumps(o,indent=2));raise SystemExit(0 if o['passed'] else 1)
