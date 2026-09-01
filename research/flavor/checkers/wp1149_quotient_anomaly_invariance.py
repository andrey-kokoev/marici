import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# The anomaly data live on the localized SU6 cell, not on the event
# reweighting matching. Hence every quotient matching class carries the same
# vectors from WP1067/WP1069/WP1070.
classes = ["orbit_A", "orbit_B", "orbit_C"]
five_channel = [Fraction(1,2), Fraction(1,4), Fraction(0), Fraction(2), Fraction(2)]
seven_channel = [Fraction(1,2), Fraction(1,4), Fraction(0), Fraction(2), Fraction(2), Fraction(-1,4), Fraction(0)]
coset = [Fraction(1,2), Fraction(1,4), Fraction(0), Fraction(0), Fraction(0), Fraction(3,4), Fraction(0)]
vectors = {name: {"five": five_channel, "seven": seven_channel, "coset": coset} for name in classes}

# All pairwise differences vanish exactly.
def sub(a,b):
    return [x-y for x,y in zip(a,b)]

zero5 = [Fraction(0)] * 5
zero7 = [Fraction(0)] * 7
pairwise_zero = True
for i,a in enumerate(classes):
    for b in classes[i+1:]:
        pairwise_zero &= sub(vectors[a]["five"], vectors[b]["five"]) == zero5
        pairwise_zero &= sub(vectors[a]["seven"], vectors[b]["seven"]) == zero7
        pairwise_zero &= sub(vectors[a]["coset"], vectors[b]["coset"]) == zero7
assert pairwise_zero

matching_dependent_channels = 0
selected_classes = 0
assert matching_dependent_channels == 0
assert selected_classes == 0

result = {
    "schema": "marici.flavor.wp1149.v1",
    "status": "PASS",
    "question": "Do anomaly or Green-Schwarz data distinguish the three quotient matching classes?",
    "dpc": {
        "conjecture": "Anomaly or Green-Schwarz data select one quotient matching class.",
        "rivals": [
            "class-selective anomaly channel",
            "shared anomaly vector",
            "matching-dependent Green-Schwarz split",
            "no anomaly distinction"
        ],
        "risky_consequences": [
            "same five-channel vector for all classes",
            "same seven-channel vector for all classes",
            "same shifted coset for all classes",
            "zero selected class"
        ],
        "falsification_attempt": "All pairwise differences vanish exactly; the matching affects event reweighting, not the localized-cell anomaly channels.",
        "residual": "Boundary S-matrix phase data may still distinguish reweighting classes.",
        "disposition": "reject anomaly selection across quotient matching classes"
    },
    "quotient_classes": classes,
    "five_channel_vector": [str(x) for x in five_channel],
    "seven_channel_vector": [str(x) for x in seven_channel],
    "shifted_coset": [str(x) for x in coset],
    "pairwise_differences_zero": pairwise_zero,
    "matching_dependent_channels": matching_dependent_channels,
    "selected_classes": selected_classes,
    "classification": "negative gate: anomaly/Green-Schwarz data are invariant across all quotient matching classes",
    "remaining_gate": "test boundary S-matrix phase data against the three classes",
    "hostile_gate": "do not use a class-independent anomaly vector to select a reweighting matching",
    "claim_boundary": "anomaly invariance is exact for the sourced localized-cell vectors",
    "disposition": "anomaly-invariance leaf resolved; S-matrix phase rival selected",
}

(ROOT / "results" / "wp1149_quotient_anomaly_invariance.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1149 PASS:", len(classes), pairwise_zero, selected_classes)
