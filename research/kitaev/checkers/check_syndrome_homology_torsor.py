import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp


modulus = 2
B1 = sp.Matrix([[1, 0, 0, 0]])
B2 = sp.Matrix([[0], [1], [0], [0]])
assert B1 * B2 == sp.zeros(1, 1)


def mat_vec_mod(matrix, vector):
    return tuple(int(value) % modulus for value in matrix * sp.Matrix(vector))


chains = list(itertools.product(range(modulus), repeat=4))
fiber = [chain for chain in chains if mat_vec_mod(B1, chain) == (1,)]
assert len(fiber) == 8

repair = (0, 1, 0, 0)


def add_mod(left, right):
    return tuple((a + b) % modulus for a, b in zip(left, right))


orbits = []
unseen = set(fiber)
while unseen:
    representative = min(unseen)
    orbit = {representative, add_mod(representative, repair)}
    orbits.append(sorted(orbit))
    unseen -= orbit

assert len(orbits) == 4
logical_labels = sorted({(orbit[0][2], orbit[0][3]) for orbit in orbits})
assert logical_labels == [(0, 0), (0, 1), (1, 0), (1, 1)]

D0 = (1, 0, 0, 0)
D1 = (1, 0, 1, 0)
assert mat_vec_mod(B1, D0) == mat_vec_mod(B1, D1) == (1,)
decoder_difference = add_mod(D0, D1)
assert decoder_difference == (0, 0, 1, 0)
assert decoder_difference not in {(0, 0, 0, 0), repair}

payload = {
    "status": "pass",
    "theorem": "a_syndrome_fiber_is_a_homology_torsor_not_a_decoder",
    "coefficient": "F2",
    "syndrome": [1],
    "chain_solution_count": len(fiber),
    "local_repair_orbit_size": 2,
    "logical_class_count": len(orbits),
    "logical_labels": [list(label) for label in logical_labels],
    "decoder_values": [list(D0), list(D1)],
    "decoder_difference": list(decoder_difference),
    "decoder_difference_logically_nontrivial": True,
    "logical_probes_select_decoder": False,
    "physical_decoder_constructed": False,
}
canonical = json.dumps(payload, indent=2, sort_keys=True) + "\n"
payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()

output = Path(__file__).parents[1] / "results" / "syndrome-homology-torsor.json"
output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(payload, sort_keys=True))
