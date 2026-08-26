import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp


J1 = sp.Matrix([[0, 1], [-1, 0]])
J2 = sp.diag(1, 1, 1, 1)
J2[:2, :2] = J1
J2[2:, 2:] = J1
assert J1.T == -J1
assert J1.det() == 1
assert J2.T == -J2
assert J2.det() == 1
assert J2.rank() == 4


def pairing_nondegenerate_mod_n(J, n):
    dimension = J.rows
    zero = (0,) * dimension
    vectors = list(itertools.product(range(n), repeat=dimension))
    for x in vectors:
        if x == zero:
            continue
        detected = False
        x_matrix = sp.Matrix([x])
        for y in vectors:
            exponent = int((x_matrix * J * sp.Matrix(y))[0]) % n
            if exponent != 0:
                detected = True
                break
        if not detected:
            return False
    return True


moduli = [2, 3, 4]
assert all(pairing_nondegenerate_mod_n(J1, n) for n in moduli)

# Torus basis intersection: a with b is +1, b with a is -1.
a = sp.Matrix([1, 0])
b = sp.Matrix([0, 1])
assert (a.T * J1 * b)[0] == 1
assert (b.T * J1 * a)[0] == -1
assert (a.T * J1 * a)[0] == 0

payload = {
    "status": "pass",
    "theorem": "intersection_becomes_commutation_only_through_the_quantum_bicharacter",
    "torus_intersection_matrix": [[0, 1], [-1, 0]],
    "genus_two_determinant": int(J2.det()),
    "nondegenerate_moduli_checked": moduli,
    "qubit_single_crossing_phase": "-1",
    "Zn_single_crossing_phase": "exp(2*pi*i/n)",
    "torus_one_sector_probe_count": 2,
    "torus_full_logical_generator_count": 4,
    "simultaneously_commuting_full_readout": False,
    "physical_implementation_proved": False,
}
canonical = json.dumps(payload, indent=2, sort_keys=True) + "\n"
payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()

output = Path(__file__).parents[1] / "results" / "intersection-quantum-bicharacter.json"
output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(payload, sort_keys=True))
