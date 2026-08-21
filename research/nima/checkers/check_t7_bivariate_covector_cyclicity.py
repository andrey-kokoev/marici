#!/usr/bin/env python3
"""Replicated finite-field bivariate cyclicity test on the frozen T7 kernel."""
import hashlib
import json
from pathlib import Path

DEPTH = 7
JET_ORDER = 2 * DEPTH


class Jet:
    prime = 0

    def __init__(self, coeffs=0):
        if isinstance(coeffs, int):
            coeffs = {(0, 0): coeffs}
        self.c = {k: v % self.prime for k, v in coeffs.items()
                  if sum(k) < JET_ORDER and v % self.prime}

    def __add__(self, other):
        other = asjet(other)
        keys = self.c.keys() | other.c.keys()
        return Jet({k: self.c.get(k, 0) + other.c.get(k, 0) for k in keys})

    __radd__ = __add__

    def __neg__(self):
        return Jet({k: -v for k, v in self.c.items()})

    def __sub__(self, other):
        return self + (-asjet(other))

    def __rsub__(self, other):
        return asjet(other) - self

    def __mul__(self, other):
        other = asjet(other)
        out = {}
        for (i, j), a in self.c.items():
            for (k, ell), b in other.c.items():
                if i + j + k + ell < JET_ORDER:
                    key = (i + k, j + ell)
                    out[key] = out.get(key, 0) + a * b
        return Jet(out)

    __rmul__ = __mul__

    def inverse(self):
        a0 = self.c.get((0, 0), 0)
        if not a0:
            raise ZeroDivisionError("zero jet constant")
        q = (self - a0) / a0
        term, ans = Jet(1), Jet(1)
        for _ in range(1, JET_ORDER):
            term = -term * q
            ans = ans + term
        return ans / a0 if a0 != 1 else ans

    def __truediv__(self, other):
        if isinstance(other, int):
            return self * pow(other % self.prime, self.prime - 2, self.prime)
        return self * asjet(other).inverse()

    def __rtruediv__(self, other):
        return asjet(other) * self.inverse()

    def __pow__(self, n):
        if n < 0:
            return self.inverse() ** (-n)
        ans, base = Jet(1), self
        while n:
            if n & 1:
                ans = ans * base
            base = base * base
            n >>= 1
        return ans

    def derivative(self, axis):
        out = {}
        for (i, j), value in self.c.items():
            exponent = i if axis == 0 else j
            if exponent:
                key = (i - 1, j) if axis == 0 else (i, j - 1)
                out[key] = out.get(key, 0) + exponent * value
        return Jet(out)

    def zero(self):
        return not self.c


def asjet(value):
    return value if isinstance(value, Jet) else Jet(value)


def zeros(rows, cols):
    return [[Jet(0) for _ in range(cols)] for _ in range(rows)]


def mm(left, right):
    out = zeros(len(left), len(right[0]))
    for i in range(len(left)):
        for k in range(len(right)):
            if not left[i][k].zero():
                for j in range(len(right[0])):
                    out[i][j] = out[i][j] + left[i][k] * right[k][j]
    return out


def madd(left, right):
    return [[left[i][j] + right[i][j] for j in range(len(left[0]))]
            for i in range(len(left))]


def mdiff(matrix, axis):
    return [[value.derivative(axis) for value in row] for row in matrix]


def rref_data(matrix, prime):
    a = [[value % prime for value in row] for row in matrix]
    row = 0
    pivots = []
    for col in range(len(a[0])):
        pivot = next((i for i in range(row, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        inv = pow(a[row][col], prime - 2, prime)
        a[row] = [x * inv % prime for x in a[row]]
        for i in range(len(a)):
            if i != row and a[i][col]:
                q = a[i][col]
                a[i] = [(a[i][j] - q * a[row][j]) % prime for j in range(len(a[0]))]
        row += 1
        pivots.append(col)
    return row, a, pivots


def rank(matrix, prime):
    return rref_data(matrix, prime)[0]


def null_vector(matrix, prime):
    r, reduced, pivots = rref_data(matrix, prime)
    if r == len(matrix[0]):
        return None
    free = next(col for col in range(len(matrix[0])) if col not in pivots)
    vector = [0] * len(matrix[0])
    vector[free] = 1
    for row, pivot in enumerate(pivots):
        vector[pivot] = -reduced[row][free] % prime
    return vector


def one_prime(packet, prime, seeds, point):
    Jet.prime = prime
    u = Jet({(0, 0): point[0], (1, 0): 1})
    v = Jet({(0, 0): point[1], (0, 1): 1})
    env = {"u": u, "v": v}
    au = [[asjet(eval(q, {"__builtins__": {}}, env)) for q in row]
          for row in packet["connection_u"]]
    av = [[asjet(eval(q, {"__builtins__": {}}, env)) for q in row]
          for row in packet["connection_v"]]
    x, y, energy = Jet(1), (u + v) / 2 - 1, u
    valg = [Jet(0)] * 6 + [
        (x**2 - y**2) * (x**2 * y**2 - energy**4),
        2 * x**2 * (energy**2 + y**2),
        -2 * y**2 * (energy**2 + x**2),
    ]
    embedding = zeros(9, 7)
    for i in range(6):
        embedding[i][i] = Jet(1)
    for i in range(9):
        embedding[i][6] = valg[i]

    induced = []
    for axis, ambient in enumerate((au, av)):
        transported = madd(mdiff(embedding, axis), mm(ambient, embedding))
        conn = zeros(7, 7)
        pivot = embedding[7][6]
        for column in range(7):
            for row in range(6):
                conn[row][column] = transported[row][column]
            conn[6][column] = transported[7][column] / pivot
            reconstructed = mm(embedding, [[conn[i][column]] for i in range(7)])
            assert all((transported[row][column] - reconstructed[row][0]).zero()
                       for row in range(9))
        induced.append(conn)

    trials = []
    all_rows = []
    for seed in seeds:
        orbit = {(0, 0): [[Jet(value) for value in seed]]}
        rows = []
        def apply_direction(prior, axis):
            derivative = mdiff(prior, axis)
            product = mm(prior, induced[axis])
            return [[derivative[0][k] - product[0][k] for k in range(7)]]
        for total in range(DEPTH):
            for i in range(total + 1):
                j = total - i
                if (i, j) != (0, 0):
                    if i:
                        prior, axis = orbit[(i - 1, j)], 0
                    else:
                        prior, axis = orbit[(i, j - 1)], 1
                    orbit[(i, j)] = apply_direction(prior, axis)
                    if i and j:
                        alternate = apply_direction(orbit[(i, j - 1)], 1)
                        assert all((orbit[(i, j)][0][k] - alternate[0][k]).c.get((0, 0), 0) == 0
                                   for k in range(7))
                rows.append([value.c.get((0, 0), 0) for value in orbit[(i, j)][0]])
        trial_rank = rank(rows, prime)
        all_rows.append(rows)
        trials.append({"seed": seed, "rank": trial_rank,
                       "null_vector": null_vector(rows, prime) if trial_rank == 6 else None})
    maximum = max(item["rank"] for item in trials)
    first_conservative_pair = None
    for left in range(len(seeds)):
        for right in range(left + 1, len(seeds)):
            if rank(all_rows[left] + all_rows[right], prime) == 7:
                first_conservative_pair = [seeds[left], seeds[right]]
                break
        if first_conservative_pair is not None:
            break
    assert first_conservative_pair is not None
    return {"prime": prime, "point": list(point), "maximum_rank": maximum,
            "first_maximum": next(item for item in trials if item["rank"] == maximum),
            "first_conservative_pair": first_conservative_pair,
            "coordinate_covector_ranks": [item["rank"] for item in trials[:7]],
            "trial_count": len(trials)}


def main():
    root = Path(__file__).resolve().parents[3]
    packet = json.loads((root / "research/benincasa/bivariate_soft_gram_connection.json").read_text())
    seeds = [[1 if i == j else 0 for i in range(7)] for j in range(7)]
    seeds += [[1] * 7, [1, -1, 1, -1, 1, -1, 1], [1, 2, 4, 8, 16, 32, 64]]
    state = 17
    for _ in range(32):
        row = []
        for _ in range(7):
            state = (1103515245 * state + 12345) & 0x7fffffff
            row.append(state % 11 - 5)
        seeds.append(row)
    replications = [one_prime(packet, p, seeds, point)
                    for point in ((3, 1), (4, 1), (5, 3))
                    for p in (1_000_000_007, 1_000_000_009)]
    assert all(item["maximum_rank"] == 6 for item in replications)
    assert all(item["first_maximum"]["seed"] == [1] * 7 for item in replications)
    assert all([i for i, value in enumerate(item["first_maximum"]["null_vector"]) if value]
               == [1, 2, 3, 4] for item in replications)
    conservative_pairs = [item["first_conservative_pair"] for item in replications]
    assert all(pair == conservative_pairs[0] for pair in conservative_pairs)
    coordinate_rank_profiles = [item["coordinate_covector_ranks"] for item in replications]
    assert all(profile == coordinate_rank_profiles[0] for profile in coordinate_rank_profiles)
    result = {
        "schema": "marici.nima.t7_bivariate_constant_covector_cyclicity.v1",
        "passed": True,
        "basis": ["e1", "e2", "e3", "e4", "e5", "e6", "v_alg"],
        "points": [[3, 1], [4, 1], [5, 3]],
        "primes": [1_000_000_007, 1_000_000_009],
        "maximum_rank": 6,
        "minimum_constant_readout_count_for_full_rank": 2,
        "first_conservative_pair": conservative_pairs[0],
        "coordinate_covector_ranks": dict(zip(
            ["e1", "e2", "e3", "e4", "e5", "e6", "v_alg"],
            coordinate_rank_profiles[0])),
        "jet_total_degree_max": DEPTH - 1,
        "constant_covectors_tested_per_replication": len(seeds),
        "first_maximum_seed": [1] * 7,
        "blind_direction_support_for_first_maximum": ["e2", "e3", "e4", "e5"],
        "mixed_derivative_base_jets_commute": True,
        "interpretation": "the full bivariate connection raises the one-readout constant-covector ceiling from five to six; a second constant readout makes the bounded orbit jointly conservative",
        "scope": "bounded census of 42 constant source-frame covectors at three generic rational points; not the physical Bunch-Davies covector and not a census of rationally varying covectors",
    }
    output = root / "research/nima/results/t7-bivariate-constant-covector-cyclicity.json"
    payload = output.read_text(encoding="utf-8")
    if json.loads(payload) != result:
        print(json.dumps(result, indent=2))
    assert json.loads(payload) == result
    print(json.dumps({"passed": True, "maximum_rank": 6,
                      "sha256": hashlib.sha256(payload.encode()).hexdigest().upper()}))


if __name__ == "__main__":
    main()
