import json
from pathlib import Path

source = json.loads(
    Path("research/benincasa/results/five-site-compatible-landau-subsets.json").read_text()
)
two = next(row for row in source["census"] if row["active_wall_count"] == 2)
records = [
    row
    for row in two["representative_records"]
    if all(label.startswith("g_") for label in row["representative"])
]

same = []
shared_one = []
disjoint = []
for row in records:
    left, right = map(set, row["cut_supports"])
    overlap = len(left & right)
    if overlap == 2:
        same.append(row)
    elif overlap == 1:
        shared_one.append(row)
    elif overlap == 0:
        disjoint.append(row)
    else:
        raise AssertionError(overlap)

assert len(records) == 30
assert (len(same), len(shared_one), len(disjoint)) == (2, 21, 7)
assert all(row["forces_t_zero"] for row in same)
assert all(not row["forces_t_zero"] for row in shared_one + disjoint)

packet = {
    "schema": "marici.five_site_region_pair_physical_gradient_reduction.v1",
    "region_pair_orbit_count": 30,
    "same_cut_orbit_count": 2,
    "same_cut_representatives": [row["representative"] for row in same],
    "same_cut_status": "t=0 and soft support; identical gradients cannot cancel with positive multipliers unless stationary",
    "one_shared_cut_orbit_count": 21,
    "one_shared_cut_representatives": [row["representative"] for row in shared_one],
    "one_shared_cut_identity": "u_a+(1+lambda)u_b+lambda*u_c=0, lambda>0",
    "triangle_equality_consequence": "u_a=u_c=-u_b, hence both region gradients vanish",
    "genuinely_coupled_survivors_with_overlapping_cuts": 0,
    "simultaneous_stationary_loci_retained": True,
    "disjoint_cut_candidate_count": 7,
    "disjoint_cut_candidates": [row["representative"] for row in disjoint],
    "next_gate": "solve seven disjoint-cut wall equations together with antiparallel nonzero physical gradients",
}

Path("research/benincasa/results/five-site-region-pair-physical-gradient-reduction.json").write_text(
    json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps({key: packet[key] for key in (
    "region_pair_orbit_count",
    "same_cut_orbit_count",
    "one_shared_cut_orbit_count",
    "genuinely_coupled_survivors_with_overlapping_cuts",
    "disjoint_cut_candidate_count",
)}, sort_keys=True))
