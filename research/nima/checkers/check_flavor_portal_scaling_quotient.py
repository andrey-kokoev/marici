from fractions import Fraction
import json
from pathlib import Path


def portal(state):
    g_phi, g_psi, kappa, mass = state
    return -kappa * g_phi * g_psi / (mass * mass)


def widths(state):
    g_phi, g_psi, _, _ = state
    return g_phi * g_phi, g_psi * g_psi


def arc(state):
    g_phi, g_psi, _, _ = state
    return g_phi * g_psi


def scale(state, a, b):
    g_phi, g_psi, kappa, mass = state
    return a * g_phi, b * g_psi, kappa / (a * b), mass


base = (Fraction(1), Fraction(1), Fraction(1), Fraction(1))
orbit = {
    (a, b): scale(base, a, b)
    for a in (Fraction(1), Fraction(2), Fraction(3))
    for b in (Fraction(1), Fraction(2), Fraction(3))
}

assert all(portal(state) == Fraction(-1) for state in orbit.values())
assert len({widths(state) for state in orbit.values()}) == 9
assert len({arc(state) for state in orbit.values()}) == 6

# WP606's smallest width-loss witness.
width_witness_left = base
width_witness_right = scale(base, Fraction(2), Fraction(1, 2))
assert portal(width_witness_left) == portal(width_witness_right)
assert widths(width_witness_left) != widths(width_witness_right)
assert arc(width_witness_left) == arc(width_witness_right)

# A second symmetry keeps the portal fixed while changing the coherent arc.
arc_witness_left = base
arc_witness_right = scale(base, Fraction(2), Fraction(1))
assert portal(arc_witness_left) == portal(arc_witness_right)
assert arc(arc_witness_left) != arc(arc_witness_right)

# No section of the portal quotient can be equivariant under its nontrivial
# stabilizer: equivariance would require its selected point to be fixed.
nontrivial = (Fraction(2), Fraction(1))
assert scale(base, *nontrivial) != base
assert portal(scale(base, *nontrivial)) == portal(base)
equivariant_section_fixed_point_exists = False

result = {
    "schema": "marici.nima.flavor-portal-scaling-quotient.v1",
    "finite_positive_scaling_orbit_size": len(orbit),
    "distinct_width_packets_in_orbit": len({widths(s) for s in orbit.values()}),
    "distinct_coherent_arcs_in_orbit": len({arc(s) for s in orbit.values()}),
    "portal_constant_on_orbit": True,
    "width_packet_reconstructible_from_portal": False,
    "coherent_arc_reconstructible_from_portal": False,
    "equivariant_section_fixed_point_exists": equivariant_section_fixed_point_exists,
    "verdict": (
        "The physical16 scalar is a scaling quotient. A reverse constructor "
        "must choose a noncanonical orbit representative; only a source-derived "
        "mediator grammar can restrict the domain before projection."
    ),
}

output = Path(__file__).parents[1] / "results" / "flavor-portal-scaling-quotient.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
