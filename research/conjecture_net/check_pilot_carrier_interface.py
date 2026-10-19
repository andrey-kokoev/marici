"""Exact executable finite adapter audit; not programme or physical admission."""
import hashlib
from itertools import product
import json
from pathlib import Path
from pilot_carrier import (LABELS, Operation, Schedule, PathRecord, TickFragment,
                           Occurrence, promote, basis, native_permutation, label_index)
from check_structural_pilot_transport import identity, mul
from admit_structural_overlap import check as check_accepted_overlap

HOME = Path(__file__).resolve().parent
ROOT = HOME.parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate_contract(contract):
    require(contract['source_instance'] == 'native-bool-square-pilot', 'wrong adapter source')
    bindings = contract['primitive_bindings']
    require(len(bindings) == 8 and len({item['primitive'] for item in bindings}) == 8, 'incomplete primitive interface')
    boundary = contract['evidence_boundary']
    require(all(boundary[key] is False for key in ('new_adapter_kernel_proved', 'full_native_agda_tick_executed_in_python',
                'universal_carrier_embedding_proved', 'physical_source_selected', 'physical_readout_authorized',
                'programme_target_outcomes_promoted')), 'adapter verification overclaim')
    require(next(item for item in bindings if item['primitive'] == 'authorized_observer_interface')['status'] ==
            'mathematical_readout_only_no_physical_authorization', 'readout promotion')


def validate_dossier(dossier):
    source_contract = json.loads((HOME / 'contracts/programme-source-interface.v1.json').read_text())['source_record_contract']
    require(len(dossier['records']) == 8 and len({record['id'] for record in dossier['records']}) == 8,
            'source dossier occurrence coverage changed')
    require(not dossier['physical_data_inputs'] and not dossier['fitting_inputs'] and not dossier['held_out_data'],
            'new physical inputs require a scoped dossier review')
    for record in dossier['records']:
        require(set(source_contract['required_fields']) <= set(record), 'incomplete source provenance')
        require(record['role'] in source_contract['roles'], 'unknown provenance role')
        require(record['target_id'] in {'unitary-local-return-pilot', 'hamiltonian-symplectic-pilot'} and
                record['source_object'] == 'native-bool-square-pilot', 'source dossier scope mismatch')
        origin = record['origin']
        require(set(source_contract['origin_required_fields']) <= set(origin), 'incomplete source origin')
        path = (ROOT / origin['source_path_or_external_reference']).resolve()
        require(path.is_relative_to(ROOT), 'source origin escapes repository')
        require(hashlib.sha256(path.read_bytes()).hexdigest() == origin['integrity_or_version'], 'stale source origin')
        require(record['allowed_uses'] and record['forbidden_promotions'] and record['frozen_before'], 'missing source-use boundaries')


def record_audit():
    operations = tuple(Operation)
    words = [word for length in range(5) for word in product(operations, repeat=length)]
    paths = [PathRecord(source, word) for source in LABELS for word in words]
    expected = {
        Operation.LEFT: ((0, 0, 1, 0), (0, 0, 0, 1), (1, 0, 0, 0), (0, 1, 0, 0)),
        Operation.RIGHT: ((0, 1, 0, 0), (1, 0, 0, 0), (0, 0, 0, 1), (0, 0, 1, 0))}
    for operation in operations:
        require(native_permutation(operation) == expected[operation], 'native permutation convention mismatch')
    for path in paths:
        matrix = identity(4)
        for operation in path.operations:
            matrix = mul(native_permutation(operation), matrix)
        encoded = [matrix[row][label_index(path.source)] for row in range(4)]
        require(tuple(encoded) == basis(path.target), 'source/matrix action square failed')
        require(path.then(PathRecord(path.target, ())) == path and PathRecord(path.source, ()).then(path) == path,
                'path identity law failed')
        require(len(path.trace) == len(path.operations) + 1, 'trace retention failed')
    short = [path for path in paths if len(path.operations) <= 2]
    triples = 0
    for first in short:
        for second in short:
            if first.target != second.source:
                continue
            composed = first.then(second)
            require(composed.target == second.target and composed.trace == first.trace + second.trace[1:],
                    'composition attachment/trace law failed')
            for third in short:
                if second.target == third.source:
                    require(composed.then(third) == first.then(second.then(third)), 'associativity failed')
                    triples += 1
    hostile_left = PathRecord(LABELS[0], (Operation.LEFT, Operation.RIGHT))
    hostile_right = PathRecord(LABELS[0], (Operation.RIGHT, Operation.LEFT))
    require(hostile_left.target == hostile_right.target and hostile_left.structural_id != hostile_right.structural_id
            and hostile_left.trace != hostile_right.trace, 'endpoint quotient erased retained schedules')
    occurrences = tuple(Occurrence('occurrence-' + str(i), path) for i, path in enumerate(paths))
    occurrences += (Occurrence('equal-record-extra-occurrence', paths[0]),)
    for grouping_key in ('source', 'target'):
        families = promote(occurrences, grouping_key, 'audit-' + grouping_key)
        flattened = [member for family in families for member in family.members]
        require(sorted(flattened, key=lambda item: item.occurrence_id) == sorted(occurrences, key=lambda item: item.occurrence_id),
                'promotion lost occurrences or multiplicity')
        require(sum(len(family.members) for family in families) == len(occurrences), 'promotion created an independent product')
        for family in families:
            require(all(getattr(member.record, grouping_key) == family.key_value for member in family.members), 'family key mismatch')
    ticks = [TickFragment(source, first, second) for source in LABELS for first in Schedule for second in Schedule]
    for tick in ticks:
        require(TickFragment.rebuild(tick.source, tick.tags) == tick, 'tag reconstruction failed')
        require(tick.routes[0].target == tick.routes[1].target, 'compared native routes disagree')
        require(tick.swap().swap() == tick and tick.swap().seam_labels == tuple(reversed(tick.seam_labels)), 'schedule swap failed')
        require((tick.seam_labels[0] == tick.seam_labels[1]) == (tick.first == tick.second), 'seam/tag correspondence failed')
    for source in LABELS:
        at_source = [tick for tick in ticks if tick.source == source]
        require(len({tick.seam_labels for tick in at_source}) == len(at_source), 'fixed-source ordered-pair separation failed')
    return {'source_labels': 4, 'native_operations': 2, 'path_words_maximum_audited_length': 4,
            'path_records_audited': len(paths), 'composable_associativity_triples_audited': triples,
            'retained_occurrences_including_equal_record_duplicate': len(occurrences),
            'fixed_source_tick_tag_cases': len(ticks),
            'boundary': 'Exact finite executable controls; general composition follows the written tuple/trace argument, not a new kernel proof. Native Tick correspondence uses existing scoped formal evidence.'}


def main():
    contract_path = HOME / 'contracts/pilot-carrier-interface.v1.json'
    contract = json.loads(contract_path.read_text())
    validate_contract(contract)
    dossier_path = HOME / 'contracts/pilot-source-records.v1.json'
    validate_dossier(json.loads(dossier_path.read_text()))
    imported = check_accepted_overlap()
    controls = record_audit()
    paths = [contract_path, dossier_path, HOME / 'pilot_carrier.py', HOME / 'PILOT-CARRIER-INTERFACE.md', Path(__file__),
             ROOT / 'research/nima/agda/ObserverCoherenceCube.agda',
             ROOT / 'research/nima/agda/TickRetainedStructure.agda',
             ROOT / 'research/nima/tick-full-structure-classification.md']
    pins = {path.relative_to(ROOT).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest() for path in paths}
    result = {'schema': 'marici.conjecture-net.pilot-carrier-interface-audit.v1', 'status': 'pass',
              'validation_only': True, 'claim': contract['id'], 'outcome': None, 'root_outcome': None,
              'controls': controls, 'imported_finite_overlap': imported, 'source_sha256': pins,
              'new_adapter_kernel_proved': False, 'full_native_agda_tick_executed_in_python': False,
              'universal_carrier_embedding_proved': False, 'physical_readout_authorized': False,
              'programme_target_outcomes_promoted': False}
    destination = HOME / 'results/pilot-carrier-interface-audit.json'
    destination.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps({key: result[key] for key in ('status', 'outcome', 'universal_carrier_embedding_proved')}, indent=2))


if __name__ == '__main__':
    main()
