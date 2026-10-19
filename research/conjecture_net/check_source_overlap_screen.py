"""Restricted overlap obstruction and faithful package; no physical admission."""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
from source_overlap_screen import fixed_port_bindings, bounded_typed_loop_screen, packaged_sources, native_characters, tag_record, restore_record, validate_indexed_word
from exchange_source_bridge import ROOT, identity, zeros, add, scale, mul, transpose, block_diagonal, spectral, complex_mul, adjoint, ExecutionLedger
from pilot_carrier import Operation, native_permutation, Occurrence, PathRecord
from check_programme_exchange import validate as validate_previous

HOME = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate_contract(contract):
    require(all(value is False for value in contract['boundary'].values()), 'overlap boundary promotion')
    screen = contract['fixed_port_screen']
    require(screen['ordered_assignments'] == 36 and screen['distinct_port_assignments'] == 30 and screen['same_port_assignments'] == 6,
            'fixed-port screen coverage changed')
    require(screen['distinct_port_maximum_map_rank'] == 1 and screen['same_port_maximum_map_rank'] == 2 and screen['faithful_map_found'] is False,
            'restricted overlap result changed')
    loop_screen = contract['bounded_typed_loop_screen']
    require(loop_screen['maximum_word_length'] == 12 and loop_screen['base_vertices'] == ['A', 'B', 'C', 'D'] and
            loop_screen['closed_nonempty_word_count'] == 840 and loop_screen['negative_eigenspace_dimension_counts'] == {'0': 520, '1': 320}
            and loop_screen['minimum_negative_dimension_needed_for_native_flip'] == 2
            and loop_screen['faithful_fixed_fibre_native_flip_candidates'] == 0, 'bounded loop screen scope/result changed')
    require(contract['indexed_package']['dimension'] == 26 and contract['indexed_package']['carrier'] == 'C4 direct_sum C22',
            'source package domain changed')
    require(contract['indexed_package']['cross_component_executable_word'] == 'rejected; no such sourced arrow has been supplied',
            'unsupported cross-source arrow')


def audit():
    characters = native_characters()
    hadamard = transpose(list(characters.values()))
    require(mul(transpose(hadamard), hadamard) == scale(4, identity(4)), 'source character basis incomplete')
    pl, pr = (native_permutation(operation) for operation in Operation)
    for signs, vector in characters.items():
        column = [[value] for value in vector]
        require(mul(pl, column) == scale(signs[0], column) and mul(pr, column) == scale(signs[1], column),
                'source character eigenvalue mismatch')
    assignments = fixed_port_bindings()
    loops = bounded_typed_loop_screen()
    require(loops['closed_nonempty_word_count'] == 840 and loops['negative_eigenspace_dimension_counts'] == {'0': 520, '1': 320}
            and loops['faithful_fixed_fibre_native_flip_candidates'] == 0, 'typed loop spectrum changed')
    package = packaged_sources()
    metric = package['metric']
    bool_j, exchange_j = package['injections']['bool'], package['injections']['exchange']
    model = package['exchange_model']
    require(mul(mul(transpose(bool_j), metric), bool_j) == identity(4), 'Bool inclusion not isometric')
    require(mul(mul(transpose(exchange_j), metric), exchange_j) == model['raw_metric'], 'exchange inclusion not isometric')
    require(mul(transpose(bool_j), exchange_j) == zeros(4, 22), 'source blocks not disjoint')
    require(add(mul(bool_j, transpose(bool_j)), mul(exchange_j, transpose(exchange_j))) == identity(26), 'source coordinates lost')
    source_operators = {('bool', operation.value): [list(row) for row in native_permutation(operation)] for operation in Operation}
    source_operators.update({('exchange', label): operator for label, operator in model['raw'].items()})
    for key, operator in package['operations'].items():
        component = key[0]
        injection = package['injections'][component]
        require(mul(operator, injection) == mul(injection, source_operators[key]), 'packaged action square failed')
        require(mul(operator, operator) == identity(26) and mul(mul(transpose(operator), metric), operator) == metric,
                'packaged metric involution failed')
        quarter = spectral(operator, F(0), F(-1))
        require(complex_mul(adjoint(quarter), complex_mul((metric, zeros(26)), quarter)) == (metric, zeros(26)),
                'packaged metric spectral control failed')
        require(complex_mul(quarter, quarter) == (operator, zeros(26)), 'packaged spectral endpoint composition failed')
    # The general composition identity follows directly from the block rule.
    for a in Operation:
        for b in Operation:
            require(mul(package['operations'][('bool', a.value)], package['operations'][('bool', b.value)]) ==
                    block_diagonal(mul(native_permutation(a), native_permutation(b)), identity(22)), 'Bool composition transport failed')
    for first, second in (('AB', 'BC'), ('AD', 'DB')):
        require(mul(package['operations'][('exchange', second)], package['operations'][('exchange', first)]) ==
                block_diagonal(identity(4), mul(model['raw'][second], model['raw'][first])), 'exchange composition transport failed')
    # All coordinate quadratic forms transport by inclusion; this is not a
    # physical instrument or cross-source readout calibration.
    readouts = 0
    for component, injection in package['injections'].items():
        size = len(injection[0])
        for coordinate in range(size):
            form = zeros(size)
            form[coordinate][coordinate] = F(1)
            extension = mul(mul(injection, form), transpose(injection))
            require(mul(mul(transpose(injection), extension), injection) == form, 'quadratic readout pullback failed')
            readouts += 1
    native_record = Occurrence('overlap-screen-example', PathRecord((False, False), (Operation.LEFT, Operation.RIGHT)))
    ledger = ExecutionLedger()
    _, exchange_records = ledger.execute(('AB', 'BC', 'CA'), [0] * 22, model['raw'], model['ports'], 'screen-example', 'A')
    require(restore_record(tag_record('bool', native_record), 'bool') is native_record, 'native record changed')
    require(all(restore_record(tag_record('exchange', record), 'exchange') is record for record in exchange_records), 'exchange record changed')
    validate_indexed_word((('bool', 'left'), ('bool', 'right')))
    validate_indexed_word((('exchange', 'AB'), ('exchange', 'BC')))
    try:
        validate_indexed_word((('bool', 'left'), ('exchange', 'AB')))
    except ValueError:
        pass
    else:
        raise ValueError('invented cross-source executable word')
    return {'fixed_port_assignments': assignments, 'fixed_port_assignment_count': 36,
            'bounded_typed_loop_screen': loops,
            'faithful_fixed_port_overlap_found': False, 'package_dimension': 26,
            'isometric_source_inclusion_count': 2, 'packaged_metric_involution_count': 8,
            'coordinate_quadratic_pullbacks': readouts, 'source_records_retained': True,
            'cross_component_executable_word_supplied': False,
            'cross_source_transport_map_constructed': False, 'one_common_physical_witness_proved': False,
            'obstruction_scope': 'Global fixed-fibre single-port assignments only; not word-valued or endpoint-dependent bindings.'}


def main():
    contract_path = HOME / 'contracts/source-overlap-screen.v1.json'
    validate_contract(json.loads(contract_path.read_text()))
    old_hierarchy_path = HOME / 'contracts/programme-hierarchy.v11.json'
    old_receipt_path = HOME / 'results/exchange-source-bridge-audit.json'
    previous = validate_previous(json.loads(old_hierarchy_path.read_text()), json.loads(old_receipt_path.read_text()))
    controls = audit()
    old_receipt = json.loads(old_receipt_path.read_text())
    pins = dict(old_receipt['source_sha256'])
    for path in (contract_path, old_hierarchy_path, old_receipt_path, Path(__file__), HOME / 'source_overlap_screen.py',
                 HOME / 'pilot_carrier.py', HOME / 'check_programme_exchange.py', HOME / 'SOURCE-OVERLAP-SCREEN.md'):
        pins[path.relative_to(ROOT).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    require(all(hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == expected for path, expected in pins.items()), 'overlap inputs changed during audit')
    receipt = {'schema': 'marici.conjecture-net.source-overlap-screen-audit.v1', 'status': 'pass',
               'validation_only': True, 'outcome': None, 'root_outcome': None, 'source_sha256': pins,
               'controls': controls, 'previous_exchange_validation': previous,
               'cross_source_identification_constructed': False, 'one_common_physical_witness_proved': False,
               'cross_component_coupling_derived': False, 'word_or_endpoint_dependent_bindings_ruled_out': False,
               'physical_source_instrument_bridge_proved': False, 'programme_outcomes_promoted': False}
    (HOME / 'results/source-overlap-screen-audit.json').write_text(json.dumps(receipt, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps({'status': 'pass', 'fixed_port_assignments': 36, 'faithful_overlap_found': False,
                      'typed_closed_words_through_length_12': 840, 'faithful_loop_flip_candidates': 0,
                      'faithful_indexed_package_dimension': 26, 'common_physical_witness': False}, indent=2))


if __name__ == '__main__':
    main()
