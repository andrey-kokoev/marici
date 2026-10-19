"""Validate a source-response obstruction without a physical/graded promotion."""
import hashlib
import json
from pathlib import Path
from check_joint_defect_audit import audit, validate_contract, SOURCE_PATHS, CONTRACT
from check_programme_endpoint_roles import validate as validate_previous

HOME = Path(__file__).resolve().parent
ROOT = HOME.parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate(hierarchy, receipt):
    old = json.loads((HOME / 'contracts/programme-hierarchy.v13.json').read_text())
    previous = validate_previous(old, json.loads((HOME / 'results/marked137-endpoint-audit.json').read_text()))
    require(hierarchy['phase'] == 'joint_defect_interface_and_response_noncollapse', 'wrong joint-defect phase')
    for key in ('root', 'obligations', 'admitted_prerequisite_links', 'promotion_policy', 'conditional_control_screens',
                'retained_source_bridges', 'shared_finite_structural_recipe', 'cross_source_overlap_screens',
                'source_endpoint_audits', 'endpoint_role_binding_gate'):
        require(hierarchy[key] == old[key], 'programme scope/outcome changed: ' + key)
    branches = hierarchy['joint_defect_interfaces']
    require(len(branches) == 1, 'unexpected joint interface count')
    branch = branches[0]
    require((branch['id'], branch['contract'], branch['implementation'], branch['receipt'], branch['admission_status']) ==
            ('joint-assembly-family-defect-audit-v1', 'research/conjecture_net/contracts/joint-defect-audit.v1.json',
             'research/conjecture_net/joint_defect_audit.py', 'research/conjecture_net/results/joint-defect-audit.json',
             'not_admitted_as_new_programme_proof_link'), 'joint interface provenance/admission changed')
    require(branch['source_stratum'] == 'rational comparison-chain coefficients on the137 bound source slot labels',
            'joint coefficient source stratum changed')
    require(branch['proof_bearing'] is False and branch['discharges_parent_obligation'] is False and
            branch['chain_map_constructed'] is False and branch['physical_preparations_authorized'] is False
            and branch['intended_T9_selected'] is False, 'joint coefficients promoted beyond their source stratum')
    require((branch['joint_rank'], branch['joint_kernel_dimension'], branch['frozen_response_completion_rank'],
             branch['uniform_source_response_minimum_linear_rank']) == (55, 82, 56, 137), 'joint response interface changed')
    require(branch['status'] == 'joint_structural_sewing_conjecture_falsified_by_unchanged_source', 'falsification silently absorbed')
    validate_contract(json.loads(CONTRACT.read_text()))
    require(receipt['status'] == 'pass' and receipt['validation_only'] is True and receipt['outcome'] is None and
            receipt['root_outcome'] is None, 'joint proof-outcome promotion')
    require(receipt['governing_conjecture_falsified'] is True, 'joint hostile relabelled as sewing proof')
    require(all(receipt[key] is False for key in ('new_kernel_theorem_proved', 'physical_preparations_authorized',
                'programme_outcomes_promoted', 'shared_sources_and_results_regenerated')), 'joint verification upgrade')
    required = SOURCE_PATHS + [CONTRACT, HOME / 'check_joint_defect_audit.py', HOME / 'joint_defect_audit.py',
                              HOME / 'marked137_endpoint_audit.py', HOME / 'source_overlap_screen.py',
                              HOME / 'exchange_source_bridge.py', HOME / 'pilot_carrier.py']
    for path in required:
        require(receipt['source_sha256'].get(path.relative_to(ROOT).as_posix()) == hashlib.sha256(path.read_bytes()).hexdigest(),
                'missing/stale joint-defect input: ' + str(path))
    for path, expected in receipt['source_sha256'].items():
        source = (ROOT / path).resolve()
        require(source.is_relative_to(ROOT) and not Path(path).is_absolute(), 'joint source escapes repository')
        require(hashlib.sha256(source.read_bytes()).hexdigest() == expected, 'stale joint source: ' + path)
    require(receipt['controls'] == audit() and previous['root_outcome'] is None, 'live joint defect audit changed')
    return {'status': 'pass', 'validation_only': True, 'joint_structural_rank': 55, 'joint_kernel_dimension': 82,
            'frozen_response_completion_rank': 56, 'uniform_source_response_minimum_linear_rank': 137,
            'governing_sewing_conjecture': 'falsified', 'chain_map_constructed': False, 'root_outcome': None}


if __name__ == '__main__':
    hierarchy = json.loads((HOME / 'contracts/programme-hierarchy.v14.json').read_text())
    receipt = json.loads((HOME / 'results/joint-defect-audit.json').read_text())
    print(json.dumps(validate(hierarchy, receipt), indent=2))
