#!/usr/bin/env python3
"""Exact provenance audit for the generic algebraic Gysin line.

This consumes the already certified QQ(a1,lambda) nine-master connection.
It does not recompute or fit that connection.  The test asks whether the
source-selected rank-one algebraic subquotient carries the published quartic
Q, or instead is a rational dlog line on a different, explicitly derived
divisor.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys
import traceback

HERE = Path(__file__).resolve().parent
def _write_uncaught(exc_type, exc, tb):
    (HERE / "generic_algebraic_line_provenance.error.txt").write_text(
        "".join(traceback.format_exception(exc_type, exc, tb)), encoding="utf-8"
    )
    sys.__excepthook__(exc_type, exc, tb)

sys.excepthook = _write_uncaught
sys.path.insert(0, str(HERE / ".tmp_sympy"))
import sympy as sp


SOURCE = HERE / "derive_nine_master_residue_connection.result.json"
OUTPUT = HERE / "generic_algebraic_line_provenance.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


data = json.loads(SOURCE.read_text(encoding="utf-8"))
assert data["status"] == "exact_connection_found"
assert data["slice"] == {
    "X1": "a1*lambda",
    "X2": "lambda",
    "X3": "1",
    "E": "a1*lambda + lambda + 1",
}
assert data["algebraic_plane"]["invariant"] is True
assert data["algebraic_plane"]["e6_subline_invariant"] is True
assert (
    data["algebraic_plane"]["selected_rank_one_subquotient"]
    == "quotient span(e6,v_alg)/span(e6), represented by v_alg"
)

a1, lam = sp.symbols("a1 lambda")
x = a1 * lam
y = lam
E = x + y + 1
alpha = sp.cancel(
    sp.sympify(
        data["algebraic_plane"]["selected_connection_coefficient"].replace(
            "lambda", "lam"
        ),
        locals={"a1": a1, "lam": lam},
    )
)
Q = sp.factor(
    sp.sympify(
        data["Q_transverse_slice"]["Q"].replace("lambda", "lam"),
        locals={"a1": a1, "lam": lam},
    )
)

D = sp.factor(E**4 - x**2 * y**2)
D_minus = sp.factor(E**2 - x * y)
D_plus = sp.factor(E**2 + x * y)
assert sp.expand(D - D_minus * D_plus) == 0
assert sp.cancel(alpha - sp.diff(D, lam) / D) == 0

ring = sp.QQ.poly_ring(a1, lam)
q_poly = sp.Poly(Q, a1, lam, domain=sp.QQ)
d_poly = sp.Poly(D, a1, lam, domain=sp.QQ)
gcd_q_d = sp.gcd(q_poly, d_poly)
assert gcd_q_d.total_degree() == 0

result = {
    "schema": "marici.benincasa.generic_algebraic_line_provenance.v1",
    "input": {
        "path": SOURCE.name,
        "sha256": sha256(SOURCE),
        "field": "QQ(a1,lambda)",
        "slice": data["slice"],
    },
    "selected_subquotient": (
        "quotient span(e6,v_alg)/span(e6), represented by v_alg"
    ),
    "connection": sp.sstr(alpha, order="lex"),
    "derived_dlog_divisor": sp.sstr(D, order="lex"),
    "factorization": {
        "D_minus": sp.sstr(D_minus, order="lex"),
        "D_plus": sp.sstr(D_plus, order="lex"),
        "identity": "D=(E^2-X1*X2)(E^2+X1*X2)",
    },
    "exact_checks": {
        "alpha_equals_dlog_D": True,
        "gcd_Q_D": sp.sstr(gcd_q_d.as_expr(), order="lex"),
        "Q_is_not_selected_algebraic_line_support": True,
    },
    "interpretation": [
        "The generic source-selected algebraic Gysin subquotient is rational dlog data.",
        "Its divisor is D=E^4-X1^2*X2^2, not the published quartic Q.",
        "This coefficient result does not define the physical moving residue cycle.",
        "It therefore neither proves nor disproves Var_Q(Gamma_phys)=0.",
    ],
}
OUTPUT.write_text(
    json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps({"status": "ok", "output": str(OUTPUT)}, indent=2))
