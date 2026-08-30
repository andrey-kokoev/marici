from fractions import Fraction


def shift(label: Fraction, prime: int) -> Fraction:
    return label * prime


def reflect(label: Fraction) -> Fraction:
    return 1 / label


seed = (Fraction(1), Fraction(2))
leakage_columns = [
    shift(label, 2) if shift(label, 2) not in seed else None for label in seed
]

assert leakage_columns == [None, Fraction(4)]
assert [[0, 0], [0, 1]] == [[0, 0], [0, int(leakage_columns[1] == 4)]]

square_23 = shift(shift(Fraction(1), 2), 3)
square_32 = shift(shift(Fraction(1), 3), 2)
assert square_23 == square_32 == 6

# Six is required as a labelled path state but is not a prime power.
assert all(6 != p**k for p in (2, 3, 5) for k in range(1, 6))

orbit = {shift(Fraction(1), 2**k) for k in range(8)}
reflected_orbit = orbit | {reflect(label) for label in orbit}
assert len(orbit) == 8
assert len(reflected_orbit) == 15

print(
    {
        "status": "passed",
        "seed": ["1", "2"],
        "leakage_gram": [[0, 0], [0, 1]],
        "mixed_square_path_state": "6",
        "finite_orbit_sizes": {"forward_8": 8, "with_reflection": 15},
        "outcome": "forced_infinite_closure",
    }
)
