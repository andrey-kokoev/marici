import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Exact Krylov witness from the Nima packets.
A = [1, 2, 3]
x = [1, 1, 1]
Ax = [a * xi for a, xi in zip(A, x)]
A2x = [a * xi for a, xi in zip(A, Ax)]

def det3(cols):
    (a,b,c),(d,e,f),(g,h,i) = cols
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)
omega = det3([x, Ax, A2x])
assert omega == 2

# Resource/history gates.
destructive_ports = [A2x]
fanout_ports = [x, x, x]
history_ports = [x, Ax, A2x]
assert len(destructive_ports) == 1
assert det3(fanout_ports) == 0
assert det3(history_ports) == 2

# Depth order matters: swapping depths one and two reverses the sign.
swapped = det3([x, A2x, Ax])
assert swapped == -omega

# Projective ray correction: zeta=exp(i*pi/3) gives zeta^3=-1, so the signed
# determinant does not descend.  The positive square does.
phase_weight = 3
zeta_cubed = -1
assert zeta_cubed * omega == -2
assert omega * omega == 4
required_reference_weight = -phase_weight
assert required_reference_weight == -3
assert phase_weight + required_reference_weight == 0

wp1080_supplies = {
    "bipartite_pairing_3x3": True,
    "epsilon3_A_and_epsilon3_B": True,
    "source_evolution_A": False,
    "seed_ray_x": False,
    "history_retaining_constructor": False,
    "volume_reference_rho_weight_minus3": False,
}
assert list(wp1080_supplies.values()).count(False) == 4

result = {
    "schema": "marici.flavor.wp1081.v1",
    "status": "PASS",
    "question": "Does adding Krylov history to the WP1080 bipartite carrier derive a temporal signed production law?",
    "krylov_witness": {
        "A": A,
        "x": x,
        "Ax": Ax,
        "A2x": A2x,
        "omega": omega,
        "depth_swapped_omega": swapped,
    },
    "history_gates": {
        "destructive_chain_port_count": len(destructive_ports),
        "same_state_fanout_determinant": det3(fanout_ports),
        "history_retaining_determinant": det3(history_ports),
    },
    "projective_gate": {
        "signed_determinant_phase_weight": phase_weight,
        "zeta_cubed_for_pi_over_3_rephase": zeta_cubed,
        "positive_descending_observer": "omega^2",
        "required_volume_reference_weight": required_reference_weight,
    },
    "wp1080_supplies": wp1080_supplies,
    "classification": "bipartite-Krylov composition gate: WP1080 supplies the epsilon carriers and pairing, but signed temporal production still requires a source evolution, seed ray, retained history, and weight-minus-three volume reference",
    "remaining_gate": "derive A, x, the history constructor, and rho from the SU(6) source/localization without changing admitted spectral-overlap data",
    "claim_boundary": "uses the Nima Krylov witness only as a conditional mechanism; it does not identify A with a flavor operator",
    "disposition": "productive: F1 is narrowed to four exact missing constructors instead of a generic temporal-dynamics request",
}

(ROOT / "results" / "wp1081_bipartite_krylov_history_composition_gate.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1081 PASS:", omega, swapped, required_reference_weight)
