"""Source-bound comparison of the literal continuum claim with its cited code.

First run collect_continuum_diagnostics.py under the admitted SciPy profile.
Then: uv run --with sympy python research/nima/checkers/check_continuum_embedding_evidence_boundary.py

Exit zero certifies the stated counterexample and surviving finite calculations,
not a continuum construction. Every transported source hash must still match.
"""
import hashlib
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / 'quarantine/20261007-continuum-evidence'
CHECKS = []


def require(name, condition):
    if not bool(condition):
        raise AssertionError(name)
    CHECKS.append(name)


def decode_grid(record):
    points, coords, neighbors, pseudo_rank = record
    return (points, {int(k): tuple(v) for k, v in coords.items()},
            {int(k): v for k, v in neighbors.items()},
            {int(k): v for k, v in pseudo_rank.items()})


def exact_integral_matrix(name, data):
    # Rational(float) preserves the exact binary value, not a rounded fit.
    # The original np.zeros buffers store integer dot products as floats.
    matrix = sp.Matrix(data).applyfunc(sp.Rational)
    require('exact-integer-matrix:' + name, all(x.q == 1 for x in matrix))
    return matrix


def hat_weights(grid, L, x):
    """The paper's Euclidean radial hats, using the actual cubic_grid output."""
    epsilon = sp.Rational(1, L)
    weights = []
    for point in grid.values():
        distance_squared_in_grid_units = sum(
            (x[a] / epsilon - point[a])**2 for a in range(3))
        weights.append(1 - sp.sqrt(distance_squared_in_grid_units)
                       if distance_squared_in_grid_units < 1 else sp.S.Zero)
    return weights


def main():
    out = ROOT/'results/continuum-embedding-evidence-boundary.json'
    out.unlink(missing_ok=True)
    CHECKS.clear()
    manifest = json.loads((ARCHIVE / 'manifest.json').read_text(encoding='utf-8'))
    for item in manifest['files']:
        require('archive:' + item['path'],
                hashlib.sha256((ARCHIVE / item['path']).read_bytes()).hexdigest()
                == item['sha256'])
    receipt_paths = [ROOT / p for p in manifest['absent_receipts_at_snapshot']]
    # Non-mutation is enforced even if someone later creates one of these files.
    receipt_before = {str(p): p.read_bytes() if p.exists() else None for p in receipt_paths}

    continuum_path = Path('checkers/check_continuum_limit.py')
    gram_path = Path('checkers/check_machian_metric_larger.py')
    transport_path = ROOT/'results/continuum-diagnostic-transport.json'
    transport = json.loads(transport_path.read_text(encoding='utf-8'))
    require('typed-diagnostic-transport', transport['schema'] ==
            'marici.nima.continuum-diagnostic-transport.v1')
    expected_transport_sources = {
        'checkers/collect_continuum_diagnostics.py', str(continuum_path).replace('\\', '/'),
        str(gram_path).replace('\\', '/'),
        'quarantine/20261007-continuum-evidence/checkers/check_continuum_limit.py',
        'quarantine/20261007-continuum-evidence/checkers/check_machian_metric_larger.py'}
    require('complete-transport-provenance',
            set(transport['source_sha256']) == expected_transport_sources)
    for path, digest in transport['source_sha256'].items():
        require('transport-source-current:' + path,
                hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == digest)
    require('collector-preserved-receipts', transport['historical_receipts_unchanged'])
    old = transport['data']['original']
    current = transport['data']['current']
    require('metadata-corrected-not-promoted', current['declared_status'] ==
            ['finite_diagnostic_only', 'finite_diagnostic_only'])
    for group in ('permutation_matrices', 'direction_matrices'):
        for name, matrix in current[group].items():
            require('old-and-current-identical:' + name, matrix == old[group][name])
    for L in range(2, 9):
        grid = decode_grid(current['grids'][str(L)])
        require('whole-grid-preserved:L=' + str(L), grid == decode_grid(old['grids'][str(L)]))
        pts, coords, neighbors, pseudo_rank = grid
        counts = {degree: sum(n == degree for n in neighbors.values())
                  for degree in (3, 4, 5, 6)}
        require('exact-grid-counts:L=' + str(L), counts == {
            3: 8, 4: 12*(L-2), 5: 6*(L-2)**2, 6: (L-2)**3})
        require('legacy-sym-rank-is-only-degree:L=' + str(L), pseudo_rank == neighbors)
        require('full-carrier-retained:L=' + str(L), len(pts) == len(coords) == L**3)

    Gs3 = exact_integral_matrix('S3', current['permutation_matrices']['G4_ind'])
    Gd4 = exact_integral_matrix('D4', current['permutation_matrices']['G_d4'])
    Gdir = exact_integral_matrix('directions', current['direction_matrices']['G'])
    directions = exact_integral_matrix('vectors', current['direction_matrices']['vecs'])
    rejected_noninteger = False
    try:
        exact_integral_matrix('injected-noninteger', [[1.125]])
    except AssertionError:
        rejected_noninteger = True
    require('no-rounding-of-noninteger-input', rejected_noninteger)
    require('exact-S3-label-spectrum', Gs3.eigenvals() == {0: 3, 6: 2, 72: 1})
    require('exact-D4-label-spectrum', Gd4.eigenvals() == {0: 5, 240: 2, 1024: 1})
    require('exact-direction-spectrum', Gdir.eigenvals() == {0: 3, 2: 3})
    require('given-euclidean-direction-gram', Gdir == directions * directions.T
            and directions.T * directions == 2 * sp.eye(3))
    require('same-size-does-not-identify-Grams', Gs3.shape == Gdir.shape
            and Gs3 != Gdir)

    x = (sp.Rational(1, 2),) * 3
    odd_sum = 8 - 4*sp.sqrt(3)
    residual = sp.simplify(odd_sum - 1)
    require('strict-positive-constant-error', residual > 0)
    rows = []
    for L in range(3, 9):
        _, coords, _, _ = decode_grid(current['grids'][str(L)])
        require('fixed-point-in-hull:L=' + str(L),
                all(0 < c < sp.Rational(L-1, L) for c in x))
        weights = hat_weights(coords, L, x)
        total = sp.simplify(sum(weights))
        expected = odd_sum if L % 2 else sp.S.One
        require('parity-subsequence:L=' + str(L), sp.simplify(total - expected) == 0)
        error_matrix = sp.simplify(total * sp.eye(3) - sp.eye(3))
        require('entire-constant-metric:L=' + str(L),
                error_matrix == (expected-1) * sp.eye(3))
        rows.append({'L': L, 'support_count': sum(w != 0 for w in weights),
                     'weight_sum': str(total), 'metric_error_diagonal': str(expected-1)})
    # Constants in the all-L argument: other half-integer grid points are
    # outside support, while every nonzero integer displacement has norm >= 1.
    nearest_d2 = 3 * sp.Rational(1, 2)**2
    next_d2 = sp.Rational(3, 2)**2 + 2 * sp.Rational(1, 2)**2
    require('all-odd-L-support-separation', nearest_d2 < 1 < next_d2)
    require('all-odd-L-weight', sp.simplify(8*(1-sp.sqrt(nearest_d2))-odd_sum) == 0)
    ell = sp.symbols('L', positive=True)
    require('interior-fraction-limit-is-valid-but-separate',
            sp.limit((ell-2)**3 / ell**3, ell, sp.oo) == 1)
    epsilon, radius = sp.symbols('epsilon radius', positive=True)
    mass = sp.integrate(4*sp.pi*radius**2*(1-radius/epsilon), (radius, 0, epsilon))
    require('unscaled-hat-mass', sp.simplify(mass - sp.pi*epsilon**3/3) == 0)
    require('unscaled-hat-not-Dirac', sp.limit(mass, epsilon, 0, dir='+') == 0)

    caught = False
    try:
        require('injected-false-partition-claim', sp.simplify(odd_sum-1) == 0)
    except AssertionError:
        caught = True
    require('failure-gate-refuses-false-partition', caught)
    require('historical-receipts-untouched', receipt_before == {
        str(p): p.read_bytes() if p.exists() else None for p in receipt_paths})

    sources = [Path(__file__).resolve(), ROOT/continuum_path, ROOT/gram_path,
               ROOT/'checkers/collect_continuum_diagnostics.py', transport_path,
               ARCHIVE/'manifest.json', ROOT/'barycentric-refinement-coherence.md',
               ROOT/'relative-anchor-coordinate-prior-clues.md']
    result = {
        'schema': 'marici.nima.continuum-embedding-evidence-boundary.v1',
        'status': 'pass',
        'scientific_disposition': 'literal-interpolant-fails; finite-diagnostics-retained-not-continuum-proof',
        'point': ['1/2', '1/2', '1/2'],
        'odd_L_weight_sum': str(odd_sum), 'even_L_weight_sum': '1',
        'odd_L_constant_metric_error': str(residual),
        'all_L_argument': 'For odd L>=3 nearest offsets are (+/-1/2)^3 with squared distance 3/4, all others at least 11/4. For even L>=4 one zero offset contributes 1; every other squared distance is at least 1.',
        'convergence_disposition': 'No pointwise limit at this fixed interior point along all integer L, hence no claimed uniform O(L^-2) convergence.',
        'unscaled_hat_mass': str(mass), 'unscaled_hat_distributional_limit': 'zero',
        'surviving_finite_objects': {
            'S3_label_Gram': {'shape': [6, 6], 'nonzero_eigenvalues': [6, 6, 72]},
            'D4_label_Gram': {'shape': [8, 8], 'nonzero_eigenvalues': [240, 240, 1024]},
            'given_direction_Gram': {'shape': [6, 6], 'nonzero_eigenvalues': [2, 2, 2]},
            'interior_fraction': '(L-2)^3/L^3 for L>=2'},
        'scope': 'The stated radial interpolant and its actual cited finite diagnostics. Not all continuum constructions, normalized discrete distribution limits, ADM closure, or the independently proved finite barycentric coherence theorem.',
        'rows': rows, 'checks': CHECKS, 'check_count': len(CHECKS),
        'source_sha256': {str(p.relative_to(ROOT)).replace('\\', '/'):
                          hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}}
    out.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'status': result['status'], 'disposition': result['scientific_disposition'],
                      'error': str(residual), 'checks': len(CHECKS)}, indent=2))


if __name__ == '__main__':
    main()
