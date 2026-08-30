#!/usr/bin/env python3
"""Triangle measure normalization versus the conductor Laurent pole."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research" / "benincasa" / "results" / "rank26-source-normalization-cancels-conductor-pole.json"
eps, A, B = sp.symbols("eps A B")

# Remove the epsilon-independent factor (16/9)*Vol(Sigma_2).
c_reduced = sp.pi**eps * 3**(2*eps) / sp.gamma(eps)
c0 = sp.limit(c_reduced/eps, eps, 0)
c1 = sp.simplify(sp.limit((c_reduced-eps)/eps**2, eps, 0))
J = A/eps+B
normalized_limit = sp.simplify(sp.limit(c_reduced*J, eps, 0))
normalized_first_grade = sp.simplify(sp.limit((c_reduced*J-A)/eps, eps, 0))

checks = {
    "normalization_has_simple_zero": c0 == 1,
    "normalization_second_coefficient": sp.simplify(sp.expand_log(c1, force=True)-(sp.EulerGamma+sp.log(sp.pi)+2*sp.log(3))) == 0,
    "conductor_pole_cancels": normalized_limit == A,
    "finite_remainder_enters_first_grade": sp.simplify(sp.expand_log(normalized_first_grade, force=True)-(B+A*(sp.EulerGamma+sp.log(sp.pi)+2*sp.log(3)))) == 0,
}

packet = {
    "schema": "marici.rank26-source-normalization-cancels-conductor-pole.v1",
    "specialization": {"d": "3+2 epsilon", "n_s": 3, "L": 1, "n_e": 3},
    "reduced_source_normalization": "pi^epsilon*3^(2 epsilon)/Gamma(epsilon)",
    "normalization_expansion": "epsilon + epsilon^2*(EulerGamma+log(pi)+2 log(3)) + O(epsilon^3)",
    "generic_conductor_jet": "A/epsilon+B+O(epsilon)",
    "normalized_grade_zero": str(normalized_limit),
    "normalized_grade_one": str(normalized_first_grade),
    "omitted_common_factor": "(16/9)*Vol(Sigma_2(P^2))",
    "checks": {key: bool(value) for key, value in checks.items()},
    "passed": all(bool(value) for value in checks.values()),
    "conclusion": "The source measure normalization has a simple zero that cancels the conductor Laurent pole. At d=3 the normalized conductor contribution is its residue A; the finite wall remainder B contributes only to the first epsilon grade.",
    "scope": "This concerns the conductor analytic family. Common marked-wall endpoint poles still require the source sewing of Entry 3857 before specialization.",
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(packet, indent=2)+"\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
if not packet["passed"]:
    raise SystemExit(1)
