"""Exact D(S3) fusion ring from induced characters on commuting pairs."""

import itertools
import json
from fractions import Fraction


class Zeta3:
    """Exact a+b*w with w^2+w+1=0."""

    def __init__(self, a=0, b=0):
        self.a = Fraction(a)
        self.b = Fraction(b)

    def __add__(self, other):
        other = as_zeta(other)
        return Zeta3(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __mul__(self, other):
        other = as_zeta(other)
        return Zeta3(
            self.a * other.a - self.b * other.b,
            self.a * other.b + self.b * other.a - self.b * other.b,
        )

    __rmul__ = __mul__

    def conjugate(self):
        return Zeta3(self.a - self.b, -self.b)

    def divide_int(self, n):
        return Zeta3(self.a / n, self.b / n)

    def __eq__(self, other):
        other = as_zeta(other)
        return self.a == other.a and self.b == other.b

    def integer(self):
        assert self.b == 0 and self.a.denominator == 1
        return int(self.a)


def as_zeta(value):
    return value if isinstance(value, Zeta3) else Zeta3(value, 0)


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
    inversions = sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3))
    return -1 if inversions % 2 else 1


def cycle_type(p):
    fixed = sum(p[i] == i for i in range(3))
    return "e" if fixed == 3 else ("t" if fixed == 1 else "c")


def main():
    group = list(itertools.permutations(range(3)))
    e = (0, 1, 2)
    t = (1, 0, 2)
    c = (1, 2, 0)
    representatives = {"e": e, "t": t, "c": c}
    classes = {name: [g for g in group if cycle_type(g) == name] for name in representatives}

    # q maps the frozen representative to each element in its conjugacy class.
    transporters = {}
    for name, elements in classes.items():
        rep = representatives[name]
        transporters[name] = {}
        for target in elements:
            transporters[name][target] = next(q for q in group if conjugate(q, rep) == target)

    labels = [
        ("A", "e", "triv", 1),
        ("B", "e", "sign", 1),
        ("C", "e", "std", 2),
        ("D", "t", "plus", 3),
        ("E", "t", "minus", 3),
        ("F", "c", "triv", 2),
        ("G", "c", "omega", 2),
        ("H", "c", "omega2", 2),
    ]

    def centralizer_character(sector, irrep, z):
        if sector == "e":
            if irrep == "triv":
                return Zeta3(1)
            if irrep == "sign":
                return Zeta3(parity(z))
            return Zeta3({"e": 2, "t": 0, "c": -1}[cycle_type(z)])
        if sector == "t":
            if irrep == "plus":
                return Zeta3(1)
            return Zeta3(1 if z == e else -1)
        # z is c^power in C3.
        powers = {e: 0, c: 1, compose(c, c): 2}
        power = powers[z]
        exponent = power * {"triv": 0, "omega": 1, "omega2": 2}[irrep] % 3
        return [Zeta3(1), Zeta3(0, 1), Zeta3(-1, -1)][exponent]

    def character(label, g, x):
        _, sector, irrep, _ = label
        if g not in classes[sector] or compose(g, x) != compose(x, g):
            return Zeta3(0)
        q = transporters[sector][g]
        z = compose(compose(inverse(q), x), q)
        return centralizer_character(sector, irrep, z)

    commuting_pairs = [(g, x) for g in group for x in group if compose(g, x) == compose(x, g)]
    assert len(commuting_pairs) == 18

    def inner(chi, psi):
        total = Zeta3(0)
        for g, x in commuting_pairs:
            total += chi(g, x).conjugate() * psi(g, x)
        return total.divide_int(len(group))

    orthogonality = []
    for left in labels:
        row = []
        for right in labels:
            value = inner(
                lambda g, x, left=left: character(left, g, x),
                lambda g, x, right=right: character(right, g, x),
            )
            row.append(value.integer())
        orthogonality.append(row)
    assert orthogonality == [[int(i == j) for j in range(8)] for i in range(8)]

    def tensor_character(left, right, g, x):
        total = Zeta3(0)
        for a in group:
            b = compose(inverse(a), g)
            total += character(left, a, x) * character(right, b, x)
        return total

    fusion = {}
    max_multiplicity = 0
    for left in labels:
        for right in labels:
            decomposition = []
            for target in labels:
                multiplicity = inner(
                    lambda g, x, target=target: character(target, g, x),
                    lambda g, x, left=left, right=right: tensor_character(left, right, g, x),
                ).integer()
                assert multiplicity >= 0
                max_multiplicity = max(max_multiplicity, multiplicity)
                decomposition.extend([target[0]] * multiplicity)
            assert sum(next(item[3] for item in labels if item[0] == name) for name in decomposition) == left[3] * right[3]
            fusion[left[0] + "x" + right[0]] = decomposition

    for item in labels:
        assert fusion["Ax" + item[0]] == [item[0]]
        assert fusion[item[0] + "xA"] == [item[0]]
    fusion_commutative = all(fusion[a[0] + "x" + b[0]] == fusion[b[0] + "x" + a[0]] for a in labels for b in labels)
    assert fusion_commutative

    nontrivial_rules = {
        key: value for key, value in fusion.items()
        if key.split("x")[0] <= key.split("x")[1] and key not in {"Ax" + item[0] for item in labels}
    }
    result = {
        "schema": "marici.s3-fusion-ring.v1",
        "anyon_labels": {label: {"sector": sector, "irrep": irrep, "quantum_dimension": dim} for label, sector, irrep, dim in labels},
        "commuting_pair_count": len(commuting_pairs),
        "character_orthogonality_matrix": orthogonality,
        "fusion_is_commutative": fusion_commutative,
        "maximum_fusion_multiplicity": max_multiplicity,
        "unordered_nontrivial_fusion_rules": nontrivial_rules,
        "aggregate_gates": {
            "eight_irreducible_characters_are_orthonormal": True,
            "vacuum_is_fusion_identity": True,
            "all_fusion_coefficients_are_nonnegative_integers": True,
            "all_fusion_rules_preserve_quantum_dimension": True,
            "fusion_ring_is_commutative": fusion_commutative,
            "fusion_multiplicity_is_at_most_one": max_multiplicity == 1,
            "fusion_ring_does_not_determine_associator_or_braiding": True,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
