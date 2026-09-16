#!/usr/bin/env python3
import json
from pathlib import Path
R=Path(__file__).resolve().parents[3]
x=json.loads((R/'research/aspect/results/iota_pair_theta_determinacy_audit.v1.json').read_text())
pair=(R/'research/nima/every-completed-theta-pair-shell-is-a-product-weighted-ratio-translate-of-one-base-correlation-kernel.md').read_text()
cat=(R/'research/voevodsky/actual_consecutive_prime_fixed_ratio_grade_and_reflection_20260912.md').read_text()
riesz=(R/'research/conjecture_replay/contracts/CR1-weighted-Riesz-U-theta-rad.candidate.v1.json').read_text()
checks={
 'product_grade_source':'ell_\\Sigma' in pair,
 'ratio_grade_source':'ell_\\Delta' in pair,
 'swap_changes_ratio':'ell_\\Delta\\longmapsto-\\ell_\\Delta' in pair,
 'consecutive_prime_index':'A source edge is therefore indexed by \\((j,k)\\)' in cat,
 'reflection_crosses_blocks':'between the \\(D\\) and \\(-D\\) blocks' in cat,
 'single_leg_basis':'e_(p,k), p prime, k>=1' in riesz,
 'missing_pair_labels':set(x['candidate_target_structure']['labels_not_intrinsic'])=={'ordered_pair','consecutive-prime shell','ratio block','slot orientation'},
 'nonunique':x['information_obstruction']['uniqueness'] is False,
 'four_collapses':len(x['nonunique_unapproved_collapses'])==4,
 'two_repairs':len(x['minimal_repair_options'])==2,
 'enlargement_recommended':x['recommended_repair']=='pair_theta_enlargement',
 'authority_required':all(r['authority_required'] for r in x['minimal_repair_options']),
 'rh_not_promoted':x['rh_implication'] is False}
o={'schema':'marici.aspect.iota-pair-theta-determinacy-audit-check.v1','passed':all(checks.values()),'checks':checks,'verdict':'pair labels do not determine a map to the single-leg prime-grade basis; pair-level target enlargement or owner incidence is required'}
(R/'research/aspect/results/iota_pair_theta_determinacy_audit.check.v1.json').write_text(json.dumps(o,indent=2)+'\n');print(json.dumps(o,indent=2));raise SystemExit(0 if o['passed'] else 1)
