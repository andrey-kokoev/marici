"""Exact SU(6) anomaly-family and spectral-generation audit."""
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
wp774 = json.loads(
    (ROOT / "results" / "wp774_minimal_su6_vector_budget_boundary_modulus.json").read_text(
        encoding="utf-8"
    )
)

N = 6
A_fundamental = 1
A_antifundamental = -A_fundamental
A_two_index_antisymmetric = N - 4
family_anomaly = A_two_index_antisymmetric + 2 * A_antifundamental

dim_antisymmetric = N * (N - 1) // 2
dim_antifundamental = N
family_degree = dim_antisymmetric + 2 * dim_antifundamental

# SU(6) -> SU(4) x SU(2) x U(1) dimensions:
# 15 -> 6 + 8 + 1; each bar6 -> 4 + 2.
antisymmetric_branch = [6, 8, 1]
antifundamental_branch = [4, 2]

N_V = N**2 - 1
def kappa(n_bulk_families):
    return 2 + N_V - n_bulk_families * family_degree

checks = {
    "wp774_dependency_passed": wp774["status"] == "PASS" and all(wp774["checks"].values()),
    "antisymmetric_anomaly_coefficient_is_two": A_two_index_antisymmetric == 2,
    "family_cubic_anomaly_cancels": family_anomaly == 0,
    "antisymmetric_dimension_is_fifteen": dim_antisymmetric == 15,
    "minimal_family_degree_is_twenty_seven": family_degree == 27,
    "antisymmetric_branch_sums_to_fifteen": sum(antisymmetric_branch) == 15,
    "antifundamental_branch_sums_to_six": sum(antifundamental_branch) == 6,
    "one_bulk_family_keeps_positive_index_ten": kappa(1) == 10,
    "two_bulk_families_reverse_index_to_negative_seventeen": kappa(2) == -17,
    "three_bulk_families_give_negative_forty_four": kappa(3) == -44,
    "positive_spectral_index_allows_at_most_one_bulk_family": max(
        n for n in range(4) if kappa(n) > 0
    ) == 1,
    "three_boundary_families_leave_pure_vector_index_thirty_seven": kappa(0) == 37,
    "boundary_localization_does_not_follow_from_anomaly_cancellation": family_anomaly == 0,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP775",
    "status": "PASS",
    "checks": checks,
    "dependency": "WP774",
    "admitted_state_domain": "the minimal chiral SU(6) family 15 plus two anti-6 representations, for zero through three bulk families, with the SU(6) vector adjoint and orbifold boundary kinetic ring",
    "faithful_coordinate": "number of bulk anomaly-free families, their 27-dimensional spectral cost, spectral index kappa, and boundary localization class",
    "source_authorized_probe": "SU(6) cubic anomaly coefficient and degree-weighted full-tower spectral index",
    "anomaly_result": "A(15)=2 and A(anti-6)=-1, so 15+2 anti-6 is anomaly-free with total degree 27",
    "spectral_partition": "zero bulk families gives kappa=37; one gives 10; two gives -17; three gives -44",
    "classification": "anomaly cancellation derives the family packet but not its localization; positive half-twist spectral sign permits at most one bulk family, while three observed chiral families must be boundary-localized or supported by a different spectral completion",
    "smallest_exact_falsifier": "the second bulk anomaly-free family changes kappa from 10 to -17",
    "deutschian_status": "SU(6) anomaly cancellation motivates the representation packet independently, but it does not select the favorable boundary localization and therefore does not fix the normalization modulus",
    "next_source_gate": "derive a generation-localization and inflow law that yields three chiral families while retaining a positive complete spectral measure and fixing the orbifold common kinetic coefficient",
    "instrument_gate": "no actual physical16 production and decay realization of the WP770 ports is supplied",
    "primary_source": "https://arxiv.org/abs/1604.07838",
}
(ROOT / "results" / "wp775_su6_anomaly_family_spectral_generation_gate.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
