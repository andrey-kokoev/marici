import json
from fractions import Fraction
from pathlib import Path


def h(s):
    return 1 + Fraction(256, 3) * s * (s - 1) * (s - Fraction(1, 2)) ** 2


def h_prime(s):
    # Exact derivative of 1 + (256/3) s(s-1)(s-1/2)^2.
    return Fraction(256, 3) * (
        (2 * s - 1) * (s - Fraction(1, 2)) ** 2
        + 2 * s * (s - 1) * (s - Fraction(1, 2))
    )


checkpoints = [Fraction(0), Fraction(1, 2), Fraction(1)]
inserted_zeros = [Fraction(1, 4), Fraction(3, 4)]
derivative_samples = [Fraction(0), Fraction(1, 4), Fraction(1, 3), Fraction(3, 4), Fraction(1)]

assert all(h(s) == 1 for s in checkpoints)
assert all(h(s) == 0 for s in inserted_zeros)
assert all(h(1 - s) == h(s) for s in derivative_samples)
assert any(h_prime(s) != 0 for s in derivative_samples)
assert all(h_prime(s) != 0 for s in inserted_zeros)

# For the trivial connection d, sigma=1 is horizontal and h*sigma is not.
source_residuals = [h_prime(s) for s in derivative_samples]

# Naturality hostile. F_0=1 forces A=0, while F_1=exp(s) requires A=1.
atom_zero_required_connection = Fraction(0)
atom_one_required_connection = Fraction(1)
assert atom_zero_required_connection != atom_one_required_connection

result = {
    "source_connection": "d",
    "source_section": "1",
    "source_section_horizontal": True,
    "hostile_multiplier": "1+(256/3)s(s-1)(s-1/2)^2",
    "hostile_preserves_checkpoints": True,
    "hostile_inserted_zeros": [str(s) for s in inserted_zeros],
    "hostile_horizontality_residual_samples": [str(value) for value in source_residuals],
    "hostile_horizontal_for_source_connection": False,
    "manufactured_connection": "d-dlog(h)",
    "manufactured_connection_regular_at_inserted_zeros": False,
    "scalar_connection_naturality_hostile": {
        "atom_at_zero_section": "1",
        "required_connection": str(atom_zero_required_connection),
        "atom_at_one_section": "exp(s)",
        "required_connection_for_atom_at_one": str(atom_one_required_connection),
        "one_connection_horizontalizes_both": False,
    },
    "verdict": "regular source horizontality rejects the central multiplier",
}

output = Path(__file__).parents[1] / "results" / "rh-source-horizontal-line.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))
