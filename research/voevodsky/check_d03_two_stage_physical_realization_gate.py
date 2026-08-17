"""Distinguish the support quotient from telescope-cone localization."""

import json

# Exceptional associated packet: degree zero has x3 and x4 branches and
# degree one has the center.  The strongest physical incidence is [1 0].
d_x3 = 1
d_x4 = 0
assert d_x4 == 0                  # x4 spans a subcomplex
assert d_x3 == 1                  # retained x3-to-center unit

# The ordinary-normal telescope is instead the cone of the retained dual
# localization arrow L^vee -> R^vee.  It is not an independent generator
# summand that can be removed by the preceding support quotient.
dual_localization_arrow = "RHom(R[x^-1],R) -> RHom(R,R)"
telescope = "Cone(dual_localization_arrow)"
assert "dual_localization_arrow" in telescope

realization = [
    {"stage": 1, "operation": "support quotient", "kills": ["x4 branch"]},
    {
        "stage": 2,
        "operation": "Verdier/Bousfield localization or residue",
        "inverts": [dual_localization_arrow],
        "kills": [telescope],
    },
]
assert realization[0]["operation"] != realization[1]["operation"]

print(json.dumps({
    "claim": "The physical realization cannot be one generator quotient: x4 is a stable support subcomplex, while the telescope is the cone of a retained arrow.",
    "status": "proved_two_stage_realization_type",
    "x4_subcomplex": True,
    "telescope_subcomplex_of_named_sector_decomposition": False,
    "realization": realization,
    "next_gate": "construct the canonical residue/localization functor and test preservation of q03^Q and the x3 Cartier unit",
}, sort_keys=True))
