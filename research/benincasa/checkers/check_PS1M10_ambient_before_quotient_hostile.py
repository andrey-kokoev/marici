#!/usr/bin/env python3
"""SCC reduction-order hostile: compare full images before the common e6 quotient."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
lay=json.loads((R/'full-rank12-cut-nearby-layers-certificate.json').read_text())
cmp=json.loads((R/'results/PS1M9_current_level_nearby_comparison.json').read_text())
phys=json.loads((R/'three-cut-relative-chain-pairing-certificate.json').read_text())
assert lay['logarithmic_algebraic_rank']==3
assert lay['cut_nearby_algebraic_rank']==3
assert lay['combined_rank']==5 and lay['intersection_rank']==1
assert lay['intersection_generator']=='e6' and not lay['strict_equality_of_algebraic_images']
assert cmp['resolution']=='++'
assert phys['six_occurrence_relative_boundary_pairing']==[0]*6
out={'schema':'marici.benincasa.PS1M10-ambient-before-quotient-hostile.v1','prospective_action':'PS1M10_compare_complete_ambient_images_before_e6_reduction','resolution':'++','ambient_invariants':{'logarithmic_rank':3,'cut_nearby_rank':3,'combined_rank':5,'intersection_rank':1,'intersection_generator':'e6','images_equal':False},'quotient_result':'PS1M9 equality holds only after projection to the common e6 line','hostile_verdict':'The common-quotient comparison is nonfaithful: two rank-three ambient images intersect in only one line. Therefore quotient equality cannot be promoted to equality of realizations.','physical_status':'The cut-nearby ambient candidate is not a second physically typed realization because its literal positive-chain six-occurrence boundary pairing is zero.','moduli_update':{'established_realizations':1,'compatible_unactivated_candidates':1,'uniqueness_proved':False,'multiplicity_proved':False},'next_falsifier':'Supply a source-authorized relative chain activating a non-e6 nearby component (e3 or e5); its nonzero pairing would produce a typed second realization distinguishable from PS1A before quotient.','passed':True}
(R/'results/PS1M10_ambient_before_quotient_hostile.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
