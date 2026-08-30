from cmath import sinh
from math import pi


def candidate(x: float) -> float:
    z = complex(x, 3 * pi / 2)
    r2 = 2 * sinh(z)
    r3 = 2 * z / (z * z - 0.25)
    return -(r2 * r3.conjugate()).real


for x in (0.05, 0.1, 0.2, 0.4):
    assert candidate(x) < 0

print("hostile_height=3pi_over_2")
print("naive_Hermitian_pairing=indefinite")
print("missing_data=source_Green_transport")

