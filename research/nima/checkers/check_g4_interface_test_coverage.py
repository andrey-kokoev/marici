"""Check that the fixture audit accounts for every proposed field, law, and hostile case."""
import json
from pathlib import Path
ROOT=Path('research/nima')
contract=json.loads((ROOT/'contracts/g4-radial-interface-candidate.v1.json').read_text())
required_fields={'radial_carrier','radial_source_map','radial_feature_map','radial_codiagonal','radial_recovery','cycle_policy','green_form','green_radical','return_map'}
required_laws={'source_typing','reciprocal_covariance','kernel_sequence','state_recovery','green_range_nondegeneracy','quotient_projection_compatibility','projective_continuity'}
expected_hostiles=9
field_coverage=required_fields <= set(contract)
law_coverage=required_laws == set(contract['laws'])
existing=json.loads((ROOT/'results/g4-radial-interface-conformance.json').read_text())
hostile_coverage=existing['hostile_count']==expected_hostiles and all(existing['hostile_results'].values())
proof_bearing={
 'source_typing':False,'reciprocal_covariance':False,'kernel_sequence':False,
 'state_recovery':False,'green_range_nondegeneracy':False,
 'quotient_projection_compatibility':False,'projective_continuity':False,
}
# Deliberate failure: literal law presence must not count as a proved law.
assert all(k in contract['laws'] for k in proof_bearing)
assert not any(proof_bearing.values())
assert field_coverage and law_coverage and hostile_coverage
out={'schema':'marici.g4-interface-test-coverage.v1','status':'passed_with_proof_gap',
 'field_requirements_accounted':len(required_fields),'law_requirements_accounted':len(required_laws),
 'required_hostiles_rejected':expected_hostiles,'proof_bearing_laws':proof_bearing,
 'first_false_positive_path':'literal declarations pass while no source map or commuting/exactness/rank witness is evaluated',
 'claim_boundary':'complete field and hostile-fixture coverage is not mathematical radial-G4 conformance'}
(ROOT/'results/g4-interface-test-coverage.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
