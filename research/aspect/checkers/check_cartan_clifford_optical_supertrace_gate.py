from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


NAMES = ("a", "b", "c")
ZERO_MONOMIAL = (0, 0, 0)


def constant(value):
    value = Fraction(value)
    return {} if value == 0 else {ZERO_MONOMIAL: value}


def variable(index):
    powers = [0, 0, 0]
    powers[index] = 1
    return {tuple(powers): Fraction(1)}


def add(left, right):
    result = dict(left)
    for monomial, coefficient in right.items():
        result[monomial] = result.get(monomial, Fraction(0)) + coefficient
        if result[monomial] == 0:
            del result[monomial]
    return result


def multiply(left, right):
    result = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            monomial = tuple(x + y for x, y in zip(left_monomial, right_monomial))
            result[monomial] = result.get(monomial, Fraction(0)) + left_coefficient * right_coefficient
    return {monomial: coefficient for monomial, coefficient in result.items() if coefficient}


def matrix_add(left, right):
    return [[add(x, y) for x, y in zip(left_row, right_row)] for left_row, right_row in zip(left, right)]


def matrix_multiply(left, right):
    return [
        [
            sum_polynomials(multiply(left[row][index], right[index][column]) for index in range(len(right)))
            for column in range(len(right[0]))
        ]
        for row in range(len(left))
    ]


def sum_polynomials(items):
    result = {}
    for item in items:
        result = add(result, item)
    return result


def identity(size, scalar):
    return [[scalar if row == column else {} for column in range(size)] for row in range(size)]


def poly_text(poly):
    if not poly:
        return "0"
    terms = []
    for monomial, coefficient in sorted(poly.items(), reverse=True):
        factors = []
        if coefficient != 1 or monomial == ZERO_MONOMIAL:
            factors.append(str(coefficient))
        for name, power in zip(NAMES, monomial):
            if power == 1:
                factors.append(name)
            elif power:
                factors.append(f"{name}^{power}")
        terms.append("*".join(factors))
    return " + ".join(terms).replace("+ -", "- ")


def serialize_matrix(value):
    return [[poly_text(entry) for entry in row] for row in value]


def main():
    zero = {}
    one = constant(1)
    a, b, c = variable(0), variable(1), variable(2)

    d2 = [[zero, a], [zero, zero]]
    q2 = [[zero, zero], [one, zero]]
    dq2 = matrix_multiply(d2, q2)
    qd2 = matrix_multiply(q2, d2)
    anti2 = matrix_add(dq2, qd2)
    assert matrix_multiply(d2, d2) == identity(2, zero)
    assert matrix_multiply(q2, q2) == identity(2, zero)
    assert anti2 == identity(2, a)

    # Basis order: visible even, visible odd, hidden even. The hidden mode is
    # coupled by b on the forward path and c on the return path.
    d3 = [[zero, a, zero], [zero, zero, zero], [zero, b, zero]]
    q3 = [[zero, zero, zero], [one, zero, c], [zero, zero, zero]]
    anti3 = matrix_add(matrix_multiply(d3, q3), matrix_multiply(q3, d3))
    target3 = identity(3, a)
    assert anti3 != target3
    assert anti3[0][0] == a
    assert anti3[1][1] == add(a, multiply(b, c))
    assert anti3[2][2] == multiply(b, c)

    # Basis order: even0, odd0, even1, odd1. A parity-balanced completion is
    # the direct sum of two exact Clifford pairs.
    d4 = [
        [zero, a, zero, zero],
        [zero, zero, zero, zero],
        [zero, zero, zero, a],
        [zero, zero, zero, zero],
    ]
    q4 = [
        [zero, zero, zero, zero],
        [one, zero, zero, zero],
        [zero, zero, zero, zero],
        [zero, zero, one, zero],
    ]
    anti4 = matrix_add(matrix_multiply(d4, q4), matrix_multiply(q4, d4))
    assert anti4 == identity(4, a)

    result = {
        "schema": "marici.aspect.cartan-clifford-optical-supertrace-gate.v1",
        "status": "pass",
        "two_mode": {
            "dQ": serialize_matrix(dq2),
            "Qd": serialize_matrix(qd2),
            "anticommutator": serialize_matrix(anti2),
            "signed_heterodyne_witness": "both ordered paths sum to a times the calibrated input field",
            "intensity_only_limitation": "reports |a|^2 and loses the sign of normal displacement",
        },
        "unpaired_hidden_even_mode": {
            "anticommutator": serialize_matrix(anti3),
            "equals_a_identity": False,
            "visible_even_only_false_pass": poly_text(anti3[0][0]) == "a",
            "visible_odd_discrepancy": poly_text(anti3[1][1]),
            "full_residual_witnesses": ["a*c", "b", "b*c - a"],
        },
        "balanced_four_mode_completion": {
            "anticommutator": serialize_matrix(anti4),
            "equals_a_identity": True,
        },
        "general_gate": {
            "identity": "supertrace(dQ + Qd) = 0",
            "consequence": "for nonzero a, dQ + Qd = a I requires equal even and odd dimensions",
            "instrument_requirement": "completion inventories and probes both parity sectors; arbitrary scalar loss ports are not admissible",
        },
        "claim_boundary": "exact finite graded-matrix and optical readout falsifier; no theta/Tate source derivation of Q and no continuum completion theorem",
    }
    output = Path(__file__).parents[1] / "results" / "cartan_clifford_optical_supertrace_gate.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
