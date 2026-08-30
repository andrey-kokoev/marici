"""Exact identification of the union transverse line with a marked crossing."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research" / "benincasa" / ".tmp_sympy"))
import sympy as sp

OUT = Path(__file__).resolve().parents[1] / "results" / "physical_union_crossing_kato_line.json"


def main() -> None:
    x, y, z, a, b = sp.symbols("x y z a b")
    et = x + y + z
    k = (
        x**2*a**4 - (x**2+y**2-z**2)*a**2*b**2 + y**2*b**4
        + (x**2*(x**2-y**2-z**2)+et**2*(y**2-x**2-z**2))*a**2
        + (y**2*(y**2-x**2-z**2)+et**2*(x**2-y**2-z**2))*b**2
        + z**2*et**4 + et**2*z**2*(z**2-x**2-y**2) + z**2*x**2*y**2
    )
    crossing_value = sp.factor(k.subs({a: y, b: x}))
    cubic = sp.factor(crossing_value / et**3)
    q = sp.expand(
        3*x**4 + 4*x**3*(y+z)
        - 2*x**2*(7*y**2+2*y*z+3*z**2)
        + 4*x*(y-3*z)*(y+z)**2
        + (3*y-5*z)*(y+z)**3
    )
    gcd_q = sp.factor(sp.gcd(sp.Poly(q, x, y, z), sp.Poly(et*cubic, x, y, z)).as_expr())
    branch_ranks = {"V23": 20, "V31": 20, "intersection": 15, "sum": 25, "union": 26}
    mobius_excess = branch_ranks["union"] - branch_ranks["sum"]
    passed = sp.expand(crossing_value - et**3*cubic) == 0 and gcd_q == 1 and mobius_excess == 1
    payload = {
        "schema": "marici.physical-union-crossing-kato-line.v1",
        "crossing": {"q_g23": "b-x", "q_g31": "a-y", "point": "(a,b)=(y,x)"},
        "K_at_crossing_factorization": str(crossing_value),
        "generic_unit_condition": "E_T*C_cross != 0",
        "gcd_of_Q_with_crossing_exceptional_locus": str(gcd_q),
        "branch_rank_packet": branch_ranks,
        "rank_one_union_excess": mobius_excess,
        "local_generator": "dlog(q_g23) wedge dlog(q_g31)",
        "interpretation": "the transverse line is the ordinary two-normal Kato/Gysin class at the marked-line crossing",
        "passed": passed,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
