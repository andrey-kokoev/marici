"""Exact obstruction to transporting kaon-knob authority to WP400 scalar shifts."""

import json
from pathlib import Path

import sympy as sp


# Scalar mediator force: dV/dA = H*A - N.  A nonzero tadpole N makes the
# origin nonstationary.
A, H, N = sp.symbols("A H N", real=True, nonzero=True)
scalar_force = H * A - N
scalar_origin = scalar_force.subs(A, 0)

# Kaon propagation is homogeneous on its two-component state.
h11, h12, h21, h22 = sp.symbols("h11 h12 h21 h22")
Hk = sp.Matrix([[h11, h12], [h21, h22]])
psi1, psi2 = sp.symbols("psi1 psi2")
psi = sp.Matrix([psi1, psi2])
kaon_flow = Hk * psi
kaon_origin = kaon_flow.subs({psi1: 0, psi2: 0})

# Every invertible linear change of state preserves the fixed origin.
p11, p12, p21, p22 = sp.symbols("p11 p12 p21 p22")
P = sp.Matrix([[p11, p12], [p21, p22]])
conjugated_origin = sp.simplify(P * kaon_origin)

# Homogenizing the scalar affine flow requires an augmented constant reference
# coordinate.  That is a new port and changes the state domain.
augmented_scalar_generator = sp.Matrix([[H, -N], [0, 0]])
augmented_state = sp.Matrix([A, 1])
augmented_flow = augmented_scalar_generator * augmented_state

checks = {
    "scalar_tadpole_moves_origin": scalar_origin != 0,
    "kaon_homogeneous_flow_fixes_origin": kaon_origin == sp.zeros(2, 1),
    "linear_conjugacy_preserves_kaon_origin": conjugated_origin == sp.zeros(2, 1),
    "no_linear_conjugacy_to_nonzero_tadpole": scalar_origin != conjugated_origin[0],
    "augmentation_reproduces_affine_scalar_force": augmented_flow[0] == scalar_force,
    "augmentation_adds_reference_dimension": augmented_state.rows == psi.rows and augmented_state[1] == 1,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP411",
    "title": "Kaon-to-scalar transport gate",
    "wp400_operation": "affine scalar force H*A-N with independently shifted curvature and tadpole",
    "kaon_operation": "homogeneous non-Hermitian two-state propagation with dispersive and absorptive matter terms",
    "origin_test": {"scalar": str(scalar_origin), "kaon": [str(x) for x in kaon_origin]},
    "required_repair": "augment the state by a constant reference/source coordinate, defining a new physical port and groupoid",
    "classification": "no authority-preserving linear transport from WP406-WP410 to the WP400 tadpole objective",
    "smallest_exact_falsifier": "zero is fixed by every homogeneous kaon propagator but is moved by every nonzero scalar tadpole",
    "checks": checks,
    "passed": all(checks.values()),
}

if not result["passed"]:
    raise SystemExit("WP411 exact checks failed")

out = Path(__file__).parents[1] / "results" / "wp411_kaon_scalar_transport_gate.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
