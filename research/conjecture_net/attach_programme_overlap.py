"""Record the finite structural overlap while leaving physical bridges open."""
import copy
import hashlib
import json
from pathlib import Path

HOME = Path(__file__).resolve().parent


def load(path):
    return json.loads((HOME / path).read_text(encoding='utf-8'))


if __name__ == '__main__':
    hierarchy = copy.deepcopy(load('contracts/programme-hierarchy.v4.json'))
    hierarchy.update(schema='marici.conjecture-net.programme-hierarchy.v5',
                     id='marici.relational-carrier-physics-programme.v5',
                     phase='defined_finite_structural_overlap',
                     predecessor='research/conjecture_net/contracts/programme-hierarchy.v4.json',
                     terms='research/conjecture_net/contracts/programme-terms.v4.json',
                     overlap_contract='research/conjecture_net/contracts/programme-overlaps.v1.json',
                     overlap_audit='research/conjecture_net/results/programme-overlap-audit.json')
    hierarchy['overlap_status'] = {'finite_structural_overlap': 'defined_with_exact_coordinate_controls',
                                   'physical_sector_overlap': 'not_defined',
                                   'compton_source_bridge': 'missing', 'proof_bearing': False}
    terms = copy.deepcopy(load('contracts/programme-terms.v3.json'))
    terms.update(schema='marici.conjecture-net.programme-terms.v4',
                 hierarchy='research/conjecture_net/contracts/programme-hierarchy.v5.json',
                 predecessor='research/conjecture_net/contracts/programme-terms.v3.json',
                 review_status='candidate_terms_with_finite_structural_overlap')
    shared = next(t for t in terms['terms'] if t['id'] == 'shared_regimes')
    shared.update(status='reviewed_candidate',
                  definition='Explicitly declared overlap domains with a common source witness, state/operator maps, parameter and unit conventions, retained-record transport and commuting observable laws. The finite unitary/Hamiltonian overlap is specified; physical cross-sector overlaps are not thereby established.',
                  assumptions=['Restrict to the same finite Bool spectral witness and mathematical records; physical measurement authorization is separate.'],
                  counterexamples=['Equal quadratic records need not identify the underlying state or retained schedule.', 'A factor-of-two energy convention or missing pi scale can invalidate a supposed agreement.'],
                  residuals=['Physical common-source/instrument bridges and overlap domains remain unconstructed.', 'Programme proof admission and any stronger kernel transport requirement remain open.'],
                  evidence=[{'source_path': 'research/conjecture_net/contracts/programme-overlaps.v1.json',
                             'source_sha256': hashlib.sha256((HOME / 'contracts/programme-overlaps.v1.json').read_bytes()).hexdigest(),
                             'role': 'finite_structural_overlap_specification_not_physical_proof'}])
    artifacts = {'contracts/programme-hierarchy.v5.json': hierarchy,
                 'contracts/programme-terms.v4.json': terms}
    for path, data in artifacts.items():
        destination = HOME / path
        content = json.dumps(data, indent=2, sort_keys=True) + '\n'
        if destination.exists() and destination.read_text(encoding='utf-8') != content:
            raise ValueError('Refusing implicit overlap correction: ' + path)
    for path, data in artifacts.items():
        destination = HOME / path
        if not destination.exists():
            destination.write_text(json.dumps(data, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print('Recorded v5 finite overlap and candidate shared-regime definition; no physical bridge or proof admission.')
