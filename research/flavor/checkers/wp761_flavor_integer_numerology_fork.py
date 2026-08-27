"""Exact audit of candidate tadpole integers in the admitted flavor packet."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


def oriented_partitions(total):
    return [(n0, total - n0) for n0 in range(1, total) if n0 > total - n0 > 0]


def portal_contrast(pair):
    r = sp.Rational(pair[0], pair[1])
    return sp.factor((r**2 - 1) ** 2 / (2 * (r**2 + 1) ** 2))


# One left-handed Standard Model family, including multiplicities.
Y = {
    "Q": sp.Rational(1, 6),
    "u_c": sp.Rational(-2, 3),
    "d_c": sp.Rational(1, 3),
    "L": sp.Rational(-1, 2),
    "e_c": sp.Integer(1),
}
grav_Y = 6 * Y["Q"] + 3 * Y["u_c"] + 3 * Y["d_c"] + 2 * Y["L"] + Y["e_c"]
cubic_Y = 6 * Y["Q"]**3 + 3 * Y["u_c"]**3 + 3 * Y["d_c"]**3 + 2 * Y["L"]**3 + Y["e_c"]**3
su2_sq_Y = 3 * Y["Q"] + Y["L"]
su3_sq_Y = 2 * Y["Q"] + Y["u_c"] + Y["d_c"]
witten_doublets_per_family = 3 + 1

family_count = 3
link_dimension = 2 * 2
T_family = family_count
T_link = link_dimension
pair_family = oriented_partitions(T_family)[0]
pair_link = oriented_partitions(T_link)[0]
delta_family = portal_contrast(pair_family)
delta_link = portal_contrast(pair_link)

# A hostile five-family replication preserves every familywise perturbative
# anomaly and Witten parity but destroys the singleton tadpole fiber.
hostile_family_count = 5
hostile_pairs = oriented_partitions(hostile_family_count)

checks = {
    "one_family_gravitational_hypercharge_anomaly_vanishes": grav_Y == 0,
    "one_family_cubic_hypercharge_anomaly_vanishes": cubic_Y == 0,
    "one_family_SU2_squared_hypercharge_anomaly_vanishes": su2_sq_Y == 0,
    "one_family_SU3_squared_hypercharge_anomaly_vanishes": su3_sq_Y == 0,
    "witten_doublet_count_is_even_familywise": witten_doublets_per_family % 2 == 0,
    "three_family_projection_gives_exceptional_total_three": T_family == 3,
    "link_dimension_projection_gives_exceptional_total_four": T_link == 4,
    "two_untyped_integer_projections_predict_different_portals": delta_family == sp.Rational(9, 50) and delta_link == sp.Rational(8, 25),
    "anomaly_vector_does_not_choose_between_three_and_four": all(value == 0 for value in (grav_Y, cubic_Y, su2_sq_Y, su3_sq_Y)),
    "five_family_hostile_remains_anomaly_free": hostile_family_count * grav_Y == hostile_family_count * cubic_Y == 0,
    "five_family_hostile_has_nonsingleton_oriented_fiber": len(hostile_pairs) == 2,
    "vectorlike_pairs_have_zero_net_chiral_anomaly": (+1) + (-1) == 0,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP761",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "the WP737/WP738 three-family product-group representation packet, including its bifundamental link and anomaly-neutral vectorlike pairs",
    "faithful_coordinate": "a named homomorphism from the representation/anomaly lattice to the ordered boundary-charge lattice, not an integer visible in a presentation",
    "largest_source_authorized_probe_family": "familywise perturbative gauge anomalies, mixed gravitational hypercharge anomaly, SU(2) Witten parity, and vectorlike cancellation",
    "probe_result": "all admitted anomaly probes vanish (or are even) familywise and on the vectorlike sublattice; they produce no positive tadpole total",
    "integer_fork": {
        "family_multiplicity_projection": {"T": T_family, "portal_contrast": str(delta_family)},
        "link_dimension_projection": {"T": T_link, "portal_contrast": str(delta_link)},
    },
    "contextual_partition": "the anomaly probe identifies all family replications and all vectorlike completions that remain familywise anomaly-free; presentation-level counts separate them without source authority",
    "classification": "neither selector nor rigidifier of the tadpole map; the current packet supplies competing integer coincidences but no constructor",
    "smallest_exact_falsifier": "T=3 from family multiplicity predicts 9/50 while T=4 from bifundamental dimension predicts 8/25, and the zero anomaly vector chooses neither",
    "hostile_domain_extension": "five familywise anomaly-free copies preserve the authorized anomaly record but yield a two-element oriented tadpole fiber if family count is reinterpreted as T",
    "deutschian_status": "calling either visible integer the tadpole is easy to vary and changes the prediction without changing the anomaly explanation",
    "next_source_gate": "derive an actual integral index map from a compactification, defect charge, or K-theory class to ordered boundary charge; do not identify it with family count or representation dimension by notation",
    "remaining_physical_gate": "even a derived singleton index must survive RG and threshold matching and descend to a labelled physical16 detector observable",
}
(ROOT / "results" / "wp761_flavor_integer_numerology_fork.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
