import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

q = [Fraction(x,23) for x in (6,8,1,4,2,2)]
u = Fraction(1,6)
matchings = [
    ((0,2),(1,4),(3,5)),
    ((0,2),(1,5),(3,4)),
    ((0,4),(1,2),(3,5)),
    ((0,4),(1,5),(2,3)),
    ((0,5),(1,2),(3,4)),
    ((0,5),(1,4),(2,3)),
]

# The only equal source weights are the two dimension-2 branches, indices 4,5.
equal_pairs = [(i,j) for i in range(6) for j in range(i+1,6) if q[i] == q[j]]
assert equal_pairs == [(4,5)]
swap = [0,1,2,3,5,4]

def normalize(matching):
    return tuple(sorted(tuple(sorted(pair)) for pair in matching))

def act(matching):
    return normalize(tuple((swap[i], swap[j]) for i,j in matching))

normalized = [normalize(m) for m in matchings]
assert len(set(normalized)) == 6
images = [act(m) for m in normalized]
assert set(images) == set(normalized)

# Group the six matchings into twin-swap orbits.
remaining = set(normalized)
orbits = []
while remaining:
    m = remaining.pop()
    image = act(m)
    assert image != m
    assert image in remaining
    remaining.remove(image)
    orbits.append(tuple(sorted((m,image))))

assert len(orbits) == 3
assert all(len(orbit) == 2 for orbit in orbits)
assert sum(len(orbit) for orbit in orbits) == 6

# Equal weights preserve q and the target, but do not prove a physical branch
# exchange representation or production-kernel invariance.
weight_preserving = all(q[i] == q[swap[i]] for i in range(6))
physical_exchange_certificates = 0
kernel_invariance_certificates = 0
assert weight_preserving
assert physical_exchange_certificates == 0
assert kernel_invariance_certificates == 0

result = {
    "schema": "marici.flavor.wp1146.v1",
    "status": "PASS",
    "question": "Does the equal-weight twin swap reduce six matchings to a unique orbit?",
    "dpc": {
        "conjecture": "The equal-weight twin symmetry uniquely reduces the six rank-three matchings.",
        "rivals": [
            "six labeled matchings",
            "three twin-swap orbits",
            "one selected orbit",
            "no algebraic uniqueness"
        ],
        "risky_consequences": [
            "only branches 4 and 5 have equal source weights",
            "the swap preserves q and u",
            "orbits have size two",
            "no fixed matching exists"
        ],
        "falsification_attempt": "The twin swap acts freely and produces exactly three two-element orbits, so it does not select a unique matching.",
        "residual": "A sourced branch-exchange representation or production kernel may reduce the orbits further.",
        "disposition": "reject algebraic uniqueness and classify three twin-swap orbits"
    },
    "equal_weight_pairs_zero_based": [list(pair) for pair in equal_pairs],
    "matching_count": 6,
    "orbit_count": len(orbits),
    "orbit_sizes": [len(orbit) for orbit in orbits],
    "fixed_matchings": 0,
    "weight_preserving": weight_preserving,
    "physical_exchange_certificates": physical_exchange_certificates,
    "kernel_invariance_certificates": kernel_invariance_certificates,
    "classification": "classification gate: equal weights give three orbits, not a selected matching",
    "remaining_gate": "test whether equal-dimension branches carry a sourced physical exchange symmetry",
    "hostile_gate": "do not treat equal dimensions as production-kernel exchange symmetry",
    "claim_boundary": "orbit reduction is algebraic; physical exchange remains open",
    "disposition": "matching-orbit leaf resolved; twin-exchange rival selected",
}

(ROOT / "results" / "wp1146_matching_symmetry_orbits.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1146 PASS:", len(orbits), physical_exchange_certificates)
