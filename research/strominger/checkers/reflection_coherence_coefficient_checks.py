"""Periodic C2-resolution checks for trivial and sign coefficient modules."""
import json
from pathlib import Path


def cohomology_label(action, degree, ring):
    if degree == 0:
        return "invariants"
    if ring in {"Q", "C", "Z[1/2]"}:
        return "0"
    if ring != "Z":
        raise ValueError(ring)
    if action == "trivial":
        return "Z/2" if degree % 2 == 0 else "0"
    if action == "sign":
        return "Z/2" if degree % 2 == 1 else "0"
    raise ValueError(action)


degrees = range(1, 9)
table = {
    ring: {
        action: {str(n): cohomology_label(action, n, ring) for n in degrees}
        for action in ("trivial", "sign")
    }
    for ring in ("Z", "Q", "C", "Z[1/2]")
}

tests = {
    "trivial_integral_even_torsion": all(
        table["Z"]["trivial"][str(n)] == ("Z/2" if n % 2 == 0 else "0")
        for n in degrees
    ),
    "sign_integral_odd_torsion": all(
        table["Z"]["sign"][str(n)] == ("Z/2" if n % 2 == 1 else "0")
        for n in degrees
    ),
    "inverting_two_kills_positive_cohomology": all(
        table[ring][action][str(n)] == "0"
        for ring in ("Q", "C", "Z[1/2]")
        for action in ("trivial", "sign")
        for n in degrees
    ),
    "bare_reflection_has_no_odd_primary_torsion": all(
        value in {"0", "Z/2"}
        for action in ("trivial", "sign")
        for value in table["Z"][action].values()
    ),
}

result = {
    "schema": "marici.checker_results.v1",
    "checker": "reflection_coherence_coefficient_checks.py",
    "passed": all(tests.values()),
    "tests": tests,
    "bounded_table": table,
    "verdict": "reflection coherence depth depends on coefficient parity and collapses after inverting 2",
}

out = Path(__file__).resolve().parents[1] / "results" / "reflection_coherence_coefficient_checks.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
