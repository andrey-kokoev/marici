#!/usr/bin/env python3
"""Audit whether the primary source fixes an analytic regularization section."""
from __future__ import annotations

import json
import tarfile
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "temp" / "arxiv-2408.16386-source.tar"
OUT = ROOT / "research" / "benincasa" / "results" / "rank26-source-analytic-regularization-section.json"

with tarfile.open(SOURCE) as archive:
    cosmology = archive.extractfile("sections/cosmologicalintegrals.tex").read().decode("utf-8")
    full = archive.extractfile("sections/Fullintegration.tex").read().decode("utf-8")
    applications = archive.extractfile("sections/applications.tex").read().decode("utf-8")

d, eps = sp.symbols("d eps")
n_s = 3
loops = 1
measure_exponent = sp.simplify((d-n_s-loops)/2)
regulated_exponent = sp.simplify(measure_exponent.subs(d, 3+2*eps))

checks = {
    "source_defines_dimension_dependent_measure": "\\mu_d= c_{d,n_e" in cosmology,
    "source_defines_dimension_dependent_normalization": "c_{d,n_e^{(L)},L}" in cosmology,
    "source_declares_d_3_plus_2epsilon": "d=3+2\\epsilon" in full or "d=3+2\\epsilon" in applications,
    "source_calls_epsilon_analytic_regulator": "with $\\epsilon$ playing the role of an analytic regulator" in full,
    "triangle_exponent_is_minus_half_plus_epsilon": regulated_exponent == eps-sp.Rational(1, 2),
    "source_requires_independent_boundary_values_for_DE_solution": "have to be provided independently" in full,
    "source_lists_direct_integration_or_regularity": "direct integration" in applications and "imposing regularity" in applications,
    "no_explicit_renormalization_scale_string": "renormalization scale" not in (cosmology+full+applications).lower(),
}

packet = {
    "schema": "marici.rank26-source-analytic-regularization-section.v1",
    "primary_source": "arXiv:2408.16386 source archive",
    "provenance": {
        "measure": "sections/cosmologicalintegrals.tex, equations mCM and constant",
        "analytic_family": "sections/Fullintegration.tex, d=3+2 epsilon paragraph",
        "boundary_data": "sections/Fullintegration.tex and sections/applications.tex",
    },
    "triangle_measure_exponent": str(regulated_exponent),
    "checks": {key: bool(value) for key, value in checks.items()},
    "passed": all(bool(value) for value in checks.values()),
    "conclusion": "The primary source fixes a normalized analytic family K^(-1/2+epsilon). Its meromorphic continuation has source-defined Laurent coefficients once the original integral boundary data are retained. An arbitrary cutoff-scale torsor is not part of this frozen source family.",
    "scope": "This falsifies the claim that the source supplies only an unnormalized logarithmic torsor. It does not prove that the Laurent finite coefficient is a scheme-independent renormalized physical observable after additional local counterterms are admitted.",
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(packet, indent=2)+"\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
if not packet["passed"]:
    raise SystemExit(1)
