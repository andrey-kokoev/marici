"""Attach the implemented finite fragment; do not generalize its scope."""
import hashlib
import json
from pathlib import Path

HOME = Path(__file__).resolve().parent


if __name__ == '__main__':
    hierarchy = json.loads((HOME / 'contracts/programme-hierarchy.v6.json').read_text())
    hierarchy.update(schema='marici.conjecture-net.programme-hierarchy.v7',
                     id='marici.relational-carrier-physics-programme.v7',
                     phase='implemented_finite_source_fragment',
                     predecessor='research/conjecture_net/contracts/programme-hierarchy.v6.json')
    contract = HOME / 'contracts/pilot-carrier-interface.v1.json'
    hierarchy['implemented_source_fragments'] = [{
        'id': 'native-bool-retained-programme-fragment.v1',
        'source_instance': 'native-bool-square-pilot',
        'contract': 'research/conjecture_net/contracts/pilot-carrier-interface.v1.json',
        'contract_sha256': hashlib.sha256(contract.read_bytes()).hexdigest(),
        'implementation': 'research/conjecture_net/pilot_carrier.py',
        'audit_receipt': 'research/conjecture_net/results/pilot-carrier-interface-audit.json',
        'target_obligation': 'carrier-and-geometric-dynamics',
        'scope': 'Finite Bool records/operations, source-linearized witness binding and grouping; no universal carrier or physical instrument.',
        'status': 'implemented_and_finitely_audited',
        'admission_status': 'not_admitted_as_new_programme_proof_link',
        'proof_bearing': False, 'discharges_parent_obligation': False
    }]
    content = json.dumps(hierarchy, indent=2, sort_keys=True) + '\n'
    destination = HOME / 'contracts/programme-hierarchy.v7.json'
    if destination.exists() and destination.read_text() != content:
        raise ValueError('Refusing implicit fragment hierarchy correction')
    if not destination.exists():
        destination.write_text(content, encoding='utf-8')
    print('Recorded v7 finite implemented fragment; accepted prerequisite unchanged and programme outcomes open.')
