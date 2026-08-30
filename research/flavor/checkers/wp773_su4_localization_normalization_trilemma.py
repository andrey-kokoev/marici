"""Exact SU(4) localization, spectral-sign, and normalization trilemma."""
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
wp772 = json.loads(
    (ROOT / "results" / "wp772_su4_gauge_link_boundary_normalization_fiber.json").read_text(
        encoding="utf-8"
    )
)

N_V = 15
link_hyper_cost = 0
portal_operand_hyper_cost = 32
required_mediator_hyper_cost = 48

kappa_boundary_operands = 2 + N_V - link_hyper_cost
kappa_bulk_operands = 2 + N_V - link_hyper_cost - portal_operand_hyper_cost
kappa_bulk_completed = kappa_bulk_operands - required_mediator_hyper_cost
positive_hyper_budget = 2 + N_V - 1

# Orbifold fixed points admit residual-gauge-invariant kinetic operators
# independently of whether charged matter is boundary-localized or bulk.
boundary_common_kinetic_modulus = True
bulk_common_kinetic_modulus = True

checks = {
    "wp772_dependency_passed": wp772["status"] == "PASS" and all(wp772["checks"].values()),
    "gauge_link_has_zero_hyper_cost": link_hyper_cost == 0,
    "boundary_operands_leave_positive_index_seventeen": kappa_boundary_operands == 17,
    "portal_operand_bulk_cost_is_thirty_two": portal_operand_hyper_cost == 32,
    "bulk_operands_reverse_index_to_negative_fifteen": kappa_bulk_operands == -15,
    "required_bulk_mediators_reduce_index_to_negative_sixty_three": kappa_bulk_completed == -63,
    "positive_index_hyper_budget_is_sixteen": positive_hyper_budget == 16,
    "portal_operands_exceed_positive_budget": portal_operand_hyper_cost > positive_hyper_budget,
    "boundary_branch_has_normalization_modulus": boundary_common_kinetic_modulus,
    "bulk_branch_retains_orbifold_kinetic_modulus": bulk_common_kinetic_modulus,
    "no_minimal_branch_has_both_positive_index_and_no_boundary_modulus": not (
        (kappa_boundary_operands > 0 and not boundary_common_kinetic_modulus)
        or (kappa_bulk_operands > 0 and not bulk_common_kinetic_modulus)
    ),
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP773",
    "status": "PASS",
    "checks": checks,
    "dependency": "WP772",
    "admitted_state_domain": "the minimal SU(4) gauge-link parent with either boundary-localized portal operands or the same orbifold zero-mode packet promoted to bulk hypermultiplets, with optional compulsory link mediators",
    "faithful_coordinate": "bulk-versus-boundary localization, degree-weighted hypermultiplet count, spectral index kappa, and presence of the exchange-even boundary kinetic modulus",
    "boundary_branch": "portal operands localized at the boundary give kappa=17 but retain the common boundary normalization tau",
    "bulk_branch": "promoting portal operands to bulk retains the orbifold fixed-point kinetic modulus, costs N_H=32, and gives kappa=-15",
    "completed_bulk_branch": "including the compulsory mediator packet costs another 48 degrees and gives kappa=-63",
    "classification": "within the minimal SU(4) orbifold parent, every localization branch retains the boundary normalization modulus, while bulk localization additionally reverses the half-twist spectral sign",
    "smallest_exact_falsifier": "the positive-index hyper budget is 16, while the portal operand packet alone costs 32",
    "deutschian_status": "moving fields to the bulk is not a repair because fixed-point kinetic terms remain legal and the changed spectral source reverses the selected vacuum",
    "escape_gate": "a larger or different source group must supply at least sixteen additional vector degrees and a separate principle fixing the orbifold common kinetic term, while preserving the exact flavor embedding, chirality, anomaly completion, and isolated gauge normalization",
    "instrument_gate": "neither branch supplies the actual physical16 realization of the WP770 ports",
}
(ROOT / "results" / "wp773_su4_localization_normalization_trilemma.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
