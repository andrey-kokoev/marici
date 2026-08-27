#!/usr/bin/env python3
"""Exact generic-fiber source-normalization gate for the final rank-12 block."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from math import isqrt
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research" / "benincasa" / ".tmp_sympy"))

from sympy.polys.domains import QQ
from sympy.polys.matrices import DomainMatrix


CRATE = ROOT / "research" / "benincasa" / "marici-gm"
CANDIDATE = ROOT / "research" / "benincasa" / "marked-extension-charzero-candidate.json"
RESULT = ROOT / "research" / "benincasa" / "results" / "marked_extension_exact_point_certificate.json"
POINTS = tuple(
    tuple(int(value) for value in pair.split(","))
    for pair in os.environ.get("MARICI_EXACT_POINTS", "7,11;8,13;11,7").split(";")
)
FIXED = (8, 9, 10, 11)


def fraction(text: str) -> Fraction:
    return Fraction(text)


def export(point: tuple[int, int], axis: str, master: int, feature: str | None) -> dict:
    env = os.environ.copy()
    env.update(
        MARICI_EXACT_POINT_SOURCE_MODE="1",
        MARICI_EXACT_U=str(point[0]),
        MARICI_EXACT_V=str(point[1]),
        MARICI_EXACT_AXIS=axis,
        MARICI_EXACT_MASTER=str(master),
        MARICI_EXACT_RAW_RESIDUES="1",
    )
    command = ["cargo", "run", "--quiet", "--release", "--bin", "marked_relative_reduction_engine"]
    if feature:
        command.extend(["--features", feature])
    result = subprocess.run(command, cwd=CRATE, env=env, check=True, capture_output=True, text=True)
    return json.loads(result.stdout)


def crt(left: int, p: int, right: int, q: int) -> tuple[int, int]:
    modulus = p * q
    return (left + p * (((right - left) * pow(p, -1, q)) % q)) % modulus, modulus


def rational_reconstruct(value: int, modulus: int) -> Fraction:
    bound = isqrt(modulus // 2)
    old_remainder, remainder = modulus, value
    old_denominator, denominator = 0, 1
    while abs(remainder) > bound:
        quotient = old_remainder // remainder
        old_remainder, remainder = remainder, old_remainder - quotient * remainder
        old_denominator, denominator = denominator, old_denominator - quotient * denominator
    if not denominator or abs(denominator) > bound:
        raise ValueError("CRT rational reconstruction exceeded its uniqueness window")
    if denominator < 0:
        remainder, denominator = -remainder, -denominator
    if (remainder - value * denominator) % modulus:
        raise ValueError("invalid CRT rational reconstruction")
    return Fraction(remainder, denominator)


def combine_packets(left: dict, right: dict) -> dict:
    assert (left["u"], left["v"], left["axis"], left["master"]) == (right["u"], right["v"], right["axis"], right["master"])
    assert left["unknowns"] == right["unknowns"] and len(left["rows"]) == len(right["rows"])
    combined = dict(left)
    combined["prime"] = left["prime"] * right["prime"]
    rows = []
    for left_row, right_row in zip(left["rows"], right["rows"]):
        assert left_row["monomial"] == right_row["monomial"]
        assert [entry[0] for entry in left_row["entries"]] == [entry[0] for entry in right_row["entries"]]
        entries = []
        for (column, a), (_, b) in zip(left_row["entries"], right_row["entries"]):
            residue, modulus = crt(int(a), left["prime"], int(b), right["prime"])
            entries.append([column, str(rational_reconstruct(residue, modulus))])
        residue, modulus = crt(int(left_row["rhs"]), left["prime"], int(right_row["rhs"]), right["prime"])
        rows.append({"monomial": left_row["monomial"], "entries": entries, "rhs": str(rational_reconstruct(residue, modulus))})
    combined["rows"] = rows
    return combined


def exact_fixed_values(packets: list[dict]) -> tuple[list[list[Fraction]], tuple[int, ...]]:
    rows = len(packets[0]["rows"])
    unknowns = packets[0]["unknowns"]
    assert all(len(packet["rows"]) == rows and packet["unknowns"] == unknowns for packet in packets)
    dod: dict[int, dict[int, object]] = {}
    for row_index, row in enumerate(packets[0]["rows"]):
        entries: dict[int, object] = {}
        for column, value in row["entries"]:
            q = fraction(value)
            entries[column] = QQ(q.numerator, q.denominator)
        for master, packet in enumerate(packets):
            q = fraction(packet["rows"][row_index]["rhs"])
            if q:
                entries[unknowns + master] = QQ(q.numerator, q.denominator)
        if entries:
            dod[row_index] = entries
    matrix = DomainMatrix.from_dod(dod, (rows, unknowns + len(packets)), QQ)
    reduced, pivots = matrix.rref()
    reduced_dod = reduced.to_dod()
    free = set(range(unknowns)) - set(pivots)
    values: list[list[Fraction]] = []
    certified: list[int] = []
    for coordinate in FIXED:
        row_index = pivots.index(coordinate)
        row = reduced_dod.get(row_index, {})
        if any(row.get(column, QQ.zero) != QQ.zero for column in free):
            continue
        certified.append(coordinate)
        coordinate_values = []
        for master in range(len(packets)):
            value = row.get(unknowns + master, QQ.zero)
            coordinate_values.append(Fraction(int(value.numerator), int(value.denominator)))
        values.append(coordinate_values)
    return values, tuple(certified)


def monomials(degree: int):
    for total in range(degree + 1):
        for u_degree in range(total + 1):
            yield u_degree, total - u_degree


def evaluate(coefficients: list[str], degree: int, u: int, v: int) -> Fraction:
    return sum(
        (fraction(coefficient) * u**i * v**j for coefficient, (i, j) in zip(coefficients, monomials(degree))),
        Fraction(0),
    )


def candidate_value(entries: list[dict], point: tuple[int, int], axis: str, row: int, column: int) -> Fraction:
    entry = next(e for e in entries if e["axis"] == axis and e["row"] == row and e["column"] == column)
    numerator = evaluate(entry["numerator"], entry["numerator_degree"], *point)
    denominator = evaluate(entry["denominator"], entry["denominator_degree"], *point)
    assert denominator
    return numerator / denominator


def main() -> None:
    candidate = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    report = {"schema": "marici.benincasa.marked_extension_exact_point_certificate.v2", "fibers": []}
    for point in POINTS:
        fiber = {"point": list(point), "axes": {}}
        for axis in ("u", "v"):
            packets = [export(point, axis, master, None) for master in range(3)]
            replicas = [export(point, axis, master, "replication-prime") for master in range(3)]
            combined = [combine_packets(left, right) for left, right in zip(packets, replicas)]
            exact, certified = exact_fixed_values(combined)
            assert certified == FIXED
            expected = [[candidate_value(candidate["entries"], point, axis, row, column) for column in range(3)] for row in range(4)]
            assert exact == expected
            fiber["axes"][axis] = {
                "primes": [packets[0]["prime"], replicas[0]["prime"]],
                "crt_source_reconstruction": True,
                "rank": 117,
                "certified_source_coordinates": list(certified),
                "candidate_equal": True,
                "values": [[str(value) for value in row] for row in exact],
            }
        report["fibers"].append(fiber)
    report["all_candidate_values_equal"] = True
    report["checked_values"] = 24 * len(POINTS)
    text = json.dumps(report, indent=2) + "\n"
    RESULT.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
