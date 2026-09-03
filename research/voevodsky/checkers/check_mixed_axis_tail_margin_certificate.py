from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/mixed-axis-tail-margin-certificate-v1.json")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    c, L = sp.symbols("c L", positive=True, real=True)
    a = 1 / (4 * c)
    integral = sp.exp(1 / (16 * c)) * (
        sp.exp(-c * (L - a) ** 2) / (2 * c)
        + sp.sqrt(sp.pi) * sp.erfc(sp.sqrt(c) * (L - a)) / (8 * c * sp.sqrt(c))
    )
    integrand_at_L = L * sp.exp(L / 2 - c * L**2)
    assert sp.simplify(sp.diff(integral, L) + integrand_at_L) == 0
    assert sp.limit(integral, L, sp.oo) == 0

    # Exact Weyl-margin fixtures with ||R||_op <= delta.
    delta = sp.Rational(1, 10)
    positive_truncation = sp.diag(sp.Rational(1, 4), sp.Rational(1, 2))
    positive_tail = sp.diag(-delta, delta)
    positive_full = positive_truncation + positive_tail
    assert min(positive_truncation.diagonal()) - delta >= 0
    assert min(positive_full.diagonal()) >= 0

    negative_truncation = sp.diag(sp.Rational(-1, 4), sp.Rational(1, 2))
    negative_tail = sp.diag(delta, -delta)
    negative_full = negative_truncation + negative_tail
    assert min(negative_truncation.diagonal()) + delta < 0
    assert min(negative_full.diagonal()) < 0

    unresolved_truncation = sp.diag(sp.Rational(1, 20), sp.Rational(1, 2))
    assert abs(min(unresolved_truncation.diagonal())) <= delta

    status = contract["status"]
    assert status["source_constant_C_c"] == "not sourced here"
    result = {
        "schema":"marici.voevodsky.mixed-axis-tail-margin-certificate-check.v1",
        "status":"mixed_axis_margin_logic_verified",
        "erfc_integral_antiderivative_verified":True,
        "positive_margin_fixture":True,
        "negative_margin_fixture":True,
        "unresolved_interval_fixture":True,
        "source_constants_supplied":False,
        "global_all_packet_positivity":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
