"""Sparse exact super-momentum-twistor primitives.

A fermionic coordinate is represented by its linear coefficients in external
chi labels. The same coefficient map applies independently to all four SU(4)
components.
"""
from dataclasses import dataclass
from itertools import product
from typing import Mapping, Hashable
import sympy as s
from momentum_twistor_constructors import four_bracket


@dataclass(frozen=True)
class SuperTwistor:
    z: s.Matrix
    chi: Mapping[Hashable, s.Expr]


def external_supertwistor(label, z):
    """Create (Z_label, chi_label)."""
    return SuperTwistor(z, {label: s.Integer(1)})


def scale_supertwistor(alpha, twistor):
    """Apply the projective scaling (Z,chi) -> alpha*(Z,chi)."""
    return SuperTwistor(
        s.expand(alpha * twistor.z),
        {label: s.expand(alpha * coefficient)
         for label, coefficient in twistor.chi.items()},
    )


def _linear_chi(alpha, left, beta, right):
    labels = set(left) | set(right)
    return {k: s.expand(alpha * left.get(k, 0) + beta * right.get(k, 0))
            for k in labels
            if s.expand(alpha * left.get(k, 0) + beta * right.get(k, 0)) != 0}


def super_line_plane_point(a, b, c, d, e):
    """Return the supertwistor (ab) intersect (cde).

    This is a*<bcde> + b*<cdea>, applied identically to bosonic and
    fermionic coordinates.
    """
    alpha = four_bracket(b.z, c.z, d.z, e.z)
    beta = four_bracket(c.z, d.z, e.z, a.z)
    return SuperTwistor(
        s.expand(alpha * a.z + beta * b.z),
        _linear_chi(alpha, a.chi, beta, b.chi),
    )


def super_five_bracket(vertices):
    """Return [abcde] as sparse coefficients of its degree-four delta.

    Keys (i1,i2,i3,i4) represent chi_i1^1 chi_i2^2 chi_i3^3 chi_i4^4.
    Arguments may be external or constructed SuperTwistors.
    """
    if len(vertices) != 5:
        raise ValueError("a five-bracket requires exactly five supertwistors")
    a, b, c, d, e = vertices
    qs = (
        four_bracket(b.z, c.z, d.z, e.z),
        four_bracket(c.z, d.z, e.z, a.z),
        four_bracket(d.z, e.z, a.z, b.z),
        four_bracket(e.z, a.z, b.z, c.z),
        four_bracket(a.z, b.z, c.z, d.z),
    )
    denominator = s.prod(qs)
    if denominator == 0:
        raise ValueError("singular five-bracket denominator")
    delta = {}
    for q, vertex in zip(qs, vertices):
        for label, coefficient in vertex.chi.items():
            delta[label] = s.expand(delta.get(label, 0) + q * coefficient)
    delta = {label: coefficient for label, coefficient in delta.items() if coefficient != 0}
    labels = tuple(delta)
    return {monomial: s.factor(s.prod(delta[i] for i in monomial) / denominator)
            for monomial in product(labels, repeat=4)}


def super_five_bracket_product_component(left, right, pairs):
    """Return one canonical degree-eight component of left wedge right.

    ``pairs`` gives the ordered pair of external labels for each SU(4)
    component. Only 2^4 assignments between the factors are required.
    """
    if len(pairs) != 4 or any(len(pair) != 2 or pair[0] == pair[1] for pair in pairs):
        raise ValueError("expected four pairs of distinct Grassmann labels")
    total = s.Integer(0)
    for choices in product((0, 1), repeat=4):
        lm = tuple(pairs[a][choices[a]] for a in range(4))
        rm = tuple(pairs[a][1 - choices[a]] for a in range(4))
        # Canonical reordering sign within each SU(4) component.
        sign = s.prod(1 if str(lm[a]) <= str(rm[a]) else -1 for a in range(4))
        total += sign * left.get(lm, 0) * right.get(rm, 0)
    return s.factor(total)


def multiply_super_five_brackets(left, right):
    """Exterior product of two sparse five-bracket coefficient maps.

    Output keys are four ordered label-pairs, one pair for each SU(4)
    component. Terms repeating the same Grassmann generator vanish.
    """
    out = {}
    for lm, lc in left.items():
        for rm, rc in right.items():
            if any(lm[a] == rm[a] for a in range(4)):
                continue
            sign = s.Integer(1)
            pairs = []
            for a in range(4):
                if str(lm[a]) <= str(rm[a]):
                    pairs.append((lm[a], rm[a]))
                else:
                    pairs.append((rm[a], lm[a])); sign = -sign
            key = tuple(pairs)
            out[key] = out.get(key, 0) + sign * lc * rc
    return {key: s.factor(value) for key, value in out.items() if value != 0}
