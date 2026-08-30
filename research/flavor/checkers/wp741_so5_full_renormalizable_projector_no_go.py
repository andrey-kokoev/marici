"""Exact no-go for a 3+1+1 vacuum of one symmetric-traceless SO(5) field."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
t, l1, l2 = sp.symbols("t lambda_1 lambda_2", real=True)
x, y = sp.symbols("x y", real=True)

# Fix the repeated eigenvalue to one; every nonzero candidate is obtained by
# restoring its overall scale. Tracelessness fixes the fifth eigenvalue.
eigenvalues = (1, 1, 1, t, -3 - t)
s2 = sp.factor(sum(q**2 for q in eigenvalues))
mu = 2 * l2
m2 = sp.factor(l1 * s2 + l2 * (t**2 + 3*t + 3))

def stationarity_polynomial(q):
    return sp.expand(-m2*q + mu*q**2 + l1*s2*q + l2*q**3)

stationarity_differences = tuple(
    sp.factor(stationarity_polynomial(q) - stationarity_polynomial(1))
    for q in (t, -3-t)
)

# The two SO(3)-invariant diagonal fluctuations are (x,x,x,y,-3x-y).
fluctuations = (x, x, x, y, -3*x-y)
shifted = tuple(a + h for a, h in zip(eigenvalues, fluctuations))
tr2 = sum(q**2 for q in shifted)
potential = sp.expand(
    -m2 * tr2 / 2
    + mu * sum(q**3 for q in shifted) / 3
    + l1 * tr2**2 / 4
    + l2 * sum(q**4 for q in shifted) / 4
)
gradient = tuple(sp.factor(sp.diff(potential, q).subs({x: 0, y: 0})) for q in (x, y))
singlet_hessian = sp.simplify(sp.hessian(potential, (x, y)).subs({x: 0, y: 0}))
singlet_det = sp.factor(singlet_hessian.det())
singlet_minor = sp.factor(singlet_hessian[0, 0])

A = sp.factor((t - 1) * (t + 4))
D = l2 + 2*l1
shape_coefficient = sp.factor(-l2 * A)

# Derive, rather than insert, one representative of the five-dimensional
# symmetric-traceless shape sector inside the repeated eigenspace.
h = sp.symbols("h", real=True)
phi = sp.diag(*eigenvalues)
shape = sp.zeros(5)
shape[0, 1] = shape[1, 0] = h
shape_field = phi + shape
shape_tr2 = sp.trace(shape_field**2)
shape_potential = sp.expand(
    -m2*shape_tr2/2
    + mu*sp.trace(shape_field**3)/3
    + l1*shape_tr2**2/4
    + l2*sp.trace(shape_field**4)/4
)
derived_shape_coefficient = sp.factor(sp.diff(shape_potential, h, 2).subs(h, 0)/2)
minor_obstruction_identity = sp.factor(singlet_minor - (6*l2*A + 9*D*(t+4)**2))
det_obstruction_identity = sp.factor(
    singlet_det + 6*shape_coefficient*D*(2*t+3)**2
)

# A concrete attempted repair: its shape modes are positive and its invariant
# determinant is positive, but the leading invariant minor is negative.
hostile = {t: 2, l1: 0, l2: -1}
hostile_shape = shape_coefficient.subs(hostile)
hostile_det = singlet_det.subs(hostile)
hostile_minor = singlet_minor.subs(hostile)

checks = {
    "candidate_is_traceless": sum(eigenvalues) == 0,
    "stationarity_fixes_cubic_coefficient": mu == 2*l2,
    "stationarity_fixes_mass_coefficient": sp.simplify(m2 - (l1*s2 + l2*(t**2 + 3*t + 3))) == 0,
    "all_three_eigenvalues_obey_one_stationarity_equation": stationarity_differences == (0, 0),
    "invariant_gradient_vanishes": gradient == (0, 0),
    "shape_coefficient_is_exact": shape_coefficient == -l2*(t-1)*(t+4),
    "shape_coefficient_is_derived_from_full_matrix_potential": sp.simplify(derived_shape_coefficient-shape_coefficient) == 0,
    "singlet_determinant_is_exact": singlet_det == 6*l2*D*(t-1)*(t+4)*(2*t+3)**2,
    "determinant_obstruction_identity_is_exact": det_obstruction_identity == 0,
    "minor_obstruction_identity_is_exact": minor_obstruction_identity == 0,
    "hostile_shape_is_positive": hostile_shape == 6,
    "hostile_singlet_determinant_is_positive": hostile_det == 1764,
    "hostile_leading_minor_is_negative": hostile_minor == -360,
    "deliberate_failure_residual_is_nonzero": hostile_minor != 0,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP741",
    "status": "PASS",
    "checks": checks,
    "source_domain": "one real symmetric-traceless 14 of SO(5) with its complete renormalizable invariant potential, including Tr(Phi^3)",
    "candidate_family": "diag(1,1,1,t,-3-t), up to nonzero scale and SO(5) rotation",
    "stationarity_relations": {
        "mu": "2 lambda_2 in unit repeated-eigenvalue normalization",
        "m_squared": str(m2),
    },
    "classification": "neither selector nor stable rigidifier: every distinct 3+1+1 stationary orbit is unstable or non-isolated",
    "exact_obstruction": "shape positivity gives lambda_2 A<0; positive singlet determinant then gives lambda_2+2 lambda_1<0; the leading singlet minor equals 6 lambda_2 A+9(lambda_2+2 lambda_1)(t+4)^2 and is therefore negative",
    "degenerate_boundaries": "t=1 or t=-4 makes a shape mode flat; t=-3/2 merges the two singlets and makes the singlet determinant zero; lambda_2=0 also leaves shape flats",
    "smallest_exact_falsifier": "t=2, lambda_1=0, lambda_2=-1 gives shape coefficient 6 and singlet determinant 1764, but leading singlet minor -360",
    "deliberate_failure_residual": str(hostile_minor),
    "claim_boundary": "single renormalizable symmetric-traceless 14; multiple fields, higher operators, radiative effective potentials, or different representations are not excluded",
    "remaining_source_gate": "a new independently required source object must change the vacuum Hessian obstruction rather than add a coefficient solely to fit the desired projector",
    "remaining_fixed_point_gate": "not opened because the full one-14 renormalizable source has no stable projector vacuum",
    "remaining_physical_gate": "not opened; a surviving construction must still transport its labelled projector through thresholds to calibrated physical16 channels",
}
(ROOT / "results" / "wp741_so5_full_renormalizable_projector_no_go.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
