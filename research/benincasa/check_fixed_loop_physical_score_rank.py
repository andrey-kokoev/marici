#!/usr/bin/env python3
"""Physical score rank directly on the fixed loop-vector cycle."""

from __future__ import annotations

from dataclasses import dataclass
import itertools
import json
import math
from pathlib import Path

import sympy as sp


ORDER = 3
NVAR = 3
ZERO = (0,0,0)
TARGETS = [
    (1,0,0),(0,1,0),(0,0,1),
    (2,0,0),(1,1,0),(1,0,1),(0,2,0),(0,1,1),(0,0,2),
    (1,1,1),
]


@dataclass(frozen=True)
class Jet:
    terms: dict[tuple[int,int,int], int]
    prime: int

    def __post_init__(self) -> None:
        object.__setattr__(self, "terms", {
            exponent: coefficient % self.prime
            for exponent, coefficient in self.terms.items()
            if coefficient % self.prime and sum(exponent) <= ORDER
        })

    @staticmethod
    def scalar(value: int, prime: int) -> "Jet":
        value %= prime
        return Jet({ZERO:value} if value else {}, prime)

    @staticmethod
    def variable(axis: int, prime: int) -> "Jet":
        exponent = [0,0,0]
        exponent[axis] = 1
        return Jet({tuple(exponent):1}, prime)

    def constant(self) -> int:
        return self.terms.get(ZERO,0)

    def coerce(self, other: "Jet" | int) -> "Jet":
        if isinstance(other, Jet):
            assert other.prime == self.prime
            return other
        return Jet.scalar(other,self.prime)

    def __add__(self, other: "Jet" | int) -> "Jet":
        other = self.coerce(other)
        result = dict(self.terms)
        for exponent, coefficient in other.terms.items():
            result[exponent] = (result.get(exponent,0)+coefficient) % self.prime
        return Jet(result,self.prime)

    __radd__ = __add__

    def __neg__(self) -> "Jet":
        return Jet({exponent:-coefficient for exponent,coefficient in self.terms.items()},self.prime)

    def __sub__(self, other: "Jet" | int) -> "Jet":
        return self + (-self.coerce(other))

    def __rsub__(self, other: int) -> "Jet":
        return Jet.scalar(other,self.prime)-self

    def __mul__(self, other: "Jet" | int) -> "Jet":
        other = self.coerce(other)
        result: dict[tuple[int,int,int],int] = {}
        for left_exp,left_coefficient in self.terms.items():
            for right_exp,right_coefficient in other.terms.items():
                exponent = tuple(left_exp[i]+right_exp[i] for i in range(NVAR))
                if sum(exponent) <= ORDER:
                    result[exponent] = (
                        result.get(exponent,0)+left_coefficient*right_coefficient
                    ) % self.prime
        return Jet(result,self.prime)

    __rmul__ = __mul__

    def __pow__(self, exponent: int) -> "Jet":
        assert exponent >= 0
        result = Jet.scalar(1,self.prime)
        base = self
        while exponent:
            if exponent & 1:
                result *= base
            base *= base
            exponent >>= 1
        return result

    def inverse(self) -> "Jet":
        constant = self.constant()
        if constant == 0:
            raise ZeroDivisionError
        inverse_constant = pow(constant,-1,self.prime)
        reduced = (self-constant)*inverse_constant
        result = Jet.scalar(0,self.prime)
        term = Jet.scalar(1,self.prime)
        for degree in range(ORDER+1):
            result += term if degree % 2 == 0 else -term
            term *= reduced
        return result*inverse_constant

    def __truediv__(self, other: "Jet" | int) -> "Jet":
        return self*self.coerce(other).inverse()


def sqrt_mod(value: int, prime: int) -> int:
    roots = sp.sqrt_mod(value % prime, prime, all_roots=True)
    if not roots:
        raise ValueError("nonsquare")
    return int(min(roots))


def sqrt_jet(value: Jet) -> Jet:
    prime = value.prime
    constant = value.constant()
    root = sqrt_mod(constant,prime)
    reduced = (value-constant)*pow(constant,-1,prime)
    result = Jet.scalar(0,prime)
    term = Jet.scalar(1,prime)
    coefficient = 1
    # binomial(1/2,k) recursively modulo p
    inv2 = pow(2,-1,prime)
    for degree in range(ORDER+1):
        if degree:
            coefficient = coefficient*((inv2-(degree-1)) % prime)*pow(degree,-1,prime) % prime
        result += term*coefficient
        term *= reduced
    return result*root


def matrix_rank_mod(matrix: list[list[int]], prime: int) -> int:
    work = [[value % prime for value in row] for row in matrix]
    rows = len(work)
    columns = len(work[0]) if rows else 0
    rank = 0
    for column in range(columns):
        pivot = next((row for row in range(rank,rows) if work[row][column]),None)
        if pivot is None:
            continue
        work[rank],work[pivot] = work[pivot],work[rank]
        inverse = pow(work[rank][column],-1,prime)
        work[rank] = [(value*inverse)%prime for value in work[rank]]
        for row in range(rows):
            if row != rank and work[row][column]:
                factor = work[row][column]
                work[row] = [
                    (work[row][j]-factor*work[rank][j])%prime
                    for j in range(columns)
                ]
        rank += 1
        if rank == rows:
            break
    return rank


def physical_response_row(
    loop_point: tuple[int,int,int], energies: tuple[int,int,int], prime: int
) -> list[int] | None:
    nu = [Jet.variable(i,prime) for i in range(3)]
    p_squared = [Jet.scalar(energy**2,prime)+nu[i] for i,energy in enumerate(energies)]
    try:
        p2 = sqrt_jet(p_squared[1])
        x4 = (p_squared[0]+p_squared[1]-p_squared[2])/(2*p2)
        y4 = sqrt_jet(p_squared[0]-x4*x4)
        lx,ly,lz = loop_point
        c = sqrt_mod(lx*lx+ly*ly+lz*lz,prime)
        a = sqrt_jet((Jet.scalar(lx,prime)-p2)**2+ly*ly+lz*lz)
        b = sqrt_jet((Jet.scalar(lx,prime)-x4)**2+(Jet.scalar(ly,prime)-y4)**2+lz*lz)
        walls = [
            Jet.scalar(c+energies[0],prime)+b,
            Jet.scalar(c+energies[1],prime)+a,
            a+b+energies[2],
            Jet.scalar(c+energies[1]+energies[2],prime)+b,
        ]
        density = Jet.scalar(1,prime)
        for wall in walls:
            density /= wall
        density0_inverse = pow(density.constant(),-1,prime)
    except (ValueError,ZeroDivisionError):
        return None

    row = []
    for exponent in TARGETS:
        coefficient = density.terms.get(exponent,0)
        multiplicity = math.prod(math.factorial(value) for value in exponent)
        row.append(coefficient*multiplicity*density0_inverse % prime)
    return row


def run_packet(prime: int, energies: tuple[int,int,int]) -> dict[str,object]:
    assert sp.isprime(prime)
    rows: list[list[int]] = []
    points: list[list[int]] = []
    for point in itertools.product(range(-12,13),repeat=3):
        if point == (0,0,0):
            continue
        row = physical_response_row(point,energies,prime)
        if row is not None:
            rows.append(row+[1])
            points.append(list(point))
            if len(rows) == 28:
                break
    assert len(rows) == 28
    response_rank = matrix_rank_mod([row[:10] for row in rows],prime)
    rank_with_constant = matrix_rank_mod(rows,prime)
    assert response_rank == 10
    assert rank_with_constant == 11
    return {
        "prime":prime,
        "energies":list(energies),
        "accepted_point_count":len(points),
        "accepted_points":points,
        "response_rank":response_rank,
        "rank_with_constant":rank_with_constant,
    }


def main() -> None:
    runs = [
        run_packet(32003,(3,4,5)),
        run_packet(32009,(4,13,15)),
    ]
    packet = {
        "schema":"marici.benincasa.fixed-loop-physical-score-rank.v1",
        "status":"passed",
        "physical_cycle":"Gamma_l=R^3 in the original loop-vector coordinates",
        "density":"1/(q_g1*q_g2*q_g3*q_g23)",
        "source_response_labels":[
            "nu1","nu2","nu3","nu1^2","nu1*nu2","nu1*nu3",
            "nu2^2","nu2*nu3","nu3^2","nu1*nu2*nu3",
        ],
        "runs":runs,
        "generic_response_rank":10,
        "generic_rank_with_constant":11,
        "source_interaction_quotient_rank":7,
        "regulated_physical_score_kernel_on_source_quotient":0,
        "gradient_pivot_or_moving_boundary_denominators":False,
        "new_carrier_support":False,
        "classification":(
            "the full physical density-response tower is faithful directly on "
            "the fixed loop-vector cycle at generic unequal energies"
        ),
        "scope_warning":(
            "The modular ranks certify generic function-field independence and, "
            "with positivity, regulated score-Gram faithfulness. They do not fix "
            "a UV renormalization prescription or prove scheme-independent finite-part rank."
        ),
    }
    output = Path(__file__).with_name("fixed-loop-physical-score-rank.json")
    output.write_text(json.dumps(packet,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(packet,indent=2,sort_keys=True))


if __name__ == "__main__":
    main()
