"""Attach a defined same-witness pilot transport without promoting outcomes."""
import copy
import hashlib
import json
from pathlib import Path

HOME = Path(__file__).resolve().parent
ROOT = HOME.parents[1]


def build():
    hierarchy = json.loads((HOME / 'contracts/programme-hierarchy.v3.json').read_text(encoding='utf-8'))
    transport = json.loads((HOME / 'contracts/structural-pilot-transport.v1.json').read_text(encoding='utf-8'))
    hierarchy = copy.deepcopy(hierarchy)
    hierarchy.update(schema='marici.conjecture-net.programme-hierarchy.v4',
                     id='marici.relational-carrier-physics-programme.v4',
                     phase='defined_finite_structural_pilot_transport',
                     predecessor='research/conjecture_net/contracts/programme-hierarchy.v3.json')
    hierarchy['structural_pilot_transports'] = [{
        'id': transport['id'],
        'contract': 'research/conjecture_net/contracts/structural-pilot-transport.v1.json',
        'contract_sha256': hashlib.sha256((HOME / 'contracts/structural-pilot-transport.v1.json').read_bytes()).hexdigest(),
        'audit_receipt': 'research/conjecture_net/results/structural-pilot-transport-audit.json',
        'targets': transport['targets'],
        'source_instance': transport['source_instance'],
        'relation': 'defined_same_witness_transport',
        'definition_status': 'written_with_exact_coordinate_controls',
        'admission_status': 'not_admitted_as_programme_proof_link',
        'proof_bearing': False,
        'boundary': 'Concrete common finite witness only; does not implement the universal carrier, prove kernel realification, or supply physical confirmation.'
    }]
    return hierarchy


if __name__ == '__main__':
    payload = json.dumps(build(), indent=2, sort_keys=True) + '\n'
    destination = HOME / 'contracts/programme-hierarchy.v4.json'
    if destination.exists() and destination.read_text(encoding='utf-8') != payload:
        raise ValueError('Refusing implicit hierarchy correction')
    if not destination.exists():
        destination.write_text(payload, encoding='utf-8')
    print('Recorded v4 finite same-witness transport; programme outcomes unchanged.')
