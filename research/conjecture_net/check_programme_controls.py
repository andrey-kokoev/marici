"""Validate conditional control synthesis without physical source authorization."""
import hashlib
import json
from pathlib import Path
from check_pilot_control_screen import audit, validate_contract
from check_programme_observers import validate as validate_previous

HOME = Path(__file__).resolve().parent
ROOT = HOME.parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate(hierarchy, receipt):
    old = json.loads((HOME / 'contracts/programme-hierarchy.v9.json').read_text())
    previous = validate_previous(old, json.loads((HOME / 'results/pilot-observer-extension-audit.json').read_text()))
    require(hierarchy['phase'] == 'screened_conditional_control_source_extensions', 'wrong control phase')
    for key in ('root', 'obligations', 'admitted_prerequisite_links', 'mathematical_observer_extensions', 'promotion_policy'):
        require(hierarchy[key] == old[key], 'programme scope/outcome changed: ' + key)
    screens = hierarchy['conditional_control_screens']
    require(len(screens) == 1 and screens[0]['proof_bearing'] is False and screens[0]['discharges_parent_obligation'] is False
            and screens[0]['physical_source_selection'] == 'not_supplied'
            and screens[0]['phase_framing'] == 'assumed_not_physically_supplied', 'conditional controls promoted beyond scope')
    validate_contract(json.loads((HOME / 'contracts/pilot-control-screen.v1.json').read_text()))
    require(receipt['status'] == 'pass' and receipt['validation_only'] is True and receipt['outcome'] is None
            and receipt['root_outcome'] is None, 'control outcome promotion')
    require(all(receipt[key] is False for key in ('added_controls_physically_authorized',
            'added_controls_derived_from_native_flips', 'phase_framing_physically_supplied',
            'new_kernel_control_theorem', 'programme_outcomes_promoted')), 'control verification upgrade')
    for path, expected in receipt['source_sha256'].items():
        source = (ROOT / path).resolve()
        require(source.is_relative_to(ROOT) and not Path(path).is_absolute(), 'source escapes repository')
        require(hashlib.sha256(source.read_bytes()).hexdigest() == expected, 'stale control source: ' + path)
    require(receipt['controls'] == audit() and receipt['previous_observer_validation'] == previous, 'control screen changed')
    require(all(fork['status'] == 'candidate' and fork['outcome'] is None for fork in hierarchy['candidate_synthesis_forks']),
            'conditional algebra promoted to physical synthesis')
    require(all(bridge['status'] == 'candidate_not_constructed' and bridge['outcome'] is None
                for bridge in hierarchy['next_source_bridge_candidates']), 'unconstructed source bridge promoted')
    return {'status': 'pass', 'validation_only': True, 'conditional_u4_family_supplied': True,
            'physical_control_authorization': False, 'original_continuous_control_dimension': 2,
            'source_bridge_constructed': False, 'root_outcome': None}


if __name__ == '__main__':
    hierarchy = json.loads((HOME / 'contracts/programme-hierarchy.v10.json').read_text())
    receipt = json.loads((HOME / 'results/pilot-control-screen.json').read_text())
    print(json.dumps(validate(hierarchy, receipt), indent=2))
