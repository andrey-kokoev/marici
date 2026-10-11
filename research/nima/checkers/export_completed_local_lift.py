"""Explicit first export of the completed local-lift net; never silently advance a head."""
from pathlib import Path
import hashlib
import json
import sys

REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / 'research/conjecture_net'))
from outcome_reference import SEMANTICS, file_hash, load, resolve

CONTRACT = 'research/nima/contracts/current-problem-conjecture-net.v1.json'
RESULT = 'research/nima/results/current-problem-conjecture-net.json'
RECEIPT = 'research/nima/results/spectral-whole-return.json'
HEAD = 'research/nima/exports/standard-local-lift.head.json'
CLAIM = 'source-derived-intermediate-locality-preserving-lift'

def prepare():
    contract, result, receipt = (load(REPO, p) for p in (CONTRACT, RESULT, RECEIPT))
    index = next(i for i, n in enumerate(contract['conjectures']) if n['id'] == CLAIM)
    node = contract['conjectures'][index]
    assert node['outcome'] == '++' and result['status'] == receipt['status'] == 'pass'
    assert result['lift_outcome_split']['parent'] == CLAIM
    assert result['lift_outcome_split']['parent_outcome'] == '++'
    pins = dict(result['source_sha256'])
    for path, digest in pins.items():
        assert file_hash(REPO, path) == digest, f'stale source net: {path}'
    for relative, digest in receipt['source_sha256'].items():
        path = 'research/nima/' + relative
        assert file_hash(REPO, path) == digest, f'stale return evidence: {path}'
        pins[path] = digest
    for path in (CONTRACT, RESULT, RECEIPT):
        pins[path] = file_hash(REPO, path)
    bindings = {key: f'/conjectures/{index}/{key}' for key in ('id', 'statement', 'scope_id', 'scope_status')}
    bindings.update({key: '/' + key for key in ('source_derivation_policy', 'return_interpretation_policy')})
    claim = {key: node[key] for key in ('id', 'statement', 'scope_id', 'scope_status')}
    claim.update({key: contract[key] for key in ('source_derivation_policy', 'return_interpretation_policy')})
    verification = {key: receipt[key] for key in (
        'proof_kind', 'kernel_verified_analytic_theorem', 'completion_backend_verified',
        'cubical_pointwise_decoder_constructed', 'C1_at_seam_claimed')}
    export = {
        'schema': 'marici.conjecture-net.outcome-export.v1',
        'export_id': 'nima.standard-local-lift.v1', 'head_path': HEAD,
        'outcome_semantics': SEMANTICS, 'outcome': '++',
        'claim': claim, 'claim_bindings': bindings,
        'source': {'contract': CONTRACT, 'result': RESULT, 'node_pointer': f'/conjectures/{index}',
                   'result_claim_pointer': '/lift_outcome_split/parent',
                   'result_outcome_pointer': '/lift_outcome_split/parent_outcome'},
        'verification_receipt': RECEIPT, 'verification': verification,
        'artifact_sha256': dict(sorted(pins.items())),
        'correction_policy': 'Any source/evidence drift, revocation or changed head blocks live imports. A correction requires a new export and explicit consumer re-pinning; never silently upgrade.',
        'boundary': 'Exports the scoped proposition, not termination or a kernel-verified analytic theorem. No source uniqueness, operational completion, or physical interpretation is imported.',
    }
    payload = (json.dumps(export, indent=2, sort_keys=True) + '\n').encode()
    digest = hashlib.sha256(payload).hexdigest()
    ref = {'path': f'research/nima/exports/standard-local-lift/{digest}.json', 'sha256': digest}
    pointer = {'schema': 'marici.conjecture-net.outcome-pointer.v1', 'export': ref, 'head': HEAD,
               'expected_claim': claim, 'expected_outcome': '++', 'accepted_verification': verification}
    return export, payload, pointer

def main():
    export, payload, pointer = prepare()
    head = {'schema': 'marici.conjecture-net.outcome-head.v1', 'export_id': export['export_id'],
            'status': 'active', 'export': pointer['export'], 'supersedes': None}
    head_path = REPO / HEAD
    if head_path.exists() and load(REPO, HEAD) != head:
        raise RuntimeError('Refusing to advance/reactivate export head implicitly. Publish a reviewed correction explicitly.')
    destination = REPO / pointer['export']['path']
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists() and destination.read_bytes() != payload:
        raise RuntimeError('Immutable export collision')
    if not destination.exists():
        destination.write_bytes(payload)
    if not head_path.exists():
        head_path.write_text(json.dumps(head, indent=2) + '\n', encoding='utf-8')
    resolve(REPO, pointer)
    print(json.dumps(pointer, indent=2))

if __name__ == '__main__':
    main()
