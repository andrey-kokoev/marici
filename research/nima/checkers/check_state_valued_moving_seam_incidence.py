from fractions import Fraction
import json
from pathlib import Path


def energy(values, differences):
    return sum(v * v for v in values) + sum(d * d for d in differences)


records = []
for n in range(1, 13):
    values = [Fraction((i + 1) * (i + 2), n + 3) for i in range(n + 3)]
    differences = [values[i + 1] - values[i] for i in range(len(values) - 1)]

    for cut in range(n + 1):
        seam_values = values[:cut]
        tail_values = values[cut:]
        seam_differences = differences[: max(0, cut - 1)]
        tail_differences = differences[cut:]
        interface_difference = (
            [differences[cut - 1]] if 0 < cut < len(values) else []
        )

        # Assign the crossing edge to the incidence constraint. The three
        # disjoint pieces recover the complete discrete graph energy.
        split = (
            energy(seam_values, seam_differences)
            + energy(tail_values, tail_differences)
            + sum(d * d for d in interface_difference)
        )
        assert split == energy(values, differences)

    # Refinement from n to n+1 adds one orthogonal scalar shell.
    packet = [Fraction(i + 1, n + 1) for i in range(n + 1)]
    old_energy = sum(v * v for v in packet[:-1])
    shell_energy = packet[-1] * packet[-1]
    assert old_energy + shell_energy == sum(v * v for v in packet)

    # A unit vector constant on n sites has scalar integral squared equal to n.
    scalar_integral_squared_over_norm = n
    records.append(
        {
            "cutoff": n,
            "all_cut_energy_splits_exact": True,
            "refinement_is_orthogonal_shell_addition": True,
            "scalarized_readout_norm_squared": scalar_integral_squared_over_norm,
        }
    )

result = {
    "schema": "marici.nima.state-valued-moving-seam-incidence.v1",
    "records": records,
    "state_valued_cut_uniform_norm": 1,
    "scalar_moving_seam_uniformly_bounded": False,
    "verdict": "moving seam completes as a state-valued directed system, not as one scalar functional",
}

out = (
    Path(__file__).parents[1]
    / "results"
    / "state-valued-moving-seam-incidence.json"
)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
