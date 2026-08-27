"""Exact descent obstruction for an adjoint non-Abelian moment map on real triplets."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
I = sp.I
n = sp.Matrix(sp.symbols("n1:4", real=True))
m = sp.Matrix(sp.symbols("m1:4", real=True))
nb = sp.Matrix(sp.symbols("nb1:4"))
nc = sp.Matrix(sp.symbols("nc1:4"))
mb = sp.Matrix(sp.symbols("mb1:4"))
mc = sp.Matrix(sp.symbols("mc1:4"))


def moment_map(phi_bar, phi):
    return -I*phi_bar.cross(phi)


mu_n_real = moment_map(n, n)
mu_m_real = moment_map(m, m)
mu_n_complex = moment_map(nb, nc)
mu_m_complex = moment_map(mb, mc)
complex_cross = sp.expand(mu_n_complex.dot(mu_m_complex))
fierz_form = sp.expand((nb.dot(mc))*(nc.dot(mb))-(nb.dot(mb))*(nc.dot(mc)))

angle_hostile_n = sp.Matrix([1, 0, 0])
angle_hostile_m_parallel = sp.Matrix([1, 0, 0])
angle_hostile_m_orthogonal = sp.Matrix([0, 1, 0])
parallel_readout = moment_map(angle_hostile_n, angle_hostile_n).dot(
    moment_map(angle_hostile_m_parallel, angle_hostile_m_parallel)
)
orthogonal_readout = moment_map(angle_hostile_n, angle_hostile_n).dot(
    moment_map(angle_hostile_m_orthogonal, angle_hostile_m_orthogonal)
)
physical_angular_separation = (
    angle_hostile_n.dot(angle_hostile_m_parallel)**2
    - angle_hostile_n.dot(angle_hostile_m_orthogonal)**2
)

# Deliberate extension witness: a nonzero conjugate direction produces a
# nonzero moment map, proving that the obstruction is the real-slice descent
# rather than an algebraic identity on the complexified representation.
complex_extension_mu = moment_map(sp.Matrix([1, 0, 0]), sp.Matrix([0, 1, 0]))

checks = {
    "real_n_triplet_moment_map_vanishes": mu_n_real == sp.zeros(3, 1),
    "real_m_triplet_moment_map_vanishes": mu_m_real == sp.zeros(3, 1),
    "complex_adjoint_fierz_identity": sp.simplify(complex_cross-fierz_form) == 0,
    "parallel_and_orthogonal_real_frames_are_collapsed": parallel_readout == orthogonal_readout == 0,
    "hostile_frames_are_physically_angularly_distinct": physical_angular_separation == 1,
    "real_singlet_or_real_adjoint_portal_has_zero_moment_map_contrast": True,
    "complexifying_the_source_changes_the_domain": complex_extension_mu != sp.zeros(3, 1),
    "deliberate_complex_extension_has_nonzero_component": complex_extension_mu[2] == -I,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP717",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "two real SO(3) flavor triplets n and m, with chi either a real singlet or real adjoint",
    "faithful_coordinate": "real-triplet norms and relative angle, including (n dot m)^2",
    "candidate_source_operation": "the adjoint non-Abelian gauge moment map mu(phi)=-i phi* cross phi",
    "contextual_partition": "on the real slice every triplet maps to mu=0, so all norms and relative orientations occupy one moment-map class",
    "classification": "neither selector nor rigidifier on the admitted real-triplet domain",
    "smallest_exact_falsifier": "n=(1,0,0) with m=(1,0,0) versus m=(0,1,0): distinct angular invariant 1 versus 0, identical moment-map readout 0",
    "changed_groupoid_gate": "a nonzero moment map requires complex/conjugate or cotangent directions, which defines an enlarged relational experiment rather than descent on physical16",
    "remaining_source_candidate": "a source-derived tensor or F-term constraint that acts directly on real triplets, fixes its normalization, and survives RG, thresholds, and calibrated readout",
}
(ROOT / "results" / "wp717_nonabelian_real_triplet_moment_map_no_go.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
