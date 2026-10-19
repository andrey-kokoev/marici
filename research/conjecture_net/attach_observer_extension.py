"""Attach a complete mathematical probe subbranch without physical promotion."""
import json
from pathlib import Path

HOME = Path(__file__).resolve().parent


if __name__ == '__main__':
    hierarchy = json.loads((HOME / 'contracts/programme-hierarchy.v8.json').read_text())
    hierarchy.update(schema='marici.conjecture-net.programme-hierarchy.v9',
                     id='marici.relational-carrier-physics-programme.v9',
                     phase='constructed_complete_finite_mathematical_probes',
                     predecessor='research/conjecture_net/contracts/programme-hierarchy.v8.json')
    hierarchy['mathematical_observer_extensions'] = [{
        'id': 'uniform-source-polynomial-mathematical-probes.v1',
        'contract': 'research/conjecture_net/contracts/pilot-observer-extension.v1.json',
        'implementation': 'research/conjecture_net/pilot_observers.py',
        'receipt': 'research/conjecture_net/results/pilot-observer-extension-audit.json',
        'source_instance': 'native-bool-square-pilot',
        'status': 'constructed_and_exactly_audited', 'hermitian_observation_rank': 16,
        'physical_observer_authorization': 'not_supplied',
        'admission_status': 'not_admitted_as_new_programme_proof_link',
        'proof_bearing': False, 'discharges_parent_obligation': False
    }]
    for fork in hierarchy['candidate_synthesis_forks']:
        if fork['id'] == 'authorize-richer-observers':
            fork['mathematical_subbranch'] = 'Complete finite source-polynomial family constructed under declared coordinate marking and complex background.'
            fork['physical_subbranch'] = 'Source/preparation/instrument authorization and calibration remain open.'
    content = json.dumps(hierarchy, indent=2, sort_keys=True) + '\n'
    destination = HOME / 'contracts/programme-hierarchy.v9.json'
    if destination.exists() and destination.read_text() != content:
        raise ValueError('Refusing implicit observer hierarchy correction')
    if not destination.exists():
        destination.write_text(content, encoding='utf-8')
    print('Recorded v9 mathematical observer construction; physical authorization and richer control remain open.')
