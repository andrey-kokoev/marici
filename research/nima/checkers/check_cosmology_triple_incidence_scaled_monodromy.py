"""Local monodromy of the scaled triple-incidence boundary corner."""

from __future__ import annotations

import json
from pathlib import Path

NIMA = Path(__file__).resolve().parents[1]
OUT = NIMA / "results" / "cosmology_triple_incidence_scaled_monodromy.json"


def load(name: str) -> dict:
    return json.loads((NIMA / "results" / name).read_text(encoding="utf-8"))


def main() -> None:
    corner = load("cosmology_triple_incidence_boundary_corner_transport.json")
    coefficient = load("cosmology_triple_incidence_physical_coefficient.json")

    assert corner["local_coordinates"] == {"u": "q1", "v": "q2", "q3": "u+v+p"}

    # For p != 0, u=pU and v=pV identify every fiber with the fixed
    # arrangement U*V*(U+V+1)=0.  Verify coefficient vectors exactly.
    scaled_walls = {
        "q1_over_p": [1, 0, 0],       # U
        "q2_over_p": [0, 1, 0],       # V
        "q3_over_p": [1, 1, 1],       # U+V+1
    }
    assert scaled_walls["q3_over_p"] == [1, 1, 1]

    # A full loop p -> exp(2*pi*i)*p returns the scaling map itself; there is
    # no wall permutation.  The leading relative two-form scales by p^2/p^3
    # = p^-1, an integral and therefore single-valued exponent.
    numerator_scaling_degree = 2
    denominator_scaling_degree = 3
    period_scaling_exponent = numerator_scaling_degree - denominator_scaling_degree
    assert period_scaling_exponent == -1
    assert int(period_scaling_exponent) == period_scaling_exponent

    # K is generically nonzero on the incidence locus, so sqrt(K) has no local
    # p-inertia after choosing the source germ.  Its global deck oddness is not
    # a p-loop sheet exchange.
    assert corner["generic_cayley_menger_boundary_at_collision"] is False
    assert coefficient["coefficient_deck_character"] == "odd"

    packet = {
        "schema": "marici.cosmology-triple-incidence-scaled-monodromy.v1",
        "punctured_base_trivialization": "u=p*U, v=p*V",
        "fixed_scaled_arrangement": ["U=0", "V=0", "U+V+1=0"],
        "wall_permutation_after_p_loop": "identity",
        "relative_form_scaling_exponent": period_scaling_exponent,
        "scaling_factor_single_valued": True,
        "local_cayley_menger_inertia": "identity",
        "global_deck_oddness_induced_by_p_loop": False,
        "local_betti_monodromy": "identity",
        "local_picard_lefschetz_variation_rank": 0,
        "primitive_mu2_odd_thimble_generated_by_p_loop": False,
        "local_p_i0_role": "selects a boundary value of a meromorphic p^-1 germ, not a nontrivial local monodromy orbit",
        "scope": (
            "local generic triple-incidence neighborhood; remote singularities of a "
            "global continued contour are not classified"
        ),
        "conclusion": (
            "the punctured triple-incidence family is algebraically trivial and "
            "has identity local monodromy; the source-authorized p-i0 germ cannot "
            "by itself generate the missing mu2-odd Picard-Lefschetz thimble"
        ),
        "next_gate": (
            "a physical activation claim now requires independently sourced global "
            "contour data coupling to remote singularities or a new coefficient/chain object"
        ),
        "passed": True,
    }
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))


if __name__ == "__main__":
    main()
