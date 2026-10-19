"""Validate the endpoint-role branch without promoting metadata to physics."""
import hashlib
import json
from pathlib import Path
from check_marked137_endpoint_audit import audit, validate_contract, SOURCE_PATHS, CONTRACT
from check_programme_source_overlap import validate as validate_previous

HOME = Path(__file__).resolve().parent
ROOT = HOME.parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate(hierarchy, receipt):
    old = json.loads((HOME / 'contracts/programme-hierarchy.v12.json').read_text())
    previous = validate_previous(old, json.loads((HOME / 'results/source-overlap-screen-audit.json').read_text()))
    require(hierarchy['phase'] == 'marked137_endpoint_roles_and_partial_readout', 'wrong endpoint audit phase')
    for key in ('root', 'obligations', 'admitted_prerequisite_links', 'promotion_policy', 'conditional_control_screens',
                'retained_source_bridges', 'shared_finite_structural_recipe', 'cross_source_overlap_screens'):
        require(hierarchy[key] == old[key], 'programme scope/outcome changed: ' + key)
    branches = hierarchy['source_endpoint_audits']
    require(len(branches) == 1, 'unexpected endpoint audit count')
    branch = branches[0]
    require(branch['proof_bearing'] is False and branch['discharges_parent_obligation'] is False and
            branch['full_response_descent'] is False and branch['readout_is_invertible_connector'] is False and
            branch['intended_T9_selected'] is False and branch['physical_readout_authorized'] is False,
            'endpoint observer promoted to a constructor/physical bridge')
    require((branch['carrier_target_keys'], branch['assembly_target_keys'], branch['parent153_marked137_overlap'],
             branch['partial_endpoint_readouts']) == (32, 1, 130, 145), 'endpoint role/domain findings changed')
    require(hierarchy['endpoint_role_binding_gate']['authority_only_branch_actionable'] is False, 'waiting branch made actionable')
    validate_contract(json.loads(CONTRACT.read_text()))
    require(receipt['status'] == 'pass' and receipt['validation_only'] is True and receipt['outcome'] is None and
            receipt['root_outcome'] is None, 'endpoint proof-outcome promotion')
    require(all(receipt[key] is False for key in ('original_sources_and_results_regenerated', 'new_kernel_theorem_proved',
                'physical_readout_authorized', 'programme_outcomes_promoted')), 'endpoint verification upgrade')
    required = SOURCE_PATHS + [CONTRACT, HOME / 'check_marked137_endpoint_audit.py', HOME / 'marked137_endpoint_audit.py']
    for path in required:
        require(receipt['source_sha256'].get(path.relative_to(ROOT).as_posix()) == hashlib.sha256(path.read_bytes()).hexdigest(),
                'missing/stale endpoint input: ' + str(path))
    for path, expected in receipt['source_sha256'].items():
        source = (ROOT / path).resolve()
        require(source.is_relative_to(ROOT) and not Path(path).is_absolute(), 'endpoint source escapes repository')
        require(hashlib.sha256(source.read_bytes()).hexdigest() == expected, 'stale endpoint source: ' + path)
    require(receipt['controls'] == audit(), 'live endpoint audit changed')
    require(previous['root_outcome'] is None, 'previous programme outcome changed')
    return {'status': 'pass', 'validation_only': True, 'endpoint_role_grouping_counts': [32, 1],
            'parent153_marked137_overlap': 130, 'partial_endpoint_readouts': 145,
            'response_level_transport': False, 'intended_T9_selected': False, 'root_outcome': None}


if __name__ == '__main__':
    hierarchy = json.loads((HOME / 'contracts/programme-hierarchy.v13.json').read_text())
    receipt = json.loads((HOME / 'results/marked137-endpoint-audit.json').read_text())
    print(json.dumps(validate(hierarchy, receipt), indent=2))
