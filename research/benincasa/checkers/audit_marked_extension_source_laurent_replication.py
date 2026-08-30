"""Aggregate independent source-Laurent sign replications."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research" / "benincasa" / ".tmp_sympy"))

import sympy as sp


RESULTS = ROOT / "research" / "benincasa" / "results"
u, v = sp.symbols("u v")
CANDIDATE = ROOT / "research" / "benincasa" / "marked-extension-charzero-candidate.json"
PACKETS = (
    RESULTS / "marked_extension_source_laurent_lead_prime3921.json",
    RESULTS / "marked_extension_source_laurent_lead_prime3951_v5.json",
    RESULTS / "marked_extension_source_laurent_lead_prime3951_v7.json",
)
RESULT = RESULTS / "marked_extension_source_laurent_lead.json"


def monomials(degree: int):
    for total in range(degree + 1):
        for u_degree in range(total + 1):
            yield u**u_degree * v ** (total - u_degree)


def expression(coefficients: list[str], degree: int):
    return sum(sp.Rational(coefficient) * term for coefficient, term in zip(coefficients, monomials(degree)))


def candidate_principal(candidate: dict, fiber: int):
    double, simple = [], []
    for row in range(4):
        double_row, simple_row = [], []
        for column in range(3):
            entry = next(
                item for item in candidate["entries"]
                if item["axis"] == "u" and item["row"] == row and item["column"] == column
            )
            value = sp.cancel(
                expression(entry["numerator"], entry["numerator_degree"])
                / expression(entry["denominator"], entry["denominator_degree"])
            )
            coefficient2 = sp.factor(sp.limit(u**2 * value, u, 0))
            coefficient1 = sp.factor(sp.limit(u * (value - coefficient2 / u**2), u, 0))
            double_row.append(str(coefficient2.subs(v, fiber)))
            simple_row.append(str(coefficient1.subs(v, fiber)))
        double.append(double_row)
        simple.append(simple_row)
    return double, simple


def main() -> None:
    packets = [json.loads(path.read_text(encoding="utf-8")) for path in PACKETS]
    candidate = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    assert all(packet["status"] == "pass" for packet in packets)
    assert all(packet["held_out_polynomial_identity"] for packet in packets)
    assert all(packet["target_fixed"] for packet in packets)
    assert {packet["target_rational_reconstruction"] for packet in packets} == {"-1/8"}
    assert {packet["rank"] for packet in packets} == {655}
    assert len({packet["prime"] for packet in packets}) == 2
    assert len({packet["v"] for packet in packets}) == 2
    unfixed_e6 = {}
    for packet in packets:
        candidate_double, candidate_simple = candidate_principal(candidate, packet["v"])
        assert packet["fixed_u_minus_2_matrix"] == candidate_double
        assert all(value is None for value in packet["fixed_u_minus_1_matrix"][0])
        assert packet["fixed_u_minus_1_matrix"][1:] == candidate_simple[1:]
        unfixed_e6[str(packet["v"])] = candidate_simple[0]
    output = {
        "schema": "marici.benincasa.marked_extension_source_laurent_replication.v1",
        "status": "pass",
        "target": packets[0]["target"],
        "target_rational_reconstruction": "-1/8",
        "primes": sorted({packet["prime"] for packet in packets}),
        "generic_v_fibers": sorted({packet["v"] for packet in packets}),
        "ranks": sorted({packet["rank"] for packet in packets}),
        "fixed_double_matrix_equals_candidate": True,
        "fixed_simple_rows_e7_to_e9_equal_candidate": True,
        "simple_e6_row_source_fixed": False,
        "candidate_simple_e6_row_by_v": unfixed_e6,
        "replications": [path.name for path in PACKETS],
        "scope": "source-direct modular Laurent theorem; characteristic-zero universal identity remains a separate claim",
    }
    RESULT.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
