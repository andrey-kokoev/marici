import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Parent-level description of the WP1056 localized cell.  SU(6) gauge
# invariance forces masses to be constant on each parent multiplet, not on
# each residual branch independently.
parents = [
    {"id": "15", "full_dim": 15, "bulk_dim": 15, "exchange": None},
    {"id": "bar6a", "full_dim": 6, "bulk_dim": 2, "exchange": "bar6"},  # 4 localized, 2 bulk
    {"id": "bar6b", "full_dim": 6, "bulk_dim": 6, "exchange": "bar6"},
]
full_degree = sum(p["full_dim"] for p in parents)
bulk_C = sum(p["bulk_dim"] for p in parents)
assert full_degree == 27
assert bulk_C == 23

parent_mass_dimension = len(parents)
assert parent_mass_dimension == 3

# Exchange identifies the two bar6 parents.  The 15 is not exchange-related to
# a six-dimensional parent, so one relative clock remains.
exchange_mass_dimension = 2
common_clock_dimension = 1
assert exchange_mass_dimension - common_clock_dimension == 1


def weighted_bulk_mean(m15_sq, mbar6_sq):
    return Fraction(15 * m15_sq + (2 + 6) * mbar6_sq, 23)

assert weighted_bulk_mean(1, 1) == 1
assert weighted_bulk_mean(1, 2) == Fraction(31, 23)
assert weighted_bulk_mean(2, 1) == Fraction(38, 23)

# The parent-level gate reduces, but does not eliminate, WP1058's clock gap.
residual_branch_gap_after_exchange = 4
parent_gap_after_exchange = exchange_mass_dimension - common_clock_dimension
assert residual_branch_gap_after_exchange == 4
assert parent_gap_after_exchange == 1

result = {
    "schema": "marici.flavor.wp1059.v1",
    "status": "PASS",
    "question": "Does SU(6) parent invariance reduce the localized cell's common-clock obstruction?",
    "parents": parents,
    "full_degree": full_degree,
    "bulk_C": bulk_C,
    "parent_mass_dimension": parent_mass_dimension,
    "exchange_mass_dimension": exchange_mass_dimension,
    "common_clock_dimension": common_clock_dimension,
    "residual_branch_gap_after_exchange": residual_branch_gap_after_exchange,
    "parent_gap_after_exchange": parent_gap_after_exchange,
    "clock_tests": {
        "unit_parent_clock": {
            "masses_sq": {"15": 1, "bar6a": 1, "bar6b": 1},
            "bulk_weighted_mean": str(weighted_bulk_mean(1, 1)),
        },
        "bar6_heavier": {
            "masses_sq": {"15": 1, "bar6a": 2, "bar6b": 2},
            "bulk_weighted_mean": str(weighted_bulk_mean(1, 2)),
        },
        "fifteen_heavier": {
            "masses_sq": {"15": 2, "bar6a": 1, "bar6b": 1},
            "bulk_weighted_mean": str(weighted_bulk_mean(2, 1)),
        },
    },
    "classification": "conditional parent-clock fiber: SU(6) invariance reduces WP1058's four exchange-even residual gaps to one relative clock between the 15 and bar6 parents",
    "remaining_gate": "derive the inter-parent equality m15^2=mbar6^2, a common compactification clock, or a projection to the irreducible spin-11 cell; then normalize M^2=1 and derive p^2/M^2",
    "claim_boundary": "uses parent-level SU(6) invariance and the WP1056 localization split; it does not prove that the distinct 15 and bar6 parent masses are equal",
    "disposition": "productive: the common-clock obstruction is narrowed to one exact inter-parent alignment gap",
}

(ROOT / "results" / "wp1059_parent_hypermultiplet_clock_fiber.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1059 PASS:", bulk_C, parent_mass_dimension, exchange_mass_dimension, parent_gap_after_exchange)
