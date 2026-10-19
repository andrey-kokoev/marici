"""Validate the complete mathematical-probe subbranch, not a detector or actuator."""
import hashlib
import json
from pathlib import Path
from check_programme_capabilities import validate as validate_previous
from check_pilot_observer_extension import audit, validate_contract

HOME = Path(__file__).resolve().parent
ROOT = HOME.parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate(hierarchy, receipt):
    old = json.loads((HOME / 'contracts/programme-hierarchy.v8.json').read_text())
    previous = validate_previous(old, json.loads((HOME / 'results/pilot-capability-audit.json').read_text()))
    require(hierarchy['phase'] == 'constructed_complete_finite_mathematical_probes', 'wrong observer phase')
    for key in ('root', 'obligations', 'admitted_prerequisite_links', 'capability_audits', 'promotion_policy'):
        require(hierarchy[key] == old[key], 'programme scope/outcome changed: ' + key)
    extensions = hierarchy['mathematical_observer_extensions']
    require(len(extensions) == 1, 'unexpected observer extension count')
    extension = extensions[0]
    require(extension['source_instance'] == 'native-bool-square-pilot' and extension['proof_bearing'] is False
            and extension['discharges_parent_obligation'] is False
            and extension['physical_observer_authorization'] == 'not_supplied', 'observer branch promoted beyond scope')
    validate_contract(json.loads((HOME / 'contracts/pilot-observer-extension.v1.json').read_text()))
    require(receipt['status'] == 'pass' and receipt['validation_only'] is True and receipt['outcome'] is None
            and receipt['root_outcome'] is None, 'observer outcome promotion')
    require(all(receipt[key] is False for key in ('physical_observers_authorized', 'new_controls_supplied',
            'new_kernel_observer_theorem', 'infinite_completion_stability_proved', 'programme_outcomes_promoted')),
            'observer verification upgrade')
    for path, expected in receipt['source_sha256'].items():
        source = (ROOT / path).resolve()
        require(source.is_relative_to(ROOT) and not Path(path).is_absolute(), 'source escapes repository')
        require(hashlib.sha256(source.read_bytes()).hexdigest() == expected, 'stale observer source: ' + path)
    require(receipt['controls'] == audit() and receipt['previous_capability_validation'] == previous, 'observer audit changed')
    require(extension['hermitian_observation_rank'] == receipt['controls']['hermitian_observation_rank'], 'observer rank mismatch')
    require(all(fork['status'] == 'candidate' and fork['outcome'] is None for fork in hierarchy['candidate_synthesis_forks']),
            'physical synthesis fork promoted by mathematical construction')
    return {'status': 'pass', 'validation_only': True, 'mathematical_observation_rank': 16,
            'physical_observers_authorized': False, 'continuous_control_dimension': 2,
            'root_outcome': None, 'programme_parent_obligation_discharged': False}


if __name__ == '__main__':
    hierarchy = json.loads((HOME / 'contracts/programme-hierarchy.v9.json').read_text())
    receipt = json.loads((HOME / 'results/pilot-observer-extension-audit.json').read_text())
    print(json.dumps(validate(hierarchy, receipt), indent=2))
