#!/usr/bin/env python3
"""Typed instantiation audit for the current theta Clark--seam source packet."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
G = ROOT / "research" / "grothendieck"
FILES = {
    "pro_gram": G / "theta-constructor-generated-pro-gram-topology.md",
    "endpoint_no_go": G / "theta-endpoint-readout-is-not-continuous-in-the-full-tail-seam-gram.md",
    "withdrawn_fourier_candidate": G / "theta-endpoint-repair-must-use-the-scale-flow-graph-norm.md",
    "native_endpoint": G / "theta-native-first-order-bulk-exactly-controls-the-endpoint.md",
    "tail_closed_range": G / "theta-first-order-tail-channel-has-no-completion-escape.md",
    "seam_escape": G / "theta-seam-cannot-be-a-bounded-function-of-the-retained-tail.md",
    "full_gram_escape": G / "theta-full-tail-seam-gram-is-faithful-but-not-closed-range-on-unrestricted-packets.md",
    "three_stage": G / "theta-three-stage-seam-reservoir-green-repair-compiler.md",
}
OUT = ROOT / "research" / "kitaev" / "results" / "theta-clark-seam-pro-gram-instantiation.json"


def sharp_constant(Q: sp.Matrix, H: sp.Matrix) -> sp.Expr | None:
    if any(H * v != sp.zeros(H.rows, 1) for v in Q.nullspace()):
        return None
    return max((abs(v) for v in (Q.pinv() * H).eigenvals()), default=sp.Integer(0))


def main() -> None:
    text = {name: path.read_text(encoding="utf-8") for name, path in FILES.items()}
    assert "P,Q:" in text["three_stage"]
    assert "before testing their braids" in text["three_stage"]
    assert "does not, without an\nadditional intertwining theorem" in text["withdrawn_fourier_candidate"]
    assert "|G(0)|^2" in text["native_endpoint"]
    assert "no bounded" in text["seam_escape"]
    assert "not closed" in text["full_gram_escape"]

    # Smallest common-carrier incidence witness. The first three coordinates
    # represent the presently typed Clark-1, Clark-2, and seam outputs. The
    # arithmetic primitive and square incidence coordinates are absent.
    Q_partial = sp.diag(1, 1, 1, 0, 0)
    L_primitive = sp.Matrix([[0, 0, 0, 1, 0]])
    L_square = sp.Matrix([[0, 0, 0, 0, 1]])
    v_primitive = sp.Matrix([0, 0, 0, 1, 0])
    v_square = sp.Matrix([0, 0, 0, 0, 1])
    assert Q_partial * v_primitive == sp.zeros(5, 1)
    assert L_primitive * v_primitive == sp.ones(1, 1)
    assert Q_partial * v_square == sp.zeros(5, 1)
    assert L_square * v_square == sp.ones(1, 1)
    assert sharp_constant(Q_partial, L_primitive.T * L_primitive) is None
    assert sharp_constant(Q_partial, L_square.T * L_square) is None

    # Exact finite coordinate model of the native q-flow endpoint identity at
    # a=1/2: ||A_s G||^2=||h'||^2+a^2||h||^2+a|h(0)|^2.
    a = sp.Rational(1, 2)
    Q_graph = sp.diag(1, a * a, a)
    L_endpoint = sp.Matrix([[0, 0, 1]])
    endpoint_M2 = sharp_constant(Q_graph, L_endpoint.T * L_endpoint)
    assert endpoint_M2 == 2  # |h(0)|^2 <= (1/a) energy.

    result = {
        "schema": "marici.kitaev.theta-clark-seam-pro-gram-instantiation.v1",
        "source_sha256": {
            str(path.relative_to(ROOT)).replace("\\", "/"): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in FILES.values()
        },
        "requested_feature_map_status": {
            "G_X_plus_f_X": "source-derived on q-flow graph domain",
            "a_d_z_G_X": "source-derived Clark feature, but not a coefficient-Fourier multiplier",
            "H_X_seam": "source-derived independent direct-sum component",
            "P_X_arithmetic_primitive": "density typed; incidence map into retained boundary module missing",
            "Q_X_prime_square": "density typed; incidence map into retained boundary module missing",
            "single_common_J_X_matrix_constructed": False,
        },
        "first_exact_matrix_witness": {
            "meaning": "incidence typing model, not fitted theta coefficients",
            "Q_partial": Q_partial.tolist(),
            "primitive_kernel_witness": list(v_primitive),
            "square_kernel_witness": list(v_square),
            "primitive_domination_constant": None,
            "square_domination_constant": None,
            "decision": "typed kernel/continuity obstruction",
        },
        "endpoint_audit": {
            "bulk_tail_seam_L2_endpoint_continuous": False,
            "Clark_z_derivative_Fourier_weight_application_authorized": False,
            "reason": "d_z differentiates the relative tail coordinate and no intertwiner to Phihat'/Phihat has been derived",
            "unnormalized_weight_integrability_test_evaluated": False,
            "native_q_flow_graph_endpoint_continuous": True,
            "exact_model_a": "1/2",
            "Q_graph": [[1, 0, 0], [0, "1/4", 0], [0, 0, "1/2"]],
            "endpoint_sharp_M_squared": "2",
            "uniform_region": "compact subsets with Re(s)<=1-delta",
        },
        "observability_status": {
            "finite_A_X_matrix_supplied": False,
            "finite_R_X_matrix_supplied": False,
            "commutator_test_typed": False,
            "full_W_X_computable": False,
            "one_sided_tail_escape_closed": True,
            "full_tail_plus_seam_uniform_observability": False,
            "cause": "full synthesis is faithful but not bounded below on unrestricted coefficient packets",
        },
        "hostile_witness_inventory": {
            "tail_translation_escape": "source exact: ||g_p||->0 while ||h_p||->||Phi||_2; seam cannot be reconstructed from tail",
            "adjacent_label_collapse": "source exact in analytic Gram; arithmetic constructor descent compiler applies",
            "finite_observability_nonuniform": "compiler exact fixture available; theta full synthesis has the analogous high-frequency modulation escape",
            "cutoff_constants_diverge": "compiler exact fixture available; theta-specific matrices absent",
            "cutoff_dependent_constructor_family": "compiler exact fixture available; theta-specific optimization not yet typed",
            "unauthorized_constructor": "prohibited by frozen M_src boundary",
            "scalar_typed_cancellation": "compiler exact fixture available; full theta residual matrices absent",
        },
        "currently_authorized_subsystem": {
            "constructors": ["S seam retention", "R_f continuous forcing reservoir", "D doubled Clark-Green operation"],
            "orders": ["S R_f D", "R_f S D"],
            "braid_residual": 0,
            "arithmetic_P_Q_adjoinable": False,
            "archimedean_incidence_matrix_supplied": False,
            "full_mixed_Green_matrix_supplied": False,
        },
        "machine_rejection": {
            "code": "theta_pro_gram_instantiation_blocked_missing_incidence",
            "current": "arithmetic_primitive_and_square",
            "cutoff": "all presently declared X",
            "constructor_subset": ["S", "R_f", "D"],
            "kernel_witness": [0, 0, 0, 1, 0],
            "sharp_domination_constant": None,
            "uniform_bound_failed": True,
            "unauthorized_constructor_required": False,
            "missing_source_maps": ["P_X: valuation/Fock -> boundary", "Q_X: valuation/Fock -> boundary"],
        },
        "verdict": "The requested full theta/Tate compiler instance is presently blocked before generalized-eigenvalue testing: primitive and square incidence maps, archimedean row, full mixed Green matrix, and common finite dynamics are absent. The native one-sided q-flow endpoint channel is continuously and uniformly controlled on compact open-sector sets, but the withdrawn Clark-z Fourier weight must not be used. The smallest honest decision is a typed kernel/continuity obstruction, not pointwise or uniform full-system observability.",
    }
    # Convert exact SymPy integers in the incidence matrix/witnesses.
    result["first_exact_matrix_witness"]["Q_partial"] = [[int(x) for x in row] for row in Q_partial.tolist()]
    result["first_exact_matrix_witness"]["primitive_kernel_witness"] = [int(x) for x in v_primitive]
    result["first_exact_matrix_witness"]["square_kernel_witness"] = [int(x) for x in v_square]
    result["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
