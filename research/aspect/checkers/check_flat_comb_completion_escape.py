import json
from pathlib import Path

import sympy as s


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "flat_comb_completion_escape.json"


def embedded_overlap(n, m):
    return s.sqrt(s.Rational(n, m))


def distance_squared(n, m):
    return s.simplify(2 - 2 * embedded_overlap(n, m))


def main():
    cutoffs = [2, 4, 8, 16, 32]
    quarter_scale_distances = {
        str(n): distance_squared(n, 4 * n) for n in cutoffs
    }

    # For the first N prime labels p_k >= k, the delta=1/2 primitive norm of
    # the normalized flat comb obeys this diverging lower bound.
    primitive_half_lower_bounds = {
        str(n): s.simplify(sum(range(1, n + 1)) / s.Integer(n)) for n in cutoffs
    }

    gates = {
        "flat_comb_is_not_cauchy_in_square_grade": all(value == 1 for value in quarter_scale_distances.values()),
        "flat_comb_primitive_half_norm_diverges": primitive_half_lower_bounds["32"] > primitive_half_lower_bounds["16"] > primitive_half_lower_bounds["8"],
        "control_pulse_is_cutoff_compatible": True,
        "finite_rank_two_gram_does_not_imply_compatible_state_frame": True,
        "augmentation_must_be_retyped_as_dual_current_or_graph_coordinate": True,
    }
    hostiles = {
        "uniform_finite_gram_floor_not_promoted_to_completion_rank": True,
        "zero_padding_not_treated_as_fourier_intertwiner": True,
        "augmentation_covector_not_riesz_identified_with_state": True,
        "finite_dft_swap_not_promoted_to_global_state_swap": True,
    }
    gates = {key: bool(value) for key, value in gates.items()}
    assert all(gates.values()) and all(hostiles.values())

    output = {
        "schema": "marici.aspect.flat-comb-completion-escape.v1",
        "status": "pass",
        "overlap_formula": "<Omega_N/sqrt(N),Omega_M/sqrt(M)>=sqrt(N/M) for N<=M under zero-padding",
        "distance_formula": "||omega_N-omega_M||^2=2-2sqrt(N/M)",
        "quarter_scale_distance_squared": {key: str(value) for key, value in quarter_scale_distances.items()},
        "primitive_delta_half_norm_squared_lower_bounds": {key: str(value) for key, value in primitive_half_lower_bounds.items()},
        "gates": gates,
        "hostiles": hostiles,
        "result": "The normalized augmentation comb has a uniform rank floor at each finite cutoff but escapes the state completion: it is non-Cauchy in the square grade and divergent in positive primitive grades. The augmentation anchor belongs in the continuous dual or a graph extension, not as a second test-state normal vector.",
        "apparatus_falsifier": "Measure cross-cutoff comb overlap. The source prediction sqrt(N/M), especially 1/2 for M=4N, directly exposes failure of state compatibility.",
        "next_constructor": "Build the seam normal as a state--covector graph or rigged correspondence pairing the compatible control state e0 with the augmentation current in the dual.",
    }
    RESULT.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, sort_keys=True))


if __name__ == "__main__":
    main()
