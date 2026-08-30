import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).parents[1]
ensemble = json.loads((ROOT/"results"/"wp20_valley_audit.json").read_text())
wp109 = json.loads((ROOT/"results"/"wp109_jarlskog_normalized_margin.json").read_text())

X = sp.diag(-1, 0, 1)
t = sp.Rational(6, 5)
Y = sp.Matrix([[0, 1, -sp.I*t], [1, 0, 1], [sp.I*t, 1, 0]])
C = X*Y-Y*X
lam = sp.symbols("lambda")
charpoly = sp.factor(Y.charpoly(lam).as_expr())
disc_y_sq = sp.factor(sp.discriminant(charpoly, lam))
delta_x = sp.Integer(2)
det_c = sp.factor(C.det())
J2 = sp.factor(
    det_c*sp.conjugate(det_c)/(4*delta_x**2*disc_y_sq)
)

assert charpoly == lam*(25*lam**2-86)/25
assert disc_y_sq == sp.Rational(2544224, 15625)
assert det_c == 24*sp.I/5
assert J2 == sp.Rational(5625, 636056)
assert wp109["identity"] == "det[Hu,Hd]=2 i J Delta_u Delta_d"

# Direct and square maps fail before an ensemble comparison.
assert min(X.eigenvals()) < 0
assert sorted((X**2).eigenvals().values()) == [1, 2]

# Exact comparison against decimal records as stored. Converting their string
# representations to Rational avoids introducing a new floating tolerance.
Js = [abs(sp.Rational(str(record["J"]))) for record in ensemble["records"]]
assert len(Js) == ensemble["n_minima_audited"] == 1210
assert all(value < sp.Rational(1, 1000) for value in Js)
assert J2 > sp.Rational(1, 1000)**2

# Deliberate-failure test: a noninjective spectral map may change the apparent
# mixing basis, but it creates a degenerate spectrum and leaves physical16.
assert len((X**2).eigenvals()) < 3

result = {
    "schema": "marici.flavor.wp1011.v1",
    "status": "PASS",
    "map_class": "Hu=f(X), Hd=g(Y), positive nondegenerate separate spectral maps",
    "selected_orbit_J_squared": str(J2),
    "selected_orbit_abs_J_decimal": str(sp.sqrt(J2).evalf(16)),
    "ensemble_sheets": len(Js),
    "ensemble_min_abs_J": str(min(Js)),
    "ensemble_max_abs_J": str(max(Js)),
    "exact_separation_threshold": "1/1000",
    "contextual_partition": "selected spectral-map image disjoint from all 1210 fitted sheets",
    "classification": "global auxiliary selector with no viable separate-spectral physical16 image",
    "remaining_gate": "source-derived mixed covariant portal changing relative spectral projectors",
}

out = ROOT/"results"/"wp1011_selected_orbit_spectral_physical16_no_go.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print("WP1011 PASS: selected spectral-map image is disjoint from the fitted physical16 ensemble")

