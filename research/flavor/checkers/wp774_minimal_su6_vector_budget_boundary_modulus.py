"""Exact minimal SU(n) vector-budget and boundary-modulus audit."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
wp773 = json.loads(
    (ROOT / "results" / "wp773_su4_localization_normalization_trilemma.json").read_text(
        encoding="utf-8"
    )
)

portal_hyper_cost = 32
mediator_hyper_cost = 48

def dim_su(n):
    return n**2 - 1

def kappa(n, hyper_cost):
    return 2 + dim_su(n) - hyper_cost

su4_dim = dim_su(4)
su5_dim = dim_su(5)
su6_dim = dim_su(6)
kappa5 = kappa(5, portal_hyper_cost)
kappa6 = kappa(6, portal_hyper_cost)
kappa6_completed = kappa(6, portal_hyper_cost + mediator_hyper_cost)
su6_branch_dimensions = [15, 3, 1, 8, 8]

C, tau = sp.symbols("C tau", positive=True, real=True)
g_boundary2 = 1 / (C + tau)
portal = g_boundary2 / 10

checks = {
    "wp773_corrected_dependency_passed": wp773["status"] == "PASS" and all(wp773["checks"].values()),
    "su4_dimension_is_fifteen": su4_dim == 15,
    "su5_dimension_is_twenty_four": su5_dim == 24,
    "su6_dimension_is_thirty_five": su6_dim == 35,
    "su5_portal_bulk_index_is_negative_six": kappa5 == -6,
    "su6_portal_bulk_index_is_positive_five": kappa6 == 5,
    "su6_is_minimal_su_n_with_positive_portal_index": all(
        kappa(n, portal_hyper_cost) <= 0 for n in range(2, 6)
    ) and kappa6 > 0,
    "su6_branching_dimensions_sum_to_thirty_five": sum(su6_branch_dimensions) == 35,
    "su6_contains_su4_parent_block": su6_branch_dimensions[0] == 15,
    "extra_su6_vector_budget_is_twenty": su6_dim - su4_dim == 20,
    "completed_mediator_packet_reverses_su6_index": kappa6_completed == -43,
    "orbifold_common_kinetic_modulus_remains": portal.has(tau),
    "hostile_boundary_pair_changes_magnitude": portal.subs({C: 1, tau: 0}) == sp.Rational(1, 10)
    and portal.subs({C: 1, tau: 1}) == sp.Rational(1, 20),
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP774",
    "status": "PASS",
    "checks": checks,
    "dependency": "corrected WP773",
    "admitted_state_domain": "the SU(n) simple-group chain containing the SU(4) gauge-link parent, with the 32-degree bulk portal operand packet, optional 48-degree compulsory mediator packet, and the complete residual-gauge-invariant orbifold boundary kinetic term",
    "faithful_coordinate": "parent rank n, vector dimension n^2-1, bulk hypermultiplet cost, spectral index kappa, and common boundary kinetic coefficient tau",
    "source_authorized_probe": "degree-weighted full-tower spectral index and exact simple-group branching dimensions",
    "minimal_group_result": "SU(5) gives kappa=-6; SU(6) gives kappa=5 and is the first SU(n) extension with positive index for the bulk portal operands",
    "branching_result": "35=15+3+1+8+8 under SU(4) x SU(2) x U(1), so the SU(4) gauge-link parent embeds as a block",
    "classification": "SU(6) repairs the vector-degree spectral budget for the portal operands but neither explains why SU(6) is selected nor removes the orbifold common kinetic modulus; the compulsory mediator bulk packet still reverses the sign",
    "smallest_exact_falsifier": "SU(5) has insufficient vector budget with kappa=-6, while SU(6) passes only the portal-operand count and falls to -43 when compulsory mediators are bulk",
    "deutschian_status": "minimality under a chosen SU(n) scan is a classification, not a source explanation; changing tau still changes the portal without changing the bulk group or spectral sign",
    "next_source_gate": "derive the SU(6) enlargement and localization from anomaly and chirality constraints, keep required mediators from reversing the spectral measure, and fix the common orbifold kinetic coefficient through a boundary source law",
    "instrument_gate": "the WP770 two-port response remains without an actual physical16 production and decay realization",
}
(ROOT / "results" / "wp774_minimal_su6_vector_budget_boundary_modulus.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
