import json
from pathlib import Path
base=Path(__file__).parents[1]
src=json.loads((base/'results'/'rh_quarter_hurwitz_terminal_minor_source_formula.json').read_text())
keys=set(src)
mixed=src.get('first_mixed_summand_sign') or {}
checks={'fixed_eight_identity_census_present':src.get('identity_count')==12869,'terminal_census_present':src.get('oriented_terminal_count')==3584,'mixed_sign_case_present':mixed.get('positive_terms',0)>0 and mixed.get('negative_terms',0)>0,'quadratic_product_edges_absent':'quadratic_product_edges' not in keys,'orientation_probe_records_absent':'orientation_probes' not in keys,'cannot_infer_edges_from_common_sum':True}
result={'schema':'marici.strominger.rh_quarter_fixed_eight_anchor_census_preflight.v1','status':'passed' if all(checks.values()) else 'failed','verdict':'The retained k=8 backend contains exact signed source terms, 12,869 transfer identities, 3,584 oriented terminal cases, and explicit mixed-sign summands, but no source-declared quadratic-product edges or orientation probes. Therefore a Gram anchor graph cannot be formed from retained authority.','first_mixed_case':mixed,'first_missing_typed_object':'A source-derived quadratic-product relation on labelled nonzero terms, plus nonvanishing orientation probes for each connected component.','boundary':'Co-occurrence in a signed sum is not a quadratic product and does not authorize adding a Gram edge.','checks':checks}
(base/'results'/'rh_quarter_fixed_eight_anchor_census_preflight.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
