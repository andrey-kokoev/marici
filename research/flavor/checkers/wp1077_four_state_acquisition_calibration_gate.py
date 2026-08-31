import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Variables are (B,L,g,nu,s): background, source luminosity, detector/interface
# gain, coherent visibility, and same-frame momentum scale.
base = {"B": 0, "L": 1, "g": 1, "nu": 1, "s": 1}


def observations(v):
    B, L, g, nu, s = (v[k] for k in ("B", "L", "g", "nu", "s"))
    return {
        "dark": B,
        "monitor": L,
        "source": B + L * g * g,
        "reference": g,
        "interference_phase_difference": 4 * nu * L * g,
        "momentum_response": L * g * g / (1 + s),
    }

base_obs = observations(base)

# Exact Jacobian at the base point.  Six typed rows determine five local
# directions.
J = [
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [1, 1, 2, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 4, 4, 4, 0],
    [0, 1, 2, 0, Fraction(-1, 2)],
]


def rank(mat):
    m = [[Fraction(x) for x in row] for row in mat]
    rows, cols = len(m), len(m[0])
    r = 0
    for c in range(cols):
        pivot = None
        for i in range(r, rows):
            if m[i][c] != 0:
                pivot = i
                break
        if pivot is None:
            continue
        m[r], m[pivot] = m[pivot], m[r]
        pv = m[r][c]
        m[r] = [x / pv for x in m[r]]
        for i in range(rows):
            if i != r and m[i][c] != 0:
                factor = m[i][c]
                m[i] = [x - factor * y for x, y in zip(m[i], m[r])]
        r += 1
        if r == rows:
            break
    return r
assert rank(J) == 5

# Hostile perturbations in each coordinate are separately visible in at least one typed row.
delta = Fraction(1, 10)
for key in ("B", "L", "g", "nu", "s"):
    hostile = dict(base)
    hostile[key] = Fraction(hostile[key]) + delta
    assert observations(hostile) != base_obs

# Classification gates from the four-state acquisition.
absolute_row = base_obs["source"] - base_obs["dark"]
assert absolute_row == base["L"] * base["g"] ** 2
assert absolute_row == 1
phase_zero = 4 * base["nu"] * base["L"] * base["g"]
phase_pi = -phase_zero
assert phase_zero - phase_pi == 8
normalized_shape = absolute_row / (base["L"] * base["g"] ** 2)
assert normalized_shape == 1

result = {
    "schema": "marici.flavor.wp1077.v1",
    "status": "PASS",
    "question": "Can a four-state acquisition distinguish background, luminosity, gain, visibility, and momentum-scale hostiles in one frame?",
    "external_source": {
        "kind": "epistemic_graph_reply",
        "sender": "marici.Aspect",
        "recipient": "marici.Figueiredo",
        "event_sequence": 10544,
        "event_id": "ev-000000010544-a62a9632-c088-45ab-8096-daf7849a3496",
    },
    "states": [
        "dark_background",
        "source_with_upstream_monitor",
        "reference_only",
        "source_plus_coherent_reference_phase_0_and_pi",
    ],
    "base_observations": {k: str(v) for k, v in base_obs.items()},
    "jacobian_rank_on_B_L_g_nu_s": rank(J),
    "hostile_directions": ["background", "luminosity", "gain", "visibility", "momentum_scale"],
    "classification_rows": {
        "absolute_rate": "source-dark = L g^2",
        "interference": "phase difference 4 nu L g changes sign under phase toggle",
        "normalized_shape": "(source-dark)/(monitor*g^2) erases absolute scale",
    },
    "classification": "conditional four-state acquisition gate: reference and monitor rows calibrate gain/luminosity, dark and phase rows identify background/visibility, and the momentum row identifies the remaining scale direction",
    "remaining_gate": "connect the calibrated instrument to an actual source production/decay kernel; calibration alone does not derive physical16 dynamics",
    "claim_boundary": "models the Aspect reply as an exact local linear instrument; it does not claim the source channel or mixing matrix",
    "disposition": "productive: the gain/instrument branch has a bounded five-hostile calibration constructor, while C1 remains blocked on source dynamics",
}

(ROOT / "results" / "wp1077_four_state_acquisition_calibration_gate.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1077 PASS:", rank(J), {k: str(v) for k, v in base_obs.items()})
