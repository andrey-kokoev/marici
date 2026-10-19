"""Attach the accepted finite prerequisite without resolving programme goals."""
import json
from pathlib import Path
from admit_structural_overlap import check, NET, CLAIM, POINTER

HOME = Path(__file__).resolve().parent


if __name__ == '__main__':
    resolved = check()
    hierarchy = json.loads((HOME / 'contracts/programme-hierarchy.v5.json').read_text(encoding='utf-8'))
    hierarchy.update(schema='marici.conjecture-net.programme-hierarchy.v6',
                     id='marici.relational-carrier-physics-programme.v6',
                     phase='accepted_finite_structural_prerequisite',
                     predecessor='research/conjecture_net/contracts/programme-hierarchy.v5.json')
    hierarchy['admitted_prerequisite_links'] = [{
        'id': 'accepted-finite-overlap-prerequisite',
        'source_net': NET, 'source_claim': CLAIM,
        'target_obligation': 'cross-sector-compatibility',
        'relation': 'supplies_scoped_prerequisite', 'status': 'admitted',
        'outcome_pointer': POINTER, 'proof_bearing': True,
        'scope_transport': 'Supplies only the finite Bool spectral overlap of the two structural pilots, not physical cross-sector compatibility or the whole target obligation.',
        'witness_transport': 'Same Bool-factor source, pi-scaled operators, accepted completion interpretation, injective realification, positive reversed schedule, and quadratic-record laws in the pinned transport/overlap contracts.',
        'verification_boundary': resolved['verification'],
        'discharges_parent_obligation': False,
        'boundary': 'Accepted prerequisite only. Parent and programme pilot outcomes remain null.'
    }]
    hierarchy['current_finite_overlap_admission'] = {
        'status': 'accepted_at_scoped_written_and_exact_algebra_level',
        'outcome': '++', 'source_claim': CLAIM, 'outcome_pointer': POINTER,
        'physical_overlap': 'not_defined', 'universal_carrier_embedding': 'not_proved'
    }
    content = json.dumps(hierarchy, indent=2, sort_keys=True) + '\n'
    destination = HOME / 'contracts/programme-hierarchy.v6.json'
    if destination.exists() and destination.read_text(encoding='utf-8') != content:
        raise ValueError('Refusing implicit accepted hierarchy correction')
    if not destination.exists():
        destination.write_text(content, encoding='utf-8')
    print('Recorded v6: one accepted finite prerequisite; root and programme pilots remain open.')
