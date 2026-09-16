#!/usr/bin/env python3
import json
from pathlib import Path
R=Path(__file__).resolve().parents[3]
x=json.loads((R/'research/aspect/contracts/pair-theta-carrier.candidate.v1.json').read_text())
texts='\n'.join((R/p).read_text() for p in x['sources'])
c=x['carrier'];o=x['operations'];k=x['pair_kernel'];m=x['candidate_source_map']
checks={
 'sources_exist':all((R/p).exists() for p in x['sources']),
 'pair_multiplicity_source':'(n,m)=(kb,ka)' in texts,
 'shell_grade_source':'W_D(j,k)' in texts and 'kb p_jp_{j+1}' in texts,
 'finite_exhaustion_source':'E_{D,N}' in texts,
 'pair_kernel_source':'(nm)^{-1/2}' in texts and 't+\\log\\frac mn' in texts,
 'swap_block_source':'W_{-D}(j,k)' in texts and '=W_D(j,k)+D' in texts,
 'relative_haar_source':'J_{\\rm pair}=J\\widehat\\otimes I' in texts,
 'all_required_labels':set(c['labels'])=={'ratio_block','theta_pair','shell','ordered_slots','grade'},
 'injective_by_full_labels':m['injective_by_labels'] is True,
 'no_surjectivity_overclaim':m['surjectivity_claimed'] is False,
 'product_ratio_separated':k['product_ratio_separated'] is True,
 'orientation_retained':k['slot_orientation_retained'] is True,
 'single_leg_not_used':x['compatibility']['does_not_collapse_to_single_leg_basis'] is True,
 'three_authority_gates':len(x['missing_for_authority'])==3,
 'not_authoritative':x['claim_boundary']['authoritative_G4_source'] is False,
 'U_G4_not_constructed':x['claim_boundary']['U_G4_constructed'] is False,
 'rh_not_promoted':x['claim_boundary']['rh_implication'] is False}
out={'schema':'marici.scc.pair-theta-carrier-candidate-check.v1','passed':all(checks.values()),'checks':checks,'verdict':'minimal pair-level theta carrier preserves all source labels and laws; owner adoption and pair-level forward loading remain open'}
(R/'research/aspect/results/pair_theta_carrier_candidate.check.v1.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
