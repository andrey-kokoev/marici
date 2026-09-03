from __future__ import annotations

import json

import sympy as sp


def common_kernel_dimension(probe_matrix: sp.Matrix, target_dimension: int) -> int:
    return target_dimension - probe_matrix.rank()


def main() -> None:
    # Residual space is M_2(R), vectorized in four coordinates.
    target_dimension = 4
    trace = sp.Matrix([[1, 0, 0, 1]])
    assert trace.rank() == 1
    assert common_kernel_dimension(trace, target_dimension) == 3
    hidden_traceless = sp.Matrix([1, 0, 0, -1])
    assert trace * hidden_traceless == sp.zeros(1, 1)

    # Full entry probes are separating in fixed presentation coordinates.
    entries = sp.eye(4)
    assert entries.rank() == target_dimension
    assert common_kernel_dimension(entries, target_dimension) == 0

    # An incomplete family leaves an exact unresolved fiber dimension.
    three_entries = sp.eye(4)[:3, :]
    assert three_entries.rank() == 3
    assert common_kernel_dimension(three_entries, target_dimension) == 1
    hidden_fourth_entry = sp.Matrix([0, 0, 0, 1])
    assert three_entries * hidden_fourth_entry == sp.zeros(3, 1)

    # Gauge descent: a probe must annihilate the declared gauge direction.
    gauge_direction = sp.Matrix([1, 0, 0, -1])
    trace_descends = (trace * gauge_direction) == sp.zeros(1, 1)
    first_entry = sp.Matrix([[1, 0, 0, 0]])
    first_entry_descends = (first_entry * gauge_direction) == sp.zeros(1, 1)
    assert trace_descends is True
    assert first_entry_descends is False

    quotient_dimension = target_dimension - 1
    assert quotient_dimension == 3
    assert trace.rank() < quotient_dimension

    result = {
        "schema": "marici.voevodsky.restricted-yoneda-probe-density.v1",
        "status": "finite_probe_separation_rank_gate_verified",
        "presentation_residual_dimension": target_dimension,
        "trace_probe_rank": trace.rank(),
        "trace_unresolved_fiber_dimension": common_kernel_dimension(trace, target_dimension),
        "full_entry_probe_rank": entries.rank(),
        "full_entry_family_separating_in_fixed_coordinates": True,
        "three_probe_unresolved_fiber_dimension": common_kernel_dimension(three_entries, target_dimension),
        "gauge_descended_trace_fixture": True,
        "nongauge_descended_entry_fixture": True,
        "rank_alone_proves_physical_admission": False,
        "Kitaev_probe_family_density_verified": False,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
