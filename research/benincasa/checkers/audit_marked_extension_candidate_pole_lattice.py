"""Factor the exact rank-12 candidate denominators over Q[u,v]."""

from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research" / "benincasa" / ".tmp_sympy"))

import sympy as sp


u, v = sp.symbols("u v")
CANDIDATE = ROOT / "research" / "benincasa" / "marked-extension-charzero-candidate.json"
RESULT = ROOT / "research" / "benincasa" / "results" / "marked_extension_candidate_pole_lattice.json"


def monomials(degree: int):
    for total in range(degree + 1):
        for u_degree in range(total + 1):
            yield u**u_degree * v ** (total - u_degree)


def polynomial(coefficients: list[str], degree: int) -> sp.Poly:
    return sp.Poly(
        sum(sp.Rational(coefficient) * term for coefficient, term in zip(coefficients, monomials(degree))),
        u,
        v,
    )


def canonical(expression) -> sp.Poly:
    return sp.Poly(expression, u, v).monic()


def main() -> None:
    packet = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    expected = {
        canonical(expression).as_expr()
        for expression in (
            u,
            v,
            u - 1,
            u - 2,
            v - 2,
            u - v,
            u - v + 2,
            u + v - 2,
            2 * u**2 + u + v - 2,
            2 * u**2 - u - v + 2,
            4 * u**2 * v - 9 * u**2 - 6 * u * v + 12 * u - v**2 + 4 * v - 4,
            u**3 - u**2 * v + 2 * u * v - 3 * u + v - 2,
        )
    }
    maximum_exponents = defaultdict(int)
    entries = []
    for entry in packet["entries"]:
        denominator = polynomial(entry["denominator"], entry["denominator_degree"])
        _, factors = sp.factor_list(denominator.as_expr())
        normalized = []
        for factor, exponent in factors:
            factor = canonical(factor).as_expr()
            assert factor in expected
            exponent = int(exponent)
            maximum_exponents[str(factor)] = max(maximum_exponents[str(factor)], exponent)
            normalized.append({"factor": str(factor), "exponent": exponent})
        entries.append(
            {
                "axis": entry["axis"],
                "row": entry["row"],
                "column": entry["column"],
                "denominator_total_degree": int(denominator.total_degree()),
                "factors": normalized,
            }
        )
    assert set(maximum_exponents) == {str(factor) for factor in expected}
    assert maximum_exponents[str(canonical(u).as_expr())] == 2
    assert all(
        exponent == 1
        for factor, exponent in maximum_exponents.items()
        if factor != str(canonical(u).as_expr())
    )
    common_degree = int(sum(
        sp.Poly(factor, u, v).total_degree() * exponent
        for factor, exponent in maximum_exponents.items()
    ))
    assert common_degree == 19
    output = {
        "schema": "marici.benincasa.marked_extension_candidate_pole_lattice.v1",
        "status": "pass",
        "candidate_entry_count": len(entries),
        "maximum_denominator_total_degree": max(entry["denominator_total_degree"] for entry in entries),
        "common_lcm_total_degree": common_degree,
        "maximum_factor_exponents": dict(sorted(maximum_exponents.items())),
        "all_factors_in_preexisting_source_support_inventory": True,
        "entries": entries,
        "scope": "exact theorem about the reconstructed candidate; source-wide pole-lattice authorization remains open",
    }
    RESULT.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
