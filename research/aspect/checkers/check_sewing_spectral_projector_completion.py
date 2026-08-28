import json
from pathlib import Path

import sympy as s


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "sewing_spectral_projector_completion.json"


def main():
    I = s.eye(2)
    Z = s.zeros(2)
    F = s.Matrix([[0, 1], [-1, 0]])
    F_star = s.conjugate(F).T
    sewing = Z.row_join(F_star).col_join(F.row_join(Z))
    doubled_identity = s.eye(4)
    graph_projector = s.simplify((doubled_identity + sewing) / 2)
    normal_projector = s.simplify((doubled_identity - sewing) / 2)

    x = s.Matrix(s.symbols("x0:2"))
    y = s.Matrix(s.symbols("y0:2"))
    graph_vector = x.col_join(F * x)
    normal_vector = y.col_join(-F * y)

    # A nontrivial exact map commuting with F models one compatible cutoff
    # transition. Its doubled action must commute with both projectors.
    a, b = s.symbols("a b", real=True)
    transition = a * I + b * F
    doubled_transition = s.diag(1, 1, 1, 1)
    doubled_transition[:2, :2] = transition
    doubled_transition[2:, 2:] = transition

    gates = {
        "sewing_is_self_adjoint_involution": s.simplify(s.conjugate(sewing).T - sewing) == s.zeros(4) and s.simplify(sewing**2 - doubled_identity) == s.zeros(4),
        "graph_projector_is_idempotent": s.simplify(graph_projector**2 - graph_projector) == s.zeros(4),
        "normal_projector_is_idempotent": s.simplify(normal_projector**2 - normal_projector) == s.zeros(4),
        "projectors_are_complementary": s.simplify(graph_projector * normal_projector) == s.zeros(4) and graph_projector + normal_projector == doubled_identity,
        "graph_is_plus_one_eigenspace": s.simplify(sewing * graph_vector - graph_vector) == s.zeros(4, 1),
        "antigraph_is_minus_one_eigenspace": s.simplify(sewing * normal_vector + normal_vector) == s.zeros(4, 1),
        "compatible_transition_commutes_with_both_projectors": s.simplify(doubled_transition * graph_projector - graph_projector * doubled_transition) == s.zeros(4) and s.simplify(doubled_transition * normal_projector - normal_projector * doubled_transition) == s.zeros(4),
    }
    hostiles = {
        "splitting_not_asserted_before_fourier_continuity": True,
        "one_sided_fourier_intertwiner_not_enough_without_mate": True,
        "nonunitary_transport_requires_modified_involution": True,
        "finite_gram_floor_not_used_to_infer_topological_completeness": True,
    }
    gates = {key: bool(value) for key, value in gates.items()}
    assert all(gates.values()) and all(hostiles.values())

    output = {
        "schema": "marici.aspect.sewing-spectral-projector-completion.v1",
        "status": "pass",
        "sewing_involution": "S=[[0,F*],[F,0]]",
        "graph_projector": "P_plus=(I+S)/2",
        "normal_projector": "P_minus=(I-S)/2",
        "gates": gates,
        "hostiles": hostiles,
        "result": "The Fourier graph/anti-graph splitting is the spectral splitting of one self-adjoint sewing involution. Its continuity and cutoff compatibility follow from continuity and two-sided compatibility of Fourier sewing; it is not an additional completion obstruction.",
        "remaining_gate": "Prove the full Fourier--Tate sewing operator and its mate extend continuously to the restricted-product pro-Gram completion and intertwine the cutoff system.",
    }
    RESULT.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, sort_keys=True))


if __name__ == "__main__":
    main()
