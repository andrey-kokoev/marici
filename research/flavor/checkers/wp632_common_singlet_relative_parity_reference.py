"""Exact WP632 parity constraints with the WP489 common singlet."""
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
fields = ("Q", "Hu", "Hd", "sigma", "AuL", "AuR", "BuL", "BuR",
          "AdL", "AdR", "BdL", "BdR", "u", "d", "S", "X")
fixed = {"Q": 0, "Hu": 0, "Hd": 1, "sigma": 1,
         "u": 0, "S": 0, "X": 0}
route_terms = (
    ("Q", "Hu", "AuR"), ("AuL", "S", "BuR"), ("BuL", "X", "u"),
    ("Q", "Hd", "AdR"), ("AdL", "S", "BdR"), ("BdL", "X", "d"),
)
singlet_masses = (("sigma", "AuL", "AuR"), ("sigma", "BuL", "BuR"),
                   ("sigma", "AdL", "AdR"), ("sigma", "BdL", "BdR"))
bare_masses = (("AuL", "AuR"), ("BuL", "BuR"),
               ("AdL", "AdR"), ("BdL", "BdR"))

def allowed(p, term):
    return sum(p[x] for x in term) % 2 == 0

free = [x for x in fields if x not in fixed]
solutions = []
for bits in itertools.product((0, 1), repeat=len(free)):
    p = fixed | dict(zip(free, bits))
    if all(allowed(p, t) for t in route_terms + singlet_masses):
        solutions.append(p)
p = solutions[0]

relative_orbits = {
    frozenset(((h, s), (-h, -s))) for h, s in itertools.product((-1, 1), repeat=2)
}
relative_values = [{h * s for h, s in orbit} for orbit in relative_orbits]

checks = {
    "unique_parity_solution": len(solutions) == 1,
    "all_route_vertices_survive": all(allowed(p, t) for t in route_terms),
    "all_singlet_masses_survive": all(allowed(p, t) for t in singlet_masses),
    "all_bare_masses_are_forbidden": all(not allowed(p, t) for t in bare_masses),
    "mixed_entrance_kinetic_term_forbidden": not allowed(p, ("Hu", "Hd")),
    "wrong_sector_entrances_forbidden": (not allowed(p, ("Q", "Hd", "AuR"))
                                         and not allowed(p, ("Q", "Hu", "AdR"))),
    "diagonal_sign_action_has_two_relative_classes": len(relative_orbits) == 2,
    "relative_product_is_constant_and_faithful": all(len(v) == 1 for v in relative_values)
                                                   and len({next(iter(v)) for v in relative_values}) == 2,
}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP632", "status": "PASS", "checks": checks,
    "parity_assignment": p,
    "admitted_domain": "WP489 singlet-generated two-stage messenger masses",
    "relative_reference": "simultaneous odd pair (Hd,sigma) with abstract invariant sign(Hd) sign(sigma)",
    "classification": "existing-source relative-reference candidate and rigidifier; selector unproved",
    "smallest_exact_falsifier": "every explicit bare messenger mass is parity odd",
    "descent_gate": "derive a matched amplitude odd in the relative class after all messenger rephasings",
    "gauging_gate": "audit discrete anomalies and gauge-defect spectrum",
}
(ROOT / "results" / "wp632_common_singlet_relative_parity_reference.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

