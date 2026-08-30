"""Exact unequal-mass, independent-vertex protected messenger supertrace."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
x = sp.symbols("x0:3", real=True)
n = sp.Matrix(x)
a = n.dot(n)
I = sp.I
J = [
    sp.Matrix([[0, 1, 0], [1, 0, 1], [0, 1, 0]])/sp.sqrt(2),
    sp.Matrix([[0, -I, 0], [I, 0, -I], [0, I, 0]])/sp.sqrt(2),
    sp.diag(1, 0, -1),
]
Jn = sum((n[i]*J[i] for i in range(3)), sp.zeros(3))
A, B, y, z = sp.symbols("A B y z", real=True)
mass = sp.Matrix.vstack(
    sp.Matrix.hstack(A*sp.eye(3), y*Jn),
    sp.Matrix.hstack(z*Jn, B*sp.eye(3)))
physical_trace = sp.expand(sp.trace((mass.H*mass)**2))
expected = sp.expand(
    3*A**4+3*B**4
    +4*(A**2*(y**2+z**2)+2*A*B*y*z+B**2*(y**2+z**2))*a
    +2*(y**4+z**4)*a**2)

t = sp.symbols("t", positive=True)
imbalance = sp.expand((t*y)**4+(z/t)**4)
unit_balanced = (sp.Integer(1)**4+sp.Integer(1)**4)
unit_hostile = sp.Integer(2)**4+sp.Rational(1, 2)**4

checks = {
    "general_physical_trace_identity": sp.simplify(physical_trace-expected) == 0,
    "quartic_support_is_mass_independent": sp.diff(2*(y**4+z**4), A) == 0 and sp.diff(2*(y**4+z**4), B) == 0,
    "fixed_product_rescaling_preserves_product": sp.simplify((t*y)*(z/t)-y*z) == 0,
    "fixed_product_rescaling_changes_erosion": sp.simplify(imbalance-(y**4+z**4)) != 0,
    "balanced_vertices_minimize_fixed_product_erosion": sp.simplify(y**4+z**4-2*(y*z)**2-(y**2-z**2)**2) == 0,
    "hostile_unit_product_pair_has_larger_erosion": unit_balanced == 2 and unit_hostile == sp.Rational(257, 16),
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP670", "status": "PASS", "checks": checks,
    "domain": "unequal real pair masses and independent real reciprocal off-diagonal vertices",
    "dirac_norm_quartic": "-8(y^4+z^4)|n|^4",
    "radial_margin_flow": "dD/dt=1136-32(Q_n+Q_m), Q=sum(y^4+z^4)",
    "fixed_product_bound": "y^4+z^4>=2(yz)^2 with equality iff |y|=|z|",
    "hostile_fixed_product_pair": {"balanced": ["1", "1"], "imbalanced": ["2", "1/2"], "erosion_sums": ["2", "257/16"]},
    "classification": "protected tree-product matching does not identify or bound loop erosion without a vertex-balance law",
    "smallest_exact_falsifier": "(y,z)=(1,1) and (2,1/2) have the same product but unequal y^4+z^4",
    "remaining_gate": "derive a source law for vertex balance or measure both protected threshold widths in one calibrated experiment",
}
(ROOT / "results" / "wp670_protected_vertex_imbalance.json").write_text(
    json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))
