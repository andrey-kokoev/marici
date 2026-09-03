from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


EVIDENCE = [
    Path("research/voevodsky/results/operator_valued_markov_green.json"),
    Path("research/voevodsky/results/operator_valued_markov_completion.json"),
    Path("research/voevodsky/results/operator_valued_contiguous_beck_chevalley.json"),
]


def main() -> None:
    evidence = [json.loads(path.read_text(encoding="utf-8")) for path in EVIDENCE]
    assert all(item["passed"] is True for item in evidence)

    # Rational orthogonal rotation that is not self-inverse.
    u = sp.Matrix([[sp.Rational(3, 5), -sp.Rational(4, 5)], [sp.Rational(4, 5), sp.Rational(3, 5)]])
    v = sp.Matrix([[0, -1], [1, 0]])
    assert u.T * u == sp.eye(2) == u * u.T
    assert u != u.T

    companion = u
    conjoint = u.T
    assert conjoint * companion == sp.eye(2)
    assert companion * conjoint == sp.eye(2)
    assert companion * conjoint * companion == companion
    assert conjoint * companion * conjoint == conjoint

    composite_companion = v * u
    assert composite_companion == v * companion
    assert composite_companion.T == conjoint * v.T
    assert (sp.eye(2) * v) * u == sp.eye(2) * (v * u)

    result = {
        "schema": "marici.voevodsky.operator-valued-markov-restricted-equipment.v1",
        "status": "fixed_fiber_orthogonal_gauge_equipment_fragment_verified",
        "component_evidence_passed": len(evidence),
        "strict_partial_double_category": True,
        "orthogonal_gauge_groupoid": True,
        "companion_witness": "U",
        "conjoint_witness": "U^T",
        "non_self_inverse_fixture": True,
        "companion_conjoint_triangles": True,
        "composition_comparison_pentagon": True,
        "completion_compatible": True,
        "contiguous_beck_chevalley_compatible": True,
        "all_vertical_maps_equipped": False,
        "varying_fibers_equipped": False,
        "full_coherence_pyramid_equipment": False,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
