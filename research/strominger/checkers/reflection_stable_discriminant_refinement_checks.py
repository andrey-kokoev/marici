import json
from pathlib import Path


P = 7


def in_l_mod_p(vector):
    x, y = vector
    return (3 * x - 2 * y) % P == 0


def in_xl_mod_p(vector):
    x, y = vector
    return (2 * x - 3 * y) % P == 0


plane = [(x, y) for x in range(P) for y in range(P)]
l_line = [v for v in plane if in_l_mod_p(v)]
xl_line = [v for v in plane if in_xl_mod_p(v)]
intersection_mod_p = [v for v in plane if in_l_mod_p(v) and in_xl_mod_p(v)]
sum_mod_p = {
    ((a[0] + b[0]) % P, (a[1] + b[1]) % P)
    for a in l_line for b in xl_line
}

diagonal = {(t, t) for t in range(P)}
anti_diagonal = {(t, (-t) % P) for t in range(P)}

orbits_under_common_mode = []
unseen = set(plane)
while unseen:
    representative = min(unseen)
    orbit = {
        ((representative[0] + t) % P, (representative[1] + t) % P)
        for t in range(P)
    }
    orbits_under_common_mode.append(sorted(orbit))
    unseen -= orbit

difference_values = {(u - v) % P for u, v in plane}
orbit_difference_values = [
    {(u - v) % P for u, v in orbit} for orbit in orbits_under_common_mode
]

gates = [
    len(l_line) == 7,
    len(xl_line) == 7,
    set(l_line) != set(xl_line),
    intersection_mod_p == [(0, 0)],
    len(sum_mod_p) == 49,
    len(plane) == 49,
    len(diagonal) == 7,
    len(anti_diagonal) == 7,
    diagonal & anti_diagonal == {(0, 0)},
    len(orbits_under_common_mode) == 7,
    all(len(orbit) == 7 for orbit in orbits_under_common_mode),
    all(len(values) == 1 for values in orbit_difference_values),
    difference_values == set(range(7)),
]

result = {
    "schema": "marici.strominger.reflection_stable_discriminant_refinement.v1",
    "prime": P,
    "one_chart_image_order_mod_p": len(l_line),
    "reflected_chart_image_order_mod_p": len(xl_line),
    "chart_lines_distinct": set(l_line) != set(xl_line),
    "intersection_mod_p": intersection_mod_p,
    "integral_intersection": "7 Z^2",
    "stable_discriminant": "(Z/7)^2",
    "stable_discriminant_order": len(plane),
    "sum_lattice": "Z^2",
    "sum_quotient_order": 1,
    "symmetric_sector_order": len(diagonal),
    "antisymmetric_sector_order": len(anti_diagonal),
    "common_mode_orbit_count": len(orbits_under_common_mode),
    "common_mode_orbit_size": 7,
    "context_coordinate": "u-v mod 7",
    "context_value_count": len(difference_values),
    "typed_conclusion": "49 raw classes are the reflection-stable two-chart discriminant; 7 contextual classes are its antisymmetric quotient",
    "gates_passed": sum(gates),
    "gates_total": len(gates),
    "all_passed": all(gates),
}

output = Path(__file__).parents[1] / "results" / "reflection_stable_discriminant_refinement_checks.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
print(json.dumps(result, indent=2))
raise SystemExit(0 if all(gates) else 1)
