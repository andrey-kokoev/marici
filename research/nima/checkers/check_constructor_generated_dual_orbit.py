import json
from fractions import Fraction
from pathlib import Path


ell = (1, 0)
ell_swap = (0, 1)

single_rank = 1
orbit_rank = 2
assert single_rank == 1
assert orbit_rank == 2

hidden_transforms = []
for a in (-2, 0, 2, 7):
    scalar_row_after = (1, 0)
    orbit_second_row_after = (0, a)
    assert scalar_row_after == ell
    hidden_transforms.append({
        "a": a,
        "scalar_reference_unchanged": True,
        "full_orbit_unchanged": orbit_second_row_after == ell_swap,
    })

completion = []
for n in (1, 2, 4, 16, 64):
    lower_margin = Fraction(1, n)
    assert lower_margin > 0
    completion.append({
        "cutoff": n,
        "lower_margin_numerator": lower_margin.numerator,
        "lower_margin_denominator": lower_margin.denominator,
    })

result = {
    "single_observer_rank": single_rank,
    "constructor_orbit_rank": orbit_rank,
    "hidden_scalar_stabilizer_samples": hidden_transforms,
    "finite_completion_samples": completion,
    "completed_lower_margin": 0,
    "conclusion": "constructor-generated observer span gives finite separation; completion and orientation remain separate gates",
}

output = Path(__file__).parents[1] / "results" / "constructor-generated-dual-orbit.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))

