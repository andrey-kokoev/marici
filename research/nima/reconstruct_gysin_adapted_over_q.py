"""Reconstruct the adapted rank-four Gysin connection over Q from two primes."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path

from sympy.polys.domains import ZZ
from sympy.polys.modulargcd import _integer_rational_reconstruction


def crt_pair(a: int, p: int, b: int, q: int) -> int:
    return (a + p * (((b - a) * pow(p, -1, q)) % q)) % (p * q)


def reconstruct(a: int, p: int, b: int, q: int) -> Fraction:
    modulus = p * q
    combined = crt_pair(a, p, b, q)
    value = _integer_rational_reconstruction(combined, modulus, ZZ)
    if value is None:
        raise ValueError(f"no bounded rational reconstruction for {a} mod {p}, {b} mod {q}")
    answer = Fraction(int(value.numerator), int(value.denominator))
    for residue, prime in ((a, p), (b, q)):
        reduced = answer.numerator * pow(answer.denominator, -1, prime) % prime
        if reduced != residue:
            raise AssertionError((answer, residue, prime, reduced))
    return answer


def terms_map(terms: list[list[int]]) -> dict[tuple[int, int], int]:
    return {(i, j): coefficient for i, j, coefficient in terms}


def encode(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("primary", type=Path)
    parser.add_argument("replication", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args()

    primary = json.loads(args.primary.read_text(encoding="utf-8"))
    replication = json.loads(args.replication.read_text(encoding="utf-8"))
    p, q = primary["prime"], replication["prime"]
    if p == q:
        raise ValueError("independent primes required")
    if len(primary["entries"]) != len(replication["entries"]):
        raise ValueError("entry counts differ")

    entries = []
    maximum_numerator = 0
    maximum_denominator = 0
    coefficient_count = 0
    for left, right in zip(primary["entries"], replication["entries"]):
        identity = (left["axis"], left["row"], left["col"])
        if identity != (right["axis"], right["row"], right["col"]):
            raise ValueError("entry order differs")
        lf, rf = left["fit"], right["fit"]
        if (lf["degree"], lf["anchor"]) != (rf["degree"], rf["anchor"]):
            raise ValueError(f"fit convention differs at {identity}")
        fit = {"degree": lf["degree"], "anchor": lf["anchor"]}
        for part in ("numerator", "denominator"):
            lm, rm = terms_map(lf[part]), terms_map(rf[part])
            if lm.keys() != rm.keys():
                raise ValueError(f"{part} support differs at {identity}")
            terms = []
            for monomial in sorted(lm):
                value = reconstruct(lm[monomial], p, rm[monomial], q)
                maximum_numerator = max(maximum_numerator, abs(value.numerator))
                maximum_denominator = max(maximum_denominator, value.denominator)
                coefficient_count += 1
                terms.append([monomial[0], monomial[1], encode(value)])
            fit[part] = terms
        entries.append({"axis": identity[0], "row": identity[1], "col": identity[2], "fit": fit})

    packet = {
        "schema": "marici.nima.gysin_adapted_reconstruction_Q.v1",
        "source_primes": [p, q],
        "reconstruction_modulus": str(p * q),
        "coefficient_encoding": "reduced rational string",
        "max_degree": primary["max_degree"],
        "entries": entries,
    }
    certificate = {
        "schema": "marici.nima.gysin_adapted_reconstruction_Q_certificate.v1",
        "source_primes": [p, q],
        "entry_count": len(entries),
        "coefficient_count": coefficient_count,
        "supports_identical": True,
        "degrees_and_anchors_identical": True,
        "reduces_to_both_inputs": True,
        "maximum_reconstructed_numerator": maximum_numerator,
        "maximum_reconstructed_denominator": maximum_denominator,
        "bound": "canonical rational reconstruction below sqrt(p*q/2)",
    }
    args.output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    args.certificate.write_text(json.dumps(certificate, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(certificate))


if __name__ == "__main__":
    main()
