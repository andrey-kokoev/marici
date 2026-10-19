"""Pinned local export of accepted mixed closure; never silently advance a head.

--check validates the existing pointer, including external/compiler pins, without
publishing or regenerating evidence. Consumers must use this live check as well
as outcome_reference.resolve, which only checks repository-local artifacts.
"""
from pathlib import Path
import argparse
import hashlib
import json
import subprocess
import sys

REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / 'research/conjecture_net'))
from outcome_reference import PORTS, SEMANTICS, file_hash, load, require, resolve

CONTRACT = 'research/nima/contracts/completion-refinement-conjecture-net.v1.json'
RESULT = 'research/nima/results/completion-refinement-conjecture-net.json'
ACCEPTED = 'research/nima/results/whole-return-mixed-level-accepted.json'
RECEIPT = 'research/nima/results/operational-whole-return-export-verification.json'
ADAPTER = 'research/nima/exports/operational-whole-return.source-adapter.v1.json'
HEAD = 'research/nima/exports/operational-whole-return.head.json'
POINTER = 'research/nima/exports/operational-whole-return.pointer.v1.json'
CLAIM = 'operational-spectral-whole-return-certificate'


def encode(value):
    return (json.dumps(value, indent=2, sort_keys=True) + '\n').encode()


def verify_external(receipt):
    require(bool(receipt['external_dependency_sha256']), 'missing external/compiler pins')
    for path, expected in receipt['external_dependency_sha256'].items():
        require(hashlib.sha256(Path(path).read_bytes()).hexdigest() == expected,
                'stale external/compiler evidence: ' + path)


def prepare():
    contract, result, accepted = (load(REPO, p) for p in (CONTRACT, RESULT, ACCEPTED))
    require(result['status'] == accepted['status'] == 'pass', 'unvalidated closure')
    require(result['target'] == accepted['claim'] == CLAIM, 'wrong target')
    require(result['net_state'] == 'positive_terminal' and result['target_outcome'] == '++',
            'target not positively terminal')
    expected = {'operational_kernel_bundle_proved': True,
                'standard_real_correspondence_written_proved': True,
                'semantic_correspondence_kernel_proved': False,
                'mixed_level_accepted': True, 'full_claim_proved_at_accepted_level': True,
                'C1_at_seam_claimed': False}
    require(all(accepted[k] == v for k, v in expected.items()), 'wrong accepted verification level')
    verify_external(accepted)
    pins = {}
    for evidence in (result, accepted):
        for path, digest in evidence['source_sha256'].items():
            require(file_hash(REPO, path) == digest, 'stale source/evidence: ' + path)
            require(path not in pins or pins[path] == digest, 'inconsistent evidence pin')
            pins[path] = digest
    for path in (CONTRACT, RESULT, ACCEPTED,
                 'research/nima/checkers/export_operational_whole_return.py',
                 'research/nima/checkers/check_completion_refinement_net.py',
                 'research/conjecture_net/outcome_reference.py'):
        pins[path] = file_hash(REPO, path)
    index = next(i for i, n in enumerate(contract['conjectures']) if n['id'] == CLAIM)
    node = contract['conjectures'][index]
    require(node['outcome'] == accepted['outcome'] == '++', 'wrong source outcome')
    require(node['scope_id'] == accepted['scope_id'], 'scope mismatch')
    require(contract['outcome_semantics'] == SEMANTICS, 'source outcome semantics mismatch')
    adapter = {'schema': 'marici.nima.outcome-export-source-adapter.v1',
               'source_contract': CONTRACT, 'source_contract_sha256': file_hash(REPO, CONTRACT),
               'source_node_pointer': f'/conjectures/{index}',
               'outcome_ports': PORTS, 'conjectures': [node],
               'boundary': 'Format adapter only; copies the validated source node without adding outcomes.'}
    adapter_payload = encode(adapter)
    pins[ADAPTER] = hashlib.sha256(adapter_payload).hexdigest()
    bindings = {key: f'/conjectures/0/{key}' for key in
                ('id', 'statement', 'scope_id', 'verification_level', 'acceptance')}
    claim = {key: node[key] for key in bindings}
    verification = dict(expected, proof_kind='operator_accepted_mixed_operational_kernel_and_written_standard_real_correspondence',
                        kernel_verified_analytic_theorem=False,
                        verification_level=accepted['verification_level'])
    receipt = dict(verification, schema='marici.nima.outcome-export-verification.v1', status='pass',
                   accepted_receipt=ACCEPTED, accepted_receipt_sha256=file_hash(REPO, ACCEPTED),
                   external_dependency_sha256=accepted['external_dependency_sha256'],
                   boundary='Verification-level adapter only; no new proof or acceptance.')
    receipt_payload = encode(receipt)
    pins[RECEIPT] = hashlib.sha256(receipt_payload).hexdigest()
    export = {
        'schema': 'marici.conjecture-net.outcome-export.v1',
        'export_id': 'nima.operational-whole-return.v1', 'head_path': HEAD,
        'outcome_semantics': SEMANTICS, 'outcome': '++', 'claim': claim, 'claim_bindings': bindings,
        'source': {'contract': ADAPTER, 'result': RESULT, 'node_pointer': '/conjectures/0',
                   'result_claim_pointer': '/target', 'result_outcome_pointer': '/target_outcome'},
        'verification_receipt': RECEIPT, 'verification': verification,
        'artifact_sha256': dict(sorted(pins.items())),
        'correction_policy': 'Drift or revocation blocks imports; corrections require a new export and explicit re-pinning.',
        'boundary': 'Fresh safe Agda operational laws plus operator-accepted written all-time correspondence. Not kernel semantic interpretation, seam C1, unique selection, Cubical pointwise decoding, or physics. External/compiler pins require the exporter --check live check.',
    }
    payload = encode(export)
    ref = {'path': 'research/nima/exports/operational-whole-return/' + hashlib.sha256(payload).hexdigest() + '.json',
           'sha256': hashlib.sha256(payload).hexdigest()}
    pointer = {'schema': 'marici.conjecture-net.outcome-pointer.v1', 'export': ref, 'head': HEAD,
               'expected_claim': claim, 'expected_outcome': '++', 'accepted_verification': verification}
    return payload, pointer, receipt_payload, adapter_payload


def check(pointer):
    resolved = resolve(REPO, pointer)
    export = load(REPO, pointer['export']['path'])
    verify_external(load(REPO, export['verification_receipt']))
    adapter = load(REPO, export['source']['contract'])
    require(adapter['source_contract'] == CONTRACT and
            adapter['source_contract_sha256'] == file_hash(REPO, CONTRACT), 'stale source adapter')
    from outcome_reference import at
    require(adapter['conjectures'][0] == at(load(REPO, CONTRACT), adapter['source_node_pointer']),
            'source adapter changed proposition/outcome')
    return resolved


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    if args.check:
        print(json.dumps(check(load(REPO, POINTER)), indent=2))
        return
    subprocess.run([sys.executable, str(REPO / 'research/nima/checkers/check_completion_refinement_net.py')],
                   cwd=REPO, check=True, stdout=subprocess.DEVNULL)
    payload, pointer, receipt_payload, adapter_payload = prepare()
    head = {'schema': 'marici.conjecture-net.outcome-head.v1', 'export_id': 'nima.operational-whole-return.v1',
            'status': 'active', 'export': pointer['export'], 'supersedes': None}
    artifacts = {HEAD: encode(head), POINTER: encode(pointer), RECEIPT: receipt_payload,
                 ADAPTER: adapter_payload, pointer['export']['path']: payload}
    # Preflight everything before writing; an existing head is never implicitly advanced.
    for path, content in artifacts.items():
        destination = REPO / path
        require(not destination.exists() or destination.read_bytes() == content,
                'Refusing implicit correction/overwrite: ' + path)
    for path, content in artifacts.items():
        destination = REPO / path
        destination.parent.mkdir(parents=True, exist_ok=True)
        if not destination.exists():
            destination.write_bytes(content)
    print(json.dumps(check(pointer), indent=2))


if __name__ == '__main__':
    main()
