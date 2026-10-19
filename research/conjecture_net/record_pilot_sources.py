"""Record structural pilot ingredient provenance; no retroactive preregistration."""
import hashlib
import json
from pathlib import Path

HOME = Path(__file__).resolve().parent
ROOT = HOME.parents[1]


if __name__ == '__main__':
    ingredients = [
        ('native-factor-maps', 'native_source_data', 'Bool pairs and their two factor flips',
         'research/nima/agda/ObserverCoherenceCube.agda',
         'Existing scoped formal source evidence via the accepted spectral witness; not newly kernel-checked here.',
         ['source operations and delta/permutation binding'], ['physical source selection', 'physical spacetime']),
        ('retained-fragment-conventions', 'declared_constructor_convention', 'Operation-word paths, occurrence IDs, explicit grouping keys and batch namespaces',
         'research/conjecture_net/pilot_carrier.py', 'New executable finite implementation; no new kernel theorem.',
         ['retained finite record interface and grouping audits'], ['source-only uniqueness', 'independent product inference', 'physical dynamics']),
        ('analytic-background', 'analytic_background', 'Free complex linearization, counting inner product, pi-scaled spectral rule and realification',
         'research/conjecture_net/contracts/structural-pilot-transport.v1.json',
         'Explicit mathematical premises; accepted written/exact transport, not a derivation of physical Hilbert space or clocks.',
         ['conditional structural realization and mathematical readout'], ['Born rule derivation', 'physical energy calibration', 'all-physics explanation']),
        ('accepted-finite-transport', 'derived_source_data', 'Scoped same-witness complex/real and quadratic-record correspondence',
         'research/conjecture_net/exports/finite-structural-overlap.pointer.v1.json',
         'Live pinned ++ at operator-accepted written/exact-algebra level with mixed operational evidence.',
         ['finite witness transport prerequisite'], ['new kernel proof', 'universal carrier embedding', 'empirical confirmation'])
    ]
    records = []
    for target in ('unitary-local-return-pilot', 'hamiltonian-symplectic-pilot'):
        for key, role, ingredient, path, level, allowed, forbidden in ingredients:
            records.append({'id': target + ':' + key, 'target_id': target,
                'source_object': 'native-bool-square-pilot', 'ingredient': ingredient, 'role': role,
                'origin': {'source_path_or_external_reference': path,
                           'integrity_or_version': hashlib.sha256((ROOT / path).read_bytes()).hexdigest(),
                           'verification_level': level},
                'scope': 'Finite retained Bool-source structural interface and its specified spectral witness only.',
                'frozen_before': 'Future programme tests using this dossier; not retroactive preregistration of prior computations.',
                'allowed_uses': allowed, 'forbidden_promotions': forbidden})
    result = {'schema': 'marici.conjecture-net.pilot-source-records.v1', 'records': records,
              'physical_data_inputs': [], 'fitting_inputs': [], 'held_out_data': [],
              'boundary': 'Structural provenance record. Empty physical datasets do not constitute empirical validation.'}
    path = HOME / 'contracts/pilot-source-records.v1.json'
    payload = json.dumps(result, indent=2, sort_keys=True) + '\n'
    if path.exists() and path.read_text() != payload:
        raise ValueError('Refusing implicit source dossier correction')
    if not path.exists():
        path.write_text(payload, encoding='utf-8')
    print('Recorded eight target-specific source ingredients with explicit provenance roles.')
