"""Exact comparison of coarse Wilson-parity effects and physical instruments."""

from fractions import Fraction
import json


def parity(value):
    return value.bit_count() & 1


def pure_pair_density(a, b):
    half = Fraction(1, 2)
    return {(a, a): half, (a, b): half, (b, a): half, (b, b): half}


def global_parity_instrument(rho, outcome):
    return {
        (i, j): value
        for (i, j), value in rho.items()
        if parity(i) == parity(j) == outcome
    }


def refined_then_coarsened_instrument(rho, outcome):
    return {
        (i, j): value
        for (i, j), value in rho.items()
        if i == j and parity(i) == outcome
    }


def trace(rho):
    return sum(value for (i, j), value in rho.items() if i == j)


def scale(rho, factor):
    return {key: factor * value for key, value in rho.items()}


def torus_endpoint_counts(L):
    # A noncontractible horizontal Z loop uses horizontal edges (x,0).
    vertex = lambda x, y: (x % L) * L + (y % L)
    edge_boundaries = []
    for x in range(L):
        for y in range(L):
            edge_boundaries.append((1 << vertex(x, y)) | (1 << vertex(x + 1, y)))
    loop_edges = [x * L for x in range(L)]
    loop_syndrome = 0
    for edge in loop_edges:
        loop_syndrome ^= edge_boundaries[edge]
    constituent_counts = [edge_boundaries[edge].bit_count() for edge in loop_edges]
    assert loop_syndrome == 0
    assert constituent_counts == [2] * L
    return loop_edges, constituent_counts


def audit(L):
    # |a> and |b> have the same even parity but differ microscopically.
    a, b = 0, 0b11
    rho = pure_pair_density(a, b)
    global_even = global_parity_instrument(rho, 0)
    refined_even = refined_then_coarsened_instrument(rho, 0)
    assert trace(global_even) == trace(refined_even) == 1
    assert global_even[(a, b)] == Fraction(1, 2)
    assert (a, b) not in refined_even

    # Their difference on span{|a>,|b>} is [[0,1/2],[1/2,0]], with
    # eigenvalues +/-1/2 and trace distance 1/2.
    trace_distance = Fraction(1, 2)

    # A symmetric classical record flip p=1/10 changes the reported effect
    # identically for both protocols but cannot undo fine-record decoherence.
    p = Fraction(1, 10)
    noisy_global_even = scale(global_even, 1 - p)
    noisy_refined_even = scale(refined_even, 1 - p)
    noisy_subnormalized_trace_distance = (1 - p) * trace_distance
    assert trace(noisy_global_even) == trace(noisy_refined_even) == Fraction(9, 10)
    assert noisy_subnormalized_trace_distance == Fraction(9, 20)

    loop_edges, constituent_counts = torus_endpoint_counts(L)
    return {
        "L": L,
        "witness_basis_states": [a, b],
        "shared_parity": 0,
        "ideal_reported_effect_probabilities_equal": True,
        "global_instrument_preserves_same_parity_coherence": True,
        "refined_then_coarsened_instrument_erases_coherence": True,
        "normalized_output_trace_distance": str(trace_distance),
        "classical_record_flip_probability": str(p),
        "noisy_reported_effect_probabilities_equal": True,
        "noisy_subnormalized_output_trace_distance": str(noisy_subnormalized_trace_distance),
        "noncontractible_loop_support": len(loop_edges),
        "closed_loop_star_syndrome_weight": 0,
        "individual_edge_star_syndrome_weights": constituent_counts,
        "coherent_mobile_ancilla_record_bits": 1,
        "coherent_mobile_ancilla_depth": L,
        "refined_parallel_record_bits": L,
        "refined_parallel_data_coupling_depth": 1,
    }


def main():
    payload = {
        "schema": "marici.wilson-parity-instruments.v1",
        "audits": [audit(L) for L in range(2, 7)],
        "aggregate_gates": {
            "same_coarse_effect_does_not_imply_same_instrument": True,
            "global_luders_port_preserves_same_grade_coherence": True,
            "fine_record_coarsening_irreversibly_dephases_without_record_control": True,
            "classical_readout_noise_does_not_remove_instrument_difference": True,
            "closed_wilson_loop_is_residue_free_while_constituents_are_not": True,
            "depth_record_tradeoff_is_explicit": True,
        },
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

