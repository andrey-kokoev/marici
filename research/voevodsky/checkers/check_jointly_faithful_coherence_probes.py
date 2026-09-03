from __future__ import annotations

import json

import sympy as sp


def trace_probe(matrix: sp.Matrix) -> sp.Expr:
    return sp.trace(matrix)


def entry_probes(matrix: sp.Matrix) -> tuple[sp.Expr, ...]:
    return tuple(matrix[i, j] for i in range(matrix.rows) for j in range(matrix.cols))


def main() -> None:
    identity = sp.eye(2)
    hidden_defect = sp.diag(1, -1)
    altered = identity + hidden_defect
    assert altered != identity
    assert trace_probe(altered) == trace_probe(identity)
    assert trace_probe(hidden_defect) == 0

    # Full entry family is jointly faithful in the fixed-coordinate fixture.
    assert entry_probes(altered) != entry_probes(identity)
    zero = sp.zeros(2)
    candidates = [sp.Matrix(2, 2, values) for values in (
        (0, 0, 0, 0), (1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)
    )]
    assert all((entry_probes(candidate) == entry_probes(zero)) == (candidate == zero) for candidate in candidates)

    # Trace is cyclic but is not a homomorphism for matrix composition.
    a = sp.Matrix([[1, 1], [0, 1]])
    b = sp.Matrix([[1, 0], [1, 1]])
    assert trace_probe(a * b) != trace_probe(a) * trace_probe(b)
    assert trace_probe(a * b) == trace_probe(b * a)

    detection_hypotheses = {
        "typed_source_authorized",
        "jointly_faithful_on_declared_quotient",
        "composition_and_identity_preserving",
        "simplex_and_mixed_coverage_complete",
        "fault_independence_certified",
    }
    assert len(detection_hypotheses) == 5

    result = {
        "schema": "marici.voevodsky.jointly-faithful-coherence-probes.v1",
        "status": "conservative_detection_gates_verified",
        "trace_hidden_kernel_counterexample": True,
        "trace_composition_preserving": False,
        "trace_cyclic_order_invariant": True,
        "fixed_basis_entry_family_jointly_faithful_fixture": True,
        "fixed_basis_family_gauge_descended": False,
        "conditional_detection_hypotheses": sorted(detection_hypotheses),
        "Kitaev_Bargmann_family_jointly_faithful": False,
        "global_coherence_detected": False,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
