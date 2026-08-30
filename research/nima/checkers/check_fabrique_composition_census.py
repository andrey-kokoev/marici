"""Bounded four-sector falsifier for the Fabrique-of-Reality conjecture."""

import json
from pathlib import Path


Y, N, U = "yes", "no", "open"
sectors = {
    "scattering": {
        "admitted_comparison": Y,
        "presentation_invariant_remainder": Y,
        "composition_or_horizontality": Y,
        "physical_population": N,
        "remainder": "alternating-fusion relative normal conductor symbol",
    },
    "cosmology": {
        "admitted_comparison": Y,
        "presentation_invariant_remainder": Y,
        "composition_or_horizontality": Y,
        "physical_population": U,
        "remainder": "rank-seven kernel / elliptic-Tate extension sector",
    },
    "radiative_gravity": {
        "admitted_comparison": Y,
        "presentation_invariant_remainder": Y,
        "composition_or_horizontality": Y,
        "physical_population": Y,
        "remainder": "corner difference / memory class",
    },
    "flavor": {
        "admitted_comparison": N,
        "presentation_invariant_remainder": N,
        "composition_or_horizontality": N,
        "physical_population": N,
        "remainder": "none: sparse loop phase is chart data, not a physical obstruction",
    },
}

# Broad v1 says every failed gluing retains meaningful physical information.
v1_survives = all(v["presentation_invariant_remainder"] == Y for v in sectors.values())
assert not v1_survives

# Authority-qualified v2 says a remainder may be formed only after an admitted
# comparison exists.  Every sector with a claimed remainder meets that gate.
v2_typing_consistent = all(
    v["admitted_comparison"] == Y
    for v in sectors.values()
    if not v["remainder"].startswith("none:")
)
assert v2_typing_consistent

# Physicality is a further, independent population/readout gate.
assert sectors["scattering"]["physical_population"] == N
assert sectors["radiative_gravity"]["physical_population"] == Y

result = {
    "status": "PASS",
    "sectors": sectors,
    "broad_v1_survives": v1_survives,
    "authority_qualified_v2_typing_consistent": v2_typing_consistent,
    "surviving_rule": (
        "Only an invariant defect of an admitted comparison morphism is a "
        "candidate remembered remainder; physical meaning additionally "
        "requires a source-derived population/readout map."
    ),
}
out = Path(__file__).parents[1] / "results" / "fabrique_composition_census.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
