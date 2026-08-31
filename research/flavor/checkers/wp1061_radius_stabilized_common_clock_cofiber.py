import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# WP790 stabilizes R_*^2=3 A n^2/(2B).  WP1060's half-twist level-zero clock
# is M^2=1/(4R_*^2).  In terms of r=B/A this is M^2=r/(6n^2).
def radius_sq(n, gauge_gravity_ratio):
    return Fraction(3 * n * n, 2 * gauge_gravity_ratio)


def clock_sq(n, gauge_gravity_ratio):
    return Fraction(gauge_gravity_ratio, 6 * n * n)

cases = {
    "unit_clock_n1": (1, 6),
    "heavy_clock_n1": (1, 12),
    "unit_clock_n2": (2, 24),
    "light_clock_n2": (2, 6),
}
computed = {}
for name, (n, r) in cases.items():
    R2 = radius_sq(n, r)
    M2 = clock_sq(n, r)
    assert M2 == Fraction(1, 4 * R2)
    computed[name] = {"n": n, "B_over_A": r, "radius_sq": R2, "clock_sq": M2}

assert computed["unit_clock_n1"]["radius_sq"] == Fraction(1, 4)
assert computed["unit_clock_n1"]["clock_sq"] == 1
assert computed["heavy_clock_n1"]["clock_sq"] == 2
assert computed["unit_clock_n2"]["radius_sq"] == Fraction(1, 4)
assert computed["unit_clock_n2"]["clock_sq"] == 1
assert computed["light_clock_n2"]["clock_sq"] == Fraction(1, 4)

# Flux reflection leaves every radius and clock invariant.
for n, r in [(1, 6), (2, 24)]:
    assert clock_sq(n, r) == clock_sq(-n, r)
    assert radius_sq(n, r) == radius_sq(-n, r)

# The exact joint condition for the desired unit clock.
unit_cases = [name for name, value in computed.items() if value["clock_sq"] == 1]
assert unit_cases == ["unit_clock_n1", "unit_clock_n2"]
for value in computed.values():
    assert (value["clock_sq"] == 1) == (value["B_over_A"] == 6 * value["n"] * value["n"])

result = {
    "schema": "marici.flavor.wp1061.v1",
    "status": "PASS",
    "question": "Does WP790 radius stabilization calibrate WP1060's common-twist clock?",
    "clock_law": "R_*^2=3 A n^2/(2B), M^2=1/(4R_*^2)=(B/A)/(6n^2)",
    "unit_clock_condition": "B/A=6 n^2",
    "cases": {
        name: {k: (str(v) if isinstance(v, Fraction) else v) for k, v in value.items()}
        for name, value in computed.items()
    },
    "mirror_invariance": "n and -n have the same radius and common clock",
    "classification": "conditional radius-clock cofiber: curvature-flux stabilization makes the inter-parent clock absolute only after the flux sector and gauge-gravity ratio are fixed",
    "remaining_gate": "derive the flux sector n and gauge-gravity ratio B/A from the same compactification; then calibrate a physical momentum p^2/M^2 in this frame",
    "claim_boundary": "uses WP790's classical Einstein-Maxwell balance and WP1060's half-twist KK clock; it does not quantize B/A or select n",
    "disposition": "productive: the absolute-clock blocker is reduced to one exact joint quantization condition, with adjacent heavy/light and flux-sector hostiles",
}

(ROOT / "results" / "wp1061_radius_stabilized_common_clock_cofiber.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1061 PASS:", computed["unit_clock_n1"]["clock_sq"], computed["unit_clock_n2"]["clock_sq"], unit_cases)
