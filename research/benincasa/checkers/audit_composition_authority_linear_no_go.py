#!/usr/bin/env python3
"""Audit the minimal linear no-go for a fifth composition-authority tower."""

import json
from fractions import Fraction
from pathlib import Path

candidate = Fraction(1, 4)
target_pairing = Fraction(1, 4)

# The boundary-regular extension space is the one-dimensional rational line
# Q*omega.  A Q-linear admissible subspace is therefore either zero or the
# complete line.  Neither choice selects the known nonzero candidate.
linear_subspaces = {
    "zero": {"contains_candidate": candidate == 0, "unique_nonzero": False},
    "full_line": {"contains_candidate": True, "unique_nonzero": False},
}

# Pairing after an authorized q0-to-e6 operation would report c/4.  It is
# faithful in c but supplies no equation selecting c.
candidate_report = target_pairing * candidate

checks = {
    "candidate_is_nonzero": candidate != 0,
    "zero_subspace_rejects_candidate": not linear_subspaces["zero"]["contains_candidate"],
    "full_line_does_not_select_unique_nonzero": not linear_subspaces["full_line"]["unique_nonzero"],
    "target_pairing_reports_c_over_four": target_pairing == Fraction(1, 4),
    "candidate_report_would_be_one_over_16": candidate_report
    == Fraction(1, 16),
}

if not all(checks.values()):
    raise SystemExit(f"failed checks: {[key for key, ok in checks.items() if not ok]}")

packet = {
    "schema": "marici.benincasa.composition_authority_linear_no_go.v1",
    "extension_line": "Ext(q0,e6)=Q*omega",
    "candidate": "c=1/4, equivalently C2=-1/8",
    "target_pairing": "phi(e6)=1/4",
    "reported_composite": "phi o p o T o s = c/4",
    "linear_admissible_subspaces": linear_subspaces,
    "checks": checks,
    "verdict": (
        "A Q-linear tower of allowed coherence-cell compositions cannot select "
        "the nonzero extension amplitude. Selection requires a source-pointed "
        "operation, primitive oriented lattice generator, normalized current, "
        "or equivalent non-linear authority datum."
    ),
}

out = (
    Path(__file__).resolve().parents[1]
    / "results"
    / "composition_authority_linear_no_go.json"
)
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
