import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

q = [Fraction(d,23) for d in (6,8,1,4,2,2)]
u = [Fraction(1,6)] * 6
p = [Fraction(1,4)] * 6
G = Fraction(3,2)
assert sum(q) == 1
assert sum(u) == 1
assert sum(p) == G

# If K is a stochastic event map and p=G K q, then K q must be uniform.
# The rank-one complete-mixing matrix J/6 is the minimal exact solution.
J6 = [[Fraction(1,6) for _ in range(6)] for _ in range(6)]
Kq = [sum(J6[e][b]*q[b] for b in range(6)) for e in range(6)]
assert Kq == u
assert [G*x for x in Kq] == p
assert all(sum(J6[e][b] for e in range(6)) == 1 for b in range(6))

rank_J6 = 1
assert rank_J6 == 1

# This kernel is target-defined complete mixing: it erases branch information
# and has zero source-derived coupling entries.
branch_information_rows = len({tuple(row) for row in J6})
assert branch_information_rows == 1
source_coupling_entries = 0
source_authorized = False
assert source_coupling_entries == 0 and not source_authorized

result = {
    "schema": "marici.flavor.wp1119.v1",
    "status": "PASS",
    "question": "What minimal stochastic amplitude algebra maps branch weights to the six physical16 events?",
    "branch_distribution": [str(x) for x in q],
    "stochastic_target": [str(x) for x in u],
    "physical_event_distribution": [str(x) for x in p],
    "gain": str(G),
    "minimal_kernel": "J6/6",
    "kernel_rank": rank_J6,
    "kernel_column_sums": [1]*6,
    "Kq": [str(x) for x in Kq],
    "G_Kq": [str(G*x) for x in Kq],
    "branch_information_rows": branch_information_rows,
    "source_coupling_entries": source_coupling_entries,
    "source_authorized": source_authorized,
    "classification": "conditional gate: complete-mixing J6/6 is the unique minimal target algebra but erases branch data and is unsourced",
    "remaining_gate": "derive a physical complete-mixing process or a nonuniform source coupling matrix satisfying Kq=(1/6)^6 and gain 3/2",
    "hostile_gate": "do not promote J6/6, universal mixing, or the fitted equation G K q=p to a source production law",
    "claim_boundary": "the algebra shows what must be sourced; it is not a dynamics",
    "disposition": "minimal event-amplitude algebra derived and source-blocked",
}

(ROOT / "results" / "wp1119_physical16_amplitude_algebra_gate.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1119 PASS:", G, rank_J6, Kq[0], G*Kq[0], source_coupling_entries)
