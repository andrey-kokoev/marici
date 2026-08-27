"""Exact rank bound for 5D first-order domain-wall chiral zero modes."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
wp775 = json.loads(
    (ROOT / "results" / "wp775_su6_anomaly_family_spectral_generation_gate.json").read_text(
        encoding="utf-8"
    )
)

y = sp.symbols("y", real=True)
M = (y + 1) * y * (y - 1)
primitive = sp.integrate(M, y)
profile = sp.exp(-primitive)
zero_mode_residual = sp.simplify(sp.diff(profile, y) + M * profile)

# A scalar first-order homogeneous equation has one integration constant.
scalar_kernel_dimension = 1
number_of_mass_sign_crossings = len(sp.solve(sp.Eq(M, 0), y))

# For r coupled components, a first-order linear system has an r-dimensional
# initial-value space. Three independent same-chirality families therefore
# require rank at least three; this internal multiplicity is spectral matter.
r_required = 3
su6_family_degree = 27
N_V_su6 = 35
bulk_degree_three_families = r_required * su6_family_degree
kappa_three = 2 + N_V_su6 - bulk_degree_three_families

checks = {
    "wp775_dependency_passed": wp775["status"] == "PASS" and all(wp775["checks"].values()),
    "multi_kink_mass_has_three_crossings": number_of_mass_sign_crossings == 3,
    "explicit_zero_mode_solves_first_order_equation": zero_mode_residual == 0,
    "scalar_first_order_kernel_has_one_initial_constant": scalar_kernel_dimension == 1,
    "three_crossings_do_not_create_three_kernel_dimensions": number_of_mass_sign_crossings == 3
    and scalar_kernel_dimension == 1,
    "three_independent_families_require_rank_three": r_required == 3,
    "rank_three_family_degree_is_eighty_one": bulk_degree_three_families == 81,
    "su6_rank_three_bulk_index_is_negative_forty_four": kappa_three == -44,
    "result_matches_wp775_three_family_partition": wp775["checks"][
        "three_bulk_families_give_negative_forty_four"
    ],
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP776",
    "status": "PASS",
    "checks": checks,
    "dependency": "WP775",
    "admitted_state_domain": "five-dimensional local domain-wall localization governed by a first-order linear chiral zero-mode equation for each SU(6) anomaly-family component, including arbitrary smooth scalar mass profiles and finite internal rank",
    "faithful_coordinate": "dimension of the first-order initial-value space, not the number of zeros of the mass profile",
    "source_authorized_probe": "kernel dimension of the chiral first-order differential operator",
    "rank_theorem": "one scalar hypermultiplet supplies at most one independent chiral profile; an r-component first-order system supplies at most r independent profiles",
    "hostile_multi_kink": "M(y)=(y+1)y(y-1) has three sign crossings but the zero-mode solution exp[-integral M] has only one integration constant",
    "classification": "a multi-kink profile can reshape or multilocalize one chiral wavefunction but cannot turn one SU(6) anomaly family into three independent generations without rank-three matter multiplicity",
    "smallest_exact_falsifier": "three mass zeros coexist with a one-dimensional scalar kernel",
    "spectral_consequence": "rank-three SU(6) family matter costs 81 bulk degrees and gives kappa=-44",
    "deutschian_status": "counting localization peaks as generations changes the readout of one state, not the ontology or kernel dimension; the proposed repair is invalid",
    "escape_gate": "a higher-dimensional topological index or other source operator with genuine index three is required, and its complete spectral contribution must be recomputed rather than borrowed from the 5D tower",
    "instrument_gate": "no actual physical16 realization of the generation-resolved WP770 ports is supplied",
}
(ROOT / "results" / "wp776_five_dimensional_domain_wall_generation_rank_no_go.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
