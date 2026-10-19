"""Validate a scoped overlap obstruction/package without promoting unification."""
import hashlib
import json
from pathlib import Path
from check_source_overlap_screen import audit, validate_contract
from check_programme_exchange import validate as validate_previous

HOME = Path(__file__).resolve().parent
ROOT = HOME.parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate(hierarchy, receipt):
    old_path = HOME / 'contracts/programme-hierarchy.v11.json'
    old_receipt_path = HOME / 'results/exchange-source-bridge-audit.json'
    old = json.loads(old_path.read_text())
    previous = validate_previous(old, json.loads(old_receipt_path.read_text()))
    require(hierarchy['phase'] == 'restricted_overlap_screen_and_indexed_package', 'wrong overlap phase')
    for key in ('root', 'obligations', 'admitted_prerequisite_links', 'promotion_policy', 'conditional_control_screens',
                'retained_source_bridges', 'shared_finite_structural_recipe'):
        require(hierarchy[key] == old[key], 'programme scope/outcome changed: ' + key)
    screens = hierarchy['cross_source_overlap_screens']
    require(len(screens) == 1, 'unexpected overlap screen count')
    screen = screens[0]
    require(screen['proof_bearing'] is False and screen['discharges_parent_obligation'] is False and
            screen['cross_source_identification'] == 'not_constructed' and screen['one_common_physical_witness'] == 'not_proved'
            and screen['cross_component_arrows'] == 'not_supplied', 'indexed package promoted to physical unification')
    require(screen['indexed_package_dimension'] == 26 and screen['package_role'] == 'faithful_isometric_source_indexed_alternatives'
            and screen['status'] == 'all_36_global_single_port_bindings_nonfaithful', 'overlap package role/result changed')
    require(screen['bounded_typed_loop_screen'] == {'maximum_word_length': 12, 'closed_nonempty_word_count': 840,
                'faithful_fixed_fibre_native_flip_candidates': 0}, 'bounded overlap horizon changed')
    contract_path = HOME / 'contracts/source-overlap-screen.v1.json'
    validate_contract(json.loads(contract_path.read_text()))
    require(receipt['status'] == 'pass' and receipt['validation_only'] is True and receipt['outcome'] is None
            and receipt['root_outcome'] is None, 'overlap proof-outcome promotion')
    require(all(receipt[key] is False for key in ('cross_source_identification_constructed', 'one_common_physical_witness_proved',
                'cross_component_coupling_derived', 'word_or_endpoint_dependent_bindings_ruled_out',
                'physical_source_instrument_bridge_proved', 'programme_outcomes_promoted')), 'overlap verification upgrade')
    required = [old_path, old_receipt_path, contract_path, HOME / 'check_source_overlap_screen.py', HOME / 'source_overlap_screen.py',
                HOME / 'pilot_carrier.py', HOME / 'check_programme_exchange.py', HOME / 'SOURCE-OVERLAP-SCREEN.md']
    for path in required:
        require(receipt['source_sha256'].get(path.relative_to(ROOT).as_posix()) == hashlib.sha256(path.read_bytes()).hexdigest(),
                'missing/stale overlap source: ' + str(path))
    for path, expected in receipt['source_sha256'].items():
        source = (ROOT / path).resolve()
        require(source.is_relative_to(ROOT) and not Path(path).is_absolute(), 'source escapes repository')
        require(hashlib.sha256(source.read_bytes()).hexdigest() == expected, 'stale overlap source: ' + path)
    require(receipt['controls'] == audit() and receipt['previous_exchange_validation'] == previous, 'overlap audit changed')
    return {'status': 'pass', 'validation_only': True, 'global_single_port_assignments': 36,
            'typed_closed_words_through_length_12': 840, 'faithful_overlap_found_in_screen': False,
            'faithful_indexed_package_dimension': 26, 'cross_source_identification': False,
            'one_common_physical_witness': False, 'all_word_bindings_ruled_out': False, 'root_outcome': None}


if __name__ == '__main__':
    hierarchy = json.loads((HOME / 'contracts/programme-hierarchy.v12.json').read_text())
    receipt = json.loads((HOME / 'results/source-overlap-screen-audit.json').read_text())
    print(json.dumps(validate(hierarchy, receipt), indent=2))
