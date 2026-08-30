"""Exact ideal source-derived cascade polarimeter for a protected channel."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
u, v = sp.symbols("u v", positive=True)
c = sp.symbols("c", real=True)
W = u+v
polarization = (u-v)/W
density = sp.Rational(1, 2)*(1+polarization*c)
normalization = sp.integrate(density, (c, -1, 1))
mean_c = sp.simplify(sp.integrate(c*density, (c, -1, 1)))
N = sp.simplify(3*W*mean_c)
response = sp.Matrix([W, N])

# Two-flip charge vectors reduced to the relevant n flip for this cascade.
charges = {"A": 0, "B": 1, "n": 1, "qR": 0, "X": 1}
parent_vertex_even = (charges["A"]+charges["B"]+charges["n"]) % 2 == 0
exit_vertex_even = (charges["B"]+charges["qR"]+charges["X"]) % 2 == 0

MA, MB, mn, mX, mq = map(sp.Integer, [5, 3, 1, 1, 0])
parent_margin = MA-MB-mn
daughter_margin = MB-mX-mq

checks = {
    "angular_density_normalized": normalization == 1,
    "signed_first_moment": mean_c == polarization/3,
    "moment_recovers_chiral_difference": N == u-v,
    "cascade_response_rank_two": response.jacobian([u, v]).det() == -2,
    "protected_parent_and_exit_vertices_are_even": parent_vertex_even and exit_vertex_even,
    "simultaneous_cascade_threshold_witness": parent_margin == 1 and daughter_margin == 2,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP674", "status": "PASS", "checks": checks,
    "cascade": "A -> B+n followed by B -> q_R+X",
    "charge_assignment": charges,
    "threshold_witness": {"masses": [5, 3, 1, 1, 0], "margins": [1, 2]},
    "ideal_distribution": "f(cos theta)=[1+((u-v)/(u+v)) cos theta]/2",
    "ports": ["W=u+v", "N=3W<cos theta>=u-v"],
    "response_determinant": "-2",
    "classification": "the admitted chiral exit route can supply a source-derived ideal polarimeter without a reverse decay or added reference port",
    "smallest_exact_falsifier": "either cascade threshold margin nonpositive, or the exit vertex has zero analyzing power",
    "remaining_gate": "derive finite-mass spin transfer and bind X and q reconstruction to an actual detector analysis with independent calibration",
}
(ROOT / "results" / "wp674_source_derived_cascade_polarimeter.json").write_text(
    json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))
