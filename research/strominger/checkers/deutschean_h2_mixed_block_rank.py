#!/usr/bin/env python3
"""Deterministically retire the invalid mixed H2 rank artifact."""

import hashlib
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
PACKET = ROOT / "research/strominger/deutschean-connected-vertex-source-frontier.md"
RESULT = ROOT / "research/strominger/results/deutschean_h2_mixed_block_rank.json"
SOURCE_CHECKER = ROOT / "research/strominger/checkers/deutschean_h2_phase_null_probe.py"
CLOSED_CHECKER = ROOT / "research/strominger/checkers/deutschean_closed_mixed_circuit.py"

# Columns: homogeneous H1 phase-null direction; phase compensation of db=1;
# explicit dc=1. Rows: stable T^2,T^3,T^4 coefficients of DH2.
matrix = sp.Matrix([
    [-sp.Rational(435, 2), -sp.Rational(53, 99), 3],
    [-sp.Rational(31065, 52), sp.Rational(13787, 2574), -2],
    [-sp.Rational(113817, 416), sp.Rational(3449, 1872), 0],
])
primitive = sp.Matrix([sp.Rational(1, 99), sp.Rational(3, 2), 1])

checks = {
    "legacy_matrix_reproduces_withdrawn_null": matrix * primitive == sp.zeros(3, 1),
    "corrected_phase_probe_transports_explicit_atom": "c*z*s.exp(T)" in SOURCE_CHECKER.read_text(),
    "corrected_closed_checker_requires_H2_obstruction": (
        "closed_mixed_circuit_has_exact_H2_obstruction" in CLOSED_CHECKER.read_text()
        and "2*T**2*(T**2-2)" in CLOSED_CHECKER.read_text()
    ),
}
payload = {
    "artifact_sha256": hashlib.sha256(PACKET.read_bytes()).hexdigest().upper(),
    "source_checker_sha256": hashlib.sha256(SOURCE_CHECKER.read_bytes()).hexdigest().upper(),
    "checks": checks,
    "observed": {
        "rows": ["T^2", "T^3", "T^4"],
        "columns": ["phase_null", "b_compensated_phase", "explicit_c"],
        "matrix": [[str(value) for value in row] for row in matrix.tolist()],
        "legacy_rank": matrix.rank(),
        "legacy_determinant": str(matrix.det()),
        "legacy_null_vector": [str(value) for value in primitive],
        "status": "withdrawn",
        "correction": "The explicit amplitude term is c*z*exp(T), not c*T, under phase deformation.",
    },
    "passed": all(checks.values()),
    "semantic_boundary": (
        "Retirement evidence for an invalid historical rank artifact. The old "
        "matrix is reproduced only to identify it; no kernel claim is retained."
    ),
}
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(0 if payload["passed"] else 1)
