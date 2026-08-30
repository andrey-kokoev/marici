"""Mass-basis cubic-vector census on a formal contact-bound witness."""

import contextlib
import io
import json
from pathlib import Path

import numpy as np
import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp508 = load("wp508_canonical_heavy_gauge_poles.json")
wp511 = load("wp511_neutral_b_current_instrument.json")
wp515 = load("wp515_bmixing_forced_pole_hierarchy.json")

# Replay the canonical WP508 mass matrix.  The witness keeps WP510's declared
# gauge/connector parameters but replaces its excluded entrance ratio by the
# formally contact-compatible ratio a/b=400 and enforces v=246 GeV.  WP519
# shows that the resulting pole spectrum lacks a source-to-WET descent.
path508 = root / "checkers" / "wp508_canonical_heavy_gauge_poles.py"
namespace = {"__file__": str(path508), "__name__": "wp508_replay"}
with contextlib.redirect_stdout(io.StringIO()):
    try:
        exec(compile(path508.read_text(encoding="utf-8"), str(path508), "exec"), namespace)
    except SystemExit as error:
        if error.code != 0:
            raise

heavy_block = namespace["heavy_block"]
components = namespace["components"]
g_f = namespace["g_f"]
g_p = namespace["g_p"]
g_e = namespace["g_e"]
mu = namespace["mu"]
s = namespace["s"]
a = namespace["a"]
b = namespace["b"]

v_squared = sp.Integer(246) ** 2
ratio = sp.Integer(400)
b_squared = sp.factor(v_squared / (2 * (ratio**2 + 1)))
a_squared = sp.factor(ratio**2 * b_squared)
witness = {
    g_f: sp.sqrt(2),
    g_p: sp.Rational(1, 10),
    g_e: sp.Rational(1, 50),
    mu: 1,
    s: 16,
    a: sp.sqrt(a_squared),
    b: sp.sqrt(b_squared),
}
matrix_exact = sp.simplify(heavy_block.subs(witness))
matrix_numeric = np.array(matrix_exact.evalf(50).tolist(), dtype=float)
mass_squared, rotation = np.linalg.eigh(matrix_numeric)
masses = np.sqrt(np.maximum(mass_squared, 0.0))

# Exact structure constants in the canonical gauge basis.  Hermitian
# generators obey [T_A,T_B]=i f_ABC T_C and tr(T_A T_B)=delta_AB/2.
i_unit = sp.I
zero = sp.Integer(0)
one = sp.Integer(1)
gell_mann = [
    sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),
    sp.Matrix([[0, -i_unit, 0], [i_unit, 0, 0], [0, 0, 0]]),
    sp.Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]]),
    sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]]),
    sp.Matrix([[0, 0, -i_unit], [0, 0, 0], [i_unit, 0, 0]]),
    sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]]),
    sp.Matrix([[0, 0, 0], [0, 0, -i_unit], [0, i_unit, 0]]),
    sp.diag(1, 1, -2) / sp.sqrt(3),
]
flavor_structure = np.zeros((8, 8, 8), dtype=float)
for left in range(8):
    for middle in range(8):
        commutator = gell_mann[left] * gell_mann[middle] - gell_mann[middle] * gell_mann[left]
        for right in range(8):
            value = sp.simplify(sp.trace(commutator * gell_mann[right]) / (4 * i_unit))
            flavor_structure[left, middle, right] = float(value)


def epsilon(left, middle, right):
    return float(sp.LeviCivita(left, middle, right))


gauge_tensor = np.zeros((14, 14, 14), dtype=float)
for left in range(8):
    for middle in range(8):
        for right in range(8):
            gauge_tensor[left, middle, right] = float(sp.sqrt(2)) * flavor_structure[left, middle, right]
for offset, coupling in ((8, 0.1), (11, 0.02)):
    for left in range(3):
        for middle in range(3):
            for right in range(3):
                gauge_tensor[offset + left, offset + middle, offset + right] = coupling * epsilon(left, middle, right)

mass_tensor = np.einsum("abc,ai,bj,ck->ijk", gauge_tensor, rotation, rotation, rotation)

# Enumerate unordered daughter pairs.  A nonzero tensor entry is a physical
# Yang--Mills vertex; the strict mass inequality is the two-body threshold.
channels = []
for parent in range(14):
    for daughter_1 in range(14):
        for daughter_2 in range(daughter_1 + 1, 14):
            coupling = float(mass_tensor[parent, daughter_1, daughter_2])
            margin = float(masses[parent] - masses[daughter_1] - masses[daughter_2])
            if margin > 1e-9 and abs(coupling) > 1e-7:
                channels.append(
                    {
                        "parent": parent,
                        "daughter_1": daughter_1,
                        "daughter_2": daughter_2,
                        "parent_mass_GeV": float(masses[parent]),
                        "daughter_masses_GeV": [float(masses[daughter_1]), float(masses[daughter_2])],
                        "threshold_margin_GeV": margin,
                        "cubic_coupling": coupling,
                    }
                )

channels.sort(key=lambda item: (-item["threshold_margin_GeV"], -abs(item["cubic_coupling"])))
largest_residual = float(np.max(np.abs(matrix_numeric @ rotation - rotation @ np.diag(mass_squared))))
orthogonality_residual = float(np.max(np.abs(rotation.T @ rotation - np.eye(14))))
minimum_reported_margin = min((item["threshold_margin_GeV"] for item in channels), default=0.0)
minimum_reported_coupling = min((abs(item["cubic_coupling"]) for item in channels), default=0.0)

checks = {
    "wp508_dependency_passed": bool(wp508["passed"]),
    "wp511_dependency_passed": bool(wp511["passed"]),
    "wp515_dependency_passed": bool(wp515["passed"]),
    "entrance_ratio_is_inside_wp515_bound": bool(
        1 / float(ratio) < wp515["source_implication"]["maximum_b_over_a"]
    ),
    "electroweak_norm_is_exactly_246_squared": sp.simplify(2 * (a_squared + b_squared) - v_squared) == 0,
    "canonical_heavy_matrix_is_positive": bool(np.min(mass_squared) > 0),
    "eigendecomposition_residual_is_below_tolerance": bool(largest_residual < 1e-10),
    "eigenvectors_are_orthonormal_below_tolerance": bool(orthogonality_residual < 1e-12),
    "structure_tensor_is_antisymmetric": bool(
        np.max(np.abs(gauge_tensor + np.swapaxes(gauge_tensor, 0, 1))) < 1e-15
    ),
    "at_least_one_strictly_open_nonzero_cubic_channel_exists": bool(len(channels) > 0),
    "reported_channels_have_resolved_threshold_margin": bool(minimum_reported_margin > 1e-6),
    "reported_channels_have_resolved_nonzero_vertex": bool(minimum_reported_coupling > 1e-7),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP516",
    "admitted_state_domain": "One aligned physical16 source witness with a/b=400 and v_phys=246 GeV. Its ratio passes the formal WP515 contact-coordinate bound, but its sub-5-GeV pole spectrum has no admitted descent to WP511's 160-GeV WET domain.",
    "source_witness": {
        "a_squared_GeV_squared": str(a_squared),
        "b_squared_GeV_squared": str(b_squared),
        "b_over_a": str(1 / ratio),
        "gauge_parameters": "g_F=sqrt(2), g_P=1/10, g_E=1/50, mu=1 GeV, s=16 GeV",
        "authority": "Existence witness only; the numerical coefficients are not source-selected.",
    },
    "mass_basis": {
        "ordered_mass_squared_GeV_squared": [float(value) for value in mass_squared],
        "ordered_masses_GeV": [float(value) for value in masses],
        "eigendecomposition_residual": largest_residual,
        "orthogonality_residual": orthogonality_residual,
    },
    "open_cubic_vector_channels": channels,
    "classification": "The formal contact-bound hierarchical witness is not protected by a universal zero-vertex theorem: it has explicit open nonzero Yang--Mills mass-basis channels. B_s compatibility is not admitted without source-to-WET threshold matching.",
    "selector": False,
    "rigidifier": bool(len(channels) > 0 and minimum_reported_coupling > 1e-7),
    "instrument": "WP511 types a WET coefficient at 160 GeV but does not yet admit this sub-5-GeV propagating pole packet; source-to-WET threshold matching and pole-resolved instrumentation are absent.",
    "smallest_exact_falsifier": "At this frozen witness, either every transported cubic tensor entry on a strict two-body threshold is zero or every nonzero entry is kinematically closed.",
    "remaining_gate": "Derive and verify the polarization-summed unequal-mass vector-to-vector-vector width functional, add scalar channels, and propagate detector resolution. This packet establishes an open vertex but does not yet assign a total width.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp516_hierarchical_mass_basis_vertices.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
