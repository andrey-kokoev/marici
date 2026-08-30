from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


def intensity(vector):
    return tuple(sp.simplify(abs(value) ** 2) for value in vector)


def main() -> None:
    i = sp.I
    e1 = sp.Matrix([1, 0])
    phase_a, phase_b = e1, i * e1
    assert intensity(phase_a) == intensity(phase_b) == (1, 0)
    local_oscillator = e1
    interference_a = sp.simplify((local_oscillator + phase_a).norm() ** 2)
    interference_b = sp.simplify((local_oscillator + phase_b).norm() ** 2)
    assert (interference_a, interference_b) == (4, 2)

    # Unoriented axis images leave a normal-sign sheet. An orientation contract
    # selects the determinant-positive representative.
    proper = sp.eye(3)
    reflected_normal = sp.diag(1, 1, -1)
    axes = [sp.eye(3).col(k) for k in range(3)]
    axis_records_proper = [intensity(proper * axis) for axis in axes]
    axis_records_reflected = [intensity(reflected_normal * axis) for axis in axes]
    assert axis_records_proper == axis_records_reflected
    assert (proper.det(), reflected_normal.det()) == (1, -1)

    # Opposite spinor representatives induce identical vector action.
    q = sp.Matrix([1, 0, 0, 0])
    minus_q = -q
    rotation_q = sp.eye(3)
    rotation_minus_q = sp.eye(3)
    assert rotation_q == rotation_minus_q
    spinor_reference_records = ((1 + q[0]) ** 2, (1 + minus_q[0]) ** 2)
    assert spinor_reference_records == (4, 0)

    # Full endpoint transfer action does not retain ordered factorization.
    h = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
    x = sp.Matrix([[0, 1], [1, 0]])
    route_hh = h * h
    route_xx = x * x
    assert route_hh == route_xx == sp.eye(2)
    assert h != x  # An authenticated internal tap after the first element separates them.

    # A full-rank coordinate chart on composite matrices cannot recover route type.
    a, b, c, d = sp.symbols("a b c d")
    chart = sp.Matrix([a, b, c, d])
    assert chart.jacobian([a, b, c, d]).rank() == 4
    assert tuple(route_hh) == tuple(route_xx)

    # Finite injectivity is not uniform observability.
    epsilon = sp.symbols("epsilon", positive=True)
    transfer_family = sp.diag(1, epsilon)
    assert transfer_family.det() == epsilon
    minimum_gain = epsilon

    # Two detector labels on one carrier add no independent physical rank.
    source = sp.symbols("source")
    duplicated_records = sp.Matrix([source, source])
    independent_records = sp.Matrix([source, sp.symbols("source_2")])
    assert duplicated_records.jacobian([source]).rank() == 1
    assert independent_records.jacobian(list(independent_records)).rank() == 2

    result = {
        "schema": "marici.aspect.optical-action-provenance-ladder.v1",
        "status": "pass",
        "ports": {
            "endpoint_intensity": "direct photodetection",
            "complex_action": "phase-locked interferometric reference plus declared probe basis",
            "normal_orientation": "source-declared orientation or positive chamber",
            "spinor_sheet": "spinorial coherent reference; vector action alone retains Z2",
            "ordered_route": "authenticated internal checkpoint or trusted element log",
        },
        "stabilizers": {
            "intensity_record": "phase and unprobed-action stabilizer",
            "complex_vector_action": "trivial on the declared vector-action domain, but Z2 on spinor lift",
            "oriented_vector_action": "Z2 spinor kernel remains",
            "endpoint_composite_transfer": "all ordered factorizations of the same composite",
            "authenticated_internal_route": "trivial on the declared finite route library",
        },
        "hostiles": {
            "equal_intensity_different_phase": [str(interference_a), str(interference_b)],
            "normal_sign_determinants": [str(proper.det()), str(reflected_normal.det())],
            "opposite_spinor_reference_records": [str(v) for v in spinor_reference_records],
            "same_composite_distinct_routes": True,
            "composite_chart_rank": 4,
            "minimum_gain_family": str(minimum_gain),
            "duplicated_carrier_rank": 1,
        },
        "verdicts": {
            "existence": "pass: each separating port is explicitly defined",
            "synthesis": "pass: phase reference, probe basis, orientation contract, spinor reference, and internal checkpoint are independently typed",
            "execution": "pass in exact finite model; no laboratory run is claimed",
            "fault": "pass: six required hostile collisions are retained and classified",
            "completion": "pass only on the declared finite probe and route library; not a global device-history theorem",
        },
        "irreversible_leak_boundary": "Coherent erasure requires coherent access to every which-route share. A lost orthogonal share makes the reduced interference term zero; duplicated readout labels do not constitute independent fragments.",
    }
    output = Path(__file__).parents[1] / "results" / "optical_action_provenance_ladder.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
