"""Exact hostile separating graph-energy and saturated-orthogonal wall/tail forms."""

import hashlib
import json
from fractions import Fraction
from pathlib import Path

records = []
for mass, tail in [
    (Fraction(1, 3), Fraction(1, 4)),
    (Fraction(2, 5), Fraction(-1, 7)),
    (Fraction(1, 2), Fraction(1, 8)),
]:
    graph_energy = Fraction(1) + (mass + tail) ** 2
    orthogonal_energy = Fraction(1) + mass**2 + tail**2
    cross_term = 2 * mass * tail
    assert graph_energy - orthogonal_energy == cross_term
    assert graph_energy != orthogonal_energy
    records.append(
        {
            "mass": str(mass),
            "tail": str(tail),
            "graph_energy": str(graph_energy),
            "saturated_orthogonal_energy": str(orthogonal_energy),
            "cross_term": str(cross_term),
            "forms_distinguished": True,
        }
    )

payload = {
    "schema": "marici.research.check.v1",
    "claim": "shifted-history graph energy and saturated wall-tail orthogonality are distinct quadratic forms",
    "exact_arithmetic": "fractions.Fraction",
    "records": records,
    "equality_condition": "Re< f, Bf > = 0 on the represented incidence range (or an explicit congruence producing cancellation)",
    "form_selection_proved": False,
    "quadratic_congruence_proved": False,
    "g1_1_closed": False,
    "verdict": "zero saturated cross loading cannot be substituted for the graph cross term without a representation theorem",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["sha256"] = hashlib.sha256(canonical).hexdigest()

out = Path(__file__).parents[1] / "results" / "rh-wall-tail-form-branch.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
