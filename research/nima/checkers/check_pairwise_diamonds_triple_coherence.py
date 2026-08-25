"""Finite GF(2) witness: pairwise cells present, triple coherence missing."""

pairwise = {
    "pq": 1,
    "qr": 0,
    "pr": 0,
}

# Minus equals plus over GF(2).
delta_h = pairwise["qr"] ^ pairwise["pr"] ^ pairwise["pq"]
assert delta_h == 1

without_k = delta_h
k = 1
with_k = delta_h ^ k
assert without_k == 1
assert with_k == 0

failure = {
    "code": "triple_coherence_cell_missing",
    "charts": ["p", "q", "r"],
    "pairwise_cells_present": sorted(pairwise),
    "triple_defect": delta_h,
    "required_k": k,
}

print("pairwise cells:", pairwise)
print("triple defect without K:", without_k)
print("total defect with K:", with_k)
print("rejection witness:", failure)
print("PASS: pairwise diamond fillings require an independent triple coherence gate")
