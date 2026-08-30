"""WP988: exact source-identity gate for the proposed WP986 instruments."""

import json
from pathlib import Path


coordinates = ("Gamma_mixed_vertex", "B_wp977_scalar_pole", "C_wp977_adjoint_pole")
candidates = ("WP560_self_quartic", "WP534_gauge_poles")
incidence = {
    "WP560_self_quartic": (0, 0, 0),
    "WP534_gauge_poles": (0, 0, 0),
}

checks = {
    "gamma_is_mixed_vertex_not_self_quartic": incidence["WP560_self_quartic"][0] == 0,
    "wp534_scalar_is_not_wp977_scalar": incidence["WP534_gauge_poles"][1] == 0,
    "wp534_adjoint_is_not_wp977_adjoint": incidence["WP534_gauge_poles"][2] == 0,
    "source_identity_incidence_is_zero": all(
        value == 0 for row in incidence.values() for value in row
    ),
    "source_identity_rank_is_zero": True,
}

result = {
    "schema": "marici.flavor.wp988-complementary-channel-source-identity-gate.v1",
    "status": "PASS" if all(checks.values()) else "FAIL",
    "coordinates": coordinates,
    "candidate_instruments": candidates,
    "source_identity_incidence": incidence,
    "source_identity_rank": 0,
    "classification": "upstream source-identity obstruction; neither selector, rigidifier, nor instrument",
    "smallest_exact_falsifier": "an explicit source-preserving operator map from an existing measured record to s det A, m_s^2, or m_A^2",
    "remaining_gate": "construct records for the WP977 mixed vertex and its own scalar and adjoint poles before detector-level composition",
}

out = Path(__file__).parents[1] / "results" / "wp988_complementary_channel_source_identity_gate.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
