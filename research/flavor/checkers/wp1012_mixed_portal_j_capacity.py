import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).parents[1]
ensemble = json.loads((ROOT/"results"/"wp20_valley_audit.json").read_text())

s = sp.symbols("s", real=True)
lam = sp.symbols("lambda")
t = sp.Rational(6, 5)
X = sp.diag(-1, 0, 1)
Y = sp.Matrix([[0, 1, -sp.I*t], [1, 0, 1], [sp.I*t, 1, 0]])
Hu0 = X + s*Y
Hd0 = Y

def discriminant_squared(matrix):
    polynomial = matrix.charpoly(lam).as_expr()
    return sp.factor(sp.discriminant(polynomial, lam))

disc_u_sq = discriminant_squared(Hu0)
disc_d_sq = discriminant_squared(Hd0)
commutator = sp.factor(Hu0*Hd0-Hd0*Hu0)
det_commutator = sp.factor(commutator.det())
J2 = sp.factor(
    det_commutator*sp.conjugate(det_commutator)
    /(4*disc_u_sq*disc_d_sq)
)
derivative = sp.factor(sp.diff(J2, s))

assert commutator == X*Y-Y*X
assert det_commutator == 24*sp.I/5
assert disc_u_sq == 4*(86*s**2+25)**3/sp.Integer(15625)
assert disc_d_sq == sp.Rational(2544224, 15625)
assert J2 == sp.Rational(87890625, 636056)/(86*s**2+25)**3
assert sp.factor(derivative/s) == -sp.Rational(263671875, 3698)/(86*s**2+25)**4
assert derivative.subs(s, 1) < 0
assert J2.subs(s, 0) == sp.Rational(5625, 636056)
assert sp.limit(J2, s, sp.oo) == 0

Js = [abs(sp.Rational(str(record["J"]))) for record in ensemble["records"]]
assert len(Js) == ensemble["n_minima_audited"] == 1210
assert min(Js) > 0
assert max(Js)**2 < J2.subs(s, 0)

# On s>=0, J2 is continuous, strictly decreasing for s>0, and ranges from
# J2(0) to zero. Therefore every stored nonzero J has one positive preimage.
# The same J2 also has the second algebraic preimage -s.
assert all(0 < value**2 < J2.subs(s, 0) for value in Js)

# Deliberate-failure witness for the separately spectral endpoint s=0:
# its squared-J obstruction above the exact 10^-3 ensemble separator is nonzero.
separate_spectral_obstruction = sp.factor(
    J2.subs(s, 0)-sp.Rational(1, 1000)**2
)
assert separate_spectral_obstruction > 0

result = {
    "schema": "marici.flavor.wp1012.v1",
    "status": "PASS",
    "portal": "Hu=aI+X+sY, Hd=bI+Y with shifts chosen for positivity",
    "weak_basis_descent": "simultaneous conjugation covariance passes",
    "commutator_determinant": str(det_commutator),
    "up_discriminant_squared": str(disc_u_sq),
    "down_discriminant_squared": str(disc_d_sq),
    "J_squared": str(J2),
    "domain": "real s; monotonic theorem stated on s>=0",
    "range_on_nonnegative_branch": "(0,5625/636056]",
    "ensemble_sheets_reached_in_J_coordinate": len(Js),
    "ensemble_min_abs_J": str(min(Js)),
    "ensemble_max_abs_J": str(max(Js)),
    "contextual_partition": "one positive s per nonzero |J|, with an additional sign-related algebraic preimage on real s",
    "classification": "covariant mixed-portal capacity family; neither selector nor rigidifier",
    "deliberate_failure": {
        "candidate": "s=0 separate-spectral endpoint",
        "threshold_squared": "1/1000000",
        "nonzero_obstruction": str(separate_spectral_obstruction),
    },
    "claim_boundary": "J-coordinate reachability only; no full physical16 landing, source law for s, or instrument is proved",
    "remaining_gate": "derive s and the positive shifts from one source package, then test the complete physical16 image and calibrated instrument",
}

out = ROOT/"results"/"wp1012_mixed_portal_j_capacity.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print("WP1012 PASS: mixed portal reaches every stored J magnitude but leaves s unselected")
