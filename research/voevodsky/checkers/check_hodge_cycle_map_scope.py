"""Typed scope and exact linear descent controls; no variety/counterexample invented."""
from fractions import Fraction as Q
from itertools import product
from hashlib import sha256
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = ROOT / 'research/conjecture_net/contracts/hodge-cycle-map-scope.v1.json'
NOTE = ROOT / 'research/voevodsky/hodge-cycle-map-scope-v1.md'
OUT = ROOT / 'research/voevodsky/results/hodge-cycle-map-scope-v1.json'


def require(condition, message):
    if not condition:
        raise ValueError(message)


def rref(matrix, variable_columns=None):
    a = [list(map(Q, row)) for row in matrix]
    columns = len(a[0]) if variable_columns is None else variable_columns
    pivots = []
    for j in range(columns):
        pivot = next((i for i in range(len(pivots), len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        r = len(pivots)
        a[r], a[pivot] = a[pivot], a[r]
        c = a[r][j]
        a[r] = [x / c for x in a[r]]
        for i in range(len(a)):
            if i != r:
                c = a[i][j]
                a[i] = [x - c * y for x, y in zip(a[i], a[r])]
        pivots.append(j)
    return a, pivots


def nullspace(s):
    reduced, pivots = rref(s)
    basis = []
    for free in range(len(s[0])):
        if free not in pivots:
            vector = [Q(0)] * len(s[0])
            vector[free] = Q(1)
            for i, pivot in enumerate(pivots):
                vector[pivot] = -reduced[i][free]
            basis.append(tuple(vector))
    return tuple(basis)


def multiply(a, b):
    return tuple(tuple(sum(x * y for x, y in zip(row, col)) for col in zip(*b)) for row in a)


def factor(s, f):
    """Find T with TS=F, choosing free extension coefficients zero; or None.
    A returned extension on the whole displayed H need not be canonical/unique.
    """
    result = []
    m = len(s)
    for row in f:
        equations = [list(column) + [value] for column, value in zip(zip(*s), row)]
        reduced, pivots = rref(equations, m)
        if any(not any(eq[:m]) and eq[m] for eq in reduced):
            return None
        answer = [Q(0)] * m
        for i, pivot in enumerate(pivots):
            answer[pivot] = reduced[i][m]
        result.append(tuple(answer))
    return tuple(result)


def validate_scope(c):
    require(c['schema'] == 'marici.hodge-cycle-map-scope.v1' and c['coefficients'] == 'Q', 'scope coefficients')
    require(c['node'] == 'scope-and-cycle-map' and
            c['resolution_kind'] == 'typed_scope_definition_and_linear_descent_lemma', 'scope binding')
    require(set(c['objects']) == {'X', 'Z', 'R_rat', 'CH', 'H', 'P', 'R_packet', 'V'}, 'typed object inventory')
    maps = {m['id']: m for m in c['maps']}
    require(len(maps) == len(c['maps']) == 6, 'typed map inventory')
    expected = {'q': ('Z', 'CH'), 'cl': ('CH', 'H'), 'a': ('R_packet', 'Z'),
                's': ('R_packet', 'H'), 'F': ('R_packet', 'V'), 'O': ('H', 'V')}
    require({k: (v['source'], v['target']) for k, v in maps.items()} == expected, 'map type mismatch')
    require(maps['a']['status'] == 'open_packet_generation_bridge' and maps['s']['formula'] == 'cl o q o a', 'unproved generation bridge')
    require(maps['cl']['claim'] == 'surjectivity_is_the_Hodge_question_not_an_assumption', 'surjectivity assumption')
    require(c['descent_lemma']['domain_of_unique_factor'] == 'im(s)' and
            c['descent_lemma']['full_H_extension_unique_without_surjectivity'] is False and
            c['descent_lemma']['Hodge_surjectivity_used'] is False, 'image/full-target conflation')
    require(set(c['admitted_scope_operations']) == {'finite_cycle_addition', 'rational_scaling_including_negative_coefficients',
            'rational_equivalence_quotient', 'cohomology_class_comparison', 'transport_along_isomorphisms_with_explicit_maps'}, 'operation scope')
    require(len(c['boundary']) == 8 and all(v is False for v in c['boundary'].values()), 'scope promoted')


def serial(x):
    if isinstance(x, Q):
        return str(x)
    if isinstance(x, dict):
        return {k: serial(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [serial(v) for v in x]
    return x


def report():
    c = json.loads(CONTRACT.read_text(encoding='utf-8'))
    validate_scope(c)
    # Formal rational presentation model only; not the cycle map of a selected X.
    s = ((Q(1), Q(0), Q(1)), (Q(0), Q(1), Q(1)), (Q(0), Q(0), Q(0)))
    kernel = nullspace(s)
    require(kernel == ((Q(-1), Q(-1), Q(1)),), 'kernel model')
    good, bad = ((Q(2), Q(-1), Q(1)),), ((Q(0), Q(0), Q(1)),)
    good_factor = factor(s, good)
    require(good_factor is not None and multiply(good_factor, s) == good, 'valid descent')
    require(factor(s, bad) is None and multiply(bad, tuple(zip(*kernel))) == ((Q(1),),), 'witness-sensitive reader should not descend')
    # Same class represented by e3 and e1+e2; the bad reader separates them.
    one, two = ((Q(0),), (Q(0),), (Q(1),)), ((Q(1),), (Q(1),), (Q(0),))
    require(multiply(s, one) == multiply(s, two), 'same-class model')
    require(multiply(bad, one) != multiply(bad, two), 'erasure hostile missing')
    alternate = ((Q(2), Q(-1), Q(7)),)
    require(multiply(alternate, s) == good and alternate != good_factor, 'extension ambiguity')
    missing = ((Q(0),), (Q(0),), (Q(1),))
    require(multiply(alternate, missing) != multiply(good_factor, missing), 'complement ambiguity')
    zero, zero_alternate = ((Q(0), Q(0), Q(0)),), ((Q(0), Q(0), Q(7)),)
    require(multiply(zero, s) == multiply(zero_alternate, s) == ((0, 0, 0),), 'zero-reader extensions')
    require(multiply(zero, missing) != multiply(zero_alternate, missing), 'annihilation does not select extension')
    surjective = s[:2]
    require(nullspace(tuple(zip(*surjective))) == (), 'surjective extension uniqueness')
    require(factor(surjective, good) == ((Q(2), Q(-1)),), 'surjective factor')
    # If specified algebraic classes span H, annihilation forces the detector zero.
    identity = ((Q(1), Q(0)), (Q(0), Q(1)))
    require(factor(identity, ((Q(0), Q(0)),)) == ((Q(0), Q(0)),), 'positive span control')

    cases = 0
    for entries in product((-1, 0, 1), repeat=4):
        matrix = (tuple(map(Q, entries[:2])), tuple(map(Q, entries[2:])))
        basis = nullspace(matrix)
        require(all(multiply(matrix, tuple((v,) for v in vector)) == ((0,), (0,)) for vector in basis), 'kernel certificate')
        for values in product((-1, 0, 1), repeat=2):
            reader = (tuple(map(Q, values)),)
            kills_kernel = all(sum(x * y for x, y in zip(reader[0], vector)) == 0 for vector in basis)
            solution = factor(matrix, reader)
            require((solution is not None) == kills_kernel, 'descent equivalence')
            if solution is not None:
                require(multiply(solution, matrix) == reader, 'factor certificate')
            cases += 1
    require(cases == 729, 'bounded census')
    checks = {
        'typed_cycle_and_packet_maps_keep_generation_bridge_open': True,
        'rational_cycle_combinations_and_kernel_policy_frozen': True,
        'witness_sensitive_reader_fails_cohomology_descent': True,
        'kernel_annihilating_reader_has_exact_factor': True,
        'factor_unique_only_on_image_without_surjectivity': True,
        'different_extensions_agree_on_source_but_differ_off_image': True,
        'surjective_target_control_has_unique_factor': True,
        'algebraic_spanning_control_forces_zero_detector': True,
        'all_729_small_rational_matrix_reader_pairs_satisfy_descent_criterion': True,
    }
    return {
        'schema': 'marici.hodge-cycle-map-scope.v1', 'passed': all(checks.values()), 'checks': checks,
        'resolution_kind': c['resolution_kind'],
        'verification_level': 'Written general linear descent proof plus exact finite rational controls; standard cycle-class facts imported, not proof-assistant formalization.',
        'formal_model': {'s': serial(s), 'kernel_basis': serial(kernel), 'valid_reader': serial(good),
                         'invalid_reader': serial(bad), 'extension_one': serial(good_factor), 'extension_two': serial(alternate),
                         'zero_reader_extensions': serial((zero, zero_alternate)),
                         'variety_realization_claimed': False},
        'packet_bridge_constructed': False, 'specific_obstruction_constructed': False,
        'Hodge_proved': False, 'Hodge_refuted': False,
        'source_sha256': {p.relative_to(ROOT).as_posix(): sha256(p.read_bytes()).hexdigest()
                          for p in (CONTRACT, NOTE, Path(__file__).resolve())},
    }


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k not in ('formal_model', 'source_sha256')}, indent=2))
