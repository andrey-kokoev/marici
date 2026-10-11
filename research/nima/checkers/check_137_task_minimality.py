"""Task-based necessity test for the existing 121+16 comparison interface.

Task A: recover ALL scalar first-order slot responses at the all-unit
factorized-leg baseline. Task B: recover independently variable slot records.
These are different admitted domains. Neither is a physical charge model.
All certificates are exact integer coefficient identities; no measured alpha.
"""
from collections import deque
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json


checks = []


def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)


def slot(n, i, j):
    # d(x_i*y_j) = dx_i + dy_j at x=y=1.
    return tuple(int(k == i or k == n + j) for k in range(2*n))


def plus(a, b):
    return tuple(x+y for x, y in zip(a, b))


def minus(a, b):
    return tuple(x-y for x, y in zip(a, b))


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def recover(n, observed):
    """Construct all responses from observed slots by alternating potentials.

Vertex 0 is a declared computational gauge; changing it does not change
any reconstructed edge response. The selected measurement frame is explicit.
"""
    adjacent = [[] for _ in range(2*n)]
    for i, j in observed:
        adjacent[i].append((n+j, slot(n, i, j)))
        adjacent[n+j].append((i, slot(n, i, j)))
    potentials = {0: (0,) * (2*n)}
    queue = deque([0])
    while queue:
        a = queue.popleft()
        for b, response in adjacent[a]:
            if b not in potentials:
                potentials[b] = minus(response, potentials[a])
                queue.append(b)
    if len(potentials) != 2*n:
        return None
    reconstructed = {(i, j): plus(potentials[i], potentials[n+j])
                     for i, j in product(range(n), repeat=2)}
    assert all(response == slot(n, i, j) for (i, j), response in reconstructed.items())
    return reconstructed


def invisible_perturbation(n, observed):
    """Disconnected observed graph yields an unobserved nonzero response."""
    adjacent = [[] for _ in range(2*n)]
    for i, j in observed:
        adjacent[i].append(n+j)
        adjacent[n+j].append(i)
    reached, queue = {0}, deque([0])
    while queue:
        a = queue.popleft()
        for b in adjacent[a]:
            if b not in reached:
                reached.add(b)
                queue.append(b)
    assert len(reached) < 2*n
    perturbation = tuple((1 if v < n else -1) if v in reached else 0
                         for v in range(2*n))
    assert all(dot(slot(n, i, j), perturbation) == 0 for i, j in observed)
    separating = next((i, j) for i, j in product(range(n), repeat=2)
                      if dot(slot(n, i, j), perturbation) != 0)
    return perturbation, separating


def analyze(n, label):
    full = tuple(product(range(n), repeat=2))
    tree = tuple((i, 0) for i in range(n)) + tuple((0, j) for j in range(1, n))
    check(label + "/full-recovery", recover(n, full) is not None)
    check(label + "/tree-recovery", recover(n, tree) is not None)
    check(label + "/tree-size", len(tree) == 2*n-1)
    for dropped in full:
        check(label + f"/full-minus-{dropped}-still-recovers",
              recover(n, tuple(e for e in full if e != dropped)) is not None)
    lower_witnesses = []
    for dropped in tree:
        reduced = tuple(e for e in tree if e != dropped)
        check(label + f"/tree-minus-{dropped}-fails", recover(n, reduced) is None)
        perturbation, separating = invisible_perturbation(n, reduced)
        lower_witnesses.append({"removed": dropped, "invisible_primitive_perturbation": perturbation,
                                "unrecovered_slot": separating})
    # A connected graph on 2n vertices needs at least 2n-1 edges.
    # The observation matrix has that rank: its kernel consists of the
    # single gauge dx_i=c, dy_j=-c. Blocks have independent gauges.
    gauge = (1,) * n + (-1,) * n
    check(label + "/one-gauge-annihilates-all", all(dot(slot(n, *e), gauge) == 0 for e in full))
    return {"slots": len(full), "minimum_response_measurements": len(tree),
            "constructive_measurement_frame": tree, "tree_deletion_witnesses": lower_witnesses}


arrow = analyze(11, "arrow")
state = analyze(4, "state")
check("137-slot-domain", arrow["slots"] + state["slots"] == 137)
check("28-response-measurements-suffice", arrow["minimum_response_measurements"] + state["minimum_response_measurements"] == 28)

# The smaller frame need not break the EXISTING marked-reference symmetry.
# Use the fixed reverse-reference arrow (1,0) as arrow pivot, and the fixed
# reference-source state 0 as state pivot. Both survive independent swaps
# of the two unmarked vertices 2,3 on each carrier.
arrows = ((1, 0),) + tuple(e for e in product(range(4), repeat=2)
                           if e[0] != e[1] and e not in ((0, 1), (1, 0)))
permutations = ((0, 1, 2, 3), (0, 1, 3, 2))
for p, q in product(permutations, repeat=2):
    arrow_frame = {(arrows[i], arrows[j]) for i, j in arrow["constructive_measurement_frame"]}
    moved_arrows = {((p[a], p[b]), (q[c], q[d])) for (a, b), (c, d) in arrow_frame}
    check(f"marked-symmetry/arrow-frame/{p}/{q}", moved_arrows == arrow_frame)
    state_frame = set(state["constructive_measurement_frame"])
    check(f"marked-symmetry/state-frame/{p}/{q}",
          {(p[a], q[b]) for a, b in state_frame} == state_frame)

# A redundant 138th sensor cannot alter recoverability of these 137 outputs.
full_arrow = tuple(product(range(11), repeat=2))
check("duplicate-138th-channel-does-not-change-task", recover(11, full_arrow + ((0, 0),)) == recover(11, full_arrow))

# Restoring the excluded reference legs CHANGES the domain to 144+16.
full_reference_tree = tuple((i, 0) for i in range(12)) + tuple((0, j) for j in range(1, 12))
check("160-domain-recovers-from-30", recover(12, full_reference_tree) is not None and len(full_reference_tree) + 7 == 30)

# Task B: arbitrary independently stored residuals. Omit record k and the
# all-zero state is indistinguishable from the unit residual at k.
for omitted in range(137):
    hostile = tuple(int(j == omitted) for j in range(137))
    check(f"independent-records/omit-{omitted}-loses-information",
          all(hostile[j] == 0 for j in range(137) if j != omitted) and hostile[omitted] == 1)

# The remaining slots have a distinct auditing role: 28 anchored responses
# plus 109 rooted mixed differences form an invertible coordinate change
# on an arbitrary 137-slot table. This does not make those defects independent
# when the table is constrained to arise from shared primitive legs.
def rectangles(n, values):
    return {(i, j): values[i, j] - values[i, 0] - values[0, j] + values[0, 0]
            for i in range(1, n) for j in range(1, n)}

for n in (11, 4):
    values = {(i, j): 17*i + 31*j + 7*i*j for i, j in product(range(n), repeat=2)}
    mixed = rectangles(n, values)
    rebuilt = {(i, j): values[i, 0] + values[0, j] - values[0, 0] + mixed.get((i, j), 0)
               for i, j in product(range(n), repeat=2)}
    check(f"{n}/frame-plus-rectangles-reconstructs", rebuilt == values)
    for location in mixed:
        hostile = dict(values)
        hostile[location] += 1
        changed = rectangles(n, hostile)
        check(f"{n}/independent-interior-test/{location}",
              all(hostile[i, 0] == values[i, 0] for i in range(n)) and
              all(hostile[0, j] == values[0, j] for j in range(n)) and
              {k for k in mixed if mixed[k] != changed[k]} == {location})
check("109-rooted-rectangle-coordinates", (11-1)**2 + (4-1)**2 == 109)
x0, y0, x1, y1 = F(1), F(1), F(5, 3), F(8, 5)
check("finite-mixed-response-is-not-zero", y1*x1-y0*x1-y1*x0+y0*x0 == F(2, 5))
check("finite-product-recovery-when-pivot-nonzero", (y0*x1)*(y1*x0)/(y0*x0) == y1*x1)

result = {
    "schema": "marici.nima.137-task-minimality.v1",
    "status": "pass",
    "checks": checks,
    "task_A": {
        "name": "recover all first-order scalar factorized comparison responses at unit baseline",
        "arrow": arrow, "state": state,
        "full_slot_count": 137, "minimum_linear_scalar_measurements": 28,
        "any_single_slot_deletion_preserves_recoverability": True,
        "lower_bound": "two independent complete-bipartite blocks have ranks 21 and 7; connected measurement graphs need 21+7 edges",
        "scope": "linear scalar measurement task on tangent responses; not nonlinear global reconstruction or native history discrimination",
        "symmetry_boundary": "28-slot frame is invariant under the existing independent marked-reference S2 x S2 relabellings; no unmarked S4-invariant choice is claimed", 
    },
    "task_B": {
        "name": "recover arbitrary independent values of all 137 retained records",
        "minimum_linear_scalar_measurements": 137,
        "reason": "137 independent record coordinates were admitted; this is a storage-domain assumption, not a derivation of 137 from primitive legs",
    },
    "controls": {"136_channels": "same Task A after any one deletion",
                 "138_channels": "same Task A with one explicitly duplicate sensor",
                 "160_channels": "different reference-inclusive domain; rank 30 rather than 28"},
    "compatibility_audit": {
        "frame_coordinates": 28, "rooted_rectangle_coordinates": 109,
        "identity": "response_ij = response_i0 + response_0j - response_00 + mixed_ij",
        "meaning": "28 frame responses plus 109 mixed checks reconstruct any table; shared-leg provenance constrains the checks",
        "finite_mixed_example": "2/5, from simultaneous primitive perturbations 2/3 and 3/5",
        "boundary": "nonzero mixed response is not automatically a coherence violation; it can be the expected bilinear term",
    },
    "physical_conclusion": "none: neither task identifies electrons, charge, graph depth, or electromagnetic coupling",
}
path = Path(__file__).resolve().parents[1] / "results" / "137-task-minimality.json"
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(f"PASS: {len(checks)} exact task checks")
print("Task A: 28 measurements recover all 137 responses; deleting any one of 137 slots still permits recovery.")
print("Task B: 137 independent records require 137 linear scalar measurements, by the admitted storage domain.")
print("The 28-slot frame preserves the existing marked-reference S2 x S2 symmetry.")
print("137 = 28 anchored response coordinates + 109 rooted mixed-response checks.")
print("No physical interpretation or unmarked reference-free frame selection is established.")
