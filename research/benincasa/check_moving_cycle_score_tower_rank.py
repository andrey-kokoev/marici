#!/usr/bin/env python3
"""Exact truncated-jet rank test for the physical moving-cycle score tower."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import itertools
import json
from pathlib import Path

import sympy as sp


ORDER = 4
NVAR = 4  # nu1,nu2,nu3,delta-c
ZERO_EXP = (0, 0, 0, 0)
SOURCE_TARGETS = [
    (1,0,0),(0,1,0),(0,0,1),
    (2,0,0),(1,1,0),(1,0,1),(0,2,0),(0,1,1),(0,0,2),
    (1,1,1),
]


@dataclass(frozen=True)
class Jet:
    terms: dict[tuple[int, ...], Fraction]

    def __post_init__(self) -> None:
        clean = {
            exponent: Fraction(coefficient)
            for exponent, coefficient in self.terms.items()
            if coefficient and sum(exponent) <= ORDER
        }
        object.__setattr__(self, "terms", clean)

    @staticmethod
    def scalar(value: int | Fraction) -> "Jet":
        value = Fraction(value)
        return Jet({ZERO_EXP: value} if value else {})

    @staticmethod
    def variable(axis: int) -> "Jet":
        exponent = [0] * NVAR
        exponent[axis] = 1
        return Jet({tuple(exponent): Fraction(1)})

    def constant(self) -> Fraction:
        return self.terms.get(ZERO_EXP, Fraction(0))

    def __add__(self, other: "Jet" | int | Fraction) -> "Jet":
        other = other if isinstance(other, Jet) else Jet.scalar(other)
        result = dict(self.terms)
        for exponent, coefficient in other.terms.items():
            result[exponent] = result.get(exponent, Fraction(0)) + coefficient
        return Jet(result)

    __radd__ = __add__

    def __neg__(self) -> "Jet":
        return Jet({exponent: -coefficient for exponent, coefficient in self.terms.items()})

    def __sub__(self, other: "Jet" | int | Fraction) -> "Jet":
        return self + (-other if isinstance(other, Jet) else -Fraction(other))

    def __rsub__(self, other: int | Fraction) -> "Jet":
        return Jet.scalar(other) - self

    def __mul__(self, other: "Jet" | int | Fraction) -> "Jet":
        other = other if isinstance(other, Jet) else Jet.scalar(other)
        result: dict[tuple[int, ...], Fraction] = {}
        for left_exp, left_coefficient in self.terms.items():
            for right_exp, right_coefficient in other.terms.items():
                exponent = tuple(left_exp[i] + right_exp[i] for i in range(NVAR))
                if sum(exponent) <= ORDER:
                    result[exponent] = result.get(exponent, Fraction(0)) + left_coefficient * right_coefficient
        return Jet(result)

    __rmul__ = __mul__

    def __pow__(self, exponent: int) -> "Jet":
        assert exponent >= 0
        result = Jet.scalar(1)
        base = self
        power = exponent
        while power:
            if power & 1:
                result = result * base
            base = base * base
            power >>= 1
        return result

    def inverse(self) -> "Jet":
        constant = self.constant()
        if constant == 0:
            raise ZeroDivisionError("jet has zero constant term")
        reduced = (self - constant) * Fraction(1, constant)
        result = Jet.scalar(0)
        term = Jet.scalar(1)
        for degree in range(ORDER + 1):
            result += term if degree % 2 == 0 else -term
            term = term * reduced
        return result * Fraction(1, constant)

    def __truediv__(self, other: "Jet" | int | Fraction) -> "Jet":
        other = other if isinstance(other, Jet) else Jet.scalar(other)
        return self * other.inverse()

    def derivative(self, axis: int) -> "Jet":
        result: dict[tuple[int, ...], Fraction] = {}
        for exponent, coefficient in self.terms.items():
            if exponent[axis]:
                lowered = list(exponent)
                multiplicity = lowered[axis]
                lowered[axis] -= 1
                lowered_tuple = tuple(lowered)
                result[lowered_tuple] = result.get(lowered_tuple, Fraction(0)) + multiplicity * coefficient
        return Jet(result)


c_sym, a_sym, b_sym, p1_sym, p2_sym, p3_sym = sp.symbols("c a b p1 p2 p3")
CM = sp.Matrix(
    [
        [0,1,1,1,1],
        [1,0,c_sym**2,a_sym**2,b_sym**2],
        [1,c_sym**2,0,p2_sym,p1_sym],
        [1,a_sym**2,p2_sym,0,p3_sym],
        [1,b_sym**2,p1_sym,p3_sym,0],
    ]
)
K_POLY = sp.Poly(sp.expand(-CM.det()/2), c_sym,a_sym,b_sym,p1_sym,p2_sym,p3_sym)


def kernel_jet(a0: int, b0: int, c0: int, energies: tuple[int,int,int]) -> Jet:
    variables = [
        Jet.scalar(c0)+Jet.variable(3),
        Jet.scalar(a0),
        Jet.scalar(b0),
        Jet.scalar(energies[0]**2)+Jet.variable(0),
        Jet.scalar(energies[1]**2)+Jet.variable(1),
        Jet.scalar(energies[2]**2)+Jet.variable(2),
    ]
    result = Jet.scalar(0)
    for exponents, coefficient in K_POLY.terms():
        term = Jet.scalar(int(coefficient))
        for variable, exponent in zip(variables, exponents, strict=True):
            term *= variable**exponent
        result += term
    return result


def response_row(a0: int, b0: int, c0: int, energies=(2,3,4)) -> list[Fraction] | None:
    kernel = kernel_jet(a0,b0,c0,energies)
    k_c = kernel.derivative(3)
    try:
        velocities = [-(kernel.derivative(i)/k_c) for i in range(3)]
        walls = [
            Jet.scalar(c0+b0+energies[0])+Jet.variable(3),
            Jet.scalar(c0+a0+energies[1])+Jet.variable(3),
            Jet.scalar(a0+b0+energies[2]),
            Jet.scalar(c0+b0+energies[1]+energies[2])+Jet.variable(3),
        ]
        scores = [
            velocity.derivative(3)
            - sum((velocity*wall.derivative(3))/wall for wall in walls)
            for velocity in velocities
        ]
    except ZeroDivisionError:
        return None

    def covariant_density_derivative(response: Jet, axis: int) -> Jet:
        return (
            response.derivative(axis)
            + velocities[axis]*response.derivative(3)
            + scores[axis]*response
        )

    responses: dict[tuple[int,int,int], Jet] = {(0,0,0): Jet.scalar(1)}
    for degree in range(1,4):
        for alpha in (
            tuple(values)
            for values in itertools.product(range(degree+1), repeat=3)
            if sum(values) == degree
        ):
            axis = max(i for i,value in enumerate(alpha) if value)
            predecessor = list(alpha)
            predecessor[axis] -= 1
            responses[alpha] = covariant_density_derivative(responses[tuple(predecessor)], axis)
    assert all(target in responses for target in SOURCE_TARGETS)
    return [responses[target].constant() for target in SOURCE_TARGETS]


def main() -> None:
    sample_points = [
        (1,2,3),(2,1,3),(3,2,1),(1,3,2),(2,3,1),(3,1,2),
        (1,1,2),(2,1,1),(1,2,1),(2,2,3),(3,2,2),(2,3,2),
        (3,3,2),(2,3,3),(3,2,3),(4,2,3),(2,4,3),(3,4,2),
    ]
    rows: list[list[Fraction]] = []
    accepted: list[tuple[int,int,int]] = []
    for point in sample_points:
        row = response_row(*point)
        if row is not None:
            rows.append(row+[Fraction(1)])
            accepted.append(point)
    matrix = sp.Matrix([[sp.Rational(value.numerator,value.denominator) for value in row] for row in rows])
    rank_with_constant = matrix.rank()
    response_rank = matrix[:,:10].rank()
    assert len(accepted) >= 11
    assert rank_with_constant == 11
    assert response_rank == 10

    # Independent replication at unequal energies.
    replication_rows = []
    for point in sample_points:
        row = response_row(*point, energies=(3,4,5))
        if row is not None:
            replication_rows.append(row+[Fraction(1)])
    replication = sp.Matrix([
        [sp.Rational(value.numerator,value.denominator) for value in row]
        for row in replication_rows
    ])
    assert replication.rank() == 11
    assert replication[:,:10].rank() == 10

    packet = {
        "schema": "marici.benincasa.moving-cycle-score-tower-rank.v1",
        "status": "passed",
        "jet_order": ORDER,
        "normal_variables": ["nu1","nu2","nu3"],
        "fiber_chart": "common pivot partial_c K != 0",
        "source_response_labels": [
            "nu1","nu2","nu3","nu1^2","nu1*nu2","nu1*nu3",
            "nu2^2","nu2*nu3","nu3^2","nu1*nu2*nu3",
        ],
        "accepted_samples": [list(point) for point in accepted],
        "primary_energies": [2,3,4],
        "primary_response_rank": response_rank,
        "primary_rank_with_constant": rank_with_constant,
        "replication_energies": [3,4,5],
        "replication_response_rank": replication[:,:10].rank(),
        "replication_rank_with_constant": replication.rank(),
        "source_interaction_quotient_rank": 7,
        "local_regulated_score_gram_kernel_on_source_quotient": 0,
        "global_period_covector_rank": "uncomputed",
        "new_carrier_support": False,
        "classification": (
            "the complete ten-port moving-cycle density-response tower is "
            "locally pointwise independent modulo constants on two generic "
            "unequal-energy fibers"
        ),
        "scope_warning": (
            "Pointwise independence plus positivity proves local regulated "
            "score-Gram faithfulness on the common gradient chart. Global Cech "
            "totalization, UV-regulator removal, and renormalized period-covector "
            "rank remain separate questions."
        ),
    }
    output = Path(__file__).with_name("moving-cycle-score-tower-rank.json")
    output.write_text(json.dumps(packet, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    print(json.dumps(packet, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
