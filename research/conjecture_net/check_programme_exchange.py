"""Validate the second sourced structural instance, not a unified physical source."""
import hashlib
import json
from pathlib import Path
from check_exchange_source_bridge import audit, live_source_pins, validate_contract
from check_programme_controls import validate as validate_previous

HOME = Path(__file__).resolve().parent
ROOT = HOME.parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate(hierarchy, receipt):
    old = json.loads((HOME / 'contracts/programme-hierarchy.v10.json').read_text())
    previous = validate_previous(old, json.loads((HOME / 'results/pilot-control-screen.json').read_text()))
    require(hierarchy['phase'] == 'constructed_retained_exchange_metric_bridge', 'wrong exchange phase')
    for key in ('root', 'obligations', 'admitted_prerequisite_links', 'promotion_policy', 'conditional_control_screens'):
        require(hierarchy[key] == old[key], 'programme scope/outcome changed: ' + key)
    bridges = hierarchy['retained_source_bridges']
    require(len(bridges) == 1, 'unexpected retained-source bridge count')
    bridge = bridges[0]
    require(bridge['proof_bearing'] is False and bridge['discharges_parent_obligation'] is False and
            bridge['physical_source_bridge'] == 'not_supplied' and bridge['cross_source_common_physical_witness'] == 'not_proved'
            and bridge['free_global_control_switching'] == 'not_supplied', 'structural source bridge promoted beyond scope')
    contract = json.loads((HOME / 'contracts/exchange-source-bridge.v1.json').read_text())
    validate_contract(contract)
    require(bridge['source_instance'] == contract['source_instance'] and bridge['target_carrier'] == contract['target']['carrier'],
            'source/target bridge mismatch')
    require(receipt['status'] == 'pass' and receipt['validation_only'] is True and receipt['outcome'] is None
            and receipt['root_outcome'] is None, 'exchange proof-outcome promotion')
    require(all(receipt[key] is False for key in ('new_kernel_spectral_bridge_proved',
                'physical_source_instrument_bridge_proved', 'freely_switchable_six_port_controls_authorized',
                'same_physical_witness_as_bool_source_proved', 'programme_outcomes_promoted')), 'exchange verification upgrade')
    for path, expected in receipt['source_sha256'].items():
        source = (ROOT / path).resolve()
        require(source.is_relative_to(ROOT) and not Path(path).is_absolute(), 'source escapes repository')
        require(hashlib.sha256(source.read_bytes()).hexdigest() == expected, 'stale exchange bridge source: ' + path)
    require(all(receipt['source_sha256'].get(path) == expected for path, expected in live_source_pins().items()),
            'exchange input evidence closure changed')
    require(receipt['controls'] == audit() and receipt['previous_control_validation'] == previous, 'exchange audit changed')
    recipe = hierarchy['shared_finite_structural_recipe']
    require(recipe['instances'] == ['native-bool-square-pilot', 'conditional-six-port-retained-exchange'] and
            recipe['one_common_physical_witness'] is False and recipe['cross_source_transport_maps'] is None,
            'shared grammar promoted to common physical witness')
    return {'status': 'pass', 'validation_only': True, 'scoped_structural_instances': 2,
            'retained_exchange_source_dimension': 22, 'active_metric_unitary_dimension': 6,
            'physical_source_bridge': False, 'cross_source_witness_maps': False,
            'free_global_control_switching': False, 'root_outcome': None}


if __name__ == '__main__':
    hierarchy = json.loads((HOME / 'contracts/programme-hierarchy.v11.json').read_text())
    receipt = json.loads((HOME / 'results/exchange-source-bridge-audit.json').read_text())
    print(json.dumps(validate(hierarchy, receipt), indent=2))
