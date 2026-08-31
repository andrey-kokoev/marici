import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# WP1056 bulk after localizing bar6a_to_4.  The remaining branches are distinct
# residual-group sectors, so an invariant mass-squared operator has one real
# eigenvalue per sector.
bulk_branches = [
    {"id": "15_to_6", "dim": 6},
    {"id": "15_to_8", "dim": 8},
    {"id": "15_to_1", "dim": 1},
    {"id": "bar6b_to_4", "dim": 4},
    {"id": "bar6a_to_2", "dim": 2, "exchange": "doublet"},
    {"id": "bar6b_to_2", "dim": 2, "exchange": "doublet"},
]
C = sum(b["dim"] for b in bulk_branches)
assert C == 23

mass_block_dimension = len(bulk_branches)
assert mass_block_dimension == 6

# Bar6 exchange identifies only the two doublet sectors.  It does not align
# their mass with the 6, 8, 1, or retained 4.
exchange_classes = []
used = set()
for i, b in enumerate(bulk_branches):
    if i in used:
        continue
    if b.get("exchange") == "doublet":
        j = next(j for j, x in enumerate(bulk_branches) if j > i and x.get("exchange") == "doublet")
        exchange_classes.append([i, j])
        used.update([i, j])
    else:
        exchange_classes.append([i])
        used.add(i)
exchange_mass_dimension = len(exchange_classes)
assert exchange_mass_dimension == 5
assert exchange_mass_dimension > 1


def weighted_mean(masses):
    assert len(masses) == len(bulk_branches)
    return sum(Fraction(b["dim"] * m) for b, m in zip(bulk_branches, masses)) / C

unit_clock = [1, 1, 1, 1, 1, 1]
retained_quartet_heavier = [1, 1, 1, 2, 1, 1]
exchange_breaking_ports = [1, 1, 1, 1, 2, 1]
assert weighted_mean(unit_clock) == 1
assert weighted_mean(retained_quartet_heavier) == Fraction(27, 23)
assert weighted_mean(exchange_breaking_ports) == Fraction(25, 23)

# Exchange-even hostile: only the retained quartet is shifted.  It preserves
# the two-port exchange symmetry but is not the common clock.
def exchange_even(masses):
    return masses[4] == masses[5]
assert exchange_even(retained_quartet_heavier)
assert not exchange_even(exchange_breaking_ports)

# WP1054's irreducible spin-11 cell forces an invariant mass operator to be
# scalar.  The localized SU(6) cell is reducible, so Schur's lemma supplies no
# such common-clock theorem here.
clock_alignment_gap_before_exchange = mass_block_dimension - 1
clock_alignment_gap_after_exchange = exchange_mass_dimension - 1
assert clock_alignment_gap_before_exchange == 5
assert clock_alignment_gap_after_exchange == 4

result = {
    "schema": "marici.flavor.wp1058.v1",
    "status": "PASS",
    "question": "Does the WP1056 localized SU(6) bulk cell derive a common pole clock?",
    "bulk_branches": bulk_branches,
    "mass_block_dimension": mass_block_dimension,
    "bar6_exchange_classes": exchange_classes,
    "exchange_mass_dimension": exchange_mass_dimension,
    "clock_alignment_gap_before_exchange": clock_alignment_gap_before_exchange,
    "clock_alignment_gap_after_exchange": clock_alignment_gap_after_exchange,
    "clock_tests": {
        "unit_clock_weighted_mean": str(weighted_mean(unit_clock)),
        "retained_quartet_heavier": {
            "masses": retained_quartet_heavier,
            "weighted_mean": str(weighted_mean(retained_quartet_heavier)),
            "exchange_even": True,
        },
        "exchange_breaking_ports": {
            "masses": exchange_breaking_ports,
            "weighted_mean": str(weighted_mean(exchange_breaking_ports)),
            "exchange_even": False,
        },
    },
    "consistency_with_wp1054": {
        "irreducible_spin11_invariant_mass_operator": "scalar",
        "localized_su6_cell": "six residual-group blocks, five after bar6 exchange",
        "implication": "the SU(6) localization cell cannot be promoted to the common-clock pole cell without an additional alignment or projection law",
    },
    "classification": "negative common-clock gate: WP1056 derives C=23 and k=2 but its bulk cell is reducible, leaving five independent exchange-even mass blocks",
    "remaining_gate": "derive a common SU(6) parent mass, branch-alignment theorem, or projection from the localized cell to the irreducible spin-11 pole cell; then derive M^2=1 and p^2/M^2 from the same source",
    "claim_boundary": "counts invariant mass blocks under the residual SU(4)xSU(2)xU(1) branching; it does not reject a future parent-level alignment law",
    "disposition": "productive: the localization direction now has an exact clock obstruction and a typed hostile against declaring M^2=1 from localization alone",
}

(ROOT / "results" / "wp1058_localized_su6_clock_alignment_gate.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1058 PASS:", C, mass_block_dimension, exchange_mass_dimension, weighted_mean(retained_quartet_heavier))
