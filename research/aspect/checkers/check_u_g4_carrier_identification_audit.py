#!/usr/bin/env python3
import json
from pathlib import Path
R=Path(__file__).resolve().parents[3]
x=json.loads((R/'research/aspect/results/u_g4_carrier_identification_audit.v1.json').read_text())
searches={
 'pair':list(R.glob('research/**/*one_leg_relative_haar_tensor_constructs_the_pair_modular_colligation_20260908.md')),
 'riesz':list(R.glob('research/**/*CR1-weighted-Riesz-U-theta-rad.candidate.v1.json')),
 'crossing':list(R.glob('research/**/*the-polarized-pair-kernel-has-a-canonical-linear-crossing-to-the-bordered-radial-response.md'))}
texts={k:'\n'.join(p.read_text() for p in v) for k,v in searches.items()}
checks={
 'all_sources_unique':all(len(v)==1 for v in searches.values()),
 'J_pair_constructed':'J_{\\rm pair}=J\\widehat\\otimes I' in texts['pair'],
 'J_pair_domain_typed':'H_a\\widehat\\otimes\\overline{\\mathcal H_m}' in texts['pair'],
 'prime_grade_basis':'e_(p,k)' in texts['riesz'],
 'riesz_location':'t=k log p' in texts['riesz'],
 'no_pair_to_prime_basis_locator':not any('e_(p,k)' in texts[k] for k in ['pair','crossing']),
 'source_identification_absent':x['source_side']['identification_constructed'] is False,
 'target_identification_absent':x['target_side']['identification_constructed'] is False,
 'comparison_target_bridge_not_independent':x['target_side']['independence_status']=='comparison_side_only',
 'domains_not_shared':x['consequence']['maps_share_declared_domain'] is False,
 'codomains_not_shared':x['consequence']['maps_share_declared_codomain'] is False,
 'defect_not_typeable':x['consequence']['forward_defect_typeable'] is False,
 'next_source_constructor':x['minimal_next_constructor']['name']=='iota_pair_theta',
 'next_target_constructor':x['second_constructor_after_source']['name']=='iota_rad_border',
 'rh_not_promoted':x['rh_implication'] is False}
o={'schema':'marici.aspect.u-g4-carrier-identification-audit-check.v1','passed':all(checks.values()),'checks':checks,'verdict':'relative-Haar colligation and pair-to-border crossing exist, but neither supplies the two independent carrier identifications'}
(R/'research/aspect/results/u_g4_carrier_identification_audit.check.v1.json').write_text(json.dumps(o,indent=2)+'\n');print(json.dumps(o,indent=2));raise SystemExit(0 if o['passed'] else 1)
