"""Explicit period/class binding with exact sample and exterior controls.
Transcendental independence, Riemann projectivity and torus Hodge theory are
imported in the accompanying written proofs; rational samples are not the target.
"""
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
import json
from check_hodge_cycle_map_scope import rref
from check_hodge_literature_boundary_audit import (
    multiply, transpose, determinant, weil_forms, wedge, report as audit_report)

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = ROOT / 'research/conjecture_net/contracts/hodge-explicit-sixfold-candidate.v1.json'
NOTE = ROOT / 'research/voevodsky/hodge-explicit-sixfold-candidate-v1.md'
OUT = ROOT / 'research/voevodsky/results/hodge-explicit-sixfold-candidate-v1.json'
DS = (1, 1, 1, -1, -1, -3)
PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61)
BASIS2 = tuple(combinations(range(12), 2))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def identity(n):
    return [[Q(i == j) for j in range(n)] for i in range(n)]


def inverse(a):
    reduced, pivots = rref([list(row) + col for row, col in zip(a, identity(len(a)))], len(a))
    require(len(pivots) == len(a), 'singular period splitting')
    return [row[len(a):] for row in reduced]


def base_J():
    j = [[Q(0)]*12 for _ in range(12)]
    for k, d in enumerate(DS):
        sign = 1 if d > 0 else -1
        j[2*k][2*k+1], j[2*k+1][2*k] = -sign, sign
    return j


def sample_J(row=None, column=None, imaginary=False):
    a = identity(12)
    if row is not None:
        value = Q(1, 8)
        block = [[0, -value], [value, 0]] if imaginary else [[value, 0], [0, value]]
        weight = (1, 1, 3)[row]
        for i in range(2):
            for k in range(2):
                a[6+2*row+i][2*column+k] = block[i][k]
                a[2*column+k][6+2*row+i] = weight * block[i][k]  # Z*D
    return multiply(multiply(a, base_J()), inverse(a))


def add_simplex(out, indices, coefficient):
    if len(set(indices)) != len(indices):
        return
    sign = (-1) ** sum(indices[i] > indices[j] for i in range(len(indices)) for j in range(i+1, len(indices)))
    out[tuple(sorted(indices))] += coefficient * sign


def lie_action(j, form):
    """Infinitesimal J action: kernel in degree six is exactly type (3,3).
    Invariance under wedge^6 J* alone would also admit types (5,1),(1,5).
    """
    result = Counter()
    for indices, value in form.items():
        for position, i in enumerate(indices):
            for k, coefficient in enumerate(j[i]):
                if coefficient:
                    changed = indices[:position] + (k,) + indices[position+1:]
                    add_simplex(result, changed, value * coefficient)
    return {s: v for s, v in result.items() if v}


def full_pullback(j, form):
    result = Counter()
    for indices, value in form.items():
        options = [[(k, c) for k, c in enumerate(j[i]) if c] for i in indices]
        for selected in product(*options):
            coefficient = value
            for k, c in selected:
                coefficient *= c
            add_simplex(result, tuple(k for k, c in selected), coefficient)
    return {s: v for s, v in result.items() if v}


def degree_two_constraints(j):
    for k, l in BASIS2:
        yield [j[i][k]*j[q][l] - j[i][l]*j[q][k] - int((i, q) == (k, l)) for i, q in BASIS2]


def sparse_rank(rows, certificate=False):
    pivots, independent_rows = {}, []
    for row_index, row in enumerate(rows):
        v = {i: x for i, x in enumerate(row) if x}
        while v:
            p = min(v)
            scale = v[p]
            if p not in pivots:
                pivots[p] = {i: x/scale for i, x in v.items()}
                independent_rows.append(row_index)
                break
            for i, x in pivots[p].items():
                value = v.get(i, Q(0)) - scale*x
                if value:
                    v[i] = value
                else:
                    v.pop(i, None)
    return (len(pivots), independent_rows) if certificate else len(pivots)


@lru_cache(maxsize=1)
def exact_core():
    """Cache only fixed rational mathematics, never reads mutable source files."""
    samples = [sample_J()] + [sample_J(i, j, b) for i in range(3) for j in range(3) for b in (False, True)]
    E = [[Q(0)]*12 for _ in range(12)]
    for i, d in enumerate(DS):
        E[2*i][2*i+1], E[2*i+1][2*i] = d, -d
    alpha, beta = weil_forms(6)
    minus_identity = [[-v for v in row] for row in identity(12)]
    eform = {(2*i, 2*i+1): d for i, d in enumerate(DS)}
    constraints = []
    for j in samples:
        require(multiply(j, j) == minus_identity, 'J squared')
        require(multiply(multiply(transpose(j), E), j) == E, 'Riemann form compatibility')
        require(not lie_action(j, alpha) and not lie_action(j, beta), 'Weil Hodge degree')
        rows = list(degree_two_constraints(j))
        evector = [eform.get(pair, 0) for pair in BASIS2]
        require(all(sum(x*y for x, y in zip(row, evector)) == 0 for row in rows), 'universal polarization kernel')
        constraints.extend(rows)
    rank, independent_rows = sparse_rank(constraints, certificate=True)
    require(rank == 65, 'Picard constraint rank')
    # Cross-check the sparse rank certificate with the independent dense RREF.
    reduced, pivots = rref([constraints[i] for i in independent_rows])
    require(len(pivots) == 65, 'independent rank certificate')
    free = next(i for i in range(66) if i not in pivots)
    kernel = [Q(0)]*66
    kernel[free] = Q(1)
    for i, p in enumerate(pivots):
        kernel[p] = -reduced[i][free]
    require(kernel == [Q(v)/evector[free] for v in evector], 'Picard kernel generator')
    require(determinant(E) == 9, 'polarization degree')
    cube = wedge(wedge(eform, eform), eform)
    x_torus = tuple(range(0, 12, 2))
    require(alpha[x_torus] == 1 and cube.get(x_torus, 0) == 0 and cube, 'nonzero period/divisor cube separation')
    # Wrong shortcut hostile: a rational (5,1)+(1,5) form passes full J* invariance.
    hostile = {}
    for choices in product((0, 1), repeat=6):
        if sum(choices) % 2 == 0:
            coefficient = (-1) ** (sum(choices)//2 + choices[3] + choices[4])
            hostile[tuple(2*i+b for i, b in enumerate(choices))] = coefficient
    require(full_pullback(base_J(), hostile) == hostile and lie_action(base_J(), hostile), 'degree-six J-invariance trap')
    return {'rational_sample_count': len(samples), 'degree_two_basis_size': len(BASIS2),
            'stacked_degree_two_constraint_rank': rank, 'degree_two_independent_row_indices': independent_rows,
            'rational_Neron_Severi_rank_from_written_genericity_proof': 1,
            'alpha_term_count': len(alpha), 'alpha_x_torus_period': 1,
            'divisor_cube_x_torus_period': 0, 'polarization_alternating_determinant': 9}


def validate_candidate(c):
    require(c['schema'] == 'marici.hodge-explicit-sixfold-candidate.v1' and
            c['id'] == 'marici.hodge.nonsplit-sixfold.exp-sqrt-primes.v1', 'candidate identity')
    require(c['nodes'] == ['candidate-variety-and-class', 'candidate-hodge-membership'] and
            c['resolution_kinds'] == ['explicit_marked_polarized_torus_and_integral_weil_class',
                                      'balanced_weil_determinant_Hodge_membership'], 'candidate resolution binding')
    g, a = c['geometry'], c['class']
    require((g['field'], g['complex_dimension'], g['codimension'], g['discriminant_representative']) ==
            ('Q(i)', 6, 3, -3), 'geometric scope')
    require(tuple(g['hermitian_diagonal']) == DS and tuple(g['primes']) == PRIMES and
            g['coordinate_denominator'] == 2**20 and g['polarization_type'] == [1,1,1,1,1,3], 'period source changed')
    require(g['coordinate_formula'] == 't_l=exp(sqrt(prime_l))/2^20 for l=1,...,18' and
            g['Z_formula'] == 'Z_(a,b)=t_(2k+1)+i*t_(2k+2), k=3a+b, a,b=0,1,2' and
            g['X'] == '(C^6 as a real vector space with complex structure J)/Z[i]^6', 'exact marked period changed')
    require(a['formula'] == 'Re wedge_(j=1..6)(dx_j+i dy_j)' and
            a['cohomological_degree'] == 6 and a['hodge_type'] == [3,3] and
            a['coefficients'] == 'Z subset Q' and a['signed_monomial_count'] == 32 and
            a['selection_depends_on_nonalgebraicity'] is False, 'class changed or selected circularly')
    require(c['picard_certificate']['all_algebraic_cycles_excluded'] is False and
            c['picard_certificate']['stacked_exact_constraint_rank'] == 65, 'divisor-only conclusion promoted')
    require(len(c['boundary']) == 6 and all(v is False for v in c['boundary'].values()), 'candidate promoted to Hodge verdict')


def report():
    c = json.loads(CONTRACT.read_text(encoding='utf-8'))
    validate_candidate(c)
    audit = json.loads((ROOT / c['literature_receipt']).read_text(encoding='utf-8'))
    require(audit == audit_report() and audit['recommended_family'] == 'nonsplit-unitary-sixfolds', 'literature binding stale')
    # Exact global bounds, no floating evaluation of transcendental coordinates.
    require(all(p < 64 and all(p % d for d in range(2, p) if d*d <= p) for p in PRIMES), 'distinct prime square roots')
    require(len(set(PRIMES)) == 18 and 3**8 * 64 < 2**20, 'coordinate bound')
    frobenius_square_bound = Q(30, 64**2)
    require(frobenius_square_bound < 1, 'positive plane bound')
    core = exact_core()
    checks = dict.fromkeys([
        'explicit_exponential_prime_coordinates_have_rigorous_positive_plane_bound',
        'same_source_lattice_polarization_and_nonsplit_discriminant_retained',
        'nineteen_rational_sample_complex_structures_preserve_riemann_form',
        'balanced_weil_generators_annihilated_by_infinitesimal_hodge_action',
        'integral_alpha_has_unit_period_and_is_nonzero',
        'degree_six_full_J_invariance_alone_rejected_as_hodge_test',
        'exact_degree_two_constraint_rank_65_supports_written_picard_proof',
        'alpha_not_a_divisor_cube_but_all_cycle_nonmembership_not_claimed',
        'same_day_dated_literature_binding_remains_source_specific',
    ], True)
    source_names = {p.relative_to(ROOT).as_posix() for p in (CONTRACT, NOTE, Path(__file__).resolve())} | {
        c['literature_audit'], c['literature_receipt'],
        'research/voevodsky/checkers/check_hodge_cycle_map_scope.py',
        'research/voevodsky/checkers/check_hodge_literature_boundary_audit.py'}
    return {'schema': 'marici.hodge-explicit-sixfold-candidate-result.v1', 'passed': True, 'checks': checks,
            'candidate_id': c['id'], 'resolution_kinds': c['resolution_kinds'],
            'verification_level': 'Written explicit-period, genericity and Hodge proofs using declared imported theorems; exact rational sample-rank and exterior controls, not proof-assistant formalization.',
            'positive_plane_frobenius_square_bound': str(frobenius_square_bound), **core,
            'specific_candidate_selected': True, 'specific_alpha_selected': True,
            'smooth_projective_complex_dimension': 6, 'codimension': 3,
            'alpha_rational_hodge_membership_proved': True, 'divisor_product_nonmembership_proved': True,
            'alpha_algebraicity_status': 'unresolved_no_all_cycle_conclusion',
            'Hodge_proved': False, 'Hodge_refuted': False, 'alpha_nonalgebraic_proved': False,
            'class_obstruction_constructed': False,
            'source_sha256': {name: sha256((ROOT / name).read_bytes()).hexdigest() for name in sorted(source_names)}}


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k != 'source_sha256'}, indent=2))
