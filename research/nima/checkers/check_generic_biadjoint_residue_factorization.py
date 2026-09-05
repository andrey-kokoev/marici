#!/usr/bin/env python3
"""Exact formal Laurent-monomial check of generic polygon residue factorization."""
import importlib.util
import json
from pathlib import Path

helper_path = Path(__file__).with_name('check_generic_polygon_face_product.py')
spec = importlib.util.spec_from_file_location('polygon_faces', helper_path)
poly = importlib.util.module_from_spec(spec)
spec.loader.exec_module(poly)

# A polynomial is a dictionary from a squarefree set of inverse propagators to
# its integer coefficient. Polygon amplitudes below have coefficient one.
def amplitude_on_diagonals(ds, maximal_size):
    return {t: 1 for t in poly.dissections_on(tuple(ds)) if len(t) == maximal_size}

def multiply(left, right):
    out = {}
    for a, ca in left.items():
        for b, cb in right.items():
            assert a.isdisjoint(b)
            monomial = a | b
            out[monomial] = out.get(monomial, 0) + ca * cb
    return out

def residue(amplitude, cut):
    # Coefficient of the product of inverse propagators indexed by cut.
    out = {}
    for monomial, coefficient in amplitude.items():
        if cut <= monomial:
            residual = monomial - cut
            out[residual] = out.get(residual, 0) + coefficient
    return out

def verify(n):
    all_dis = poly.dissections_on(poly.diagonals(n))
    amplitude = amplitude_on_diagonals(poly.diagonals(n), n - 3)
    assert len(amplitude) > 0
    comparisons = terms = 0
    for cut in all_dis:
        lhs = residue(amplitude, cut)
        rhs = {frozenset(): 1}
        regions = poly.split_regions(n, cut)
        for region in regions:
            local_ds = poly.region_diagonals(region)
            local_amplitude = amplitude_on_diagonals(local_ds, len(region) - 3)
            rhs = multiply(rhs, local_amplitude)
        assert lhs == rhs, (n, cut, lhs, rhs)
        comparisons += 1
        terms += len(lhs)
    return {
        'n': n,
        'amplitude_terms': len(amplitude),
        'dissection_residues_checked': comparisons,
        'residual_monomials_checked': terms,
        'status': 'passed'
    }

result = {
    'schema': 'marici.generic-biadjoint-residue-factorization.v1',
    'coefficient_ring': 'integers',
    'variables': 'formal squarefree inverse propagators indexed by polygon diagonals',
    'claim': 'For every tested dissection D, the coefficient residue of m_n along D equals the product of amplitudes of the regions of D.',
    'strength': 'generic executable construction with exhaustive instances n=3..7; not an internal Rzk theorem',
    'tests': [verify(n) for n in range(3, 8)]
}
out = Path('research/nima/results/generic_biadjoint_residue_factorization.json')
out.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps(result, sort_keys=True))
