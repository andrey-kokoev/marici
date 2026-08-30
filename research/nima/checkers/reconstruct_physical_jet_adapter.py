"""Reconstruct the frozen physical jet adapter and verify at a held-out prime."""

from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
RESULTS = Path(__file__).resolve().parents[1] / "results"
FIT_PRIMES = (32003, 32009, 65521, 100003, 100019, 100043)
HELDOUT_PRIME = 100049
AMBIENT, CUTOFF = 12, 6
OUT = RESULTS / "physical_half_twist_normal_jet_adapter_a12_c6_reconstruction.json"


def crt(residues, primes):
    value, modulus = 0, 1
    for residue, prime in zip(residues, primes):
        step = ((residue - value) * pow(modulus, -1, prime)) % prime
        value += modulus * step
        modulus *= prime
    return value % modulus, modulus


def rational_reconstruction(residue, modulus):
    bound = math.isqrt(modulus // 2)
    r0, r1 = modulus, residue
    t0, t1 = 0, 1
    while abs(r1) > bound:
        quotient = r0 // r1
        r0, r1 = r1, r0 - quotient * r1
        t0, t1 = t1, t0 - quotient * t1
    numerator, denominator = r1, t1
    if denominator < 0:
        numerator, denominator = -numerator, -denominator
    if (
        denominator == 0
        or abs(denominator) > bound
        or math.gcd(numerator, denominator) != 1
        or (numerator * pow(denominator, -1, modulus) - residue) % modulus
    ):
        return None
    return Fraction(numerator, denominator)


def reconstruct_sparse(matrices):
    reconstructed = []
    failures = []
    for outer_index in range(len(matrices[0])):
        keys = sorted({key for matrix in matrices for key in matrix[outer_index]})
        row = {}
        for key in keys:
            residues = [int(matrix[outer_index].get(key, 0)) for matrix in matrices]
            combined, modulus = crt(residues, FIT_PRIMES)
            fraction = rational_reconstruction(combined, modulus)
            if fraction is None:
                failures.append({"row": outer_index, "column": key, "residues": residues})
            else:
                row[key] = str(fraction)
        reconstructed.append(row)
    return reconstructed, failures


def reduce_fraction(value, prime):
    fraction = Fraction(value)
    return (fraction.numerator * pow(fraction.denominator, -1, prime)) % prime


def verify_sparse(reconstructed, observed, prime):
    failures = []
    for row_index, (row, observed_row) in enumerate(zip(reconstructed, observed)):
        keys = sorted(set(row) | set(observed_row))
        for key in keys:
            expected = reduce_fraction(row.get(key, "0"), prime)
            actual = int(observed_row.get(key, 0))
            if expected != actual:
                failures.append(
                    {"row": row_index, "column": key, "expected": expected, "actual": actual}
                )
    return failures


def main():
    packets = [
        json.loads(
            (RESULTS / f"physical_half_twist_normal_jet_defect_p{prime}_a{AMBIENT}_c{CUTOFF}.json").read_text()
        )
        for prime in FIT_PRIMES
    ]
    heldout = json.loads(
        (RESULTS / f"physical_half_twist_normal_jet_defect_p{HELDOUT_PRIME}_a{AMBIENT}_c{CUTOFF}.json").read_text()
    )
    reductions = [packet["jet_to_simple_reduction_matrix"] for packet in packets]
    reduction, reduction_failures = reconstruct_sparse(reductions)

    defect_reconstruction = []
    defect_failures = []
    for axis in range(2):
        matrices = [
            packet["explicit_graph_connection_defect_in_simple_coordinates"][axis]
            for packet in packets
        ]
        reconstructed, failures = reconstruct_sparse(matrices)
        defect_reconstruction.append(reconstructed)
        defect_failures.extend({"axis": axis, **failure} for failure in failures)

    heldout_failures = [
        {"matrix": "reduction", **failure}
        for failure in verify_sparse(
            reduction, heldout["jet_to_simple_reduction_matrix"], HELDOUT_PRIME
        )
    ]
    for axis in range(2):
        heldout_failures.extend(
            {"matrix": "defect", "axis": axis, **failure}
            for failure in verify_sparse(
                defect_reconstruction[axis],
                heldout["explicit_graph_connection_defect_in_simple_coordinates"][axis],
                HELDOUT_PRIME,
            )
        )

    packet = {
        "schema": "marici.physical-half-twist-normal-jet-adapter-reconstruction.v1",
        "fit_primes": list(FIT_PRIMES),
        "heldout_prime": HELDOUT_PRIME,
        "crt_modulus": math.prod(FIT_PRIMES),
        "ambient": AMBIENT,
        "cutoff": CUTOFF,
        "jet_to_simple_reduction_matrix": reduction,
        "connection_defect_matrices": defect_reconstruction,
        "reduction_reconstruction_failures": reduction_failures,
        "defect_reconstruction_failures": defect_failures,
        "heldout_verification_failures": heldout_failures,
    }
    packet["passed"] = not reduction_failures and not defect_failures and not heldout_failures
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    if not packet["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
