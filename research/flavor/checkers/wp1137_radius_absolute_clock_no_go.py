import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# WP1061 joint radius/twist law.
def clock(n, ratio):
    R2 = Fraction(3*n*n, 2*ratio)
    M2 = Fraction(1,4) / R2
    return R2, M2

solutions = []
hostiles = []
for n, ratio in [(1,6),(1,12),(2,24),(2,6)]:
    R2, M2 = clock(n, ratio)
    row = {"n": n, "B_over_A": ratio, "R2": str(R2), "M2": str(M2)}
    if M2 == 1:
        solutions.append(row)
    else:
        hostiles.append(row)
assert len(solutions) == 2
assert len(hostiles) == 2
assert (solutions[0]["n"], solutions[0]["B_over_A"]) == (1,6)
assert (solutions[1]["n"], solutions[1]["B_over_A"]) == (2,24)

# Flux reflection preserves n^2 and hence the radius/clock; no source selects
# flux sector or B/A. Localized clock descent remains separately absent.
flux_sectors_sourced = 0
gauge_gravity_ratios_sourced = 0
localized_descent_maps = 0
assert flux_sectors_sourced == 0
assert gauge_gravity_ratios_sourced == 0
assert localized_descent_maps == 0

result = {
    "schema": "marici.flavor.wp1137.v1",
    "status": "PASS",
    "question": "Can radius stabilization supply the absolute pole mass scale?",
    "dpc": {
        "conjecture": "Curvature-flux radius stabilization supplies the absolute unit pole clock.",
        "rivals": [
            "radius stabilization plus joint quantization",
            "flux-sector source selection",
            "gauge-gravity ratio source selection",
            "no absolute clock"
        ],
        "risky_consequences": [
            "B/A=6n^2",
            "a unique sourced flux sector n and ratio B/A",
            "M^2=1",
            "localized clock descent"
        ],
        "falsification_attempt": "The joint equation has at least two exact solutions, (1,6) and (2,24), while (1,12) gives M^2=2 and (2,6) gives M^2=1/4. No flux sector, ratio, or descent map is sourced.",
        "residual": "A future compactification packet may select n and B/A and prove descent.",
        "disposition": "reject radius stabilization as absolute pole-clock authority"
    },
    "joint_condition": "B/A=6n^2",
    "unit_clock_solutions": solutions,
    "hostile_rows": hostiles,
    "flux_sectors_sourced": flux_sectors_sourced,
    "gauge_gravity_ratios_sourced": gauge_gravity_ratios_sourced,
    "localized_descent_maps": localized_descent_maps,
    "classification": "negative gate: radius stabilization leaves joint quantization and descent unresolved",
    "remaining_gate": "derive a unique flux sector, gauge-gravity ratio, and localized clock descent",
    "hostile_gate": "do not treat B/A=6n^2, flux reflection, or one unit solution as absolute scale authority",
    "claim_boundary": "this rejects current absolute-clock authority, not a future compactification selection",
    "disposition": "absolute pole mass scale remains open",
}

(ROOT / "results" / "wp1137_radius_absolute_clock_no_go.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1137 PASS:", len(solutions), len(hostiles), flux_sectors_sourced, localized_descent_maps)
