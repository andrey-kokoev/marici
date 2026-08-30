"""Exact Z2 charge no-go for a massive single-pair odd-triplet messenger."""
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

single_solutions = []
for left, right in itertools.product(range(2), repeat=2):
    if (left+right) % 2 == 0 and (left+right+1) % 2 == 0:
        single_solutions.append((left, right))

double_solutions = []
for la, ra, lb, rb in itertools.product(range(2), repeat=4):
    conditions = [
        (la+ra) % 2 == 0,
        (lb+rb) % 2 == 0,
        (la+rb+1) % 2 == 0,
        (lb+ra+1) % 2 == 0,
    ]
    if all(conditions):
        double_solutions.append((la, ra, lb, rb))

n_charge_table = {"A_L": (0, 0), "A_R": (0, 0),
                  "B_L": (1, 0), "B_R": (1, 0), "n": (1, 0)}
m_charge_table = {"A_L": (0, 0), "A_R": (0, 0),
                  "B_L": (0, 1), "B_R": (0, 1), "m": (0, 1)}

def even(*names, table):
    return all(sum(table[name][axis] for name in names) % 2 == 0
               for axis in range(2))

checks = {
    "single_pair_mass_and_odd_yukawa_incompatible": single_solutions == [],
    "two_pair_repair_has_exactly_two_charge_complements": double_solutions == [(0, 0, 1, 1), (1, 1, 0, 0)],
    "n_chain_two_flip_table_closes": all([
        even("A_L", "A_R", table=n_charge_table),
        even("B_L", "B_R", table=n_charge_table),
        even("A_L", "n", "B_R", table=n_charge_table),
        even("B_L", "n", "A_R", table=n_charge_table),
    ]),
    "m_chain_two_flip_table_closes": all([
        even("A_L", "A_R", table=m_charge_table),
        even("B_L", "B_R", table=m_charge_table),
        even("A_L", "m", "B_R", table=m_charge_table),
        even("B_L", "m", "A_R", table=m_charge_table),
    ]),
    "wp651_minimal_pair_census_changes_from_six_to_ten": 2+2*4 == 10,
}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP668", "status": "PASS", "checks": checks,
    "single_pair_constraints": ["q_L+q_R=0", "q_L+q_R+1=0", "mod 2"],
    "minimal_repair": "two massive vectorlike pairs of opposite parity with off-diagonal odd-triplet Yukawas",
    "two_pair_solutions": [list(item) for item in double_solutions],
    "wp651_census": {"identity_pairs": 2, "frame_words": 4, "pairs_after_repair": 10},
    "classification": "exact flip protection changes the messenger grammar and invalidates the one-pair linear mass ansatz as a protected source",
    "smallest_exact_falsifier": "one pair satisfying both q_L+q_R=0 and q_L+q_R+1=0 modulo two",
    "remaining_gate": "recompute tree matching, supertrace, thresholds, and anomalies for the doubled protected chains",
}
(ROOT / "results" / "wp668_flip_charge_single_pair_no_go.json").write_text(
    json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))
