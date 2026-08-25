#!/usr/bin/env python3
"""Exact compositional law for Wilson quarter-spectrum histograms."""

from __future__ import annotations

import itertools
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
K = ROOT / "research" / "kitaev"
OUT = K / "results" / "quarter-spectrum-compositional-semiring.json"


def convolution(left, right):
    result = [0, 0, 0, 0]
    for residue_left, count_left in enumerate(left):
        for residue_right, count_right in enumerate(right):
            result[(residue_left * residue_right) % 4] += count_left * count_right
    return tuple(result)


def closed_formula(left, right):
    a0, a1, a2, a3 = left
    b0, b1, b2, b3 = right
    total_left = sum(left)
    total_right = sum(right)
    return (
        a0 * total_right + b0 * total_left - a0 * b0 + a2 * b2,
        a1 * b1 + a3 * b3,
        a1 * b2 + a2 * b1 + a2 * b3 + a3 * b2,
        a1 * b3 + a3 * b1,
    )


def triangular_coordinates(packet):
    n0, n1, n2, n3 = packet
    return (sum(packet), n1 + n3, n2, n1 - n3)


def from_triangular(coordinates):
    total, odd, residue_two, imbalance = coordinates
    assert (odd + imbalance) % 2 == 0
    return (
        total - odd - residue_two,
        (odd + imbalance) // 2,
        residue_two,
        (odd - imbalance) // 2,
    )


def triangular_product(left, right):
    total_a, odd_a, two_a, imbalance_a = left
    total_b, odd_b, two_b, imbalance_b = right
    return (
        total_a * total_b,
        odd_a * odd_b,
        two_a * odd_b + odd_a * two_b,
        imbalance_a * imbalance_b,
    )


def convolution_power(packet, exponent):
    result = (0, 1, 0, 0)
    for _ in range(exponent):
        result = convolution(result, packet)
    return result


def moment_packet(packet):
    n0, n1, n2, n3 = packet
    return (sum(packet), n0 - n2, n1 - n3, n0 + n2 - n1 - n3)


def triangular_from_moments(moments):
    total, trace1_real, trace1_imag, trace2 = moments
    odd = (total - trace2) // 2
    residue_two = (total - odd - trace1_real) // 2
    return (total, odd, residue_two, trace1_imag)


def main() -> None:
    basis = [tuple(int(i == residue) for i in range(4)) for residue in range(4)]
    multiplication_table = [[(i * j) % 4 for j in range(4)] for i in range(4)]
    assert multiplication_table == [
        [0, 0, 0, 0],
        [0, 1, 2, 3],
        [0, 2, 0, 2],
        [0, 3, 2, 1],
    ]
    for left, middle, right in itertools.product(basis, repeat=3):
        assert convolution(convolution(left, middle), right) == convolution(left, convolution(middle, right))
        assert convolution(left, right) == convolution(right, left)
        assert convolution(left, right) == closed_formula(left, right)
        assert triangular_coordinates(convolution(left, right)) == triangular_product(
            triangular_coordinates(left), triangular_coordinates(right)
        )
        assert from_triangular(triangular_coordinates(left)) == left
        assert triangular_from_moments(moment_packet(left)) == triangular_coordinates(left)
    unit = basis[1]
    assert all(convolution(unit, item) == item for item in basis)

    # Exact factor histograms from the independently checked D(S4) and D(D4)
    # packets. Tuple order is residues 0,1,2,3.
    s4_d3 = (3, 4, 0, 14)
    s4_d6 = (11, 0, 10, 0)
    d4_d2 = (12, 0, 10, 0)
    d4_d1_nonvac = (0, 14, 0, 8)
    left_product = convolution(s4_d3, d4_d2)
    right_product = convolution(s4_d6, d4_d1_nonvac)
    assert left_product == (282, 0, 180, 0)
    assert right_product == (242, 0, 220, 0)
    assert left_product != right_product
    left_coordinates = triangular_coordinates(left_product)
    right_coordinates = triangular_coordinates(right_product)
    assert left_coordinates == (462, 0, 180, 0)
    assert right_coordinates == (462, 0, 220, 0)

    # Rank and quantum dimension are scalar shadows.  Equal rank and equal
    # total sector dimension do not identify the histogram element.
    assert sum(left_product) == sum(right_product) == 462

    tensor_power_checks = {}
    for packet_name, packet in {
        "product_left": left_product,
        "product_right": right_product,
        "generic_witness": (2, 3, 5, 7),
    }.items():
        total, odd, residue_two, imbalance = triangular_coordinates(packet)
        rows = {}
        for exponent in range(1, 6):
            powered = convolution_power(packet, exponent)
            predicted_coordinates = (
                total ** exponent,
                odd ** exponent,
                exponent * residue_two * odd ** (exponent - 1),
                imbalance ** exponent,
            )
            assert triangular_coordinates(powered) == predicted_coordinates
            rows[str(exponent)] = list(powered)
        tensor_power_checks[packet_name] = rows
    assert convolution_power(left_product, 2) == (462 ** 2, 0, 0, 0)
    assert convolution_power(right_product, 2) == (462 ** 2, 0, 0, 0)

    phase_kernel = sp.Matrix(4, 4, lambda r, s: sp.I ** ((r * s) % 4))
    assert phase_kernel.rank() == 4
    support_ranks = {}
    for left_support in itertools.chain.from_iterable(itertools.combinations(range(4), k) for k in range(1, 5)):
        for right_support in itertools.chain.from_iterable(itertools.combinations(range(4), k) for k in range(1, 5)):
            support_ranks[f"{''.join(map(str, left_support))}|{''.join(map(str, right_support))}"] = phase_kernel.extract(left_support, right_support).rank()
    assert support_ranks["02|02"] == 1
    assert support_ranks["0123|0123"] == 4

    result = {
        "schema": "marici.kitaev.quarter-spectrum-compositional-semiring.v1",
        "carrier": "N[Z/4 under multiplication] represented by residue-count vectors (n0,n1,n2,n3)",
        "multiplication_table": multiplication_table,
        "closed_convolution_formula": {
            "c0": "a0*B+b0*A-a0*b0+a2*b2",
            "c1": "a1*b1+a3*b3",
            "c2": "a1*b2+a2*b1+a2*b3+a3*b2",
            "c3": "a1*b3+a3*b1",
            "A": "sum_i ai",
            "B": "sum_i bi",
        },
        "laws": {"associative": True, "commutative": True, "unit": [0, 1, 0, 0]},
        "triangular_coordinates": {
            "definition": ["N=n0+n1+n2+n3", "O=n1+n3", "T=n2", "Delta=n1-n3"],
            "inverse": ["n0=N-O-T", "n1=(O+Delta)/2", "n2=T", "n3=(O-Delta)/2"],
            "product": ["N'=Na*Nb", "O'=Oa*Ob", "T'=Ta*Ob+Oa*Tb", "Delta'=Deltaa*Deltab"],
            "interpretation": {
                "N": "total sector rank",
                "O": "multiplicity of odd quarter phases plus/minus i",
                "T": "multiplicity of residue-two phase -1",
                "Delta": "oriented imbalance between +i and -i",
            },
            "dual_number_sector": "O+T*epsilon multiplies with epsilon^2=0",
            "product_counterexample_coordinates": {
                "left": list(left_coordinates),
                "right": list(right_coordinates),
                "only_distinguishing_coordinate": "T",
            },
        },
        "minimal_spectral_moments": {
            "packet": ["N", "tau1=Tr(U)", "tau2=Tr(U^2)"],
            "tau1": "(N-O-2T)+i*Delta",
            "tau2": "N-2O",
            "reconstruction": ["O=(N-tau2)/2", "Delta=Im(tau1)", "T=(N-O-Re(tau1))/2"],
            "scope": "spectral identification only; estimating traces does not implement U or controlled-U",
        },
        "product_sector_power_law": {
            "coordinates": ["N_k=N^k", "O_k=O^k", "T_k=k*T*O^(k-1)", "Delta_k=Delta^k"],
            "checked_exponents": [1, 2, 3, 4, 5],
            "checks": tensor_power_checks,
            "even_support_cancellation": "if O=0, the Wilson quarter phase for the product sector x^{boxtimes k} is identity for k>=2",
            "not_claimed": "this is not cancellation of U_x tensor U_x; exp(pi i W_x/2) tensor exp(pi i W_x/2) has additive phases, whereas W_(x boxtimes x) has multiplicative eigenvalues",
        },
        "cross_factor_phase_kernel": {
            "entries": "K_rs=i^(r*s)",
            "full_operator_schmidt_rank": phase_kernel.rank(),
            "selected_support_ranks": {
                "even_by_even_02|02": support_ranks["02|02"],
                "full_0123|0123": support_ranks["0123|0123"],
                "s3_dimension2_by_dimension3_023|013": support_ranks["023|013"],
            },
            "consequence": "generic product-sector quarter evolution is an interacting diagonal gate and cannot be compiled as a tensor product of factor-only unitaries; rank-one support is the exceptional separable case",
        },
        "product_counterexample_reproduced": {
            "left": list(left_product),
            "right": list(right_product),
            "equal_total_rank": sum(left_product),
            "equal_quantum_dimension": 6,
            "equal_histogram": False,
        },
        "typing": {
            "shared_carrier_geometry": "tensor products multiply eigenvalues and Cartesian-product their multiplicities",
            "quantum_coefficient_lens": "selects mod-4 phase residues through exp(2 pi i lambda/4)",
            "readout_control_boundary": "histogram classifies the unitary spectrum but does not construct controlled Wilson evolution",
        },
        "replacement_dpc": "The typed Wilson quarter-spectrum packet is a symmetric monoidal invariant into N[Z/4,multiplication]; product-double predictions must be computed by this convolution, and no scalar quotient such as quantum dimension is explanatory unless its fibers are proven convolution-homogeneous.",
        "verdict": "The product-double failure has an exact compositional explanation. Quarter spectra form a commutative semiring-valued invariant whose multiplication is residue-product convolution. Quantum dimension and total rank are lossy scalar shadows, so equal values cannot justify equal control species.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
