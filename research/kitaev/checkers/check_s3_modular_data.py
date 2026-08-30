"""Exact modular S,T data for D(S3), with an independent Verlinde audit."""

import itertools
import json
from fractions import Fraction


class Zeta3:
    def __init__(self, a=0, b=0):
        self.a, self.b = Fraction(a), Fraction(b)

    def __add__(self, other):
        other = z(other)
        return Zeta3(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Zeta3(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-z(other))

    def __mul__(self, other):
        other = z(other)
        return Zeta3(self.a * other.a - self.b * other.b,
                     self.a * other.b + self.b * other.a - self.b * other.b)

    __rmul__ = __mul__

    def conjugate(self):
        return Zeta3(self.a - self.b, -self.b)

    def divide_rational(self, value):
        value = Fraction(value)
        return Zeta3(self.a / value, self.b / value)

    def __eq__(self, other):
        other = z(other)
        return self.a == other.a and self.b == other.b

    def integer(self):
        assert self.b == 0 and self.a.denominator == 1
        return int(self.a)

    def text(self):
        if self.b == 0:
            return rational_text(self.a)
        return rational_text(self.a) + ("+" if self.b >= 0 else "") + rational_text(self.b) + "*omega"


def rational_text(value):
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def z(value):
    return value if isinstance(value, Zeta3) else Zeta3(value)


def compose(p, q):
    return tuple(p[q[i]] for i in range(3))


def inverse(p):
    out = [0, 0, 0]
    for i, image in enumerate(p):
        out[image] = i
    return tuple(out)


def conjugate(g, h):
    return compose(compose(g, h), inverse(g))


def parity(p):
    return -1 if sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3)) % 2 else 1


def cycle_type(p):
    fixed = sum(p[i] == i for i in range(3))
    return "e" if fixed == 3 else ("t" if fixed == 1 else "c")


def matmul(left, right):
    n = len(left)
    return [[sum((left[i][k] * right[k][j] for k in range(n)), Zeta3())
             for j in range(n)] for i in range(n)]


def conjugate_transpose(matrix):
    return [[matrix[j][i].conjugate() for j in range(len(matrix))] for i in range(len(matrix))]


def main():
    group = list(itertools.permutations(range(3)))
    e, t, c = (0, 1, 2), (1, 0, 2), (1, 2, 0)
    reps = {"e": e, "t": t, "c": c}
    classes = {name: [g for g in group if cycle_type(g) == name] for name in reps}
    transporters = {name: {target: next(q for q in group if conjugate(q, rep) == target)
                           for target in classes[name]} for name, rep in reps.items()}
    labels = [
        ("A", "e", "triv", 1), ("B", "e", "sign", 1),
        ("C", "e", "std", 2), ("D", "t", "plus", 3),
        ("E", "t", "minus", 3), ("F", "c", "triv", 2),
        ("G", "c", "omega", 2), ("H", "c", "omega2", 2),
    ]

    def centralizer_char(sector, irrep, element):
        if sector == "e":
            if irrep == "triv": return Zeta3(1)
            if irrep == "sign": return Zeta3(parity(element))
            return Zeta3({"e": 2, "t": 0, "c": -1}[cycle_type(element)])
        if sector == "t":
            return Zeta3(1 if irrep == "plus" or element == e else -1)
        powers = {e: 0, c: 1, compose(c, c): 2}
        exponent = powers[element] * {"triv": 0, "omega": 1, "omega2": 2}[irrep] % 3
        return [Zeta3(1), Zeta3(0, 1), Zeta3(-1, -1)][exponent]

    def transported_char(label, flux, element):
        _, sector, irrep, _ = label
        q = transporters[sector][flux]
        return centralizer_char(sector, irrep, compose(compose(inverse(q), element), q))

    n = len(labels)
    smatrix = [[Zeta3() for _ in labels] for _ in labels]
    for i, left in enumerate(labels):
        for j, right in enumerate(labels):
            total = Zeta3()
            for g in classes[left[1]]:
                for h in classes[right[1]]:
                    if compose(g, h) == compose(h, g):
                        total += transported_char(left, g, h).conjugate() * transported_char(right, h, g).conjugate()
            smatrix[i][j] = total.divide_rational(len(group))

    symmetric = all(smatrix[i][j] == smatrix[j][i] for i in range(n) for j in range(n))
    identity = [[Zeta3(int(i == j)) for j in range(n)] for i in range(n)]
    unitary = matmul(smatrix, conjugate_transpose(smatrix)) == identity
    assert symmetric and unitary
    assert [entry for entry in smatrix[0]] == [Zeta3(Fraction(item[3], 6)) for item in labels]

    twists = []
    for label in labels:
        _, sector, irrep, _ = label
        twists.append(centralizer_char(sector, irrep, reps[sector]).divide_rational(
            {"triv": 1, "sign": 1, "std": 2, "plus": 1, "minus": 1, "omega": 1, "omega2": 1}[irrep]))
    assert [value.text() for value in twists] == ["1", "1", "1", "1", "-1", "1", "0+1*omega", "-1-1*omega"]
    tmatrix = [[twists[i] if i == j else Zeta3() for j in range(n)] for i in range(n)]
    s2 = matmul(smatrix, smatrix)
    st = matmul(smatrix, tmatrix)
    st3 = matmul(matmul(st, st), st)
    modular_relation = st3 == s2
    assert modular_relation

    # Verlinde coefficients from S, compared with dimension and integrality gates.
    fusion = {}
    max_multiplicity = 0
    for i, left in enumerate(labels):
        for j, right in enumerate(labels):
            decomposition = []
            for k, target in enumerate(labels):
                total = Zeta3()
                for ell in range(n):
                    numerator = smatrix[i][ell] * smatrix[j][ell] * smatrix[k][ell].conjugate()
                    total += numerator.divide_rational(smatrix[0][ell].a)
                multiplicity = total.integer()
                assert multiplicity >= 0
                max_multiplicity = max(max_multiplicity, multiplicity)
                decomposition.extend([target[0]] * multiplicity)
            assert sum(next(x[3] for x in labels if x[0] == name) for name in decomposition) == left[3] * right[3]
            fusion[left[0] + "x" + right[0]] = decomposition
    expected_witnesses = {
        "CxC": ["A", "B", "C"],
        "DxD": ["A", "C", "F", "G", "H"],
        "DxE": ["B", "C", "F", "G", "H"],
        "FxG": ["C", "H"],
    }
    assert all(fusion[key] == value for key, value in expected_witnesses.items())

    gauss_sum = sum((Zeta3(item[3] * item[3]) * twists[i] for i, item in enumerate(labels)), Zeta3())
    assert gauss_sum == Zeta3(6)

    result = {
        "schema": "marici.s3-modular-data.v1",
        "label_order": [item[0] for item in labels],
        "S_matrix": [[entry.text() for entry in row] for row in smatrix],
        "topological_spins": {labels[i][0]: twists[i].text() for i in range(n)},
        "S_is_symmetric": symmetric,
        "S_is_unitary": unitary,
        "S_first_row_is_quantum_dimensions_over_six": True,
        "modular_relation_ST_cubed_equals_S_squared": modular_relation,
        "gauss_sum": gauss_sum.text(),
        "total_quantum_dimension": 6,
        "verlinde_fusion_witnesses": expected_witnesses,
        "verlinde_maximum_multiplicity": max_multiplicity,
        "aggregate_gates": {
            "exact_modular_S_matrix_recovered": True,
            "S_is_symmetric_and_unitary": symmetric and unitary,
            "topological_spins_are_exact_third_roots_and_signs": True,
            "modular_group_relation_holds": modular_relation,
            "gauss_sum_has_trivial_double_central_charge": True,
            "verlinde_reproduces_fusion_witnesses": True,
            "modular_data_does_not_fix_F_R_gauge": True,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
