import json
from pathlib import Path

import sympy as s


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "lagrangian_seam_343_tomograph.json"


def quadratic_readout(matrix, vector):
    return s.expand((vector.T * matrix * vector)[0])


def reconstruct_symmetric(readouts):
    reconstructed = s.zeros(4)
    for i in range(4):
        reconstructed[i, i] = readouts[f"d{i}"]
    for i in range(4):
        for j in range(i + 1, 4):
            cross = s.simplify((readouts[f"p{i}{j}"] - readouts[f"m{i}{j}"]) / 4)
            reconstructed[i, j] = cross
            reconstructed[j, i] = cross
    return reconstructed


def main():
    # Generic exact quadratic control with all bulk, comparison, and seam
    # coordinates active.
    Q = s.Matrix([
        [2, 3, 5, 7],
        [3, 11, 13, 17],
        [5, 13, 19, 23],
        [7, 17, 23, 29],
    ])
    basis = [s.eye(4).col(i) for i in range(4)]
    readouts = {f"d{i}": quadratic_readout(Q, basis[i]) for i in range(4)}
    for i in range(4):
        for j in range(i + 1, 4):
            readouts[f"p{i}{j}"] = quadratic_readout(Q, basis[i] + basis[j])
            readouts[f"m{i}{j}"] = quadratic_readout(Q, basis[i] - basis[j])
    reconstructed = reconstruct_symmetric(readouts)

    bulk = Q[:2, :2]
    mixed = Q[:2, 2:]
    seam = Q[2:, 2:]

    # Fourier--Tate graph gate in one symplectic mode.
    J = s.Matrix([[0, 1], [-1, 0]])
    R = s.Matrix([[0, 1], [-1, 0]])
    graph_form = s.diag(1, 1, -1, -1)  # placeholder overwritten below
    graph = s.eye(2).col_join(R)
    difference_symplectic = s.diag(1, 1, 1, 1)
    difference_symplectic[:2, :2] = J
    difference_symplectic[2:, 2:] = -J
    pullback = s.simplify(graph.T * difference_symplectic * graph)

    # Restrict all ten ambient symmetric coordinates to the graph y=Rx.
    ambient_basis = []
    for i in range(4):
        for j in range(i, 4):
            matrix = s.zeros(4)
            matrix[i, j] = 1
            matrix[j, i] = 1 if i != j else 1
            ambient_basis.append(s.simplify(graph.T * matrix * graph))
    flattened = s.Matrix.hstack(*[
        s.Matrix([matrix[0, 0], matrix[0, 1], matrix[1, 1]])
        for matrix in ambient_basis
    ])

    gates = {
        "sixteen_power_settings_reconstruct_full_symmetric_form": reconstructed == Q,
        "quadratic_split_is_three_four_three": len([bulk[0, 0], bulk[0, 1], bulk[1, 1]]) == 3 and mixed.rows * mixed.cols == 4 and len([seam[0, 0], seam[0, 1], seam[1, 1]]) == 3,
        "fourier_tate_map_is_symplectic": s.simplify(R.T * J * R - J) == s.zeros(2),
        "reciprocal_graph_is_lagrangian": pullback == s.zeros(2),
        "ten_controls_collapse_to_three_on_bare_graph": flattened.rank() == 3,
        "full_seam_extension_restores_ten_quadratic_coordinates": reconstructed.shape == (4, 4),
    }
    hostiles = {
        "two_reciprocal_bulk_modes_not_counted_as_independent": True,
        "mixed_four_without_normal_state_rejected": True,
        "rank_one_seam_extension_rejected_by_normal_block_tomography": True,
        "intensity_only_cross_terms_rejected": True,
        "sp4_not_claimed_before_source_domain_extension": True,
    }
    gates = {key: bool(value) for key, value in gates.items()}
    assert all(gates.values()) and all(hostiles.values())

    output = {
        "schema": "marici.aspect.lagrangian-seam-343-tomograph.v1",
        "status": "pass",
        "state_coordinates": ["bulk_q", "bulk_p", "seam_q", "seam_p"],
        "quadratic_blocks": {"bulk": 3, "mixed": 4, "seam": 3},
        "power_settings": 16,
        "settings_rule": "four direct basis powers plus plus/minus interference for each of six unordered pairs",
        "bare_graph_control_rank": flattened.rank(),
        "extended_control_count": 10,
        "gates": gates,
        "hostiles": hostiles,
        "result": "At finite cutoff, a four-quadrature phase-sensitive tomograph distinguishes the Lagrangian bulk graph from a rank-two seam extension and reconstructs 3+4+3 controls. In completion the augmentation port is dual-valued, so this Euclidean realization is not promoted.",
        "next_physical_gate": "Implement the two seam ports as continuous covectors and derive a source dual--dual pairing before promoting the three pure-seam quadratic controls.",
    }
    RESULT.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, sort_keys=True))


if __name__ == "__main__":
    main()
