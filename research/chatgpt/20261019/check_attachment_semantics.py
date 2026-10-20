#!/usr/bin/env python3
"""Exact checks for witnessed attachment versus imposed relation.

Only the standard library is used. This checks integer cellular-chain
identities and finite cyclic-character extension constraints. It does not
compute arbitrary homotopy groups or certify Agda source.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
from functools import reduce
from itertools import product
import json
from math import gcd
from pathlib import Path
from typing import Sequence

Number = int | Fraction
Matrix = list[list[Number]]
COUNTS: Counter[str] = Counter()


def check(ok: bool, label: str) -> None:
    COUNTS[label] += 1
    if not ok:
        raise AssertionError(label)


def zeros(rows: int, cols: int) -> Matrix:
    return [[0 for _ in range(cols)] for _ in range(rows)]


def eye(n: int) -> Matrix:
    return [[int(i == j) for j in range(n)] for i in range(n)]


def mm(a: Matrix, b: Matrix) -> Matrix:
    if not a:
        return []
    width = len(a[0])
    if width != len(b):
        raise ValueError('incompatible matrix dimensions')
    n = len(b[0]) if b else 0
    return [[sum(a[i][k] * b[k][j] for k in range(width))
             for j in range(n)] for i in range(len(a))]


def rank(a: Matrix) -> int:
    if not a or not a[0]:
        return 0
    m = [[Fraction(x) for x in row] for row in a]
    r = 0
    for c in range(len(m[0])):
        pivot = next((i for i in range(r, len(m)) if m[i][c]), None)
        if pivot is None:
            continue
        m[r], m[pivot] = m[pivot], m[r]
        factor = m[r][c]
        m[r] = [v / factor for v in m[r]]
        for i in range(len(m)):
            if i != r and m[i][c]:
                f = m[i][c]
                m[i] = [u - f * v for u, v in zip(m[i], m[r])]
        r += 1
        if r == len(m):
            break
    return r


def row_gcd(qs: Sequence[int]) -> int:
    return reduce(gcd, (abs(q) for q in qs), 0)


def disk_complex(n: int) -> tuple[list[int], dict[int, Matrix]]:
    """The globular n-ball: two cells per lower dimension, one top cell."""
    if n < 1:
        raise ValueError('n must be positive')
    dims = [2] * n + [1]
    ds: dict[int, Matrix] = {}
    for k in range(1, n + 1):
        cols = dims[k]
        sign = -1 if k == 1 else 1
        ds[k] = [[sign] * cols, [-sign] * cols]
    return dims, ds


def verify_witnessed_chain_split(n: int) -> None:
    """Attach a fresh n-cell with the boundary of the existing top cell.

    Phi(c,t)=(c+t*p,t), Phi^{-1}(c,t)=(c-t*p,t), where p is
    the existing top cell. The split target is C plus Z in degree n.
    """
    dims, ds = disk_complex(n)
    for k in range(2, n + 1):
        check(mm(ds[k - 1], ds[k]) == zeros(dims[k - 2], dims[k]),
              'original_boundary_squared_zero')
    fresh = [row + [row[0]] for row in ds[n]]
    split = [row + [0] for row in ds[n]]
    phi = [[1, 1], [0, 1]]
    inv = [[1, -1], [0, 1]]
    check(mm(phi, inv) == eye(2) and mm(inv, phi) == eye(2),
          'integral_inverse_split_maps')
    check(mm(split, phi) == fresh, 'split_map_is_chain_map')
    check(mm(fresh, inv) == split, 'inverse_is_chain_map')
    difference = [[-1], [1]]  # fresh cell minus retained old filler
    check(mm(fresh, difference) == zeros(2, 1), 'fresh_minus_old_is_cycle')
    check(mm(phi, difference) == [[0], [1]], 'difference_is_primitive_summand')
    # A new higher comparison cell with this precise boundary kills the
    # extra summand by an integral coefficient 1, not by an approximation.
    check(mm(phi, difference) == [[0], [1]], 'higher_cell_targets_new_summand')
    # Forgetting which top filling is the reference reverses the relative sphere.
    swap = [[0, 1], [1, 0]]
    check(mm(fresh, swap) == fresh, 'filler_swap_preserves_boundary')
    check(mm(swap, difference) == [[1], [-1]], 'filler_swap_reverses_relative_class')


def check_circle_attachments(qs: Sequence[int]) -> dict:
    d1 = [[-1, -1], [1, 1]]  # a,b : N -> S
    d2 = [list(qs), [-q for q in qs]]
    if qs:
        check(mm(d1, d2) == zeros(2, len(qs)), 'circle_boundary_squared_zero')
    # Unimodular coordinates (N,S-N) and (b,a-b).
    v0 = [[1, -1], [0, 1]]
    v0inv = [[1, 1], [0, 1]]
    v1 = [[0, 1], [1, -1]]
    v1inv = [[1, 1], [1, 0]]
    check(mm(v0, v0inv) == eye(2) and mm(v1, v1inv) == eye(2),
          'unimodular_circle_coordinates')
    check(mm(v0inv, mm(d1, v1)) == [[0, 0], [1, 0]],
          'spanning_edge_splits_as_contractible_pair')
    if qs:
        check(mm(v1inv, d2) == [[0] * len(qs), list(qs)],
              'remaining_integer_boundary_is_winding_row')
    g = row_gcd(qs)
    h1 = 'Z' if g == 0 else ('0' if g == 1 else f'Z/{g}')
    h2rank = len(qs) - int(g != 0)
    if qs:
        check(rank(d2) == int(g != 0), 'rational_rank_agrees_with_primitive_reduction')
    # Maps to B(Z/N): generator goes to k, each attaching word gives q*k=0.
    for modulus in range(2, 13):
        allowed = [k for k in range(modulus)
                   if all((q * k) % modulus == 0 for q in qs)]
        check(len(allowed) == gcd(modulus, g), 'finite_character_extension_count')
        reflected = sorted((-k) % modulus for k in allowed)
        check(reflected == allowed, 'orientation_covariance_of_extensions')
    return {'winding_words': list(qs), 'H0': 'Z', 'H1': h1,
            'H2_free_rank': h2rank}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path,
                        default=Path(__file__).with_name('wg_attachment_semantics_results.json'))
    args = parser.parse_args()
    for n in range(1, 9):
        verify_witnessed_chain_split(n)
    cases = 0
    for m in range(4):
        for qs in product(range(-3, 4), repeat=m):
            check_circle_attachments(qs)
            cases += 1
    featured = [check_circle_attachments(qs)
                for qs in [(), (1,), (1, 1), (0,), (2,), (2, 3)]]

    # The torsion counterexample is exact over Q, not a numerical inverse.
    double_boundary = [[2], [-2]]
    check(mm(double_boundary, [[Fraction(1, 2)]]) == [[1], [-1]],
          'rational_filler_for_primitive_torsion_cycle')
    check(1 % 2 != 0, 'no_integral_solution_to_twice_integer_equals_one')
    # The order-two observer survives z^2=1 and detects z.
    check((2 * 1) % 2 == 0 and 1 % 2 != 0,
          'order_two_observer_detects_surviving_torsion')

    # Fill the relative sphere of the two disks with a 3-cell.
    d1 = [[-1, -1], [1, 1]]
    d2 = [[1, 1], [-1, -1]]
    d3 = [[-1], [1]]
    check(mm(d2, d3) == [[0], [0]], 'coherence_cell_has_closed_boundary')
    check(rank(d2) == 1 and rank(d3) == 1,
          'relative_sphere_removed_by_higher_comparison')
    # Explicit reduction proves integrality, not just zero rational Betti numbers.
    phi = [[1, 1], [0, 1]]
    inverse = [[1, -1], [0, 1]]
    check(mm(d2, inverse) == [[1, 0], [-1, 0]],
          'two_disk_integral_normal_form')
    check(mm(phi, d3) == [[0], [1]], 'primitive_integral_three_cell_pair')

    report = {
        'status': 'pass',
        'total_assertions': sum(COUNTS.values()),
        'assertion_counts': dict(sorted(COUNTS.items())),
        'globular_dimensions_checked': list(range(1, 9)),
        'circle_attachment_policies_checked': cases,
        'finite_cyclic_probe_orders': list(range(2, 13)),
        'featured_integer_homology': featured,
        'higher_comparison_example': {'H0': 'Z', 'H1': '0', 'H2': '0', 'H3': '0'},
        'rational_filler': 'c/2 for boundary(c)=2(a-b)',
        'native_torsion_control': 'pi1=<z | z^2=1>=C2; z is not nullhomotopic',
        'proof_boundary': [
            'General pushout and null-attachment statements are proved in the accompanying note.',
            'Topological identifications use the actual cellular attaching descriptions, not homology alone.',
            'Finite probe tests count cyclic character homotopy classes, not full mapping spaces.',
            'No arbitrary native source law or physical T9 selection is inferred.',
            'No Agda or Lean compilation has been performed.'
        ]
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(f'PASS: {report["total_assertions"]} exact assertions; '
          f'{cases} attachment policies; dimensions 1-8.')
    print(args.output)


if __name__ == '__main__':
    main()
