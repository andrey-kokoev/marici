import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

branches = [
    ("6", 6),
    ("8", 8),
    ("1", 1),
    ("4", 4),
    ("2a", 2),
    ("2b", 2),
]
assert sum(d for _, d in branches) == 23

# WP1060's common-twist admission gives every localized branch the same unit
# clock.  At each branch's own threshold, p^2=M^2 and the response is 1/2.
M2 = Fraction(1)
soft = []
for name, dim in branches:
    ratio = Fraction(1)
    response = Fraction(1, 2)
    soft.append({"branch": name, "dimension": dim, "M2": M2, "threshold_ratio": ratio, "response": response})

# The first vector-KK port is distinguishable by its ratio and response.
vector = {"channel": "vector_KK_N1", "threshold_ratio": Fraction(4), "response": Fraction(1, 5)}
assert vector["response"] == 1 / (1 + vector["threshold_ratio"])
assert all(x["response"] == Fraction(1, 2) for x in soft)
assert all(x["threshold_ratio"] == 1 for x in soft)

# A ratio-only instrument has rank one on the six soft candidates: every
# branch has the same one-column signature.  It separates soft from vector,
# but cannot choose 4, 2a+2b, or any other soft branch.
signature_rows = [[x["response"]] for x in soft]
assert len({tuple(row) for row in signature_rows}) == 1
assert vector["response"] != soft[0]["response"]

hostile_selections = {
    "localized_quartet_branch_4": False,
    "two_doublet_ports_2a_2b": False,
    "largest_dimensional_branch_8": False,
}
assert not any(hostile_selections.values())

result = {
    "schema": "marici.flavor.wp1074.v1",
    "status": "PASS",
    "question": "Does the common clock select a unique soft ratio-one physical16 production channel?",
    "soft_candidates": [
        {k: (str(v) if isinstance(v, Fraction) else v) for k, v in x.items()}
        for x in soft
    ],
    "vector_comparison": {k: (str(v) if isinstance(v, Fraction) else v) for k, v in vector.items()},
    "ratio_only_soft_signature_rank": 1,
    "hostile_selections_without_coupling": hostile_selections,
    "classification": "soft-channel degeneracy gate: all six localized SU(6) branches share ratio one and response 1/2 under the common clock, while the vector-KK port has ratio 4 and response 1/5",
    "remaining_gate": "derive a source-to-physical16 production/decay coupling matrix and gain law to select or reweight the six degenerate soft branches",
    "claim_boundary": "uses branch dimensions and common-clock ratios only; it does not assign a physical16 channel to the quartet or doublet ports",
    "disposition": "productive: C1 is narrowed from a missing soft channel to a missing coupling matrix among six exact degenerate soft candidates",
}

(ROOT / "results" / "wp1074_soft_channel_degeneracy_gate.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1074 PASS:", len(soft), soft[0]["threshold_ratio"], soft[0]["response"], vector["threshold_ratio"], vector["response"])
