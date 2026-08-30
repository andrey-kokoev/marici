#!/usr/bin/env python3
"""Finite linear-algebra witness for the T7 counterterm typing gate."""
import hashlib
import json
from fractions import Fraction
from pathlib import Path


def rank(rows):
    a = [[Fraction(x) for x in row] for row in rows]
    r = 0
    for c in range(len(a[0])):
        p = next((i for i in range(r, len(a)) if a[i][c]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        q = a[r][c]
        a[r] = [x / q for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [a[i][j] - q * a[r][j] for j in range(len(a[0]))]
        r += 1
    return r


def main():
    root = Path(__file__).resolve().parents[3]
    # Residual UV grades from the exact frozen audit.  Kappa can be changed
    # without affecting the conclusion; use one as a generic marker.
    subtraction_image = [[1, 1], [0, Fraction(-5, 3)]]
    assert rank(subtraction_image) == 2

    # A physical theory supplies a contraction/readout on this universal
    # residual.  The master-space data alone admits inequivalent contractions.
    contractions = {
        "silent": [0, 0],
        "quartic_only": [1, 0],
        "linear_only": [0, 1],
        "both": [1, 1],
    }
    activated = {
        name: [sum(c[j] * row[j] for j in range(2)) for row in subtraction_image]
        for name, c in contractions.items()
    }
    assert activated["silent"] == [0, 0]
    assert activated["quartic_only"][0] != 0 and activated["quartic_only"][1] == 0
    assert activated["linear_only"][1] != 0
    assert all(x != 0 for x in activated["both"])

    result = {
        "schema": "marici.nima.t7_counterterm_typing_gate.v1",
        "passed": True,
        "universal_residual_uv_rank": 2,
        "admissible_contractions": contractions,
        "activated_uv_grades": {k: [str(x) for x in v] for k, v in activated.items()},
        "missing_map": "source theory/numerator/couplings -> T7 master coefficients -> local operator counterterm basis",
        "verdict": "master-space UV data does not determine physical counterterm activation or admissibility",
        "required_next_input": "the full source-normalized triangle wavefunction integrand together with the declared scalar action and its symmetry-allowed local operator basis",
    }
    output = root / "research/nima/results/t7_counterterm_typing_gate.json"
    payload = output.read_text(encoding="utf-8")
    assert json.loads(payload) == result
    print(json.dumps({"passed": True, "typing_gate": "open",
                      "sha256": hashlib.sha256(payload.encode()).hexdigest().upper()}))


if __name__ == "__main__":
    main()
