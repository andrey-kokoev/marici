"""Admit/export only the explicitly accepted finite structural prerequisite.

--check validates a retained export read-only, including live upstream evidence.
No new kernel closure or physical verification is claimed.
"""
import argparse
import hashlib
import json
from pathlib import Path
from check_programme_overlap import validate_contract, validate_attachment, coefficient_audit
from check_programme_transport import validate as validate_transport
from check_structural_pilot_transport import check_export, POINTER as OPERATIONAL_POINTER
from outcome_reference import SEMANTICS, PORTS, file_hash, load, require, resolve

HOME = Path(__file__).resolve().parent
ROOT = HOME.parents[1]
ACCEPTANCE = 'research/conjecture_net/contracts/structural-overlap-acceptance.v1.json'
NET = 'research/conjecture_net/contracts/finite-structural-overlap-net.v1.json'
RESULT = 'research/conjecture_net/results/finite-structural-overlap-accepted.json'
HEAD = 'research/conjecture_net/exports/finite-structural-overlap.head.json'
POINTER = 'research/conjecture_net/exports/finite-structural-overlap.pointer.v1.json'
CLAIM = 'finite-structural-same-witness-transport-and-readout-overlap'
EXPECTED = {
    'finite_same_witness_transport_supplied': True,
    'quadratic_readout_overlap_supplied': True,
    'written_general_coordinate_argument_supplied': True,
    'exact_rational_coefficient_controls_passed': True,
    'new_transport_kernel_proved': False,
    'semantic_correspondence_kernel_proved': False,
    'physical_readout_authorized': False,
    'empirical_confirmation': False,
    'universal_carrier_embedding_proved': False,
}


def encode(value):
    return (json.dumps(value, indent=2, sort_keys=True) + '\n').encode()


def validate_acceptance(acceptance):
    require(acceptance['accepted'] is True and acceptance['operator_instructions'] == ['yes', 'accept'], 'missing explicit acceptance')
    require(acceptance['claim'] == CLAIM and acceptance['scope_id'] == 'native-bool-spectral-complex-real-structural-overlap', 'acceptance scope mismatch')
    require(acceptance['accepted_verification'] == EXPECTED, 'acceptance verification overclaim')


def prepare():
    acceptance = load(ROOT, ACCEPTANCE)
    validate_acceptance(acceptance)
    net = load(ROOT, NET)
    require(net['outcome_ports'] == PORTS and net['outcome_semantics'] == SEMANTICS, 'wrong attempt-outcome semantics')
    node = net['conjectures'][0]
    require(len(net['conjectures']) == 1 and node['id'] == CLAIM and node['outcome'] == '++'
            and node['scope_id'] == acceptance['scope_id'], 'wrong admitted node')
    require(node['acceptance'] == ACCEPTANCE and node['attempts'] == [{'intent': 'prove', 'outcome': '++', 'receipt': RESULT}], 'unbound admission receipt')
    transport_audit = load(ROOT, 'research/conjecture_net/results/structural-pilot-transport-audit.json')
    transport = validate_transport(load(ROOT, 'research/conjecture_net/contracts/programme-hierarchy.v4.json'), transport_audit)
    overlap = load(ROOT, 'research/conjecture_net/contracts/programme-overlaps.v1.json')
    validate_contract(overlap)
    validate_attachment(load(ROOT, 'research/conjecture_net/contracts/programme-hierarchy.v5.json'),
                        load(ROOT, 'research/conjecture_net/contracts/programme-terms.v4.json'), overlap)
    overlap_audit = load(ROOT, 'research/conjecture_net/results/programme-overlap-audit.json')
    require(overlap_audit['status'] == 'pass' and overlap_audit['validation_only'] is True and overlap_audit['outcome'] is None
            and overlap_audit['root_outcome'] is None and overlap_audit['programme_proof_links_admitted'] == 0
            and overlap_audit['kernel_observable_transport_proved'] is False
            and overlap_audit['physical_readout_authorized'] is False
            and overlap_audit['empirical_confirmation'] is False, 'historical overlap audit overclaim')
    require(overlap_audit['coordinate_controls'] == coefficient_audit() and
            overlap_audit['live_transport_validation'] == transport, 'overlap audit controls changed')
    operational_pointer = load(ROOT, OPERATIONAL_POINTER)
    upstream = check_export(operational_pointer)
    upstream_export = load(ROOT, operational_pointer['export']['path'])
    upstream_receipt = load(ROOT, upstream_export['verification_receipt'])
    pins = {}
    def merge(items):
        for path, expected in items.items():
            require(file_hash(ROOT, path) == expected, 'stale admission evidence: ' + path)
            require(path not in pins or pins[path] == expected, 'inconsistent evidence pin')
            pins[path] = expected
    for artifact in (transport_audit, overlap_audit):
        merge(artifact['source_sha256'])
    merge(upstream_export['artifact_sha256'])
    for review_path in ('research/conjecture_net/reviews/programme-term-review.v1.json',
                        'research/conjecture_net/reviews/programme-source-target-review.v1.json'):
        review = load(ROOT, review_path)
        merge({item['source_path']: item['source_sha256'] for item in review['sources']})
    paths = acceptance['evidence'] + [ACCEPTANCE, NET, OPERATIONAL_POINTER,
        operational_pointer['export']['path'], operational_pointer['head']]
    paths += ['research/conjecture_net/' + path for path in (
        'admit_structural_overlap.py', 'outcome_reference.py', 'check_programme_overlap.py',
        'check_programme_transport.py', 'check_structural_pilot_transport.py',
        'check_programme_pilots.py', 'check_programme_review.py',
        'contracts/programme-hierarchy.v4.json', 'contracts/programme-hierarchy.v5.json',
        'contracts/programme-terms.v4.json', 'reviews/programme-term-review.v1.json',
        'reviews/programme-source-target-review.v1.json')]
    for path in paths:
        pins[path] = file_hash(ROOT, path)
    verification = dict(EXPECTED,
        proof_kind='operator_accepted_written_coordinate_transport_and_exact_algebra_with_live_mixed_operational_import',
        kernel_verified_analytic_theorem=False, verification_level=acceptance['accepted_level'])
    result = dict(verification, schema='marici.conjecture-net.finite-structural-overlap-accepted.v1',
        status='pass', claim=CLAIM, scope_id=node['scope_id'], target=CLAIM, target_outcome='++',
        intent='prove', outcome='++', net_state='positive_terminal', terminal=True,
        acceptance=ACCEPTANCE, imported_operational_evidence=upstream,
        programme_root_outcome=None, programme_pilot_outcomes_promoted=False,
        source_sha256=dict(sorted(pins.items())),
        external_dependency_sha256=upstream_receipt['external_dependency_sha256'],
        boundary='Accepted finite structural prerequisite only; original audits remain historical and unpromoted. No kernel coordinate proof, empirical success or universal carrier.')
    result_payload = encode(result)
    pins[RESULT] = hashlib.sha256(result_payload).hexdigest()
    claim_keys = ('id', 'statement', 'scope_id', 'verification_level')
    claim = {key: node[key] for key in claim_keys}
    export = {'schema': 'marici.conjecture-net.outcome-export.v1',
        'export_id': 'marici.finite-structural-overlap.v1', 'head_path': HEAD,
        'outcome_semantics': SEMANTICS, 'outcome': '++', 'claim': claim,
        'claim_bindings': {key: '/conjectures/0/' + key for key in claim_keys},
        'source': {'contract': NET, 'result': RESULT, 'node_pointer': '/conjectures/0',
                   'result_claim_pointer': '/target', 'result_outcome_pointer': '/target_outcome'},
        'verification_receipt': RESULT, 'verification': verification,
        'artifact_sha256': dict(sorted(pins.items())),
        'correction_policy': 'Drift or revocation blocks live imports; corrections require a new export and explicit consumer re-pinning.',
        'boundary': 'Scoped finite structural prerequisite, not physical recovery. Consumers must also run admit_structural_overlap.py --check for live external/compiler and upstream evidence.'}
    payload = encode(export)
    ref = {'path': 'research/conjecture_net/exports/finite-structural-overlap/' + hashlib.sha256(payload).hexdigest() + '.json',
           'sha256': hashlib.sha256(payload).hexdigest()}
    pointer = {'schema': 'marici.conjecture-net.outcome-pointer.v1', 'export': ref, 'head': HEAD,
               'expected_claim': claim, 'expected_outcome': '++', 'accepted_verification': verification}
    return result_payload, payload, pointer


def check():
    result_payload, payload, expected = prepare()
    pointer = load(ROOT, POINTER)
    require(pointer == expected, 'admission pointer changed')
    require((ROOT / RESULT).read_bytes() == result_payload, 'accepted receipt changed')
    require((ROOT / pointer['export']['path']).read_bytes() == payload, 'accepted export changed')
    return resolve(ROOT, pointer)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    if args.check:
        print(json.dumps(check(), indent=2))
        return
    result_payload, payload, pointer = prepare()
    head = {'schema': 'marici.conjecture-net.outcome-head.v1', 'export_id': 'marici.finite-structural-overlap.v1',
            'status': 'active', 'export': pointer['export'], 'supersedes': None}
    artifacts = {RESULT: result_payload, pointer['export']['path']: payload, POINTER: encode(pointer), HEAD: encode(head)}
    for path, content in artifacts.items():
        destination = ROOT / path
        require(not destination.exists() or destination.read_bytes() == content, 'Refusing implicit admission correction: ' + path)
    for path, content in artifacts.items():
        destination = ROOT / path
        destination.parent.mkdir(parents=True, exist_ok=True)
        if not destination.exists():
            destination.write_bytes(content)
    print(json.dumps(check(), indent=2))


if __name__ == '__main__':
    main()
