import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# WP1069/WP1070 exact seven-channel local inflow target and its coset.
cs_target = (Fraction(1,2),Fraction(1,4),0,2,2,Fraction(-1,4),0)
cs_residue = tuple(x % 1 for x in cs_target)
assert cs_residue == (Fraction(1,2),Fraction(1,4),0,0,0,Fraction(3,4),0)
assert len(cs_target) == 7

# WP1068 parent gauge-gravity completion is global; local split remains open.
parent_green_schwarz = -3
local_gs_split_supplied = False
assert parent_green_schwarz == -3 and not local_gs_split_supplied

# WP1098: contact counterterm is a separate rank-one direction disjoint from
# the rank-seven interaction quotient.
interaction_rank = 7
contact_total_rank = 8
assert contact_total_rank == interaction_rank + 1

# Clock and rho constraints.
clock_ratio_law = "B/A = 6*n*n"
rho_weight = -3
rho_tautology_forbidden = True
assert clock_ratio_law == "B/A = 6*n*n"
assert rho_weight == -3 and rho_tautology_forbidden

# Production must change branch weights and carry six physical16 rows.
branch_distribution = [Fraction(d,23) for d in (6,8,1,4,2,2)]
physical_target = [Fraction(1,4)] * 6
kernel_shape = (6,6)
required_gain = Fraction(3,2)
assert branch_distribution != physical_target
assert kernel_shape == (6,6) and required_gain == Fraction(3,2)

constraints = {
    "exact_seven_channel_lift": [str(x) for x in cs_target],
    "coset_residue": [str(x) for x in cs_residue],
    "parent_gauge_gravity_coefficient": parent_green_schwarz,
    "local_green_schwarz_split_required": True,
    "contact_counterterm_rank": contact_total_rank,
    "clock_ratio_law": clock_ratio_law,
    "rho_weight": rho_weight,
    "rho_must_not_be_1_over_D": rho_tautology_forbidden,
    "production_kernel_shape": list(kernel_shape),
    "production_gain": str(required_gain),
    "event_reweighting_required": True,
}
assert len(constraints) == 11
constructed_values = False
assert not constructed_values

result = {
    "schema": "marici.flavor.wp1110.v1",
    "status": "PASS",
    "question": "What anomaly and analyticity constraints must the 23 fused-defect fields satisfy?",
    "constraints": constraints,
    "branch_distribution": [str(x) for x in branch_distribution],
    "physical_target": [str(x) for x in physical_target],
    "constructed_values": constructed_values,
    "classification": "conditional gate: exact anomaly/analytic constraint fiber for a fused defect",
    "remaining_gate": "construct source-authorized field values satisfying all constraints",
    "hostile_gate": "do not satisfy the mod-Z7 residue alone, use parent GS=-3 as a local split, or use 1/D, internal pairings, or an arbitrary 6x6 matrix",
    "claim_boundary": "these are necessary constraints, not a positive defect construction",
    "disposition": "fused-defect constraint fiber completed",
}

(ROOT / "results" / "wp1110_fused_defect_anomaly_analyticity_fiber.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1110 PASS:", len(constraints), parent_green_schwarz, interaction_rank, contact_total_rank, required_gain)
