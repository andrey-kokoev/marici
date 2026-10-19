"""Conditional control generators and exact real Lie closure for the finite pilot.

Candidate generators are mathematical source extensions, not physical actuators.
The existing native pair is never changed or silently promoted.
"""
from fractions import Fraction as F
from itertools import combinations
from check_structural_pilot_transport import identity, zeros, add, scale, complex_mul, transpose
from check_pilot_capabilities import tensor, flatten
from pilot_carrier import Operation, native_permutation
from pilot_observers import factor_generators


def subtract(a, b):
    return add(a[0], scale(-1, b[0])), add(a[1], scale(-1, b[1]))


def commutator(a, b):
    return subtract(complex_mul(a, b), complex_mul(b, a))


def skew_generator(real_h):
    # The common pi scale is nonzero and does not change a real Lie span.
    return zeros(4), scale(-1, real_h)


def projector_from_involution(real):
    return scale(F(1, 2), add(identity(4), scale(-1, real)))


def exchange_matrix():
    result = zeros(4)
    for column in range(4):
        result[2 * (column % 2) + column // 2][column] = F(1)
    return result


def candidate_families():
    left = [list(row) for row in native_permutation(Operation.LEFT)]
    right = [list(row) for row in native_permutation(Operation.RIGHT)]
    native = [projector_from_involution(left), projector_from_involution(right)]
    exchange = projector_from_involution(exchange_matrix())
    axes = factor_generators()
    zleft = tensor(axes['Z'], axes['I'])[0]
    zright = tensor(axes['I'], axes['Z'])[0]
    phase = [projector_from_involution(zleft), projector_from_involution(zright)]
    transpositions = []
    for a, b in combinations(range(4), 2):
        matrix = identity(4)
        matrix[a][a] = matrix[b][b] = F(0)
        matrix[a][b] = matrix[b][a] = F(1)
        transpositions.append(projector_from_involution(matrix))
    return {
        'native-local': native,
        'native-plus-exchange': native + [exchange],
        'all-label-transpositions': transpositions,
        'native-plus-local-phase': native + phase,
        'local-phase-plus-exchange': native + phase + [exchange]
    }


class RealSpan:
    """Exact reduced-row basis; independence never uses a float tolerance."""
    def __init__(self):
        self.rows = {}

    def add(self, vector):
        row = [F(value) for value in vector]
        for pivot, basis in sorted(self.rows.items()):
            factor = row[pivot]
            if factor:
                row = [value - factor * known for value, known in zip(row, basis)]
        pivot = next((i for i, value in enumerate(row) if value), None)
        if pivot is None:
            return False
        divisor = row[pivot]
        row = [value / divisor for value in row]
        for existing, basis in tuple(self.rows.items()):
            factor = basis[pivot]
            if factor:
                self.rows[existing] = [value - factor * known for value, known in zip(basis, row)]
        self.rows[pivot] = row
        return True

    def matrices(self):
        return [([row[4*i:4*i+4] for i in range(4)],
                 [row[16+4*i:16+4*i+4] for i in range(4)])
                for _, row in sorted(self.rows.items())]


def is_skew_hermitian(matrix):
    real, imag = matrix
    return transpose(real) == scale(-1, real) and transpose(imag) == imag


def lie_closure(hamiltonians):
    span = RealSpan()
    for h in hamiltonians:
        matrix = skew_generator(h)
        if not is_skew_hermitian(matrix):
            raise ValueError('control Hamiltonian must be real symmetric')
        span.add(flatten(matrix[0]) + flatten(matrix[1]))
    rounds = 0
    while True:
        changed = False
        basis = span.matrices()
        for a, b in combinations(basis, 2):
            bracket = commutator(a, b)
            if not is_skew_hermitian(bracket):
                raise ValueError('Lie bracket left the skew-Hermitian domain')
            changed |= span.add(flatten(bracket[0]) + flatten(bracket[1]))
        rounds += 1
        if len(span.rows) > 16:
            raise ValueError('skew-Hermitian real dimension exceeded')
        if not changed:
            return span.matrices(), rounds


def fixes_uniform(matrix):
    return all(sum(row) == 0 for part in matrix for row in part)
