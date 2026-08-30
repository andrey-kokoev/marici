"""Exact ambient-map typing of projected and genuine transport witnesses."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / "research/nima/results/ambient-map-witness-sequence.json"


def nullity(matrix: sp.Matrix) -> int:
    return matrix.cols - matrix.rank()


def same_span(left: sp.Matrix, right: sp.Matrix) -> bool:
    return left.rank() == right.rank() == left.row_join(right).rank()


# Full transported plane and preferred/alternate target observations.
M = sp.Matrix([[1, 0], [2, 0], [0, 1]])
P = sp.Matrix([[1, 0, 0], [0, 1, 0]])
P_alt = sp.Matrix([[1, 0, 0], [0, 0, 1]])
PM = P * M
P_alt_M = P_alt * M

ker_m = sp.Matrix.hstack(*M.nullspace()) if M.nullspace() else sp.zeros(M.cols, 0)
ker_pm = sp.Matrix.hstack(*PM.nullspace())
projection_loss_image = M * ker_pm
ker_p = sp.Matrix.hstack(*P.nullspace())

# In this exact packet, im(M) intersect ker(P) is the line transported from
# the apparent chart-kernel direction.
intersection = sp.Matrix([[0], [0], [1]])
left_cocircuit = sp.Matrix.hstack(*PM.T.nullspace())

# At a genuine transport degeneration, the same apparent right-kernel is
# already in ker(M), so the projection-loss quotient vanishes.
M_deg = sp.Matrix([[1, 0], [2, 0], [0, 0]])
PM_deg = P * M_deg

# Legal changes of domain and ambient target basis transport the diagram.
R = sp.Matrix([[1, 1], [0, 1]])
L = sp.Matrix([[1, 1, 0], [0, 1, 1], [0, 0, 1]])
M_changed = L * M * R
P_changed = P * L.inv()
PM_changed = sp.simplify(P_changed * M_changed)

projection_loss_dimension = nullity(PM) - nullity(M)
degenerate_projection_loss_dimension = nullity(PM_deg) - nullity(M_deg)
cokernel_dimension = PM.rows - PM.rank()

gates = {
    "full_transport_is_injective": nullity(M) == 0,
    "preferred_projection_has_artificial_right_kernel": nullity(PM) == 1,
    "projection_loss_quotient_has_dimension_one": projection_loss_dimension == 1,
    "projection_loss_maps_to_image_intersection": same_span(projection_loss_image, intersection),
    "preferred_observations_have_one_left_cocircuit": left_cocircuit.cols == 1,
    "left_cocircuit_is_dual_cokernel_dimension": left_cocircuit.cols == cokernel_dimension,
    "alternate_chart_removes_both_presentation_defects": (
        nullity(P_alt_M) == 0 and nullity(P_alt_M.T) == 0
    ),
    "true_kernel_is_not_projection_loss": degenerate_projection_loss_dimension == 0,
    "ambient_basis_change_preserves_projection_loss": (
        nullity(PM_changed) - nullity(M_changed) == projection_loss_dimension
    ),
}
assert all(gates.values()), gates

result = {
    "schema": "marici.nima.ambient-map-witness-sequence.v1",
    "diagram": "S --M--> T --P--> T_I",
    "dimensions": {
        "ker_M": nullity(M),
        "ker_PM": nullity(PM),
        "projection_loss_ker_PM_over_ker_M": projection_loss_dimension,
        "image_M_intersection_ker_P": intersection.rank(),
        "left_cocircuit": left_cocircuit.cols,
        "coker_PM": cokernel_dimension,
        "genuine_degenerate_ker_M": nullity(M_deg),
        "genuine_degenerate_projection_loss": degenerate_projection_loss_dimension,
    },
    "generators": {
        "artificial_chart_kernel": [str(x) for x in ker_pm[:, 0]],
        "transported_projection_loss": [str(x) for x in projection_loss_image[:, 0]],
        "left_cocircuit": [str(x) for x in left_cocircuit[:, 0]],
    },
    "exact_sequence": (
        "0 -> ker(M) -> ker(PM) -> im(M) intersection ker(P) -> 0"
    ),
    "gates": gates,
}

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"passed": sum(gates.values()), "total": len(gates)}))
