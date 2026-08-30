import json
import math
from fractions import Fraction
from pathlib import Path


def record(s):
    n = 4 * s - 1
    conjugated_reflection = (
        (Fraction(-1), Fraction(0)),
        (Fraction(5, n), Fraction(1)),
    )
    reflection_descends = all(value.denominator == 1
                              for row in conjugated_reflection for value in row)

    # Joint chart map has Smith form diag(1,5).  Modulo n its image has size
    # n * n/gcd(n,5), which is the index of the common kernel in Z^2.
    gcd_five = math.gcd(n, 5)
    joint_packet_size = n * (n // gcd_five)
    return {
        "s": s,
        "n": n,
        "F_inverse_X_F": [
            [[value.numerator, value.denominator] for value in row]
            for row in conjugated_reflection
        ],
        "reflection_descends_to_cokernel": reflection_descends,
        "gcd_n_5": gcd_five,
        "joint_reflected_packet_size": joint_packet_size,
        "naive_square_size": n * n,
        "five_primary_overlap": gcd_five == 5,
    }


records = [record(s) for s in range(1, 51)]
exceptional_spins = [item["s"] for item in records if item["five_primary_overlap"]]
spin_two = record(2)
spin_four = record(4)

# Explicit failure of ell(Xv)=-ell(v), using v=(1,0).
def reflection_inversion_witness(s):
    n = 4 * s - 1
    ell_v = 3 % n
    ell_xv = (-2) % n
    inverse = (-ell_v) % n
    return ell_v, ell_xv, inverse, ell_xv == inverse


gates = [
    all(not item["reflection_descends_to_cokernel"] for item in records),
    all(not reflection_inversion_witness(s)[3] for s in range(1, 51)),
    spin_two["joint_reflected_packet_size"] == 49,
    spin_four["n"] == 15,
    spin_four["joint_reflected_packet_size"] == 45,
    exceptional_spins == list(range(4, 51, 5)),
]

result = {
    "schema": "marici.strominger.reflection_falsifier_general_spin_cyclic_resolution.v1",
    "original_global_reflection_conjecture": "falsified",
    "surviving_scope": "oriented_axis_SO2_to_C_(4s-1)_restriction",
    "reflection_obstruction": "F_s^-1 X F_s has entry 5/(4s-1)",
    "joint_chart_matrix": [[3, -2], [-2, 3]],
    "joint_chart_determinant": 5,
    "joint_packet_size_law": "(4s-1)^2/gcd(4s-1,5)",
    "exceptional_spin_law": "s=4 mod 5",
    "exceptional_spins_bounded": exceptional_spins,
    "spin_two": spin_two,
    "spin_four": spin_four,
    "smallest_next_falsifier": "derive spin-four reflected boundary operator and test the predicted fivefold overlap",
    "gates_passed": sum(gates),
    "gates_total": len(gates),
    "all_passed": all(gates),
}

output = (
    Path(__file__).parents[1]
    / "results"
    / "reflection_falsifier_general_spin_cyclic_resolution.json"
)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
print(json.dumps(result, indent=2))
raise SystemExit(0 if all(gates) else 1)
