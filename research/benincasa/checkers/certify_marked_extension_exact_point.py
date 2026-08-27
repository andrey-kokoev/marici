#!/usr/bin/env python3
"""Exact generic-fiber source-normalization gate for the final rank-12 block."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research" / "benincasa" / ".tmp_sympy"))

from sympy.polys.domains import QQ
from sympy.polys.matrices import DomainMatrix


CRATE = ROOT / "research" / "benincasa" / "marici-gm"
CANDIDATE = ROOT / "research" / "benincasa" / "marked-extension-charzero-candidate.json"
RESULT = ROOT / "research" / "benincasa" / "results" / "marked_extension_exact_point_certificate.json"
POINT = (7, 11)
FIXED = (8, 9, 10, 11)


def fraction(text: str) -> Fraction:
    return Fraction(text)


def export(axis: str, master: int, feature: str | None) -> dict:
    env = os.environ.copy()
    env.update(
        MARICI_EXACT_POINT_SOURCE_MODE="1",
        MARICI_EXACT_U=str(POINT[0]),
        MARICI_EXACT_V=str(POINT[1]),
        MARICI_EXACT_AXIS=axis,
        MARICI_EXACT_MASTER=str(master),
    )
    command = ["cargo", "run", "--quiet", "--release", "--bin", "marked_relative_reduction_engine"]
    if feature:
        command.extend(["--features", feature])
    result = subprocess.run(command, cwd=CRATE, env=env, check=True, capture_output=True, text=True)
    return json.loads(result.stdout)


def prime_independent(packet: dict) -> dict:
    answer = dict(packet)
    answer.pop("prime")
    return answer


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


def candidate_value(entries: list[dict], axis: str, row: int, column: int) -> Fraction:
    entry = next(e for e in entries if e["axis"] == axis and e["row"] == row and e["column"] == column)
    numerator = evaluate(entry["numerator"], entry["numerator_degree"], *POINT)
    denominator = evaluate(entry["denominator"], entry["denominator_degree"], *POINT)
    assert denominator
    return numerator / denominator


def main() -> None:
    candidate = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    report = {"schema": "marici.benincasa.marked_extension_exact_point_certificate.v1", "point": list(POINT), "axes": {}}
    for axis in ("u", "v"):
        packets = [export(axis, master, None) for master in range(3)]
        replicas = [export(axis, master, "replication-prime") for master in range(3)]
        prime_agreement = all(prime_independent(left) == prime_independent(right) for left, right in zip(packets, replicas))
        assert prime_agreement
        exact, certified = exact_fixed_values(packets)
        assert certified == FIXED
        expected = [[candidate_value(candidate["entries"], axis, row, column) for column in range(3)] for row in range(4)]
        assert exact == expected
        report["axes"][axis] = {
            "primes": [packets[0]["prime"], replicas[0]["prime"]],
            "prime_independent_source_matrix": True,
            "rank": 117,
            "certified_source_coordinates": list(certified),
            "candidate_equal": True,
            "values": [[str(value) for value in row] for row in exact],
        }
    report["all_24_candidate_values_equal"] = True
    text = json.dumps(report, indent=2) + "\n"
    RESULT.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
