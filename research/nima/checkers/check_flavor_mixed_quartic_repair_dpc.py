import json
from collections import deque
from pathlib import Path


POINTS = tuple((a, b) for a in range(8) for b in range(8))
INDEX = {point: i for i, point in enumerate(POINTS)}


def permutation(action):
    return tuple(INDEX[action(point)] for point in POINTS)


R = permutation(lambda x: ((x[0] + 2) % 8, (x[1] + 2) % 8))
C = permutation(lambda x: ((-x[0]) % 8, (-x[1]) % 8))
T = permutation(lambda x: ((x[1] + 1) % 8, (x[0] - 1) % 8))
IDENTITY = tuple(range(len(POINTS)))
VACUA = tuple((a, b) for a in range(0, 8, 2) for b in range(1, 8, 2))


def generated_group(extra):
    generators = ((R, 0), (C, 1), (T, 0), (extra, 0))
    group = {(IDENTITY, 0)}
    queue = deque([(IDENTITY, 0)])
    while queue:
        current, parity = queue.popleft()
        for generator, generator_parity in generators:
            product = tuple(generator[current[i]] for i in range(len(POINTS)))
            key = product, parity ^ generator_parity
            if key not in group:
                group.add(key)
                queue.append(key)
    return group


candidates = []
for p in range(0, 8, 2):
    for q in range(0, 8, 2):
        # Even p,q preserve Re(z_i^4). The mixed monomial acquires phase
        # exp(i*pi*(p+q)/2), so p+q=2 mod 4 makes its real part odd.
        if (p + q) % 4 != 2:
            continue
        U = permutation(lambda x, p=p, q=q: ((x[0] + p) % 8, (x[1] + q) % 8))
        group = generated_group(U)
        cp_odd = tuple(perm for perm, parity in group if parity == 1)
        counts = tuple(sum(perm[INDEX[vacuum]] == INDEX[vacuum] for perm in cp_odd)
                       for vacuum in VACUA)
        assert len(group) == 64
        assert min(counts) == max(counts) == 2
        candidates.append({
            "rephasing_units_pi_over_4": [p, q],
            "preserves_individual_anisotropies": True,
            "forbids_mixed_quartic": True,
            "generated_group_order": len(group),
            "cp_stabilizers_per_selected_vacuum": 2,
            "passes_dpc": False,
        })

assert len(candidates) == 8
assert not any(candidate["passes_dpc"] for candidate in candidates)

result = {
    "schema": "marici.nima.flavor-mixed-quartic-repair-dpc.v1",
    "dpc": {
        "preserve_opposite_d4_anisotropy": True,
        "forbid_Re_z1_squared_z2_squared": True,
        "zero_generalized_cp_stabilizers_on_every_selected_vacuum": True,
        "renormalizable_source_action": True,
    },
    "candidate_class": "diagonal Z8 rephasings preserving both individual quartic anisotropies",
    "candidate_count": len(candidates),
    "passing_candidate_count": 0,
    "candidates": candidates,
    "verdict": "Every minimal relative-rephasing repair forbids the mixed quartic but restores generalized CP; the DPC has no solution in this candidate class."
}

out = Path(__file__).parents[1] / "results" / "flavor-mixed-quartic-repair-dpc.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
