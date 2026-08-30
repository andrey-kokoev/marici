import json
from collections import deque
from itertools import product
from pathlib import Path


PHASES = tuple(product(range(3), repeat=3))


def twice_phase_energy(q):
    total = 0
    for i in range(3):
        residue = (2 * q[i] - q[(i + 1) % 3] - q[(i + 2) % 3]) % 3
        total += 2 if residue == 0 else -1
    return total


def diagonal(q):
    return q[0], (q[1] + 1) % 3, (q[2] + 2) % 3


def center(q):
    return tuple((value + 1) % 3 for value in q)


def cycle(q):
    return q[2], q[0], q[1]


def cp(q):
    return tuple((-value) % 3 for value in q)


def orbit(seed):
    seen = {seed}
    queue = deque([seed])
    while queue:
        current = queue.popleft()
        for action in (diagonal, center, cycle):
            successor = action(current)
            if successor not in seen:
                seen.add(successor)
                queue.append(successor)
    return frozenset(seen)


energies = {q: twice_phase_energy(q) for q in PHASES}
minimum = min(energies.values())
minima = frozenset(q for q, energy in energies.items() if energy == minimum)
assert minimum == -3
assert len(minima) == 18

remaining = set(minima)
orbits = []
while remaining:
    component = orbit(next(iter(remaining)))
    assert component <= minima
    orbits.append(component)
    remaining -= component

assert sorted(map(len, orbits)) == [9, 9]
first, second = orbits
assert frozenset(cp(q) for q in first) == second
assert frozenset(cp(q) for q in second) == first
assert first.isdisjoint(second)

representative = (1, 0, 0)
representative_orbit = orbit(representative)
assert cp(representative) not in representative_orbit

result = {
    "schema": "marici.nima.delta27-collective-cp-phase-orbits.v1",
    "phase_assignments": len(PHASES),
    "minimum_twice_phase_energy": minimum,
    "minimum_count": len(minima),
    "minimum_orbit_sizes": sorted(map(len, orbits)),
    "bare_cp_exchanges_the_two_orbits": True,
    "representative": representative,
    "cp_conjugate_representative": cp(representative),
    "cp_conjugate_in_same_delta27_orbit": False,
    "generalized_cp_census_completed": False,
    "verdict": "The collective triplet phase term has two disjoint nine-state Delta(27) minimum orbits exchanged by bare CP; full explanatory authority still requires the compatible generalized-CP census and source admission."
}

out = Path(__file__).parents[1] / "results" / "delta27-collective-cp-phase-orbits.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
