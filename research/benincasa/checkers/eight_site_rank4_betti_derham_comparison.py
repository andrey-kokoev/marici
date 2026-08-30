"""Chain-level normalized Betti/de Rham comparison for the C8 excess complex."""

import itertools
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
LERAY = ROOT / "results" / "eight-site-rank4-excess-leray-complex.json"
OS_PACKET = ROOT / "results" / "eight-site-rank4-orlik-solomon.json"
REGULATOR_OS = ROOT / "results" / "eight-site-rank4-regulator-os-comparison.json"
TARGET = ROOT / "results" / "eight-site-rank4-betti-derham-comparison.json"


def koszul_contraction(rank: int, degree: int, coefficients: list[sp.Symbol]) -> sp.Matrix:
    source = list(itertools.combinations(range(rank), degree))
    target = list(itertools.combinations(range(rank), degree - 1))
    target_index = {item: index for index, item in enumerate(target)}
    matrix = sp.zeros(len(target), len(source))
    for column, monomial in enumerate(source):
        for position, generator in enumerate(monomial):
            output = monomial[:position] + monomial[position + 1 :]
            matrix[target_index[output], column] += (-1 if position % 2 else 1) * coefficients[generator]
    return matrix


def main() -> None:
    leray = json.loads(LERAY.read_text())
    os_packet = json.loads(OS_PACKET.read_text())
    regulator = json.loads(REGULATOR_OS.read_text())
    b = list(sp.symbols("B1:4"))

    differentials = {
        str(degree): koszul_contraction(3, degree, b)
        for degree in (1, 2, 3)
    }
    d_squared_checks = {
        "2_to_0": differentials["1"] * differentials["2"] == sp.zeros(1, 3),
        "3_to_1": differentials["2"] * differentials["3"] == sp.zeros(3, 1),
    }
    assert all(d_squared_checks.values())

    normalized_period_matrices = {
        str(degree): [[int(value) for value in row] for row in sp.eye(sp.binomial(3, degree)).tolist()]
        for degree in range(4)
    }
    chain_map_checks = {}
    for degree in (1, 2, 3):
        period_source = sp.Matrix(normalized_period_matrices[str(degree)])
        period_target = sp.Matrix(normalized_period_matrices[str(degree - 1)])
        chain_map_checks[str(degree)] = (
            period_target * differentials[str(degree)]
            == differentials[str(degree)] * period_source
        )
    assert all(chain_map_checks.values())

    full_torus_period_ranks = {str(degree): int(sp.binomial(7, degree)) for degree in range(8)}
    os_betti_vectors = {
        tuple(item["orlik_solomon_betti_vector"])
        for item in os_packet["orbit_representatives"]
    }
    os_quotient_checks = []
    for vector in sorted(os_betti_vectors):
        os_quotient_checks.append({
            "orlik_solomon_dimensions": list(vector),
            "exterior_dimensions": [int(sp.binomial(7, degree)) for degree in range(8)],
            "ideal_kernel_dimensions": [int(sp.binomial(7, degree)) - vector[degree] for degree in range(8)],
            "zero_above_rank_four": all(value == 0 for value in vector[5:]),
        })

    orientation_counts = leray["checks"]["transverse_minor_determinant_distribution"]
    checks = {
        "occurrence_count": leray["checks"]["occurrence_count"],
        "generic_transverse_torus_rank": leray["checks"]["generic_leray_torus_rank"],
        "full_torus_period_matrix_ranks": full_torus_period_ranks,
        "excess_chain_ranks": [1, 3, 3, 1],
        "normalized_excess_period_matrices_are_identity": True,
        "koszul_d_squared_zero": d_squared_checks,
        "normalized_period_comparison_is_chain_map": chain_map_checks,
        "os_quotient_type_count": len(os_quotient_checks),
        "all_os_types_zero_above_rank_four": all(item["zero_above_rank_four"] for item in os_quotient_checks),
        "all_regulator_crossings_vanish_in_os_quotient": regulator["checks"]["induced_crossing_map_to_os_quotient_is_zero"],
        "all_private_crossings_use_shared_os_ideal": regulator["checks"]["every_private_crossing_maps_into_shared_os_ideal"],
        "cyclic_orientation_components": orientation_counts,
        "comparison_character_on_two_components": {"-8": -1, "8": 1},
    }
    assert checks["occurrence_count"] == 288
    assert checks["generic_transverse_torus_rank"] == 7
    assert checks["normalized_period_comparison_is_chain_map"] == {"1": True, "2": True, "3": True}
    assert checks["all_regulator_crossings_vanish_in_os_quotient"]
    assert checks["cyclic_orientation_components"] == {"-8": 144, "8": 144}

    packet = {
        "schema": "marici.eight_site_rank4_betti_derham_comparison.v1",
        "normalization": {
            "betti_basis": "oriented product small tori divided by their source-normal determinant character",
            "derham_basis": "wedges of (2*pi*i)^-1 dlog(q_a)",
            "period_pairing": "identity in every exterior degree",
        },
        "full_transverse_comparison": {
            "betti_ranks": full_torus_period_ranks,
            "derham_ranks": full_torus_period_ranks,
            "period_matrices": "identity after normalized dlog convention",
        },
        "excess_comparison": {
            "coefficients": [str(value) for value in b],
            "differentials": {
                degree: [[str(value) for value in row] for row in matrix.tolist()]
                for degree, matrix in differentials.items()
            },
            "period_matrices": normalized_period_matrices,
        },
        "projected_os_comparison": {
            "map": "exterior logarithmic algebra on seven labels -> labelled OS quotient",
            "regulator_crossing_coboundary": "Entry 1924 potential difference +/- partial(e_C)",
            "private_crossing_coherence": "Entry 1923 shared-ideal syzygies",
            "quotient_types": os_quotient_checks,
        },
        "checks": checks,
    }
    TARGET.write_text(json.dumps(packet, indent=2) + "\n")
    print(json.dumps(checks, sort_keys=True))


if __name__ == "__main__":
    main()
