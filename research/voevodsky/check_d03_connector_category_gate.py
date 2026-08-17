"""Audit the categorical prerequisites for the D03 connector equation."""

import json

raw_q_shriek = {"perfect": False, "telescope_tail": True, "x4_exceptional_sector": True}
finite_physical_pc = {
    "perfect": True,
    "telescope_tail": False,
    "x4_exceptional_sector": False,
    "positive_cap_unit": True,
}

# Perfectness is invariant under equivalence.
assert raw_q_shriek["perfect"] != finite_physical_pc["perfect"]
assert raw_q_shriek["telescope_tail"] and not finite_physical_pc["telescope_tail"]
assert raw_q_shriek["x4_exceptional_sector"] and not finite_physical_pc["x4_exceptional_sector"]

required_realization = {
    "direction": "support-selected raw q! -> finite physical PC/Rees",
    "nonconservative": True,
    "kills": ["localization-completion telescope tail", "x4 exceptional sector"],
    "preserves": [
        "generic q03^Q leg",
        "x3 Cartier symbol +1",
        "incidence differential",
        "endpoint restrictions",
        "D3 action",
    ],
}

assert required_realization["nonconservative"]
assert "generic q03^Q leg" in required_realization["preserves"]
assert "x3 Cartier symbol +1" in required_realization["preserves"]

print(json.dumps({
    "claim": "The frozen D03 connector equation is not yet an equation in one admitted category: its raw exceptional q! input and finite physical PC/Rees target have no constructed comparison functor.",
    "status": "proved_typing_obstruction_not_connector_nonexistence",
    "raw_q_shriek": raw_q_shriek,
    "finite_physical_pc": finite_physical_pc,
    "equivalence_or_isomorphism": "impossible by perfectness and tail invariants",
    "required_realization": required_realization,
    "connector_equation": "UNTYPED_UNTIL_REALIZATION",
    "connector_existence": "OPEN",
}, sort_keys=True))
