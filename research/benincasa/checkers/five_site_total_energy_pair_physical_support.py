import json
from pathlib import Path

source = json.loads(
    Path("research/benincasa/results/five-site-compatible-landau-subsets.json").read_text()
)
two = next(row for row in source["census"] if row["active_wall_count"] == 2)
records = [row for row in two["representative_records"] if "G" in row["representative"]]

assert len(records) == 5
assert all(row["forces_t_zero"] for row in records)
assert all(row["t_zero_reason"] == "contains total-energy wall G=5t" for row in records)
assert sorted(len(next(s for s in row["cut_supports"] if s)) for row in records) == [1, 2, 2, 2, 2]

packet = {
    "schema": "marici.five_site_total_energy_pair_physical_support.v1",
    "pair_orbit_count": 5,
    "representatives": [row["representative"] for row in records],
    "total_energy_equation": "G=5t=0",
    "edge_pair_restriction": "G_minus_e|t=0=2*y_e",
    "region_pair_restriction": "g_A|t=0=y_i+y_j",
    "open_positive_internal_energy_survivor_count": 0,
    "remaining_support": "existing total-energy/soft intersection",
    "classification": "nearby-cycle boundary support, not a generic two-gradient loop pinch",
}

Path("research/benincasa/results/five-site-total-energy-pair-physical-support.json").write_text(
    json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps(packet, sort_keys=True))
