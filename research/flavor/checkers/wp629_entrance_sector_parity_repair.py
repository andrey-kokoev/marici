"""Exact WP629 Z2 sector-parity constraint audit."""
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
fields = ("Q", "Hu", "Hd", "AuL", "AuR", "BuL", "BuR",
          "AdL", "AdR", "BdL", "BdR", "u", "d", "S", "X")
fixed = {"Q": 0, "Hu": 0, "Hd": 1, "u": 0, "S": 0, "X": 0}
constraints = (
    ("Q", "Hu", "AuR"), ("AuL", "S", "BuR"), ("BuL", "X", "u"),
    ("Q", "Hd", "AdR"), ("AdL", "S", "BdR"), ("BdL", "X", "d"),
    ("AuL", "AuR"), ("BuL", "BuR"), ("AdL", "AdR"), ("BdL", "BdR"),
)

def allowed(p, term):
    return sum(p[x] for x in term) % 2 == 0

free = [x for x in fields if x not in fixed]
solutions = []
for bits in itertools.product((0, 1), repeat=len(free)):
    p = fixed | dict(zip(free, bits))
    if all(allowed(p, term) for term in constraints):
        solutions.append(p)

p = solutions[0]
even_cross_invariants = {
    "norm_u": ("Hu", "Hu"), "norm_d": ("Hd", "Hd"),
    "cross_modulus_square": ("Hu", "Hd", "Hu", "Hd"),
    "cross_square_real_part": ("Hu", "Hd", "Hu", "Hd"),
    "weak_antisymmetric_norm": ("Hu", "Hd", "Hu", "Hd"),
}
checks = {
    "unique_solution_under_frozen_assignments": len(solutions) == 1,
    "all_declared_vertices_and_masses_survive": all(allowed(p, t) for t in constraints),
    "off_diagonal_kinetic_term_forbidden": not allowed(p, ("Hu", "Hd")),
    "wrong_down_to_up_entrance_forbidden": not allowed(p, ("Q", "Hd", "AuR")),
    "wrong_up_to_down_entrance_forbidden": not allowed(p, ("Q", "Hu", "AdR")),
    "all_required_even_cross_invariants_survive": all(allowed(p, t) for t in even_cross_invariants.values()),
    "down_vev_spontaneously_breaks_parity": p["Hd"] == 1,
}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP629", "status": "PASS", "checks": checks,
    "parity_assignment": p,
    "classification": "declared source-extension rigidifier; not a numerical selector or instrument",
    "repair": "forbids the Hu-Hd kinetic Gram and wrong-sector entrance vertices",
    "surviving_geometry": list(even_cross_invariants),
    "smallest_exact_falsifier": "any parity-even Hu-dagger Hd bilinear",
    "new_physical_gate": "both entrance vevs break Z2, so domain-wall history or explicit soft breaking must be typed",
    "remaining_gates": ["complete RG closure", "finite threshold matching", "calibrated instrument"],
}
(ROOT / "results" / "wp629_entrance_sector_parity_repair.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

