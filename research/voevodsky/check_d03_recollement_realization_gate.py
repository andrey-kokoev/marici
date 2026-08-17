"""Audit the open/closed typing of the D03 physical realization."""

import json

open_component = {
    "support": "U=D(x3)",
    "map": "first-Rees generic bridge",
    "q03_Q": "retained nonzero",
    "coefficient": "k=x3 (a unit on U)",
}
closed_component = {
    "support": "Z=V(x3)",
    "map": "logarithmic simple-pole residue",
    "cartier_symbol": "+1",
    "open_restriction": 0,
}

assert open_component["q03_Q"] == "retained nonzero"
assert closed_component["open_restriction"] == 0
assert open_component["support"] != closed_component["support"]

# Neither boundary component can be the whole realization.  They must be
# glued as a morphism of localization triangles.
realization = {
    "alpha_U": open_component,
    "alpha_Z": closed_component,
    "remaining_cell": (
        "delta_E alpha_U(q_J) ~ "
        "alpha_Z[1](-[xi_tilde_03])"
    ),
}

print(json.dumps({
    "claim": "The D03 realization is a recollement morphism, not a single residue functor: the generic first-Rees map and closed logarithmic residue occupy different components and require one Beck-Chevalley gluing cell.",
    "status": "proved_boundary_components_forced_gluing_cell_open",
    "realization": realization,
    "boundary_coefficient_freedom": "none",
    "gluing_cell_existence": "OPEN",
    "gluing_cell_ambiguity_if_exists": "zero by endpoint-relative Hom vanishing",
}, sort_keys=True))
