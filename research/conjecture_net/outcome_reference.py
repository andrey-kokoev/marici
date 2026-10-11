"""Pinned cross-net outcome imports. Integrity/scope checking, not theorem proving.

These are attempt outcomes, never the thin-category polarity arrows.
A mutable export head allows corrections/revocations to invalidate live imports.
"""
from hashlib import sha256
import json
from pathlib import Path

SEMANTICS = 'proof-attempt-outcomes-v1'
PORTS = {
    '++': {'attempt': 'prove', 'result': 'proved'},
    '+-': {'attempt': 'prove', 'result': 'failed_to_prove'},
    '-+': {'attempt': 'reject', 'result': 'succeeded_in_rejecting'},
    '--': {'attempt': 'reject', 'result': 'failed_at_rejecting'},
}

class OutcomeReferenceError(ValueError):
    pass

def require(condition, message):
    if not condition:
        raise OutcomeReferenceError(message)

def file_at(root, relative):
    root = Path(root).resolve()
    require(isinstance(relative, str) and relative != '', 'missing artifact path')
    path = (root / relative).resolve()
    require(not Path(relative).is_absolute() and path.is_relative_to(root), 'artifact escapes repository')
    return path

def load(root, relative):
    return json.loads(file_at(root, relative).read_text(encoding='utf-8'))

def file_hash(root, relative):
    return sha256(file_at(root, relative).read_bytes()).hexdigest()

def at(document, pointer):
    require(isinstance(pointer, str) and pointer.startswith('/'), 'expected JSON pointer')
    for raw in pointer[1:].split('/'):
        key = raw.replace('~1', '/').replace('~0', '~')
        document = document[int(key)] if isinstance(document, list) else document[key]
    return document

def resolve(root, pointer):
    """Fail closed on changed evidence, source outcome/scope, export head or proof level.

A correction requires a new export and explicit re-pinning by the consumer.
No import itself proves an analytic theorem or authorizes publication.
"""
    try:
        return _resolve(root, pointer)
    except OutcomeReferenceError:
        raise
    except (OSError, KeyError, TypeError, ValueError, IndexError) as error:
        raise OutcomeReferenceError(f'malformed or unavailable outcome reference: {error}') from error

def _resolve(root, pointer):
    require(pointer['schema'] == 'marici.conjecture-net.outcome-pointer.v1', 'wrong pointer schema')
    ref = pointer['export']
    require(file_hash(root, ref['path']) == ref['sha256'], 'export digest mismatch')
    export = load(root, ref['path'])
    require(export['schema'] == 'marici.conjecture-net.outcome-export.v1', 'wrong export schema')
    require(export['outcome_semantics'] == SEMANTICS, 'polarity is not a proof outcome')
    require(pointer['head'] == export['head_path'], 'wrong export head')
    head = load(root, pointer['head'])
    require(head['schema'] == 'marici.conjecture-net.outcome-head.v1', 'wrong head schema')
    require(head['status'] == 'active' and head['export'] == ref
            and head['export_id'] == export['export_id'], 'export revoked or superseded')
    pins = export['artifact_sha256']
    require(bool(pins), 'empty evidence closure')
    for path, expected in pins.items():
        require(file_hash(root, path) == expected, f'stale source/evidence: {path}')
    source = export['source']
    for path in (source['contract'], source['result'], export['verification_receipt']):
        require(path in pins, f'unpinned source: {path}')
    contract = load(root, source['contract'])
    result = load(root, source['result'])
    require(contract['outcome_ports'] == PORTS, 'source outcome semantics mismatch')
    require(result['status'] == 'pass', 'source net validation did not pass')
    node = at(contract, source['node_pointer'])
    claim = {key: at(contract, location) for key, location in export['claim_bindings'].items()}
    require(all(key in claim and claim[key] == node[key] for key in ('id', 'statement', 'scope_id')),
            'source proposition/scope bindings incomplete or inconsistent')
    require(claim == export['claim'] == pointer['expected_claim'], 'proposition or scope mismatch')
    require(node['id'] == claim['id'] == at(result, source['result_claim_pointer']), 'wrong source claim')
    outcome = export['outcome']
    require(outcome in PORTS and node['outcome'] == outcome
            and at(result, source['result_outcome_pointer']) == outcome
            and pointer['expected_outcome'] == outcome, 'source outcome mismatch')
    receipt = load(root, export['verification_receipt'])
    require(receipt['status'] == 'pass', 'verification receipt did not pass')
    verification = {key: receipt[key] for key in export['verification']}
    require(isinstance(verification.get('proof_kind'), str)
            and isinstance(verification.get('kernel_verified_analytic_theorem'), bool), 'incomplete verification level')
    require(verification == export['verification'] == pointer['accepted_verification'], 'verification-level mismatch')
    return {
        'export_id': export['export_id'], 'source_claim': claim['id'],
        'outcome': outcome, 'proposition_truth': {'++': True, '-+': False}.get(outcome),
        'resolved_proposition': outcome in ('++', '-+'),
        'verification': verification, 'export_sha256': ref['sha256'],
        'boundary': 'A verified reference to a recorded result, not independent theorem verification.',
    }
